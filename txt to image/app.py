from tkinter import *
from customtkinter import *

from PIL import ImageTk
#from authtoken import auth_token
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

root = Tk()
root.geometry("532x622")
root.title("TEXT to Image")

set_appearance_mode("dark")

prompt = CTkEntry(height=40,width=512,font=("Arial",20),text_color="black",master=root)
prompt.place(x=10,y=10)

lmain = CTkLabel(master=root,height=512,width=512)
lmain.place(x=10,y=10)
auth_token = "YOUR_HUGGING_FACE_AUTH_TOKEN"

modelid = "CompVis/stable-diffusion-v1-4"
device = 'cuda'
pipe = StableDiffusionPipeline.from_pretrained(modelid,revision='fp16',torch_dtype=torch.float16,
                                              use_auth_token = auth_token)
pipe.to(device)

def generate():
    with autocast(device):
        image = pipe(prompt.get(),guidance_scale=8.5)['sample'][0]
    image.save("generateimage.png")
    image = ImageTk.PhotoImage(image)
    lmain.configure(image)



button = CTkButton(height=40,width=120,font=("Arial",20),text_color="blue",command=generate)
button.configure(Text='Generate')
button.place(x=201,y=10)


root.mainloop()
