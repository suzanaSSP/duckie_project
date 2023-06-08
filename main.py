from creating_nodes import Chatbot

if __name__ == "__main__":
    uri = "neo4j+s://c113e109.databases.neo4j.io"
    user = "neo4j"
    password = "1nmF-51WQhdSJPTjvE1OW4wWiqjfFJcSgZ5pQc-5q_0"
    chatbot = Chatbot(uri, user, password)
    try:
        chatbot.find_date("hw01")
    finally:
        chatbot.close()




