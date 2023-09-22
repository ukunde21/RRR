import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import * 
from PIL import Image,ImageTk


# Create the main window
root = tk.Tk()
root.title(" MUNKS Restaurant Recommender Review Page")

def rate_and_review_website():
    selected_website = website_dropdown.get()
    rating = rating_scale.get()
    review = review_text.get("1.0", "end-1c")  # Get the review text from the text widget

    if selected_website in ratings_and_reviews:
        # If the website already has a rating and review, append the new one
        existing_rating, existing_review = ratings_and_reviews[selected_website]
        updated_rating = (existing_rating + rating) / 2  # Calculate an average rating
        updated_review = f"{existing_review}\n\n{review}"  # Append the new review
        ratings_and_reviews[selected_website] = (updated_rating, updated_review)
    else:
        # If it's the first rating and review for the website, store them as is
        ratings_and_reviews[selected_website] = (rating, review)

    # Display a pop-up message confirming the rating and review
    message = f"Rating: {rating}\nReview:\n{review}\n\nGiven to {selected_website}"
    messagebox.showinfo("Rating and Review Confirmation", message)

# Function to handle writing a review
#def write_review():
    #rating = rating_var.get()
    #review_text = review_entry.get("1.0", "end-1c")
    
    #if rating == 0:
    #    messagebox.showerror("Error", "Please select a rating.")
   # elif not review_text:
  #      messagebox.showerror("Error", "Please enter a review.")
 #   else:
#        messagebox.showinfo("Thank you!", "Review submitted successfully.")

# Function to open a new window to display selected images
def display_images():
    new_window = tk.Toplevel(root)
    new_window.title("Inserted Images")
    
    if selected_images:
        for image in selected_images:
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(new_window, image=photo)
            image_label.photo = photo  # To prevent the image from being garbage collected
            image_label.pack()

# Function to open a file dialog to choose multiple image files
def browse_images():
    file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif *.bmp")])
    if file_paths:
        for file_path in file_paths:
            # Open and display each selected image
            image = Image.open(file_path)
            selected_images.append(image)

        # Display a pop-up message indicating that images have been added to your website
        message = f"{len(file_paths)} images added to your website!"
        messagebox.showinfo("Image Upload", message)




# Function to handle adding photos
#def add_photos():
    #file_paths = filedialog.askopenfilenames(title="Select Photos")
    # Add your code to save and display the selected photos
    #pass

# Function to handle saving photos
#def save_photos():
    # Add your code to save photos
    #pass

# Function to handle sharing photos
#def share_photos():
    # Add your code to implement sharing functionality
    #pass



#Create a background image.
#my_image=PhotoImage(file="C:/Users/DELL/OneDrive/Desktop/Python/pic4.png")
#lbl=Label(image=my_image)
#bgImage=ImageTk.PhotoImage(file='restro(1).jpg')
#bgLabel=Label(root,image=bgImage)

# Load and set a background image (replace 'background.jpg' with your image file)
#bg_image = Image.open("download.png")
#bg_photo = ImageTk.PhotoImage(bg_image)
#bg_label = tk.Label(root, image=bg_photo)
#bg_label.place(relwidth=1, relheight=1)

#image = PhotoImage(file="download.png")  # Replace "your_image.png" with your image file path
#label = tk.Label(root, image=image)
#label.pack()

# Load the background image using PhotoImage
#background_image = tk.PhotoImage(file="down.png")  # Replace with your image file path
#background_label = tk.Label(root, image=background_image)
#background_label.place(relwidth=1, relheight=1)

# Open the image using PIL (Pillow)
background_img = Image.open("right.png")  # Replace with your image file path

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Resize the image to fit the screen size
background_img = background_img.resize((screen_width, screen_height))

# Convert the resized image to a Tkinter PhotoImage
background_photo = ImageTk.PhotoImage(background_img)

# Create a Label widget to display the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)




#frame=Frame(root,bg='white')
#frame.place(x=554,y=200)

# Create a label for your website name
label = tk.Label(root, text="    MUNKS  REVIEW  PAGE     ", font=("Monotype Corsiva", 35,'bold'))
label.configure(fg="black")
#label.configure(bg="White")
label.pack(pady=40)
 # Create a list of restaurants (replace with your own data)
#restaurants = [" Name of Restaurant 1", "Name of Restaurant 2", " Name of Restaurant 3"]

# Create a horizontal row of restaurant options
#restaurant_frame = ttk.Frame(root)
#restaurant_label = tk.Label(restaurant_frame, text="Select Restaurant you want to rate : " ,font=("Cambria", 20,'bold'))
#restaurant_label.configure(fg="red")
#restaurant_frame.pack(pady=20)
#restaurant_label.pack(side="left")
#restaurant_combobox = ttk.Combobox(restaurant_frame, values=restaurants)
#restaurant_combobox.pack(side="left")

# List of websites
websites = ["Website 1", "Website 2", "Website 3", "Website 4"]

# Dictionary to store website ratings and reviews
ratings_and_reviews = {}

# Label for selecting a website
website_label = tk.Label(root, text=" Select a website : ",fg='red',font=("Georgia", 20,'bold'))
website_label.pack(pady=5)

# Dropdown list to select a website
website_dropdown = ttk.Combobox(root, values=websites)
website_dropdown.pack(pady=5)

# Label for rating
rating_label = tk.Label(root, text=" Rate the website : ",fg='red',font=("Times new roman", 21,'bold'))
rating_label.pack(pady=5)

# Rating scale
rating_scale = tk.Scale(root, from_=1, to=5, orient="horizontal", length=200)
rating_scale.pack(pady=10)

# Label for writing a review
review_label = tk.Label(root, text=" Write a review : ",fg='red',font=("Georgia", 18,'bold'))
review_label.pack(pady=10)

# Text widget for writing a review
review_text = tk.Text(root, height=5, width=40)
review_text.pack(pady=13)

# Button to submit the rating and review
rate_and_review_button = tk.Button(root, text=" Rate and Review",fg="white",bg="Black",font=("Times New Roman", 15,'bold','italic'), command=rate_and_review_website)
rate_and_review_button.pack()

# Label to display "Share your past experience"
label_text = tk.Label(root, text="  You can Share your past experience : ", fg="red",font=("Lucida Calligraphy", 17,'bold'))
#label_text.configure(fg="Black")
label_text.pack( padx =30,pady=10)

# Button to browse for multiple images
browse_button = tk.Button(root, text=" Add Photos to Website ", fg="white",bg="Black",font=("Verdana",13,'bold','italic'),command=browse_images)
browse_button.pack(pady=5)

# Button to display inserted images on a new page
display_button = tk.Button(root, text=" View Images inserted by user ",fg="white",bg="Black",font=("Verdana",13,'bold','italic'), command=display_images)
display_button.pack(pady=5)

# List to store selected images
selected_images = []

# Create a button to add photos
#add_photos_button = tk.Button(root, text="Add Photos", font=("Times new roman",12,'bold','italic'),command=add_photos)
#add_photos_button.pack()



# Create a button to save photos
#save_photos_button = tk.Button(root, text="Save Photos", font=custom_font,fg="white",bg="Black",command=save_photos)
#save_photos_button.pack(pady=10)

# Create a button to share photos
#share_photos_button = tk.Button(root, text="Share Photos",font=custom_font, fg="white",bg="Black",command=share_photos)
#share_photos_button.pack(pady=15)



root.mainloop()