import customtkinter as ctk
import sqlite3

# ------------------- Database Initialization -------------------
def init_db():
    conn = sqlite3.connect("schedule.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS schedule (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day TEXT NOT NULL,
            time TEXT NOT NULL,
            subject TEXT NOT NULL,
            location TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# ------------------- App Class -------------------
class ScheduleApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SKEJUL")
        self.geometry("360x600")
        self.configure(fg_color="#0A1446")

        self.build_ui()

    def build_ui(self):
        # Header: Title + Add Button
        header = ctk.CTkFrame(self, fg_color="#0A1446", corner_radius=0)
        header.pack(fill="x", pady=(10, 0), padx=10)

        title = ctk.CTkLabel(header, text="SKEJÜL", font=("Helvetica", 24, "bold"), text_color="white")
        title.pack(side="left", padx=(10, 0))

        add_btn = ctk.CTkButton(header, text="+", width=32, height=32,
                                font=("Helvetica", 18, "bold"),
                                fg_color="#4CD964", text_color="white",
                                corner_radius=20, command=self.add_task)
        add_btn.pack(side="right", padx=(0, 10))

        # Day Label
        day_label = ctk.CTkLabel(self, text="Rabu", font=("Helvetica", 18), text_color="white")
        day_label.pack(pady=(5, 10))

        # Schedule Cards
        self.create_card("09.00", "Bahasa Pemrograman", "Digital Center 3A")
        self.create_card("13.00", "Statistika", "D5 304")

        # Select Day Button
        select_btn = ctk.CTkButton(self, text="Select Day", fg_color="#706EFF",
                                   hover_color="#5858DC", text_color="white",
                                   font=("Helvetica", 12, "bold"), corner_radius=10)
        select_btn.pack(pady=20)

        # Table Display
        self.create_table()

    def create_card(self, time, subject, location):
        card = ctk.CTkFrame(self, fg_color="#1F2A6B", corner_radius=12)
        card.pack(padx=20, pady=5, fill="x")

        time_label = ctk.CTkLabel(card, text=time, font=("Helvetica", 14, "bold"), text_color="white")
        time_label.pack(anchor="w", padx=10, pady=(8, 0))

        subject_label = ctk.CTkLabel(card, text=subject, font=("Helvetica", 12, "bold"), text_color="white")
        subject_label.pack(anchor="w", padx=10, pady=(2, 0))

        location_label = ctk.CTkLabel(card, text=location, font=("Helvetica", 10), text_color="lightgray")
        location_label.pack(anchor="w", padx=10, pady=(0, 8))

    def create_table(self):
        table = ctk.CTkFrame(self, fg_color="#2A3C91", corner_radius=12)
        table.pack(padx=20, pady=5, fill="x")

        # Header
        headers = ["Jam", "Kegiatan", "Keterangan"]
        for i, h in enumerate(headers):
            label = ctk.CTkLabel(table, text=h, font=("Helvetica", 10, "bold"), text_color="white")
            label.grid(row=0, column=i, padx=10, pady=5)

        # Sample row
        row = ["09.00", "Bahasa Pemrograman", "D5 304"]
        for i, value in enumerate(row):
            label = ctk.CTkLabel(table, text=value, font=("Helvetica", 10), text_color="white")
            label.grid(row=1, column=i, padx=10, pady=5)

        # Delete Button
        delete_btn = ctk.CTkButton(table, text="❌", width=30, height=30, font=("Helvetica", 12),
                                   fg_color="#D9534F", hover_color="#C9302C", text_color="white",
                                   corner_radius=15)
        delete_btn.grid(row=1, column=3, padx=5)

    def add_task(self):
        print("Add button clicked - feature coming soon!")


# ------------------- Run App -------------------
if __name__ == "__main__":
    init_db()
    app = ScheduleApp()
    app.mainloop()
