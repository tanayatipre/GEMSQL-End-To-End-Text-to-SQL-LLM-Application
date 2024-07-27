from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from dotenv import load_dotenv
import os
import re
import pymysql
from sqlalchemy import create_engine

class CustomLLM(GoogleGenerativeAI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _generate(self, prompts, **kwargs):
        prompts = [
            "You are a helpful assistant. When writing SQL queries, output only the SQL query without any additional text. Do not include the word 'SQLQuery:' in the output."
            " Write only and only SQL query and nothing else."
            " Do not include Markdown formatting characters such as ``` or ```sql. Here is the question: " + prompt
            for prompt in prompts
        ]
        return super()._generate(prompts, **kwargs)

load_dotenv()  # Load environment variables from .env

def get_db_chain():
    # Database credentials
    db_user = "root"
    db_password = "root"
    db_host = "localhost"
    db_port = 3307
    db_name = "general_data"

    # Create SQLAlchemy engine
    connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(connection_string)

    # Create SQL database connection
    db = SQLDatabase.from_uri(
        connection_string,
        sample_rows_in_table_info=3,
    )
    print(db.table_info)
    
    # Initialize the language model
    llm = CustomLLM(model='gemini-pro', google_api_key=os.getenv('GOOGLE_API_KEY'), temperature=0.5)
    
    # Create the SQL Database Chain
    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
    
    return chain

def sanitize_query(output):
    # Remove markdown backticks and extra newlines
    output = re.sub(r'```|```sql|```|\n', '', output).strip()
    # Extract SQL query from the provided text
    sql_match = re.search(r'(SELECT.*?;)', output, re.IGNORECASE | re.DOTALL)
    if sql_match:
        return sql_match.group(1).strip()
    return output

def execute_query(chain, question):
    # Generate and sanitize the SQL query
    generated_query = chain.run(question)
    sanitized_query = sanitize_query(generated_query)
    
    # Debug output
    print("Generated Query:", generated_query)
    print("Sanitized Query:", sanitized_query)

    # Execute the sanitized query
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="general_data",
        port=3307,
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(sanitized_query)
            result = cursor.fetchall()
            return {
                "result": result,
                "query": sanitized_query
            } 
    except pymysql.MySQLError as e:
        print(f"SQL Error: {e}")
        return None
    finally:
        connection.close()

# Example usage
if __name__ == "__main__":
    chain = get_db_chain()
    question = "How many users are there in the database?"
    result = execute_query(chain, question)
    print("Query Result:", result)
