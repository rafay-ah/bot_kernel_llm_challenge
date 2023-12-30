import os
from openai import OpenAI


class Chatbot:
    
    def create_agent(self):    
        self.agent = OpenAI(api_key= os.environ.get("OPEN_AI_KEY"))


    def query_agent(self, query, schema):
        message=[{"role": "assistant", "content": f"You are a chatbot designed to interact with an SQLite database. You are to convert user queries into SQL statements that can be executed on SQLite database. Use the follwing database schema and donot deviate from it {schema}. Ensure that the generated SQL code follows secure practices.Provide clear error messages if the user input is ambiguous or cannot be translated into a valid SQL query.Only send SQl statement as response."},
                  {"role": "user", "content": query}]
        
        response = self.agent.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = message,
        temperature=0.2)

        print(response.choices[0].message.content)
        return response.choices[0].message.content
