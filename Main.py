import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import time
from MetroTicketingSystem import MetroTicketingSystem

metro_system = MetroTicketingSystem()

source_entry = None
destination_entry = None
cancel_ticket_entry = None
view_ticket_entry = None
recharge_card_entry = None
recharge_amount_entry = None
check_card_entry = None
name_entry = None
pass_entry = None
show_password = None
admin_name = "user"
admin_password = "user123"

user_window = None
admin_window = None
buy_ticket_window = None
cancel_ticket_window = None
view_ticket_window = None
recharge_card_window = None
check_card_details_window = None
admin_password_window = None


# User Portal ********************************************************
# Purchase Ticket*****************************************************
def buy_ticket():
    try:
        source = int(source_entry.get())
        destination = int(destination_entry.get())

        ticket = metro_system.buy_ticket(source, destination)
        if ticket is None:
            messagebox.showerror("Ticket Purchase Failed", "Ticket purchase failed. Please try again.")
        buy_ticket_window.destroy()    
    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_buy_ticket_window():
    global buy_ticket_window
    buy_ticket_window = tk.Toplevel(window)
    buy_ticket_window.title("Ticket Purchase")
    buy_ticket_window.geometry("300x200")
    buy_ticket_window.iconbitmap(r'C:\\Users\\Family\\Documents\\GitHub\\Metro_System_GUI_Python\\metro.ico')
    buy_ticket_window.configure(bg = "#9e9e9e")

    main_heading = tk.Label(buy_ticket_window, text = "Ticket Purchase", font = ("Helvetica", 10, "bold", "underline"), fg = "#000000", bg = "#9e9e9e")
    main_heading.pack(pady = 20)

    source_label = tk.Label(buy_ticket_window, text = "Source Station:", fg = "#000000", bg = "#9e9e9e")
    source_label.pack()
    global source_entry
    source_entry = tk.Entry(buy_ticket_window)
    source_entry.pack()

    destination_label = tk.Label(buy_ticket_window, text = "Destination Station:", fg = "#000000", bg = "#9e9e9e")
    destination_label.pack()
    global destination_entry
    destination_entry = tk.Entry(buy_ticket_window)
    destination_entry.pack()

    buy_ticket_button = tk.Button(buy_ticket_window, text = "Buy Ticket", command = buy_ticket, bg = "#009688", fg = "#ffffff")
    buy_ticket_button.pack(padx = 10, pady = 10)


# Cancel Ticket*****************************************************
def cancel_ticket():
    try:
        ticket_id = int(cancel_ticket_entry.get())
        refund_amount = metro_system.cancel_ticket(ticket_id)
        if refund_amount is not None:
            messagebox.showinfo("Ticket Canceled", f"Ticket {ticket_id} canceled successfully. Please Collect your Refund amount: Rs.{refund_amount}")
        else:
            messagebox.showerror("Ticket Cancellation Failed", f"Ticket cancellation failed. Ticket ID {ticket_id} not found.")
        cancel_ticket_window.destroy()    
    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_cancel_ticket_window():
    global cancel_ticket_window
    cancel_ticket_window = tk.Toplevel(window)
    cancel_ticket_window.title("Ticket Cancellation")
    cancel_ticket_window.geometry("300x200")
    cancel_ticket_window.iconbitmap(r'C:\\Users\\Family\\Documents\\GitHub\\Metro_System_GUI_Python\\metro.ico')
    cancel_ticket_window.configure(bg = "#9e9e9e")

    main_heading = tk.Label(cancel_ticket_window, text = "Ticket Cancellation", font = ("Helvetica", 10, "bold", "underline"), fg = "#000000", bg = "#9e9e9e")
    main_heading.pack(pady = 20)

    cancel_ticket_label = tk.Label(cancel_ticket_window, text = "Ticket ID to Cancel:", fg = "#000000", bg = "#9e9e9e")
    cancel_ticket_label.pack()
    global cancel_ticket_entry
    cancel_ticket_entry = tk.Entry(cancel_ticket_window)
    cancel_ticket_entry.pack()

    cancel_ticket_button = tk.Button(cancel_ticket_window, text = "Cancel Ticket", command = cancel_ticket, bg = "#009688", fg = "#ffffff")
    cancel_ticket_button.pack(padx = 10, pady = 10)


# View Ticket Information*************************************
def view_ticket_information():
    try:
        ticket_id = int(view_ticket_entry.get())
        metro_system.view_ticket_information(ticket_id)
        view_ticket_window.destroy()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_view_ticket_information_window():
    global view_ticket_window
    view_ticket_window = tk.Toplevel(window)
    view_ticket_window.title("Ticket Information")
    view_ticket_window.geometry("300x200")
    view_ticket_window.iconbitmap(r'C:\\Users\\Family\\Documents\\GitHub\\Metro_System_GUI_Python\\metro.ico')
    view_ticket_window.configure(bg = "#9e9e9e")

    main_heading = tk.Label(view_ticket_window, text = "Ticket Information", font = ("Helvetica", 10, "bold", "underline"), fg = "#000000", bg = "#9e9e9e")
    main_heading.pack(pady = 20)

    view_ticket_label = tk.Label(view_ticket_window, text = "Ticket ID to View:", fg = "#000000", bg = "#9e9e9e")
    view_ticket_label.pack()
    global view_ticket_entry
    view_ticket_entry = tk.Entry(view_ticket_window)
    view_ticket_entry.pack()

    view_ticket_button = tk.Button(view_ticket_window, text = "View Ticket", command = view_ticket_information, bg = "#009688", fg = "#ffffff")
    view_ticket_button.pack(padx = 10, pady = 10)


# Purchase Card*******************************************************
def purchase_card():
    try:
        metro_system.purchase_card()
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Recharge Card*******************************************************
def recharge_card():
    try:
        card_id = recharge_card_entry.get()
        card = metro_system.get_card_by_id(card_id)
        if card is None:
            messagebox.showerror("Card Not Found", "Card not found. Please try again.")
        else:
            recharge_amount = int(recharge_amount_entry.get())
            card.recharge(recharge_amount)
            messagebox.showinfo("Card Recharged", f"Card successfully recharged. New balance: Rs.{card.get_balance()}")
        recharge_card_window.destroy()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_recharge_card_window():
    global recharge_card_window
    recharge_card_window = tk.Toplevel(window)
    recharge_card_window.title("Recharge Card")
    recharge_card_window.geometry("300x200")
    recharge_card_window.iconbitmap(r'C:\\Users\\Family\\Documents\\GitHub\\Metro_System_GUI_Python\\metro.ico')
    recharge_card_window.configure(bg = "#9e9e9e")

    main_heading = tk.Label(recharge_card_window, text = "Recharge Card", font = ("Helvetica", 10, "bold", "underline"), fg = "#000000", bg = "#9e9e9e")
    main_heading.pack(pady = 20)

    recharge_card_label = tk.Label(recharge_card_window, text = "Card ID:", fg = "#000000", bg = "#9e9e9e")
    recharge_card_label.pack()
    global recharge_card_entry
    recharge_card_entry = tk.Entry(recharge_card_window)
    recharge_card_entry.pack()

    recharge_amount_label = tk.Label(recharge_card_window, text = "Recharge Amount:", fg = "#000000", bg = "#9e9e9e")
    recharge_amount_label.pack()
    global recharge_amount_entry
    recharge_amount_entry = tk.Entry(recharge_card_window)
    recharge_amount_entry.pack()

    recharge_card_button = tk.Button(recharge_card_window, text = "Recharge Card", command = recharge_card, bg = "#009688", fg = "#ffffff")
    recharge_card_button.pack(padx = 10, pady = 10)


# Card Information******************************************
def check_card_details():
    try:
        card_id = check_card_entry.get()
        card = metro_system.get_card_by_id(card_id)
        if card is None:
            messagebox.showerror("Card Not Found", "Card not found. Please try again.")
        else:
            messagebox.showinfo("Card Details", f"Card Number: {card.get_id()}\nCard Holder Name: {card.holder_name}\nAvailable Balance: Rs.{card.get_balance()}")
        check_card_details_window.destroy()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_check_card_details_window():
    global check_card_details_window
    check_card_details_window = tk.Toplevel(window)
    check_card_details_window.title("Check Card Details")
    check_card_details_window.geometry("300x200")
    check_card_details_window.iconbitmap(r'C:\\Users\\Family\\Documents\\GitHub\\Metro System (GUI) _ Python\\metro.ico')
    check_card_details_window.configure(bg = "#9e9e9e")

    main_heading = tk.Label(check_card_details_window, text = "Card Information", font = ("Helvetica", 10, "bold", "underline"), fg = "#000000", bg = "#9e9e9e")
    main_heading.pack(pady = 20)

    check_card_label = tk.Label(check_card_details_window, text = "Card ID:", fg = "#000000", bg = "#9e9e9e")
    check_card_label.pack()
    global check_card_entry
    check_card_entry = tk.Entry(check_card_details_window)
    check_card_entry.pack()

    check_card_button = tk.Button(check_card_details_window, text = "Check Card Details", command = check_card_details, bg = "#009688", fg = "#ffffff")
    check_card_button.pack(padx = 10, pady = 10)



# Admin Portal**************************************************
# Total Revenue*************************************************
def calculate_total_revenue():
    try:
        total_revenue = metro_system.calculate_total_revenue()
        messagebox.showinfo("Total Revenue", f"Total Revenue: Rs.{total_revenue}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Average Ticket Price*****************************************
def calculate_average_ticket_price():
    try:
        average_price = metro_system.calculate_average_ticket_price()
        messagebox.showinfo("Average Ticket Price", f"Average Ticket Price: Rs.{average_price}")
    except Exception as e:
        messagebox.showerror("Error", str(e))




# User Portal*******************************************************
def close_user_window():
    response = messagebox.askyesno("Exit", "Do you want to exit?")
    if response:
        user_window.destroy()

def user_window():
    global user_window
    user_window = tk.Toplevel(window)
    user_window.title("User Portal")
    user_window.geometry("300x400")
    user_window.iconbitmap(r'C:\\Users\\Family\\Documents\\GitHub\\Metro System (GUI) _ Python\\metro.ico')
    user_window.configure(bg = "#9e9e9e")

    main_heading = tk.Label(user_window, text = "Welcome to User Portal", font = ("Helvetica", 12, "bold", "underline"), fg = "#000000", bg = "#9e9e9e")
    main_heading.pack(pady=20)

    buy_ticket_button = tk.Button(user_window, text = "Buy Ticket", command = open_buy_ticket_window, width = 20, bg = "#009688", fg = "#ffffff")
    buy_ticket_button.pack(padx = 10, pady = 10)

    cancel_ticket_button = tk.Button(user_window, text = "Cancel Ticket", command = open_cancel_ticket_window, width = 20, bg = "#009688", fg = "#ffffff")
    cancel_ticket_button.pack(padx = 10, pady = 10)

    view_ticket_button = tk.Button(user_window, text = "View Ticket Information", command = open_view_ticket_information_window, width = 20, bg = "#009688", fg = "#ffffff")
    view_ticket_button.pack(padx = 10, pady = 10)

    purchase_card_button = tk.Button(user_window, text = "Purchase Card", command = purchase_card, width = 20, bg = "#009688", fg = "#ffffff")
    purchase_card_button.pack(padx = 10, pady = 10)

    recharge_card_button = tk.Button(user_window, text = "Recharge Card", command = open_recharge_card_window, width = 20, bg = "#009688", fg = "#ffffff")
    recharge_card_button.pack(padx = 10, pady = 10)

    check_card_details_button = tk.Button(user_window, text = "Check Card Details", command = open_check_card_details_window, width = 20, bg = "#009688", fg = "#ffffff")
    check_card_details_button.pack(padx = 10, pady = 10)

    exit_button = tk.Button(user_window, text = "Exit", command = close_user_window, width = 20, bg = "#009688", fg = "#ffffff")
    exit_button.pack(padx = 10, pady = 10)



# Admin Portal*******************************************************
def toggle_password_visibility():
    global show_password
    if show_password.get():
        pass_entry.config(show = "")
    else:
        pass_entry.config(show = "*")

def close_admin_window():
    response = messagebox.askyesno("Exit", "Do you want to exit?")
    if response:
        admin_window.destroy()

def open_admin_window():
    if admin_name == str(name_entry.get()) and admin_password == str(pass_entry.get()):
        admin_password_window.destroy()

        global admin_window
        admin_window = tk.Toplevel(window)
        admin_window.title("Admin Portal")
        admin_window.geometry("300x250")
        admin_window.iconbitmap(r'C:\\Users\\Family\\Documents\\GitHub\\Metro System (GUI) _ Python\\metro.ico')
        admin_window.configure(bg = "#9e9e9e")
    
        main_heading = tk.Label(admin_window, text = "Welcome to Admin Portal", font = ("Helvetica", 12, "bold", "underline"), fg = "#000000", bg = "#9e9e9e")
        main_heading.pack(pady = 20)

        calculate_total_revenue_button = tk.Button(admin_window, text = "Total Revenue", command = calculate_total_revenue, width = 20, bg = "#009688", fg = "#ffffff")
        calculate_total_revenue_button.pack(padx = 10, pady = 10)

        calculate_average_ticket_price_button = tk.Button(admin_window, text = "Average Ticket Price", command = calculate_average_ticket_price, width = 20, bg = "#009688", fg = "#ffffff")
        calculate_average_ticket_price_button.pack(padx = 10, pady = 10)

        exit_button = tk.Button(admin_window, text = "Exit", command = close_admin_window, width = 20, bg = "#009688", fg = "#ffffff")
        exit_button.pack(padx = 10, pady = 10)

    else:
        messagebox.showerror("Error", "Incorrect Username or Password. Please try again")

def open_admin_password_window():
    global admin_password_window
    admin_password_window = tk.Toplevel(window)
    admin_password_window.title("Admin Portal")
    admin_password_window.geometry("300x250")
    admin_password_window.iconbitmap(r'C:\\Users\\Family\\Documents\\GitHub\\Metro System (GUI) _ Python\\metro.ico')
    admin_password_window.configure(bg = "#9e9e9e")
    
    main_heading = tk.Label(admin_password_window, text = "Welcome to Admin Portal", font = ("Helvetica", 12, "bold", "underline"), fg = "#000000", bg = "#9e9e9e")
    main_heading.pack(pady = 20)

    name_label = tk.Label(admin_password_window, text = "Enter Your Username:", fg = "#000000", bg = "#9e9e9e")
    name_label.pack()
    global name_entry
    name_entry = tk.Entry(admin_password_window)
    name_entry.pack()

    pass_label = tk.Label(admin_password_window, text = "Enter Your Password:", fg = "#000000", bg = "#9e9e9e")
    pass_label.pack()
    global pass_entry
    pass_entry = tk.Entry(admin_password_window, show = "*")
    pass_entry.pack()

    global show_password
    show_password = tk.BooleanVar()
    show_password_checkbox = tk.Checkbutton(admin_password_window, text = "Show Password", variable = show_password, command = toggle_password_visibility, bg = "#9e9e9e")
    show_password_checkbox.pack()

    enter_button = tk.Button(admin_password_window, text = "Enter", command = open_admin_window, bg = "#009688", fg = "#ffffff")
    enter_button.pack(padx = 10, pady = 10)



# Close Window function*********************************************
def close_window():
    response = messagebox.askyesno("Exit", "Do you want to exit?")
    if response:
        window.destroy()



# Splash Screen*******************************************************
def show_splash_screen():
    splash_root = tk.Tk()
    splash_root.geometry("550x500")
    splash_root.title("Metro Ticketing System")
    splash_root.iconbitmap(r'C:\\Users\\Family\\Documents\\GitHub\\Metro System (GUI) _ Python\\metro.ico')
    splash_root.configure(bg = "#9e9e9e")

    image = Image.open("C:\\Users\\Family\\Documents\\GitHub\\Metro System (GUI) _ Python\\metro.png")
    photo = ImageTk.PhotoImage(image)

    splash_image = tk.Label(splash_root, image = photo)
    splash_image.pack(pady = 50, padx = 50)

    splash_root.update()

    time.sleep(2)

    splash_root.destroy()


# Main Window*******************************************************
show_splash_screen()
window = tk.Tk()
window.title("Metro Ticketing System")
window.geometry("400x300")
window.iconbitmap(r'C:\\Users\\Family\\Documents\\GitHub\\Metro System (GUI) _ Python\\metro.ico')
window.configure(bg = "#9e9e9e")

main_heading = tk.Label(window, text = "Welcome to Metro Ticketing System", fg = "#000000", bg = "#9e9e9e", font = ("Helvetica", 14, "bold", "underline"))
main_heading.pack(pady=20)

user_button = tk.Button(window, text = "User Portal", command = user_window, width = 20, bg = "#009688", fg = "#ffffff")
user_button.pack(pady = 10)

admin_button = tk.Button(window, text = "Administrator Portal", command = open_admin_password_window, width = 20, bg = "#009688", fg = "#ffffff")
admin_button.pack(pady = 10)

exit_button = tk.Button(window, text = "Exit", command = close_window, width = 20, bg = "#009688", fg = "#ffffff")
exit_button.pack(padx = 10, pady = 10)


window.mainloop()
