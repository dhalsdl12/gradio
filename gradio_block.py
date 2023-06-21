import gradio as gr


def greet(name):
    return 'hello ' + name + '!!'


with gr.Blocks() as demo:
    name = gr.Textbox(label='name')
    output = gr.Textbox(label='Output Box')
    greet_btn = gr.Button('Greet')
    greet_btn.click(fn=greet, inputs=name, outputs=output)

demo.launch()