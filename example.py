example = [
    {
        
    "Query": "Display the details of all cities in Gujarat.",
    "SQLQuery": "SELECT * FROM indiavotes WHERE State = 'Gujarat';",
    "SQLResult": "Result of the SQL query",
    "Answer": '''4, Ahmedabad East, 7, GEN, Gujarat, Hasmukhbhai Patel (H.S.PATEL), Bharatiya Janta Party, 20,38,162, 11,28,339, 55.40%, 4,61,755, 40.90%
5, Ahmedabad West, 8, SC, Gujarat, Dineshbhai Makwana (ADVOCATE), Bharatiya Janta Party, 17,26,987, 9,66,646, 56.00%, 2,86,437, 29.60%'''


    },
    {
       
    "Query": "Count the number of seats in each state.",
    "SQLQuery": "SELECT State, SUM(`No. of seats`) as Total_Seats FROM indiavotes GROUP BY State;",
    "SQLResult": "Result of the SQL query",
    "Answer": '''Telangana, 1
Uttar Pradesh [2000 Onwards], 18
Maharashtra, 37
Gujarat, 15
...'''

    },
    {
    "Query": "Show the winning candidate and their party for the city of Agra.",
    "SQLQuery": "SELECT `Winning Candidate`, `Political Party` FROM indiavotes WHERE City = 'Agra';",
    "SQLResult": "Result of the SQL query",
    "Answer": "Prof S P Singh Baghel, Bharatiya Janta Party"
},
{
    "Query": "List the cities where the winning margin percentage is greater than 20%.",
    "SQLQuery": "SELECT City, `Winning Candidate`, `Political Party`, `Margin percentage` FROM indiavotes WHERE `Margin percentage` > '20%';",
    "SQLResult": "Result of the SQL query",
    "Answer": '''Agra, Prof S P Singh Baghel, Bharatiya Janta Party, 24.10%
Ahmedabad East, Hasmukhbhai Patel (H.S.PATEL), Bharatiya Janta Party, 40.90%
Ahmedabad West, Dineshbhai Makwana (ADVOCATE), Bharatiya Janta Party, 29.60%
...'''
},
{
        
    "Query": "List all cities that fall under the ST category.",
    "SQLQuery": "SELECT City FROM indiavotes WHERE Category = 'ST';",
    "SQLResult": "Result of the SQL query",
    "Answer": '''Adilabad,
Alipurduars,
Aruku,
Banswara,
Bardoli,
Bastar,
Bellary,
Betul,
Chhota, Udaipur,
Dahod,
Dausa,
Dhar,
Dindori,
Diphu,
Dumka,
Gadchiroli-Chi,
Jhargram,
Kanker,
Keonjhar,
Khargone,
Khunti,
Kokrajhar,
Koraput,
Lohardaga,
Mahabubabad,
Mandla,
Mayurbhanj,
Mizoram,
Nabarangpur,
Nagaland,
Nandurbar,
Outer, Manipur,
Palghar,
Raichur,
Raigarh,
Rajmahal,
Ratlam,
Sarguja,
Shahdol,
Shillong,
Singhbhum,
Sundargarh,
Tripura, East,
Tura,
Udaipur,
Valsad'''

},
{
        
    "Query": "Find the total number of electors in Telangana.",
    "SQLQuery": "SELECT SUM(Electors) FROM indiavotes WHERE State = 'Telangana';"
    "SQLResult": "Result of the SQL query",
    "Answer": '''325'''

},
{
        
    "Query": "List the cities with a voter turnout percentage greater than 85%.",
    "SQLQuery": "SELECT City FROM indiavotes WHERE Turnout > 85;",
    "SQLResult": "Result of the SQL query",
    "Answer": '''Arunachal, East,
Bapatla,
Barpeta,
Bishnupur,
Chittoor,
Dhubri,
Hindupur,
Kanthi,
Lakshadweep,
Machilipatnam,
Nagaon,
Narasaraopet,
Ongole,
Tamluk'''

},
{
        
    "Query": "Calculate the average margin percentage for each state.",
    "SQLQuery": "SELECT State, AVG(`Margin percentage`) AS Average_Margin_Percentage FROM indiavotes GROUP BY State;",
    "SQLResult": "Result of the SQL query",
    "Answer": '''Telangana, 16
Uttar Pradesh [2000, Onwards], 8.666249999999998
Maharashtra, 9.097916666666668
Gujarat, 27.184615384615384
Rajasthan, 12.700000000000003
Kerala, 11.814999999999998
West Bengal, 9.735714285714286
Uttarakhand, 25.559999999999995
Andhra Pradesh, [2014, Onwards], 15.276
Haryana, 9.809999999999999
Punjab, 6.907692307692309
Jammu & Kashmir, 19.34
Andaman & Nicobar Islands, 12
Tamil, Nadu, 20.146153846153844
Bihar [2000, Onwards], 9.632500000000002
Arunachal, Pradesh, 17.3
Orissa, 8.842857142857142
Karnataka, 10.010714285714286
Madhya Pradesh [2000, Onwards], 25.99310344827586
Assam, 17.57142857142857
Chhattisgarh, 11.39090909090909
Chandigarh, 0.6
Delhi [1977, Onwards], 11
Jharkhand, 15.685714285714287
Dadra & Nagar Haveli, 28
Daman & Diu, 6.7
Himachal Pradesh, 14.625
Manipur, 12.25
Ladakh, 20.6
Lakshadweep, 5.4
Mizoram, 13.9
Nagaland, 6.7
Goa, 14.2
Pondicherry, 16.9
Meghalaya, 29.4
Sikkim, 21
Tripura, 46.75'''

},
{
        
    "Query": "Display the details of top 5 cities where the margin percentage is above 10% & the political party is 'Bharatiya Janta Party'.",
    "SQLQuery": "SELECT * FROM indiavotes WHERE `Margin percentage` > 10 AND `Political Party` = 'Bharatiya Janta Party' LIMIT 5;",
    "SQLResult": "Result of the SQL query",
    "Answer": '''2,	Agra,	18,	SC,	Uttar Pradesh [2000 Onwards],	Prof S P Singh Baghel,	Bharatiya Janta Party,	20,72,685,	11,23,779,	54.20%,	2,71,294,	24.10%
4,	Ahmedabad East,	7,	GEN,	Gujarat, Hasmukhbhai Patel (H.S.PATEL),	Bharatiya Janta Party,	20,38,162,	11,28,339,	55.40%,	4,61,755,	40.90%
5,	Ahmedabad West,	8,	SC,	Gujarat, Dineshbhai Makwana (ADVOCATE),	Bharatiya Janta Party,	17,26,987,	9,66,646,	56.00%,	2,86,437,	29.60%
6,	Ajmer,	13,	GEN, Rajasthan,	Bhagirath Choudhary, Bharatiya Janta Party,	19,95,699,	12,01,179,	60.20%,	3,29,991,	27.50%
14,	Almora,	3,	SC,	Uttarakhand, Ajay Tamta,	Bharatiya Janta Party,	13,39,327,	6,68,497,	49.90%,	2,34,097,	35.00%'''

},
{
        
    "Query": "Find the political party with the highest total number of seats won across all states.",
    "SQLQuery": "SELECT `Political Party`, SUM(`No. of seats`) AS Total_Seats FROM indiavotes GROUP BY `Political Party` ORDER BY Total_Seats DESC LIMIT 1;",
    "SQLResult": "Result of the SQL query",
    "Answer": '''Bharatiya Janta Party,	3746'''

},
{
        
    "Query": " Find the top 3 political parties with the highest average turnout percentage across all cities.",
    "SQLQuery": "SELECT `Political Party`, AVG(`Turnout`) AS `Average Turnout` FROM indiavotes GROUP BY `Political Party` ORDER BY `Average Turnout` DESC LIMIT 3",
    "SQLResult": "Result of the SQL query",
    "Answer": '''Asom Gana Parishad, 85.7
United Peoples Party Liberal, 83.6
Janasena Party,	83.30000000000001'''

},
{
        
    "Query": " Identify political parties that have more than one winning candidate in the same city.",
    "SQLQuery": "SELECT City, `Political Party`, COUNT(DISTINCT `Winning Candidate`) AS Num_Winning_Candidates FROM indiavotes GROUP BY City, `Political Party` HAVING COUNT(DISTINCT `Winning Candidate`) > 1;",
    "SQLResult": "Result of the SQL query",
    "Answer": '''Maharajganj,	Bharatiya Janta Party,	2'''

},

        ]