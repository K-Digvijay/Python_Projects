from tkinter import *
from tkinter import messagebox
import requests
from PIL import ImageTk,Image
from io import BytesIO
import urllib.parse
import requests


class Request:
    def __init__(self,method,args):
        self.args = args
        self.method = method
inc = 0
def fetch_information(title,poster,date,rating):
    global inc
    inc = inc+1
    text[f'a{inc}'].config(text=title)
    if poster !='N/A':
        response = requests.get(poster)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        resized_image = img.resize((140,200))
        photo2 = ImageTk.PhotoImage(resized_image)
        image[f'b{inc}'].config(image=photo2)
        image[f'b{inc}'].image=photo2
    else:
        image[f'b{inc}'].config(text="No change")



def show_menu(event):
    menu.post(event.x_root,event.y_root)

def search_menu():
    global inc
    request  = Request('GET',{'search':Search.get()})


    if request.method == 'GET':
        search = urllib.parse.quote(request.args.get('search',''))
        url = f"https://www.googleapis.com/books/v1/volumes?q={search}&maxResults=5"
        response = requests.get(url)
        #print(response.json())

        if response.status_code==200: # 200 means the request was successful, 404 unauthorised
            data = response.json()
            for item in data.get('items',[]):
                volume_info = item.get('volumeInfo',{})
                title = volume_info.get('title','N/A')
                publisher = volume_info.get('publisher','N/A')
                published_data = volume_info.get('publishedDate','N/A')
                author= volume_info.get('authors',['N/A'])
                rating = volume_info.get('averageRating',['N/A'])
                image_links = volume_info.get('imageLink',{})
                image = image_links.get('thumbnail','N/A')
               

                fetch_information(title,image,published_data,rating)


                print(title)
                print(publisher)
                print(published_data)
                print(author)
                print(rating)
                print(image)

                #fetch_information(title,publisher,published_data,author,rating,image)

                if check_var.get() or check_var1.get():
                    frame11.place(x=160,y=600)
                    frame21.place(x=360,y=600)
                    frame31.place(x=560,y=600)
                    frame41.place(x=760,y=600)
                    frame51.place(x=960,y=600)
                else:
                    frame11.place_forget()
                    frame21.place_forget()
                    frame31.place_forget()
                    frame41.place_forget()
                    frame51.place_forget()

        else:
            print(f"Error: {response.status_code}")
            messagebox.showinfo("Info","Fail to fetch data from Google Books API")


root = Tk()
root.title("Book Recoment System")
root.geometry("1250x700+150+50")
root.config(bg="#111119")
root.resizable(False,False)

# 
icon_image = PhotoImage(file ='D:\TinkerForm\Recoment_system\icon.png')
root.iconphoto(False,icon_image)

# background
heading_image = PhotoImage(file='D:\TinkerForm\Recoment_system\\background.png')
Label(root,image=heading_image,bg='#111119').pack()

logo_image = PhotoImage(file='D:\TinkerForm\Recoment_system\logo.png')
Label(root,image=logo_image,bg='#0099ff').place(x=300,y=80)

heading = Label(root,text='BOOK RECOMENDATION',bg='#0099ff',font=('leto', 30, 'bold'))
heading.place(x=410,y=90)

#search background
search_background = PhotoImage(file='D:\TinkerForm\Recoment_system\Rectangle 2.png')
Label(root,image=search_background,bg='#0099ff').place(x=300,y=155)

#entry search box
Search = StringVar()
Search_entry = Entry(root,textvariable=Search,width=22,font=('leto', 30, 'bold'))
Search_entry.place(x=400,y=170)

recomend_button_image = PhotoImage(file='D:\TinkerForm\Recoment_system\Search.png')
recomend_button = Button(root, image=recomend_button_image,bg='#0099ff',bd=0,activebackground='#252532',cursor='hand2',command=search_menu)
recomend_button.place(x=888,y=169)

setting_button_image = PhotoImage(file='D:\TinkerForm\Recoment_system\setting.png')
setting_button = Button(root, image=setting_button_image,bg='#0099ff',bd=0,activebackground='#252532',cursor='hand2')
setting_button.place(x=1050,y=173)
setting_button.bind('<Button-1>',show_menu)


menu = Menu(root,tearoff=0)
check_var = BooleanVar()
menu.add_checkbutton(label='Publish Date',variable=check_var,
                     command=lambda: print(f"check option is {'checked' if check_var.get() else 'unchecked'}"))

check_var1 = BooleanVar()
menu.add_checkbutton(label='rating',variable=check_var1,
                     command=lambda: print(f"Rating check option is {'checked' if check_var1.get() else 'unchecked'}"))



logout_button_image = PhotoImage(file='D:\TinkerForm\Recoment_system\logout.png')
logout_button = Button(root, image=logout_button_image,bg='#0099ff',bd=0,activebackground='#252532',cursor='hand2',
                       command=lambda : root.destroy())
logout_button.place(x=1150,y=20)

frame1 = Frame(root,width=150,height=240,bg='white')
frame1.place(x=160,y=350)

frame2 = Frame(root,width=150,height=240,bg='white')
frame2.place(x=360,y=350)

frame3 = Frame(root,width=150,height=240,bg='white')
frame3.place(x=560,y=350)

frame4 = Frame(root,width=150,height=240,bg='white')
frame4.place(x=760,y=350)

frame5 = Frame(root,width=150,height=240,bg='white')
frame5.place(x=960,y=350)


text = {'a1': Label(frame1,text="Book Title",font=('arial',10),fg='green'),
        'a2': Label(frame2,text="Book Title",font=('arial',10),fg='green'),
        'a3': Label(frame3,text="Book Title",font=('arial',10),fg='green'),
        'a4': Label(frame4,text="Book Title",font=('arial',10),fg='green'),
        'a5': Label(frame5,text="Book Title",font=('arial',10),fg='green')}
text['a1'].place(x=10,y=2)
text['a2'].place(x=10,y=2)
text['a3'].place(x=10,y=2)
text['a4'].place(x=10,y=2)
text['a5'].place(x=10,y=2)


image = {'b1':Label(frame1),
         'b2':Label(frame1),
         'b3':Label(frame1),
         'b4':Label(frame1),
         'b5':Label(frame1)}
image['b1'].place(x=3,y=30)
image['b2'].place(x=3,y=30)
image['b3'].place(x=3,y=30)
image['b4'].place(x=3,y=30)
image['b5'].place(x=3,y=30)


frame11 = Frame(root,width=150,height=50,bg='#6e6e6e')
#frame11.place(x=160,y=600)

frame21 = Frame(root,width=150,height=50,bg='#6e6e6e')
#frame21.place(x=360,y=600)

frame31 = Frame(root,width=150,height=50,bg='#6e6e6e')
#frame31.place(x=560,y=600)

frame41 = Frame(root,width=150,height=50,bg='#6e6e6e')
#frame41.place(x=760,y=600)

frame51 = Frame(root,width=150,height=50,bg='#6e6e6e')
#frame51.place(x=960,y=600)


#publish date

text2 = {'a11':Label(frame11,fg='red',text='Date',font=('arial',10),bg='#6e6e6e'),
         'a21':Label(frame21,fg='red',text='Date',font=('arial',10),bg='#6e6e6e'),
         'a31':Label(frame31,fg='red',text='Date',font=('arial',10),bg='#6e6e6e'),
         'a41':Label(frame41,fg='red',text='Date',font=('arial',10),bg='#6e6e6e'),
         'a51':Label(frame51,fg='red',text='Date',font=('arial',10),bg='#6e6e6e')}
text2['a11'].place(x=20,y=2)
text2['a21'].place(x=20,y=2)
text2['a31'].place(x=20,y=2)
text2['a41'].place(x=20,y=2)
text2['a51'].place(x=20,y=2)

#rating
text3 = {'a11':Label(frame11,text='Rating',font=('arial',10),bg='#6e6e6e'),
         'a21':Label(frame21,text='Rating',font=('arial',10),bg='#6e6e6e'),
         'a31':Label(frame31,text='Rating',font=('arial',10),bg='#6e6e6e'),
         'a41':Label(frame41,text='Rating',font=('arial',10),bg='#6e6e6e'),
         'a51':Label(frame51,text='Rating',font=('arial',10),bg='#6e6e6e')}
text3['a11'].place(x=20,y=30)
text3['a21'].place(x=20,y=30)
text3['a31'].place(x=20,y=30)
text3['a41'].place(x=20,y=30)
text3['a51'].place(x=20,y=30)



root.mainloop()