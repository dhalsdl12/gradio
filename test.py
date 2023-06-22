from PIL import Image
import numpy as np
import gradio as gr


def flip_text(x):
    return x[::-1]

def flip_image(x):
    print(x.name)
    image = Image.open(x.name)
    print(image)
    return image

with gr.Blocks() as demo:
    gr.Markdown('Flip text or image files using this demo.')

    with gr.Tab('Flip Text'):
        text_input = gr.Textbox()
        text_button = gr.Button('flip')
        text_output = gr.Textbox()
    
    with gr.Tab('Flip Image'):
        with gr.Row():
            image_input = gr.File()
            image_output = gr.Image()
        
        image_button = gr.Button('flip')
    
    with gr.Accordion('Open for More!'):
        gr.Markdown('Look at me...')


    text_button.click(flip_text, inputs=text_input, outputs=text_output)
    image_button.click(flip_image, inputs=image_input, outputs=image_output)


demo.launch()