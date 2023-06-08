import logging
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

class Chatbot:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Remember to close your driver when finished
        self.driver.close()

    def create_duedates(self, hw_name, date):
        # Create nodes with the function create_and_return_nodes
         with self.driver.session() as session:
            result = session.execute_write(self.create_and_return_nodes, hw_name, date)
            for record in result:
                print("Created relationship between: {date1}, {hw1}".format(
                    date1=record['date1'], hw1=record['hw1']))

    def create_and_return_nodes(self, tx, hw_name, date):
        # Create nodes and relationships on the query
        # TO DO: add a parameter that lets you create a relationship, or name your relationship
        query = (
            "CREATE (date1:Dates { name: $date }) "
            "CREATE (hw1:Homework { name: $hw_name })"
            "CREATE (hw1)-[:IS_DUE_ON]->(date1)"
            "RETURN date1, hw1"
        )
        result = tx.run(query, date=date, hw_name=hw_name)
        try:
            return [{"date1": record["date1"]["name"], "hw1": record["hw1"]["name"]}
                    for record in result]
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise
    def find_date(self, hw_name):
        # Return the duedate of a homework using the function find_date_of_hw
        with self.driver.session() as session:
            result = session.execute_read(self.find_date_of_hw, hw_name)
            for record in result:
                print("The duedate of {hw_name} is: {record}".format(record=record, hw_name=hw_name))

    @staticmethod
    def find_date_of_hw(tx, hw_name):
        query = (
            "MATCH (hw1)-[:IS_DUE_ON]->(date1) "
            "WHERE hw1.name = $hw_name "
            "RETURN date1.name AS name"
        )
        result = tx.run(query, hw_name=hw_name)
        return [record["name"] for record in result]
    

