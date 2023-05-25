from neo4j import GraphDatabase

# Change uri, username, and password to align with my own instance. I can edit nodes and relationships in here and it'll appear in neo4j
uri = 'neo4j+s://defb11b9.databases.neo4j.io'
username = 'neo4j'
password = 'xAIypHcqh3vmH9wxKnh3tfR5Izs8YeTWLL8zVZK31As'

driver = GraphDatabase.driver(uri, auth=(username, password))

with driver.session() as session:
    result = session.run('match(Student:Person) match(cs111:class) create (Student)-[:TA_in]->(cs111)')
    for record in result:
        print(record)