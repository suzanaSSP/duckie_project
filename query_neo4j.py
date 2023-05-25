from neo4j import GraphDatabase

# Change uri, username, and password to align with my own instance. I can edit nodes and relationships in here and it'll appear in neo4j
uri = 'neo4j+s://7e7dd47b.databases.neo4j.io'
username = 'neo4j'
password = '0cmS1soOEKbmzWoXetpCFiqtfg_9SywYdRcVVAMo-_M'

driver = GraphDatabase.driver(uri, auth=(username, password))

def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return result
    
query = "match (duedate1:Dates)-[:is_duedate_of]->(hw01:Homework) return duedate1.name"
result = run_query(query)


# Be able to extract the result from neo4j and show it in python
# Create a function that asks that question to neo4j, then answers it to python
# Print everything

