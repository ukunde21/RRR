# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 20:21:38 2023

@author: shahn
"""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Pillow library for image handling

# Sample data of restaurants (replace with data from your database)
restaurants = [
    {"name": "Restaurant A", "cuisine": "Italian", "location": "City A", "budget": "High", "capacity": 50},
    {"name": "Restaurant B", "cuisine": "Mexican", "location": "City B", "budget": "Medium", "capacity": 30},
    {"name": "Restaurant C", "cuisine": "Italian", "location": "City A", "budget": "Low", "capacity": 40},
    {"name": "Restaurant D", "cuisine": "Chinese", "location": "City C", "budget": "Medium", "capacity": 60},
    {"name": "Restaurant E", "cuisine": "Indian", "location": "City B", "budget": "High", "capacity": 45},
    {"name": "Restaurant F", "cuisine": "Mexican", "location": "City D", "budget": "Low", "capacity": 35},
    # Add more restaurant data here
]

# Initialize recommended_text and recommended_listbox as global variables
recommended_text = None
recommended_listbox = None

# Function to handle restaurant recommendations
def recommend_restaurants():
    selected_cuisine = cuisine_combobox.get()
    selected_location = location_entry.get()
    selected_budget = budget_combobox.get()
    persons = int(persons_entry.get())

    # Filter restaurants based on user input
    recommended_restaurants = [
        restaurant for restaurant in restaurants
        if restaurant["cuisine"] == selected_cuisine
        and restaurant["location"] == selected_location
        and restaurant["budget"] == selected_budget
        and restaurant["capacity"] >= persons
    ]

    # Display up to 5 recommended restaurants with images
    recommended_text.set("Recommended Restaurants:")
    recommended_listbox.delete(0, tk.END)  # Clear previous recommendations

    for i, restaurant in enumerate(recommended_restaurants[:5]):
        restaurant_name = restaurant["name"]
        image_path = f"{restaurant_name.lower().replace(' ', '_')}.jpg"  # Example image filename

        try:
            # Load restaurant image
            img = Image.open(image_path)
            img.thumbnail((100, 100))  # Resize image as needed
            img = ImageTk.PhotoImage(img)

            # Display restaurant name and image
            recommended_listbox.insert(tk.END, f"{i + 1}. {restaurant_name}")
            recommended_listbox.image_create(tk.END, image=img)
            img.image = img  # Keep a reference to the image

        except FileNotFoundError:
            # Handle missing image files
            recommended_listbox.insert(tk.END, f"{i + 1}. {restaurant_name} (Image not found)")

# Create the main window
root = tk.Tk()
root.title("Restaurant Recommender")

# Load and set a background image (replace 'background.jpg' with your image file)
bg_image = Image.open("peakpx (1).jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)


# Create a canvas widget for displaying the background image
canvas = tk.Canvas(root, width=bg_photo.width(), height=bg_photo.height())
canvas.pack()

# Display the background image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

# Create centered text on the canvas
centered_text = "Welcome to Munks Recommendor System!!"
canvas.create_text(
    bg_photo.width() // 2.3, 
    bg_photo.height() // 2, 
    text=centered_text, 
    font=("Clibri", 26,"bold italic"), 
    fill="white"
)
# Function to remove the centered text
def remove_centered_text():
    canvas.delete(centered_text)

# Schedule the removal of the centered text after 3 seconds
root.after(1000, remove_centered_text)




# Display the name of the website in the center
#website_name_label = tk.Label(root, text="My Restaurant Recommender", font=("LazyDog", 24),bg="red")
#website_name_label.place(relx=0.5, rely=0.5, anchor="center")

def create_input_fields(root):
# Create input labels and entry fields directly on the image
    cuisine_label = tk.Label(root, text="Select Cuisine:")
    cuisine_label.place(relx=0.1, rely=0.1)

    cuisine_combobox = ttk.Combobox(root, values=list(set(restaurant["cuisine"] for restaurant in restaurants)))
    cuisine_combobox.place(relx=0.1, rely=0.2)

    location_label = tk.Label(root, text="Enter Location:")
    location_label.place(relx=0.3, rely=0.1)

    location_entry = tk.Entry(root)
    location_entry.place(relx=0.3, rely=0.2)

    budget_label = tk.Label(root, text="Select Budget:")
    budget_label.place(relx=0.5, rely=0.1)

    budget_combobox = ttk.Combobox(root, values=list(set(restaurant["budget"] for restaurant in restaurants)))
    budget_combobox.place(relx=0.5, rely=0.2)

    persons_label = tk.Label(root, text="Number of Persons:")
    persons_label.place(relx=0.7, rely=0.1)

    persons_entry = tk.Entry(root)
    persons_entry.place(relx=0.7, rely=0.2)

    # Search button
    search_button = tk.Button(root, text="Search", command=recommend_restaurants)
    search_button.place(relx=0.5, rely=0.3)
    

    # Recommended restaurants label and listbox with images
    recommended_text = tk.StringVar(value="Recommended Restaurants")
    recommended_label = tk.Label(root, textvariable=recommended_text)
    recommended_label.place(relx=0.4, rely=0.4)
 
    recommended_listbox = tk.Listbox(root, width=50 ,height=7)
    recommended_listbox.place(relx=0.4, rely=0.5)

# Add a delay of 2 seconds before showing the buttons
root.after(2000, lambda: create_input_fields(root))


# Start the Tkinter event loop
root.mainloop()
