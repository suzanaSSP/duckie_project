from neo4j import GraphDatabase

# Change uri, username, and password to align with my own instance. I can edit nodes and relationships in here and it'll appear in neo4j
uri = 'neo4j+s://defb11b9.databases.neo4j.io'
username = 'neo4j'
password = 'xAIypHcqh3vmH9wxKnh3tfR5Izs8YeTWLL8zVZK31As'

driver = GraphDatabase.driver(uri, auth=(username, password))

with driver.session() as session:
    result = session.run('')
    for record in result:
        print(record)

# Asking neo4j for the result of my query
query = "match (duedate01:Dates {name: 'May09'})-[:is_duedate_of]->(hw01:Homework {name:'hw01'}) return duedate01.name"
with driver.session() as session:
    nodes = session.run(query)
    for node in nodes:
        print(type(node))

