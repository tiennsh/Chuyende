import numpy as np
import tensorflow
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title('Fetal Health app')
window['bg'] = "#FFFFCC"
window.geometry('900x600')
s= Label(window, text= "Path image : ", width=0 , font = 50, anchor= 'ne', bg="#FFFFCC")
s.grid(column = 1, row = 1)
ea = Entry(window, width=100 )
ea.grid(column = 2, row = 1)

output = Label(window, text = "", font = 30, fg='#660000', bg="#FFFFCC")
output.place(x=600, y=300)

def image_prediction():
    new_image_path = f"{url()}"
    test_image = tensorflow.keras.utils.load_img(new_image_path, target_size = (224, 224))
    test_image = tensorflow.keras.utils.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    test_image = test_image / 255.0
    model_loaded = tensorflow.keras.models.load_model("D:/Chuyên đề/my_pneumonia_detection_model.h5")
    prediction = model_loaded.predict(test_image)
    if(prediction[0] > 0.5):
        statistic = prediction[0] * 100
        output_text = ("This image is %.3f percent %s"% (statistic, "\nP N E U M O N I A"))
        output.configure(text =f"{output_text}")
    else:
        statistic = (1.0 - prediction[0]) * 100
        output_text = ("This image is %.3f percent %s" % (statistic, "\nN O R M A L"))
        output.configure(text =f"{output_text}")
    window.mainloop()
    return 0

def show_img():
    print(url())
    image = Image.open(f"{url()}")
    image = image.resize((512, 512))

    img = ImageTk.PhotoImage(image)
    panel = Label(window, image=img)
    panel.place(x=20, y=20)
    udl = Button(window, text="Check", bg='#99CCFF', command=image_prediction)
    udl.place(x=600, y=200)
    window.mainloop()

def url():
    path = ea.get()[1:-1].split('\\')

    path_new = ""
    for i in path:
        path_new += f"{i}/"

    return path_new[:-1]




# call and use the function
udl = Button(window, text = "search", bg= '#99CCFF', command=show_img)
udl.grid(column = 3, row = 1)



window.mainloop()

