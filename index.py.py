import tkinter as tk
from tkinter import Scrollbar, Canvas
from PIL import Image, ImageTk, ImageDraw, ImageFont
import webbrowser

def open_link(link):
    webbrowser.open(link)

def menu_item_selected(item):
    print(f"You selected {item}.")

def draw_menu_items(image, items):
    draw = ImageDraw.Draw(image)
    text_color = (255, 255, 255)
    font_size = 24
    font = ImageFont.truetype("arial.ttf", font_size)

    x = 50
    y = 50

    for item in items:
        draw.text((x, y), item, fill=text_color, font=font)
        x += 150

def on_mousewheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

app = tk.Tk()
app.title("Restaurant Recommendation System")

canvas = Canvas(app)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

yscroll = Scrollbar(app, command=canvas.yview)
yscroll.pack(side=tk.LEFT, fill=tk.Y)
canvas.config(yscrollcommand=yscroll.set)

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.bind_all("<MouseWheel>", on_mousewheel)

background_img = Image.open("homepage_pic.jpg")
new_width = app.winfo_screenwidth()
new_height = app.winfo_screenheight() - 400
background_img = background_img.resize((new_width, new_height), Image.BILINEAR)
draw = ImageDraw.Draw(background_img)

text = "Welcome to MUNKS"
text_color = (255, 255, 255)
font_size = 70
font = ImageFont.truetype("ariali.ttf", font_size)
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
x = (new_width - text_width) // 2
y = (new_height - text_height) // 2

draw.text((x, y), text, fill=text_color, font=font)

new_text = "A Crazy place for crazy foody - Heart of Perfect Food Hangout!"
new_text_color = (255, 255, 255)
new_font_size = 24
new_font = ImageFont.truetype("arial.ttf", new_font_size)
new_text_bbox = draw.textbbox((0, 0), new_text, font=new_font)
new_x = (new_width - new_text_bbox[2] + new_text_bbox[0]) // 2
new_y = y + text_height + 40

draw.text((new_x, new_y), new_text, fill=new_text_color, font=new_font)

menu_items = ["Login", "Signup", "Review", "Contact us", "Exit"]
draw_menu_items(background_img, menu_items)

background_photo = ImageTk.PhotoImage(background_img)
background_label = tk.Label(frame, image=background_photo)
background_label.photo = background_photo
background_label.pack(fill=tk.BOTH, expand=True)

image_frame = tk.Frame(frame)
image_frame.pack(fill=tk.BOTH, expand=True)

image1 = Image.open("food.jpg")
image2 = Image.open("service.jpg")
image3 = Image.open("taste.jpg")

image_width = new_width // 6
image_height = new_height // 6
image1 = image1.resize((image_width, image_height), Image.BILINEAR)
image2 = image2.resize((image_width, image_height), Image.BILINEAR)
image3 = image3.resize((image_width, image_height), Image.BILINEAR)
image1 = ImageTk.PhotoImage(image1)
image2 = ImageTk.PhotoImage(image2)
image3 = ImageTk.PhotoImage(image3)

padding = 150
image_label1 = tk.Label(image_frame, image=image1)
image_label2 = tk.Label(image_frame, image=image2)
image_label3 = tk.Label(image_frame, image=image3)

image_label1.grid(row=0, column=0, padx=padding, pady=padding)
image_label2.grid(row=0, column=1, padx=padding, pady=padding)
image_label3.grid(row=0, column=2, padx=padding, pady=padding)

logo_frame = tk.Frame(frame, bg="lightyellow")
logo_frame.pack(side=tk.BOTTOM, fill=tk.X)

bottom_text_frame = tk.Frame(logo_frame, bg="lightgreen")
bottom_text_frame.pack()

bottom_text = tk.Label(bottom_text_frame, text="For More Details Follow Us On", font=("Arial", 12))
bottom_text.pack()

logo_frame = tk.LabelFrame(logo_frame, bg="lightyellow")
logo_frame.pack()

logo_data = [
    {"path": "logo_1.png", "link": "https://web.whatsapp.com/"},
    {"path": "logo_2.jpg", "link": "https://www.instagram.com/"},
    {"path": "logo_3.png", "link": "https://twitter.com/login?lang=en"},
    {"path": "logo_4.jpg", "link": "https://www.facebook.com/"}
]

logo_widgets = []

for logo_info in logo_data:
    try:
        logo_image = Image.open(logo_info["path"])
        logo_image = logo_image.resize((40, 40), Image.BILINEAR)
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_widget = tk.Label(logo_frame, image=logo_photo, bg="lightyellow", cursor="hand2")
        logo_widget.photo = logo_photo
        logo_widget.pack(side=tk.LEFT, padx=10, pady=10)
        logo_widget.bind("<Button-1>", lambda event, link=logo_info["link"]: open_link(link))
        logo_widgets.append(logo_widget)
    except Exception as e:
        print(f"Error loading logo: {str(e)}")

frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

app.mainloop()
