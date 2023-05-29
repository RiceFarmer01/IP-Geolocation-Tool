import tkinter as tk
import requests

def fetch_data():
    ip_address = entry.get()
    api_key = "72c225ff7f2092"  # Replace with your IPInfo API key
    url = f"https://ipinfo.io/{ip_address}?token={api_key}"
    session = requests.Session()
    response = session.get(url)
    if response.status_code == 200:
        data = response.json()
        city_var.set(data['city'])
        region_var.set(data['region'])
        country_var.set(data['country'])
        isp_var.set(data['org'])
        lat_var.set(data['loc'].split(',')[0])
        long_var.set(data['loc'].split(',')[1])
    else:
        city_var.set("")
        region_var.set("")
        country_var.set("")
        isp_var.set("")
        lat_var.set("")
        long_var.set("")

root = tk.Tk()
root.title("IP Geolocation")
root.geometry("500x250")
root.configure(bg="#121212")

frame = tk.Frame(root, bg="#1e1e1e", padx=10, pady=10, bd=2, relief=tk.FLAT)
frame.pack(fill=tk.BOTH, expand=True)

label = tk.Label(frame, text="Enter IP address:", bg="#1e1e1e", fg="white", font=("Helvetica", 12))
label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(frame, width=20, font=("Helvetica", 12))
entry.grid(row=0, column=1, padx=5, pady=5)

button = tk.Button(frame, text="Fetch Data", command=fetch_data, bg="#121212", fg="white", font=("Helvetica", 12))
button.grid(row=0, column=2, padx=5, pady=5)

city_var = tk.StringVar()
city_label = tk.Label(frame, textvariable=city_var, bg="#1e1e1e", fg="white", font=("Helvetica", 12))
city_label.grid(row=1, column=0, padx=5, pady=5)

region_var = tk.StringVar()
region_label = tk.Label(frame, textvariable=region_var, bg="#1e1e1e", fg="white", font=("Helvetica", 12))
region_label.grid(row=1, column=1, padx=5, pady=5)

country_var = tk.StringVar()
country_label = tk.Label(frame, textvariable=country_var, bg="#1e1e1e", fg="white", font=("Helvetica", 12))
country_label.grid(row=1, column=2, padx=5, pady=5)

isp_var = tk.StringVar()
isp_label = tk.Label(frame, textvariable=isp_var, bg="#1e1e1e", fg="white", font=("Helvetica", 12))
isp_label.grid(row=2, column=0, padx=5, pady=5)

lat_var = tk.StringVar()
lat_label = tk.Label(frame, textvariable=lat_var, bg="#1e1e1e", fg="white", font=("Helvetica", 12))
lat_label.grid(row=2, column=1, padx=5, pady=5)

long_var = tk.StringVar()
long_label = tk.Label(frame, textvariable=long_var, bg="#1e1e1e", fg="white", font=("Helvetica", 12))
long_label.grid(row=2, column=2, padx=5, pady=5)

tk.Grid.columnconfigure(frame, 0, weight=1)
tk.Grid.columnconfigure(frame, 1, weight=1)
tk.Grid.columnconfigure(frame, 2, weight=1)
tk.Grid.rowconfigure(frame, 0, weight=1)
tk.Grid.rowconfigure(frame, 1, weight=1)
tk.Grid.rowconfigure(frame, 2, weight=1)

made_by_label = tk.Label(root, text="Made by Jaiden", bg="#121212", fg="white", font=("Helvetica", 8, "bold"))
made_by_label.pack(side=tk.LEFT, padx=5, pady=5)

def open_link(event):
    import webbrowser
    webbrowser.open("https://github.com/RiceFarmer01")

link_label = tk.Label(root, text="https://github.com/RiceFarmer01", bg="#121212", fg="white", font=("Helvetica", 8, "bold"), cursor="hand2")
link_label.pack(side=tk.LEFT, padx=5, pady=5)
link_label.bind("<Button-1>", open_link)
link_label.bind("<Enter>", lambda e: link_label.configure(fg="cyan"))
link_label.bind("<Leave>", lambda e: link_label.configure(fg="white"))

root.mainloop()
