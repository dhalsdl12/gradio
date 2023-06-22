from PIL import Image
import numpy as np
import gradio as gr
import pydicom


def file2image(input_file):
    file_name = input_file.name.split('\\')[-1]
    file_type = file_name.split('.')[-1]

    print(file_name, file_type)
    if file_type == 'dcm' or file_type == 'DCM':
        dcm = pydicom.dcmread(file_name)
        image = dcm.pixel_array

        return image

    image = Image.open(input_file.name)
    print(image)
    return image


with gr.Blocks() as demo:
    gr.Markdown('Image files using this demo.')
    
    with gr.Tab('Flip Image'):
        with gr.Row():
            image_input = gr.File()
            image_output = gr.Image()
        
        image_button = gr.Button('flip')
    
    with gr.Accordion('Open for More!'):
        gr.Markdown('Look at me...')

    image_button.click(file2image, inputs=image_input, outputs=image_output)


demo.launch()