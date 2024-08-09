# Chatbot demo with multimodal input (text, markdown, LaTeX, code blocks, image, audio, & video).
# Plus shows support for streaming text.
import json
import gradio as gr

from chat import rewrite, translate
from text2image import generate


def print_like_dislike(x: gr.LikeData):
    print(x.index, x.value, x.liked)


def add_message(history, message):
    for x in message["files"]:
        history.append(((x,), None))
    if message["text"] is not None:
        history.append((message["text"], None))
    return history, gr.MultimodalTextbox(value=None, interactive=False)


def bot(history):
    rewrite_question = rewrite(messages=history)
    text_prompt = translate(rewrite_question)
    json_content = generate(text_prompt)
    image_content = json.loads(json_content)["image"]
    response = f'{rewrite_question}\n<img src="data:image/png;base64,{image_content}" width="512" height="512" alt="user upload image" />'
    history[-1][1] = response
    return history


with gr.Blocks(fill_height=True) as demo:
    chatbot = gr.Chatbot(
        elem_id="chatbot",
        bubble_full_width=False,
        scale=1,
    )

    clear = gr.Button("清除历史对话")

    chat_input = gr.MultimodalTextbox(interactive=True,
                                      file_count="multiple",
                                      placeholder="Enter message or upload file...", show_label=False)

    chat_msg = chat_input.submit(add_message, [chatbot, chat_input], [chatbot, chat_input])
    bot_msg = chat_msg.then(bot, chatbot, chatbot, api_name="bot_response")
    bot_msg.then(lambda: gr.MultimodalTextbox(interactive=True), None, [chat_input])

    chatbot.like(print_like_dislike, None, None)

    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8080)
