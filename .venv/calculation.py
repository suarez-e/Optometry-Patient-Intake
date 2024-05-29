import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image


def show():
    item = []
    item_prices = []
    adds = add_option.get()
    service = service_option.get()
    lens = lens_option.get()
    prescription = scrip_option.get()
    item.extend([service, lens, prescription, adds])
    display_dict = {'Transition Lenses': 'Transition Lenses - $50', 'Anti-Reflective Coating': 'AR Coating - $70',
            'Blue Light Filter': 'Blue Light Filter - $50', 'UV Coating': 'UV Coating - $60',
            'Opticals/Frames': 'Opticals/Frames - $120', 'Eye Care': 'Eye Care - $30', 'Plastic': 'Plastic - $20',
            'Polycarbonate': 'Polycarbonate - $65', 'Glass': 'Glass - $20', 'Single Vision': 'Single Vision - $20',
            'Progressive': 'Progressive - $50', 'Bifocal': 'Bifocal - $75', 'Active': 'Active - $80',
            'High Index': 'High Index - $100', }
    prices = {'Transition Lenses': 50, 'Anti-Reflective Coating': 70, 'Blue Light Filter': 50,
              'UV Coating': 60, 'Opticals/Frames': 120, 'Eye Care': 30, 'Plastic': 20, 'Polycarbonate': 65,
              'Glass': 20, 'Single Vision': 20, 'Progressive': 50, 'Bifocal': 75, 'Active': 80, 'High Index': 100}
    Lb1 = Listbox(window, borderwidth=2, width=20, height=10, fg='black', bg='white', font='Calibri 16')
    count = 0
    for i in range(0, 4):
        Lb1.insert(count, display_dict[item[i]])
        count += 1
    for x in range(0, 4):
        item_prices.append(prices[item[x]])
    total_price = sum(item_prices)
    total = Label(master=window, text='Your total is ${}.00'.format(total_price),
                  font='Calibri 16', bg='white', fg='black')
    total.place(x=918, y=290)
    Lb1.place(x=875, y=120)


if __name__ == '__main__':
    items = []
    # window
    window = tk.Tk()
    window.title("Compton Vision Hub")
    window.geometry('1200x700')
    window.config(bg='#f7eae7')
    style = ttk.Style()
    style.theme_use('clam')
    # creating bg image
    background_image = Image.open('stock photos.png').resize((1200, 700))
    background_image = ImageTk.PhotoImage(background_image)
    # create label for image
    glass_pic = Label(master=window, image=background_image)
    glass_pic.place(x=0, y=0)

    # title
    title_label = ttk.Label(master=window, text="New Patient Vision Intake", font='Calibri 28',
                            background='#c0e7fa')
    title_label.grid(row=0, column=6, sticky='n', pady=15, padx=115)

    # widgets/labels
    add_on = ttk.Label(master=window, text='Eye-Wear Add-Ons', font='Calibri 16', background='#b0d4fc')
    services = ttk.Label(master=window, text='Custom Services', font='Calibri 16', background='#bfe6fa')
    lens_material = ttk.Label(master=window, text='Lens Material', font='Calibri 16', background='#bae0fb')
    scrip_type = ttk.Label(master=window, text="Prescription Type", font='Calibri 16', background='#bae0fb')
    total_label = ttk.Label(master=window, text='Total', font='Calibri 16', background='#f7eae7')
    summary_label = ttk.Label(master=window, text='Order Summary', font='Calibri 16', background='#f7eae7')
    notes = ttk.Label(master=window, text="Notes/Comments", font='Calibri 16', background='#aacefc')
    comments = Text(height=9, width=114, bg='white', fg='black', font='Calibri 16', borderwidth=10)
    #personal info
    name = ttk.Label(master=window, text='Name:', font='Calibri 16', background='#bfe6fa')
    name_input = ttk.Entry(width=25, font='Calibri 14')
    #dob
    dob = ttk.Label(master=window, text='DOB:', font='Calibri 16', background='#bde4fa')
    dob_input = ttk.Entry(width=10, font='Calibri 14')
    #address
    street = ttk.Label(master=window, text='Street:', font='Calibri 16', background='#bbe1fc')
    street_input = ttk.Entry(width=25, font='Calibri 14')
    city = ttk.Label(master=window, text='City:', font='Calibri 16', background='#bbe1fc')
    city_input = ttk.Entry(width=12, font='Calibri 14')
    zip_code = ttk.Label(master=window, text='Zip Code:', font='Calibri 16', background='#bbe1fc')
    zip_input = ttk.Entry(width=10, font='Calibri 14')
    insurance = ttk.Label(master=window, text='Insurance:', font='Calibri 16', background='#f7eae7')
    phone = ttk.Label(master=window, text="Phone Number:", font='Calibri 16', background='#b5dbfb')
    phone_input = ttk.Entry(width=13, font='Calibri 14')
    date_of_visit = ttk.Label(master=window, text='Date of Visit:', font='Calibri 16', background='#b2d8fb')
    date_input = ttk.Entry(width=13, font='Calibri 14')

    add_option = tk.StringVar()
    add_list = [
        "Transition Lenses",
        "Anti-Reflective Coating",
        "Blue Light Filter",
        "UV Coating"
    ]

    service_option = tk.StringVar()
    service_list = [
        "Opticals/Frames",
        "Eye Care",
    ]

    lens_option = tk.StringVar()
    lens_list = [
        "Plastic",
        "Polycarbonate",
        "Glass"
    ]

    scrip_option = tk.StringVar()
    scrip_list = [
        "Single Vision",
        "Progressive",
        "Bifocal",
        "Active",
        "High Index"
    ]

    #create the drop down menu
    add_drop = ttk.OptionMenu(window, add_option, 'Select Add-On', *add_list)
    add_drop.grid(row=3, column=1, sticky='w')
    add_drop.config(width=15)

    service_drop = ttk.OptionMenu(window, service_option, 'Select Service', *service_list)
    service_drop.grid(row=0, column=1, pady=70, sticky='nw')
    service_drop.config(width=15)

    lens_drop = ttk.OptionMenu(window, lens_option, 'Select Material', *lens_list)
    lens_drop.grid(row=1, column=1, sticky='w')
    lens_drop.config(width=15)

    scrip_drop = ttk.OptionMenu(window, scrip_option, 'Select Type', *scrip_list)
    scrip_drop.grid(row=2, column=1, sticky='w')
    scrip_drop.config(width=15)

    #text widgets
    add_on.grid(row=3, column=0, sticky='w', padx=15)
    services.grid(row=0, column=0, sticky='w', padx=15)
    lens_material.grid(row=1, column=0, sticky='w', padx=15)
    scrip_type.grid(row=2, column=0, pady=65, sticky='w', padx=15)
    notes.grid(column=0, row=4, sticky='w', padx=15, pady=65)
    comments.place(x=15, y=485)
    name.place(x=420, y=74)
    name_input.place(x=475, y=73)
    dob.place(x=420, y=120)
    dob_input.place(x=475, y=119)
    street.place(x=420, y=165)
    street_input.place(x=475, y=164)
    city.place(x=420, y=210)
    city_input.place(x=475, y=210)
    zip_code.place(x=590, y=210)
    zip_input.place(x=667, y=210)
    phone.place(x=420, y=255)
    phone_input.place(x=540, y=255)
    date_of_visit.place(x=420, y=295)
    date_input.place(x=520, y=295)

    #button
    summaryButton = ttk.Button(window, text="Click for Summary", command=show)
    summaryButton.place(x=910, y=69)
    print_button = ttk.Button(window, text="Save")
    print_button.place(x=1050, y=15)

    #run
    window.mainloop()

