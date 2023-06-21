import gradio as gr

'''
def greet(name):
    return "Hello " + name + "!!"
'''

def greet(name, is_morning, temperature):
    salutation = 'Good morning'
    if not is_morning:
        salutation = 'Good evening'
    
    greeting = f'{salutation} {name}. It is {temperature} degrees today'
    greeting2 = salutation + ' ' + name + '. It is ' + str(temperature) + ' degrees today'

    celsius = (temperature - 32) * 5 / 9
    return greeting2, round(celsius, 2)
    


'''
iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
'''

'''
iface = gr.Interface(fn=greet, 
                     inputs=gr.inputs.Textbox(lines=2, placeholder="이름을 입력하세요."),
                     outputs="text")
iface.launch()
'''

demo = gr.Interface(fn=greet, 
                     inputs=['text', 'checkbox', gr.Slider(0, 100)],
                     outputs=['text', 'number'],
                     )

demo.launch()