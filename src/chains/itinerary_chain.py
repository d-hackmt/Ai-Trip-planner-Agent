from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import *

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.5,  # Imaking it a more creative one
    top_p=0.9,        # nucleus sampling makes it a balanced point that sets a bar
    max_tokens=256    # lim for token usage to avoid misuse
)

## in what way llm has to give answer

itnineary_prompt = ChatPromptTemplate([
    
    ## system msg - msg to ai as prompt
    
    ("system" , """
    You are a helpful travel asssistant. Create a one day trip itineary 
    for {city} based on user's interest : {interests}. 
    Provide a brief , bulleted itineary
    """),
    
    ## human msg - given by us , first msg by us to ai 
    
    ("human" , "Create an intresting itineary for my one day trip")
])


# this input will be given from streamlit

def generate_itineary(city:str , interests:list[str]) -> str:
    response = llm.invoke(
        itnineary_prompt.format_messages(city=city,
                                        interests=', '.join(interests))
    )

    # answer is stored in content , out actual output
    
    return response.content
