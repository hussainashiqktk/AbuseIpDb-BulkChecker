import requests
import json
import tkinter as tk
from tkinter import ttk, messagebox


def bulk_check(ip_list, output_box, table):
    # Hardcoded API key
    api_key = "" # USE YOUR OWN API
    
    table.delete(*table.get_children())  # Clear the table
    output_box.delete("1.0", tk.END)  # Clear the output box
    
    ip_list = ip_list.strip().split("\n")  # Split IPs by new lines
    total_ips = len(ip_list)
    if total_ips == 0:
        output_box.insert(tk.END, "No IPs entered. Please provide IPs to check.\n")
        return

    progress_bar["value"] = 0
    progress_bar["maximum"] = total_ips

    for i, ip in enumerate(ip_list):
        ip = ip.strip()
        if not ip:
            continue

        try:
            response = requests.get(
                f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}",
                headers={
                    "Accept": "application/json",
                    "Key": api_key
                },
            )
            if response.status_code == 200:
                data = response.json().get("data", {})
                table.insert("", "end", values=(
                    data.get("ipAddress", "N/A"),
                    data.get("abuseConfidenceScore", "N/A"),
                    data.get("isp", "N/A"),
                    data.get("domain", "N/A"),
                    data.get("countryCode", "N/A"),
                    data.get("totalReports", "N/A"),
                    data.get("lastReportedAt", "N/A"),
                ))
            else:
                output_box.insert(tk.END, f"Error for IP {ip}: {response.status_code}\n")
        except Exception as e:
            output_box.insert(tk.END, f"Exception for IP {ip}: {str(e)}\n")

        # Update progress bar
        progress_bar["value"] = i + 1
        root.update_idletasks()

    output_box.insert(tk.END, "IP check completed.\n")


def main():
    global root, progress_bar
    root = tk.Tk()
    root.title("AbuseIPDB Bulk Checker by Hussain Ashiq")
    root.geometry("700x500")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # IP Entry Section
    ip_label = ttk.Label(frame, text="Enter IPs (one per line):")
    ip_label.grid(row=0, column=0, sticky=tk.W)
    ip_text = tk.Text(frame, width=50, height=10)
    ip_text.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

    # Submit Button
    submit_button = ttk.Button(
        frame,
        text="Check IPs",
        command=lambda: bulk_check(ip_text.get("1.0", tk.END), output_box, result_table),
    )
    submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Progress Bar
    progress_bar = ttk.Progressbar(frame, orient="horizontal", length=400, mode="determinate")
    progress_bar.grid(row=3, column=0, columnspan=2, pady=5)

    # Output Section
    output_label = ttk.Label(frame, text="Output:")
    output_label.grid(row=4, column=0, sticky=tk.W)
    output_box = tk.Text(frame, width=50, height=5, state="normal")
    output_box.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E))

    # Results Table
    table_frame = ttk.Frame(frame)
    table_frame.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E))
    columns = ("IP", "Confidence", "ISP", "Domain", "Country", "Reports", "Last Reported")
    result_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
    for col in columns:
        result_table.heading(col, text=col)
        result_table.column(col, width=100)
    result_table.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=result_table.yview)
    result_table.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()


if __name__ == "__main__":
    main()
