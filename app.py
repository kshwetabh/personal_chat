import os
from shiny.express import ui
from chatlas import ChatGoogle
from dotenv import load_dotenv

load_dotenv()

ui.page_opts(
    title="Jarvis",
    fillable=True,
    fillable_mobile=True,
)

# Create a chat instance and display it 
chat = ui.Chat(id="chat")  
chat.ui()
chat_client = ChatGoogle(api_key=os.getenv("GOOGLE_API_KEY"))


# Define a callback to run when the user submits a message 
@chat.on_user_submit  
async def handle_user_input(user_input: str):  
    # Simply echo the user's input back to them 
    response = await chat_client.stream_async(user_input)
    await chat.append_message_stream(response)