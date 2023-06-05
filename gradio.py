# -*- coding: utf-8 -*-
"""Gradio.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1px3vSWnxymg9dPr3bWV919gaD9ExzsR8
"""

!pip install gradio

from ast import Return
import gradio as gr
def greet(name):
  return "Hello "  +  name +  " !!"
iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()

import gradio as gr
def moor(name, es_morgen,temp):
  solution = "Guten Morgen" if es_morgen else "Guten Tag"
  mooring = "%s %s. It is %s degrees today" % (mooring , name, temp)
  cel = (temp -32)*5/9
  return mooring, round(cel, 2)
iface = gr.Interface(
    fn = moor,
    inputs=["text","checkbox", gr.inputs.Slider(10,100)],
    outputs =["text", "number"]
)
iface.launch()




