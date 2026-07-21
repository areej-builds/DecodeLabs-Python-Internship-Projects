import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")       # "dark", "light", or "system"
ctk.set_default_color_theme("green")  # "blue", "green", "dark-blue"


def add_expense(new_expense: float, total_spent: float) -> float:
    """Add the new expense to the running total (pure calculation, no I/O)."""
    return total_spent + new_expense


class ExpenseTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Expense Tracker")
        self.geometry("440x600")
        self.resizable(False, False)

        self.total_spent = 0.0
        self.expenses = []  # history of (description, amount)

        self._build_ui()

    def _build_ui(self):
        # --- Title ---
        title = ctk.CTkLabel(
            self, text="💰 Expense Tracker", font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(25, 5))

        # --- Total card ---
        self.total_card = ctk.CTkFrame(self, corner_radius=15)
        self.total_card.pack(pady=15, padx=25, fill="x")

        ctk.CTkLabel(
            self.total_card, text="Total Spent", font=ctk.CTkFont(size=13),
            text_color="gray"
        ).pack(pady=(15, 0))

        self.total_label = ctk.CTkLabel(
            self.total_card, text="$0.00", font=ctk.CTkFont(size=32, weight="bold")
        )
        self.total_label.pack(pady=(0, 15))

        # --- Input form card ---
        form_card = ctk.CTkFrame(self, corner_radius=15)
        form_card.pack(pady=10, padx=25, fill="x")

        self.desc_entry = ctk.CTkEntry(
            form_card, placeholder_text="Description (e.g. Groceries)", height=40
        )
        self.desc_entry.pack(pady=(15, 8), padx=15, fill="x")

        self.amount_entry = ctk.CTkEntry(
            form_card, placeholder_text="Amount ($)", height=40
        )
        self.amount_entry.pack(pady=(0, 15), padx=15, fill="x")
        self.amount_entry.bind("<Return>", lambda event: self.handle_add_expense())

        add_btn = ctk.CTkButton(
            form_card, text="➕ Add Expense", height=40,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.handle_add_expense
        )
        add_btn.pack(pady=(0, 15), padx=15, fill="x")

        # --- History section ---
        history_label = ctk.CTkLabel(
            self, text="Expense History", font=ctk.CTkFont(size=15, weight="bold")
        )
        history_label.pack(pady=(15, 5), anchor="w", padx=25)

        self.history_frame = ctk.CTkScrollableFrame(self, height=180, corner_radius=15)
        self.history_frame.pack(pady=5, padx=25, fill="both", expand=True)

        self.empty_label = ctk.CTkLabel(
            self.history_frame, text="No expenses yet", text_color="gray"
        )
        self.empty_label.pack(pady=20)

        # --- Reset button ---
        reset_btn = ctk.CTkButton(
            self, text="Reset All", height=35, fg_color="#B33636", hover_color="#8f2b2b",
            command=self.handle_reset
        )
        reset_btn.pack(pady=15)

    def handle_add_expense(self):
        amount_text = self.amount_entry.get().strip()
        description = self.desc_entry.get().strip() or "Unnamed expense"

        try:
            new_expense = float(amount_text)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the amount.")
            return

        if new_expense < 0:
            messagebox.showwarning("Invalid Amount", "Expense amount cannot be negative!")
            return

        self.total_spent = add_expense(new_expense, self.total_spent)
        self.expenses.append((description, new_expense))

        if self.empty_label.winfo_exists():
            self.empty_label.destroy()

        row = ctk.CTkFrame(self.history_frame, fg_color="transparent")
        row.pack(fill="x", pady=4)

        ctk.CTkLabel(row, text=description, anchor="w").pack(side="left", padx=(5, 0))
        ctk.CTkLabel(
            row, text=f"${new_expense:.2f}", font=ctk.CTkFont(weight="bold")
        ).pack(side="right", padx=(0, 5))

        self.total_label.configure(text=f"${self.total_spent:.2f}")

        self.desc_entry.delete(0, "end")
        self.amount_entry.delete(0, "end")
        self.desc_entry.focus()

    def handle_reset(self):
        confirm = messagebox.askyesno("Reset", "Clear all expenses and reset total to zero?")
        if confirm:
            self.total_spent = 0.0
            self.expenses.clear()

            for widget in self.history_frame.winfo_children():
                widget.destroy()

            self.empty_label = ctk.CTkLabel(
                self.history_frame, text="No expenses yet", text_color="gray"
            )
            self.empty_label.pack(pady=20)

            self.total_label.configure(text="$0.00")


def main():
    app = ExpenseTrackerApp()
    app.mainloop()


if __name__ == "__main__":
    main()
