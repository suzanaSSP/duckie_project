from neo4j import GraphDatabase

# Change uri, username, and password to align with my own instance. I can edit nodes and relationships in here and it'll appear in neo4j
uri = 'neo4j+s://7e7dd47b.databases.neo4j.io'
username = 'neo4j'
password = '0cmS1soOEKbmzWoXetpCFiqtfg_9SywYdRcVVAMo-_M'

driver = GraphDatabase.driver(uri, auth=(username, password))

# Asking neo4j for the result of my query
query = "match (duedate01:Dates {name: 'May09'})-[:is_duedate_of]->(hw01:Homework {name:'hw01'}) return duedate01.name"
with driver.session() as session:
    nodes = session.run(query)
    for node in nodes:
        print(node)


# Be able to extract the result from neo4j and show it in python
# Create a function that asks that question to neo4j, then answers it to python
# Print everything


