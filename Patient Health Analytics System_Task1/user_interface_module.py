import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv

class PatientGUI:

    def __init__(self, query_obj, stats_obj):
        self.query = query_obj
        self.stats = stats_obj

        self.root = tk.Tk()
        self.root.title("Patient Health Analytics System")
        self.root.geometry("750x550")

        # COLORS (Cyberpunk Theme)
        self.bg_color = "#0B0005"
        self.frame_color = "#120007"
        self.neon_pink = "#FF007F"
        self.glow_pink = "#FF2DAA"
        self.text_color = "#FFFFFF"

        self.root.configure(bg=self.bg_color)

        # STYLE FOR COMBOBOX
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "TCombobox",
            fieldbackground="#1A0010",
            background="#1A0010",
            foreground="white"
        )

        # TITLE
        tk.Label(
            self.root,
            text="Patient Health Analytics System",
            font=("Arial", 16, "bold"),
            bg=self.bg_color,
            fg=self.neon_pink
        ).pack(pady=10)

        # MENU FRAME
        menu_frame = tk.Frame(self.root, bg=self.frame_color)
        menu_frame.pack(pady=5)

        tk.Label(
            menu_frame,
            text="Select Query:",
            bg=self.frame_color,
            fg=self.text_color
        ).grid(row=0, column=0, padx=5)

        self.query_var = tk.StringVar()
        self.query_menu = ttk.Combobox(
            menu_frame,
            textvariable=self.query_var,
            state="readonly",
            width=40
        )

        self.query_menu["values"] = [
            "Smokers with Hypertension Stats",
            "Heart Disease Stats",
            "Descriptive Statistics (Any Feature)"
        ]

        self.query_menu.grid(row=0, column=1, padx=10)

        tk.Button(
            menu_frame,
            text="Run Query",
            command=self.run_query,
            bg="#1A0010",
            fg=self.neon_pink,
            activebackground=self.neon_pink,
            activeforeground="#0B0005",
            relief="flat",
            highlightbackground=self.neon_pink,
            highlightthickness=1
        ).grid(row=0, column=2, padx=5)

        # INPUT FRAME
        input_frame = tk.Frame(self.root, bg=self.frame_color)
        input_frame.pack(pady=10)

        tk.Label(
            input_frame,
            text="Feature Name (for descriptive stats):",
            bg=self.frame_color,
            fg=self.text_color
        ).pack()

        self.feature_entry = tk.Entry(
            input_frame,
            width=25,
            bg="#1A0010",
            fg=self.text_color,
            insertbackground=self.text_color
        )
        self.feature_entry.pack(pady=5)

        # OUTPUT AREA
        self.output = tk.Text(
            self.root,
            height=18,
            width=85,
            bg="#1A0010",
            fg=self.neon_pink,
            insertbackground="white",
            highlightbackground=self.neon_pink,
            highlightthickness=1
        )
        self.output.pack(pady=10)

        # EXPORT BUTTON
        tk.Button(
            self.root,
            text="Export Result to CSV",
            command=self.export_results,
            bg="#1A0010",
            fg=self.neon_pink,
            activebackground=self.neon_pink,
            activeforeground="#0B0005",
            relief="flat",
            highlightbackground=self.neon_pink,
            highlightthickness=1
        ).pack(pady=5)

        # QUIT BUTTON
        tk.Button(
            self.root,
            text="Quit",
            command=self.root.quit,
            bg="#1A0010",
            fg=self.neon_pink,
            activebackground=self.neon_pink,
            activeforeground="#0B0005",
            relief="flat",
            highlightbackground=self.neon_pink,
            highlightthickness=1
        ).pack(pady=5)

        self.last_result = None


    def run_query(self):
        choice = self.query_var.get()
        self.output.delete("1.0", tk.END)

        try:
            if choice == "Smokers with Hypertension Stats":
                result = self.query.smokers_with_hypertension()
                self.display_dict(result)

            elif choice == "Heart Disease Stats":
                result = self.query.heart_disease_patients()
                self.display_heart_disease(result)

            elif choice == "Descriptive Statistics (Any Feature)":
                feature = self.feature_entry.get()

                if feature == "":
                    messagebox.showerror("Error", "Enter feature name.")
                    return

                result = self.stats.descriptive_stats(
                    self.query.data, feature
                )
                self.display_dict(result)

            else:
                messagebox.showerror("Error", "Please select a query.")

            self.last_result = result

        except Exception as e:
            messagebox.showerror("Error", str(e))


    def display_dict(self, result):
        if isinstance(result, str):
            self.output.insert(tk.END, result)
            return

        for k, v in result.items():
            self.output.insert(tk.END, f"{k}: {v}\n")


    def display_heart_disease(self, result):
        if isinstance(result, str):
            self.output.insert(tk.END, result)
            return

        self.output.insert(tk.END, "Age Statistics\n")
        self.output.insert(tk.END, "-" * 30 + "\n")

        for k, v in result["Age Stats"].items():
            self.output.insert(tk.END, f"{k}: {v:.2f}\n")

        self.output.insert(tk.END, "-" * 30 + "\n")
        self.output.insert(
            tk.END,
            f"Average Glucose Level: {result['Average Glucose']:.2f}"
        )


    def export_results(self):
        if self.last_result is None:
            messagebox.showerror("Error", "No results to export.")
            return

        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")]
        )

        if filename == "":
            return

        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)

                if isinstance(self.last_result, dict):
                    writer.writerow(["Metric", "Value"])
                    for k, v in self.last_result.items():
                        writer.writerow([k, v])
                else:
                    writer.writerow(["Result"])
                    writer.writerow([self.last_result])

            messagebox.showinfo("Success", "Results exported.")

        except Exception as e:
            messagebox.showerror("Error", str(e))


    def run(self):
        self.root.mainloop()