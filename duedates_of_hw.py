from neo4j import GraphDatabase

# Change uri, username, and password to align with my own instance. I can edit nodes and relationships in here and it'll appear in neo4j
uri = 'neo4j+s://7e7dd47b.databases.neo4j.io'
username = 'neo4j'
password = '0cmS1soOEKbmzWoXetpCFiqtfg_9SywYdRcVVAMo-_M'

driver = GraphDatabase.driver(uri, auth=(username, password))

"""
# Relationship 1
with driver.session() as session:
    result = session.run('create (duedate01:Dates {name: "May09"}) -[:is_duedate_of]->(hw01:Homework {name:"hw01"})')
    for record in result:
        print(record) 

# Relationship 2
with driver.session() as session:
    result = session.run('create (duedate02:Dates {name: "May11"}) -[:is_duedate_of]->(hw02:Homework {name:"hw02"})')
    for record in result:
        print(record)

# Relationship 3
with driver.session() as session:
    result = session.run('create (duedate03:Dates {name: "May16"}) -[:is_duedate_of]->(hw03:Homework {name:"hw03"})')
    for record in result:
        print(record)     
"""
# From an empty database, create 5 nodes with relationships
# Query the databse (If there is a relationship between a student and a class, you can ask for the student and it'll return the student's information, etc.)