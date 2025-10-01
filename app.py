"""
Simple Gradio chat application that communicates with an LLM via OpenAI API.
Works with OpenAI API or local LLMs with OpenAI-compatible endpoints.
"""

import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI client
# For local LLMs, set OPENAI_API_BASE to your local endpoint (e.g., http://localhost:8080/v1)
client = OpenAI(
    api_key = "not-needed-for-local-docker-model-runner",
    base_url = os.getenv("CHAT_MODEL_URL")
)

# Model configuration
MODEL_NAME = os.getenv("CHAT_MODEL_NAME")
SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT", "You are a helpful AI assistant.")


def chat_with_llm(message, history):
    """
    Send a message to the LLM and return the response.

    Args:
        message: The user's message
        history: The chat history in Gradio format [(user_msg, assistant_msg), ...]

    Returns:
        The updated chat history with the LLM's response
    """
    # Convert Gradio history format to OpenAI messages format
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        if assistant_msg:
            messages.append({"role": "assistant", "content": assistant_msg})

    # Add the current message
    messages.append({"role": "user", "content": message})

    try:
        # Call the LLM
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.7,
            max_tokens=1000,
            stream=True
        )

        # Stream the response
        full_response = ""
        for chunk in response:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
                # Yield the updated history with the current message and partial response
                yield history + [(message, full_response)]

    except Exception as e:
        yield history + [(message, f"Error: {str(e)}\n\nPlease check your API configuration.")]








































# Create Gradio interface
with gr.Blocks(title="LLM Chat") as demo:
    gr.Markdown("# 🤖 Chat with LLM")
    gr.Markdown(
        f"Connected to: `{os.getenv("CHAT_MODEL_URL")}` | "
        f"Model: `{MODEL_NAME}`"
    )

    chatbot = gr.Chatbot(
        height=500,
        bubble_full_width=False,
        show_label=False
    )

    with gr.Row():
        msg = gr.Textbox(
            placeholder="Type your message here...",
            show_label=False,
            scale=4,
            container=False
        )
        submit_btn = gr.Button("Send", scale=1, variant="primary")

    with gr.Row():
        clear_btn = gr.Button("Clear Chat")

    gr.Markdown(
        """
        ### Configuration
        Set these environment variables in `.env` file:
        - `OPENAI_API_KEY`: Your API key (use "not-needed-for-local" for local LLMs)
        - `OPENAI_API_BASE`: API endpoint (e.g., http://localhost:8080/v1 for local)
        - `MODEL_NAME`: Model to use (default: gpt-3.5-turbo)
        - `SYSTEM_PROMPT`: System prompt for the assistant
        """
    )

    # Event handlers
    msg.submit(chat_with_llm, [msg, chatbot], [chatbot])
    msg.submit(lambda: "", None, [msg])

    submit_btn.click(chat_with_llm, [msg, chatbot], [chatbot])
    submit_btn.click(lambda: "", None, [msg])

    clear_btn.click(lambda: None, None, [chatbot])


if __name__ == "__main__":
    # Get host and port from environment variables
    host = os.getenv("GRADIO_HOST", "0.0.0.0")
    port = int(os.getenv("GRADIO_PORT", "8000"))

    demo.launch(
        server_name=host,
        server_port=port,
        share=False
    )
