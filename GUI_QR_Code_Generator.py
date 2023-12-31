#Creator: Israel Showell
#Date Created: 10-11-23
#Allows a user to create a QR Code by entering a URL of sorts in the directory where the script is located.

# Import the tkinter library for GUI
import tkinter as tk
from tkinter import messagebox

#Imports the qrcode library
import qrcode as q


def generateQRCode():
    
    URL = URL_entry.get() #Gets the text stored in the text area
    
    print(URL) #Prints the entered URL. I used this to figure out some odd errors I was
    
    qr = q.QRCode(
    version=1, #QR Code Version
    error_correction=q.constants.ERROR_CORRECT_L, #Error correction level (L for low), see documentation of the qrcode library
    box_size=10, #Size of each "box" or module in the QR code
    border=4, #Size of the border around the QR code (in modules)
    )

    #Adds the data to the QR code
    qr.add_data(URL)

    qr.make(fit=True)

    # Creates a QR code image
    img = qr.make_image()

    # Saves the QR code image
    img.save("QR_Code.png")



# Creates the main window
root = tk.Tk()
root.title("GUI QRCode Generator")  # Sets the window title

# Creates input fields and labels
URL_label = tk.Label(root, text="Enter your URL:")  # Create a label
URL_label.pack()  # Packs the label into the window
URL_entry = tk.Entry(root)  # Creates an input field to enter the a URL
URL_entry.pack()  # Packs the input field into the window


run_button = tk.Button(root, text="Generate QRCode", command=generateQRCode)  # Creates a button that calls the function
run_button.pack()  # Packs the button into the window

root.mainloop()