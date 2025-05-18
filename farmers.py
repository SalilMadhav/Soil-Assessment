import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from math import *
from py import *

def fertility_score_acidic(ph, moisture):
    if 4.5 <= ph <= 5.5:
        ph_score = 50
    elif 5.5 < ph <= 8.0:
        ph_score = 10
    else:
        ph_score = 0

    if 20 <= moisture <= 60:
        moisture_score = 50
    elif 60 < moisture <= 100:
        moisture_score = 10
    else:
        moisture_score = 0

    return ph_score + moisture_score

def fertility_score_normal(ph, moisture):
    if 6.0 <= ph <= 7.0:
        ph_score = 50
    elif 7.1 <= ph <= 8.0:
        ph_score = 10
    else:
        ph_score = 0

    if 20 <= moisture <= 60:
        moisture_score = 50
    elif 60 < moisture <= 100:
        moisture_score = 10
    else:
        moisture_score = 0

    return ph_score + moisture_score

# Define colors for both Light and Dark modes
LIGHT_MODE = {
    "bg": "#ecf0f1", "fg": "#2c3e50", "button_bg": "#3498db", "button_fg": "white", 
    "active_bg": "#2980b9", "input_bg": "white", "input_fg": "black"
}

DARK_MODE = {
    "bg": "#2c3e50", "fg": "#ecf0f1", "button_bg": "#34495e", "button_fg": "white", 
    "active_bg": "#1abc9c", "input_bg": "#34495e", "input_fg": "white"
}

current_mode = LIGHT_MODE  # Default mode is Light Mode

def toggle_dark_mode():
    global current_mode
    if current_mode == LIGHT_MODE:
        current_mode = DARK_MODE
    else:
        current_mode = LIGHT_MODE
    
    # Update the window's background color
    root.configure(bg=current_mode["bg"])
    
    # Update the title and labels
    title_label.config(bg=current_mode["bg"], fg=current_mode["fg"])
    
    # Update button styles
    style.configure("TButton", background=current_mode["button_bg"], foreground=current_mode["button_fg"])
    style.map("TButton", background=[('active', current_mode["active_bg"])])
    
    # Update input fields
    entry_ph.config(bg=current_mode["input_bg"], fg=current_mode["input_fg"])
    entry_moisture.config(bg=current_mode["input_bg"], fg=current_mode["input_fg"])
    
    # Update all labels in the app
    for label in root.winfo_children():
        if isinstance(label, ttk.Label):
            label.config(bg=current_mode["bg"], fg=current_mode["fg"])
        if isinstance(label, ttk.Button):
            label.config(bg=current_mode["button_bg"], fg=current_mode["button_fg"])

def assess_acidic_plants(ph):
    if 4.5 <= ph <= 5.5:
        return "✅ Your soil pH is ideal for acidic plants."
    elif ph < 4.5:
        return "⚠️ Too acidic! Consider adding a base like:\n - Calcium Carbonate (CaCO₃)\n - Wood Ash\n - Dolomitic Lime"
    else:
        return "⚠️ Too alkaline! Consider adding an acid like:\n - Sulfur\n - Peat Moss\n - Citric Acid (Vinegar)"

def assess_normal_plants(ph):
    if 6.0 <= ph <= 7.0:
        return "✅ Your soil pH is ideal for neutral or alkaline plants."
    elif ph < 6.0:
        return "⚠️ Too acidic! Consider adding a base like:\n - Calcium Carbonate (CaCO₃)\n - Dolomitic Lime"
    else:
        return "⚠️ Too alkaline! Consider adding an acid like:\n - Sulfur\n - Aluminum Sulfate\n - Vinegar"

def calculate_fertility():
    try:
        ph = float(entry_ph.get())
        moisture = int(entry_moisture.get())
        plant_type = plant_var.get()

        if moisture < 20:
            messagebox.showwarning("Moisture Alert", "⚠️ Soil is too dry! Consider watering more.")
        elif moisture > 100:
            messagebox.showwarning("Moisture Alert", "⚠️ Soil moisture too high! Ensure proper drainage.")

        if plant_type == "Acidic":
            assessment = assess_acidic_plants(ph)
            score = fertility_score_acidic(ph, moisture)
        else:
            assessment = assess_normal_plants(ph)
            score = fertility_score_normal(ph, moisture)

        result_text = f"Assessment:\n{assessment}\n\nFertility Score: {score}/100"
        messagebox.showinfo("Soil Assessment Result", result_text)
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for pH and moisture.")

# --- Main Window Setup ---
root = tk.Tk()
root.title("🌱 Soil Assessment Tool")
root.geometry("420x400")
root.configure(bg="#ecf0f1")

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Segoe UI", 11), background="#ecf0f1", foreground="#2c3e50")
style.configure("TButton", font=("Segoe UI", 11, "bold"), background="#3498db", foreground="white")
style.map("TButton", background=[('active', '#2980b9')])

# Title Label
title_label = ttk.Label(root, text="Soil pH & Moisture Assessment", font=("Segoe UI", 16, "bold"))
title_label.pack(pady=15)

# Input Frame
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

# pH Input
ttk.Label(input_frame, text="Enter Soil pH (0.0 - 14.0):").grid(row=0, column=0, padx=10, pady=8, sticky='w')
entry_ph = ttk.Entry(input_frame, width=30)
entry_ph.grid(row=0, column=1, pady=8)

# Moisture Input
ttk.Label(input_frame, text="Enter Soil Moisture (0 - 100):").grid(row=1, column=0, padx=10, pady=8, sticky='w')
entry_moisture = ttk.Entry(input_frame, width=30)
entry_moisture.grid(row=1, column=1, pady=8)

# Plant Type Radio Buttons
ttk.Label(input_frame, text="Is your plant acidic?").grid(row=2, column=0, padx=10, pady=12, sticky='w')
plant_var = tk.StringVar(value="Acidic")
radio_frame = ttk.Frame(input_frame)
radio_frame.grid(row=2, column=1, pady=5, sticky='w')

ttk.Radiobutton(radio_frame, text="Yes (Acidic)", variable=plant_var, value="Acidic").pack(anchor="w")
ttk.Radiobutton(radio_frame, text="No (Normal)", variable=plant_var, value="Normal").pack(anchor="w")

# Calculate Button
calc_button = ttk.Button(root, text="🌿 Calculate Soil Assessment", command=calculate_fertility)
calc_button.pack(pady=25)

# Dark Mode Toggle Button
dark_mode_button = ttk.Button(root, text="🌓 Toggle Dark Mode", command=toggle_dark_mode)
dark_mode_button.pack(pady=10)

root.mainloop()