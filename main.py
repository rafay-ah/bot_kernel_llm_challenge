import streamlit as st
import pandas as pd
from db_interface import DataInterface
from chatbot import Chatbot


st.title("Bot Kernel LLM Challenge")
query = st.text_area("Insert your question to explore the table")

db = DataInterface()
db_schema = db.get_schema() # to provide context to agent

bot = Chatbot()
bot.create_agent()


def write_response(table):
  st.table(table) # can add multiple formatting opertaions here


if st.button("Submit Query", type="primary"):

  # Route the query to agent to be executed.
  response = bot.query_agent(query,db_schema)
  result = db.execute_query(response)

  # Format the response to be GUI friendly.
  write_response(result)
