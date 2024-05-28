import tkinter as tk
from tkinter import ttk
from tkinter import *


def show():
    item = []
    adds = add_option.get()
    service = service_option.get()
    lens = lens_option.get()
    prescription = scrip_option.get()
    item.extend([service, lens, prescription, adds])
    dict = {'Transition Lenses': 'Transition Lenses - $50', 'Anti-Reflective Coating': 'AR Coating - $70',
            'Blue Light Filter': 'Blue Light Filter - $50', 'UV Coating': 'UV Coating - $60',
            'Opticals/Frames': 'Opticals/Frames - $120', 'Eye Care': 'Eye Care - $30', 'Plastic': 'Plastic - $20',
            'Polycarbonate': 'Polycarbonate - $65', 'Glass': 'Glass - $20', 'Single Vision': 'Single Vision - $20',
            'Progressive': 'Progressive - $50', 'Bifocal': 'Bifocal - $75', 'Active': 'Active - $80',
            'High Index': 'High Index - $100', }
    Lb1 = Listbox(window, borderwidth=2, width=20, height=10, fg='black', bg='white', font='Calibri 16')
    count = 0
    for i in range(0, 4):
        Lb1.insert(count, dict[item[i]])
        count += 1
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

    # title
    title_label = ttk.Label(master=window, text="New Patient Vision Intake", font='Calibri 28',
                            background='#f7eae7')
    title_label.grid(row=0, column=6, sticky='n', pady=15, padx=115)

    # widgets/labels
    add_on = ttk.Label(master=window, text='Eye-Wear Add-Ons', font='Calibri 16', background='#f7eae7')
    services = ttk.Label(master=window, text='Custom Services', font='Calibri 16', background='#f7eae7')
    lens_material = ttk.Label(master=window, text='Lens Material', font='Calibri 16', background='#f7eae7')
    scrip_type = ttk.Label(master=window, text="Prescription Type", font='Calibri 16', background='#f7eae7')
    total_label = ttk.Label(master=window, text='Total', font='Calibri 16', background='#f7eae7')
    summary_label = ttk.Label(master=window, text='Order Summary', font='Calibri 16', background='#f7eae7')
    notes = ttk.Label(master=window, text="Notes/Comments", font='Calibri 16', background='#f7eae7')
    comments = Text(height=9, width=114, bg='white', fg='black', font='Calibri 16', borderwidth=10)
    #personal info
    name = ttk.Label(master=window, text='Name:', font='Calibri 16', background='#f7eae7')
    name_input = ttk.Entry(width=25, font='Calibri 14')
    #dob
    dob = ttk.Label(master=window, text='DOB:', font='Calibri 16', background='#f7eae7')
    dob_input = ttk.Entry(width=10, font='Calibri 14')
    #address
    street = ttk.Label(master=window, text='Street:', font='Calibri 16', background='#f7eae7')
    street_input = ttk.Entry(width=25, font='Calibri 14')
    city = ttk.Label(master=window, text='City:', font='Calibri 16', background='#f7eae7')
    city_input = ttk.Entry(width=13, font='Calibri 14')
    zip_code = ttk.Label(master=window, text='Zip Code:', font='Calibri 16', background='#f7eae7')
    zip_input = ttk.Entry(width=10, font='Calibri 14')
    insurance = ttk.Label(master=window, text='Insurance:', font='Calibri 16', background='#f7eae7')

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
    dob_input.place(x=465, y=119)
    street.place(x=420, y=165)
    street_input.place(x=475, y=164)
    city.place(x=420, y=210)
    city_input.place(x=460, y=210)
    zip_code.place(x=590, y=210)
    zip_input.place(x=667, y=210)

    #button
    summaryButton = ttk.Button(window, text="Click for Summary", command=show)
    summaryButton.place(x=910, y=69)

    #run
    window.mainloop()

