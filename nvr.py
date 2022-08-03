#!/usr/bin/env python3.10 

import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as scrolledtext
from PIL import Image, ImageTk
import subprocess

main_window = tk.Tk()
main_window.title("nvr")
main_window.geometry('900x800+0+0')
main_window.configure(bg="#702963")
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(2, weight=1)
main_window.rowconfigure(3, weight=1)
main_window.rowconfigure(4, weight=1)
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)
main_window.columnconfigure(3, weight=1)
main_window.columnconfigure(4, weight=1)
# Formatting of the main window

nvrlogo = ImageTk.PhotoImage(Image.open(r"nvrlogo.png")) 
main_label = tk.Label(main_window, image=nvrlogo, bg="#702963")
main_label.grid(row=0, column=1, sticky="w", padx=10)
sub_label = tk.Label(main_window, text="E-Z recon tool", font="bold", fg="white", bg="#702963")
sub_label.configure(font=("Arial", 30))
sub_label.grid(row=0, column=1, sticky="e")
topleft_frame = tk.Frame(main_window)
topleft_frame.configure(bg="#702963")
topleft_frame.grid(row = 2, column =1, padx=10, pady=10, sticky ="nw")
topleft_frame.rowconfigure(0, weight=1)
topleft_frame.rowconfigure(1, weight=1)
topleft_frame.rowconfigure(2, weight=1)
topleft_frame.rowconfigure(3, weight=1)
topleft_frame.rowconfigure(4, weight=1)
topleft_frame.rowconfigure(5, weight=1)
topleft_frame.rowconfigure(6, weight=1)
eye = (Image.open("eye.png"))
resized_eye = eye.resize((50,32), Image.ANTIALIAS)
eyeicon = ImageTk.PhotoImage(resized_eye) 
eye_label = tk.Label(topleft_frame, image=eyeicon, 
    text="   Start here to begin your scan:", 
    compound="left", font="bold", fg="white", bg="#702963")
eye_label.configure(font=("Arial", 16))
eye_label.grid(row=0, sticky="", pady=15)
# Top Left frames with eye, instructions and entry fields.
#Additionally, topleft frame with rows and the eye icon.

IP_input = tk.Label(topleft_frame, text = "IP or Subnet (format: '192.168.56.101' or '192.168.56.1/24')", 
    font="bold", fg="white", bg="#702963")
IP_input.grid(row=1, sticky="w", padx=10, pady=10) 
IP_input_area = tk.Entry(topleft_frame, width = 30, fg="#702963", bg="#CBC3E3")
IP_input_area.grid(row=2, sticky="w", padx=10, pady=10)
# Label and Area for IP Input

def clear_fields():
    IP_input_area.delete(0, END)
    filename_input_area.delete(0, END)
    var_ping.set(0)
    var_tcp.set(0)
    var_udp.set(0)
    var_os.set(0)
    var_sversion.set(0)
    var_verb.set(0)
    var_out.set(0) 
# Function to clear input fields.

clear_fields_button = tk.Button(topleft_frame, text = "Clear IP and Options", fg="#702963", bg="#CBC3E3", width = 20, command = clear_fields)
clear_fields_button.grid(row=5, sticky="w", padx=10, pady=20)
# Button to trigger field-clearing function

topright_frame = tk.Frame(main_window)
topright_frame.configure(bg="#702963")
topright_frame.grid(row = 2, column =2, padx=10, pady=10, sticky ="nw")
# Top-Right frame with check boxes and submit button.

topright_frame.rowconfigure(0, weight=1)
topright_frame.rowconfigure(1, weight=1)
topright_frame.rowconfigure(2, weight=1)
topright_frame.rowconfigure(3, weight=1)
topright_frame.rowconfigure(4, weight=1)
topright_frame.rowconfigure(5, weight=1)
topright_frame.rowconfigure(6, weight=1)
topright_frame.rowconfigure(7, weight=1)
topright_frame.rowconfigure(8, weight=1)
topright_frame.rowconfigure(9, weight=1)
topright_frame.rowconfigure(10, weight=1) # Let's do this button
# topright_frame.rowconfigure(XX, weight=1) # Vuln scan button; item for later versions
# Top-right frame rows.

Label(topright_frame, text="Scan options:", 
    font="bold", fg="white", bg="#702963").grid(row=0, sticky='w', padx=10, pady=10)
# Scan options label. 

var_ping = IntVar()
var_tcp = IntVar()
var_udp = IntVar()
var_os = IntVar()
var_sversion = IntVar()
var_verb = IntVar()
var_out = IntVar()
# Checkbox variables. Might get rid of these later.

Button1_ping = Checkbutton(topright_frame, text="Ping ", 
                variable=var_ping, 
                font="bold", fg="#702963", bg="#CBC3E3", 
                onvalue=1, 
                offvalue=0,
                height = 1,
                width = 20,
                anchor="w")

Button2_tcp = Checkbutton(topright_frame, text="TCP Connections ", 
                variable=var_tcp, 
                font="bold", fg="#702963", bg="#CBC3E3", 
                onvalue=1, 
                offvalue=0,
                height = 1,
                width = 20,
                anchor="w")

Button3_udp = Checkbutton(topright_frame, text="UDP Connections ", 
                variable=var_udp, 
                font="bold", fg="#702963", bg="#CBC3E3", 
                onvalue=1, 
                offvalue=0,
                height = 1,
                width = 20,
                anchor="w")

Button4_os = Checkbutton(topright_frame, text="OS and Services ", 
                variable=var_os, 
                font="bold", fg="#702963", bg="#CBC3E3", 
                onvalue=1, 
                offvalue=0,
                height = 1,
                width = 20,
                anchor="w")

Button5_sv = Checkbutton(topright_frame, text="Service Versions ", 
                variable=var_sversion, 
                font="bold", fg="#702963", bg="#CBC3E3", 
                onvalue=1, 
                offvalue=0,
                height = 1,
                width = 20,
                anchor="w")

Button6_v = Checkbutton(topright_frame, text="Verbosity ", 
                variable=var_verb, 
                font="bold", fg="#702963", bg="#CBC3E3", 
                onvalue=1, 
                offvalue=0,
                height = 1,
                width = 20,
                anchor="w")

Button7_v = Checkbutton(topright_frame, text="Output File", 
                variable=var_out, 
                font="bold", fg="#702963", bg="#CBC3E3", 
                onvalue=1, 
                offvalue=0,
                height = 1,
                width = 20,
                anchor="w")

Button1_ping.grid(row=1, sticky='w')
Button2_tcp.grid(row=2, sticky='w')
Button3_udp.grid(row=3, sticky='w')
Button4_os.grid(row=4, sticky='w')
Button5_sv.grid(row=5, sticky='w')
Button6_v.grid(row=6, sticky='w')
Button7_v.grid(row=7, sticky='w')

filename_input = tk.Label(topright_frame, text = "If output, enter filename:", 
    font="bold", fg="white", bg="#702963")
filename_input.grid(row=8, sticky="w", padx=10, pady=10) 
filename_input_area = tk.Entry(topright_frame, width = 30, fg="#702963", bg="#CBC3E3")
filename_input_area.grid(row=9, sticky="w", padx=10, pady=10)

def flagMatcher():
    ping = var_ping.get()
    tcp = var_tcp.get()
    udp = var_udp.get()
    os = var_os.get()
    sversion = var_sversion.get()
    verb = var_verb.get()
    out = var_out.get()
    flagArray = [ping, tcp, udp, os, sversion, verb, out]
    argsArray = ["-sn", "-sT", "-sU", "-A", "-sV", "-v", "-oN"] 
    commandArray = ["sudo", "nmap", "--unique"]
    for i in range(0,len(flagArray)):
        # iterates through the numbers 0-length of flagArray
        match flagArray[i]:
        # references flagArray at the iterated index
            case 0:
            # if the value of the iterated index is 0, nothing happens.
                continue
            case 1:
            # if the value of the iterated index is 1, print argsArray at the same index
                commandArray.append(argsArray[i])
    return commandArray
 
    
def nmap_scan():
    commandArray = flagMatcher()
    if filename_input_area.get() != "":
        commandArray.append(filename_input_area.get())
    else:
        commandArray = commandArray
    commandArray.append(IP_input_area.get())
    response = subprocess.check_output(commandArray)
    return response 
outputframe = tk.Frame(main_window)
outputframe.grid(row=3, column=0, columnspan=4, padx=5, pady=5)
def terminalOutput():
    message=nmap_scan()
    scrollbar = Scrollbar(outputframe)
    output_box = tk.Text(outputframe, width=80, height=10, yscrollcommand=scrollbar.set, fg="#702963", bg="#CBC3E3")
    scrollbar.config(command=output_box.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    output_box.pack(side="left")
    output_box.insert(tk.END, message)
    output_box.see(tk.END)

# def openVulnScanWindow():  <--- hold for future inclusion of vuln scanner
     
#     # Toplevel object which will
#     # be treated as a new window
#     newWindow = Toplevel(main_window)
#     newWindow.configure(bg="#702963")
#     newWindow.title("Vuln Scan Results")
#     newWindow.geometry("900x700+50+0")
#     newWindow.rowconfigure(0, weight=1)
#     newWindow.rowconfigure(2, weight=1)
#     newWindow.rowconfigure(3, weight=1)
#     newWindow.rowconfigure(4, weight=1)
#     newWindow.columnconfigure(0, weight=1)

#     main_label2 = tk.Label(newWindow, image=nvrlogo, bg="#702963")
#     main_label2.grid(row=0, column=0, sticky="ew", padx=10)
#     sub_label2 = tk.Label(newWindow, text="Vulnerability Scan Results", font="bold", fg="white", bg="#702963")
#     sub_label2.configure(font=("Arial", 30))
#     sub_label2.grid(row=1, column=0, sticky="ew")
    
#     # Formatting of the newWindow
#     outputframe2 = tk.Frame(newWindow)
#     outputframe2.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
#     VulnMessage="Vuln Output"
#     VSscrollbar = Scrollbar(outputframe2)
#     VSoutput_box = tk.Text(outputframe2, width=80, height=10, yscrollcommand=VSscrollbar.set, fg="#702963", bg="#CBC3E3")
#     VSscrollbar.config(command=VSoutput_box.yview)
#     VSscrollbar.pack(side=RIGHT, fill=Y)
#     VSoutput_box.pack(side="left")
#     VSoutput_box.insert(tk.END, VulnMessage)
#     VSoutput_box.see(tk.END)
#     submit_button = tk.Button(newWindow, text = "Close Window", width = 20, fg="white", bg="#770737", command = newWindow.destroy)
#     submit_button.grid(row=4, column=0, padx=5, pady=10) 

def clear_output():
    for widgets in outputframe.winfo_children():
        widgets.destroy()
    
clear_button=tk.Button(main_window, text = "Clear Results", fg="white", bg="#770737", command = clear_output)
clear_button.grid(row=4, column=3, padx=10, pady=10, sticky="e")
clear_button_label = tk.Label(main_window, text = "Please clear results before starting new scan.", 
fg="white", bg="#702963")
clear_button_label.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="e")
# Clear button

submit_button = tk.Button(topright_frame, text = "Let's Do This!", fg="white", bg="#770737", width = 20, command = terminalOutput)
submit_button.grid(row=10, sticky="w", padx=5, pady=10) 
# button to conduct nmap scan

# hold below for future vuln scan inclusion:
# submit_button = tk.Button(topright_frame, text = "Second, vuln scan results", fg="white", bg="#770737", width = 20, command = openVulnScanWindow)
# submit_button.grid(row=XX, sticky="w", padx=5, pady=0) 
# button to open new window with vuln scan results

exit_button=tk.Button(main_window, text = "Exit nvr", fg="white", bg="#770737", command = main_window.destroy)
exit_button.grid(row=4, column=1, padx=10, pady=10, sticky="w")
main_window.mainloop()
# The app exit button, and the loop running the window itself. 
