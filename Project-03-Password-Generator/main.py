import string
import secrets
import math

import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Professional dark-purple palette
BG_MAIN = "#181521"
BG_CARD = "#241f33"
ACCENT = "#7c5cf0"
ACCENT_HOVER = "#6a49dd"
ACCENT_LIGHT = "#a78bfa"
BORDER = "#3a3352"
TEXT_MUTED = "#9d97b5"


def calculate_entropy(length: int, pool_size: int) -> float:
    """Calculates the information entropy of the password in bits."""
    if pool_size <= 0 or length <= 0:
        return 0.0
    return length * math.log2(pool_size)


def build_character_pool(use_upper, use_lower, use_digits, use_symbols) -> str:
    """Builds the character pool string based on selected options."""
    pool = ""
    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation
    return pool


def generate_secure_password(length: int, pool: str) -> str:
    """Generates a cryptographically secure password from the given pool."""
    return "".join(secrets.choice(pool) for _ in range(length))


class PasswordGeneratorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("DecodeLabs Enterprise Password Generator")
        self.geometry("480x680")
        self.resizable(False, False)
        self.configure(fg_color=BG_MAIN)

        self.history = []

        self._build_ui()

    def _build_ui(self):
        ctk.CTkLabel(
            self, text="🔐 Enterprise Password Generator",
            font=ctk.CTkFont(size=20, weight="bold"), text_color=ACCENT_LIGHT
        ).pack(pady=(25, 2))

        ctk.CTkLabel(
            self, text="DecodeLabs Security Tools", font=ctk.CTkFont(size=12),
            text_color=TEXT_MUTED
        ).pack(pady=(0, 15))

        display_card = ctk.CTkFrame(self, corner_radius=15, fg_color=BG_CARD,
                                     border_width=1, border_color=BORDER)
        display_card.pack(padx=25, pady=10, fill="x")

        self.password_display = ctk.CTkEntry(
            display_card, height=45, font=ctk.CTkFont(size=16, family="Consolas"),
            justify="center", fg_color=BG_MAIN, border_color=ACCENT, border_width=1
        )
        self.password_display.pack(pady=(15, 8), padx=15, fill="x")

        btn_row = ctk.CTkFrame(display_card, fg_color="transparent")
        btn_row.pack(pady=(0, 15), padx=15, fill="x")

        self.copy_btn = ctk.CTkButton(
            btn_row, text="📋 Copy", width=100, command=self.handle_copy,
            fg_color=BG_MAIN, hover_color=BORDER, border_width=1, border_color=ACCENT,
            text_color=ACCENT_LIGHT
        )
        self.copy_btn.pack(side="left", padx=(0, 5), expand=True, fill="x")

        self.generate_btn = ctk.CTkButton(
            btn_row, text="⚡ Generate", width=100,
            font=ctk.CTkFont(weight="bold"), command=self.handle_generate,
            fg_color=ACCENT, hover_color=ACCENT_HOVER
        )
        self.generate_btn.pack(side="left", padx=(5, 0), expand=True, fill="x")

        length_card = ctk.CTkFrame(self, corner_radius=15, fg_color=BG_CARD,
                                    border_width=1, border_color=BORDER)
        length_card.pack(padx=25, pady=10, fill="x")

        self.length_label = ctk.CTkLabel(
            length_card, text="Password Length: 16", font=ctk.CTkFont(size=13, weight="bold"),
            text_color=ACCENT_LIGHT
        )
        self.length_label.pack(pady=(15, 5), padx=15, anchor="w")

        self.length_slider = ctk.CTkSlider(
            length_card, from_=4, to=64, number_of_steps=60,
            command=self.handle_slider_change,
            progress_color=ACCENT, button_color=ACCENT_LIGHT, button_hover_color=ACCENT_HOVER,
            fg_color=BORDER
        )
        self.length_slider.set(16)
        self.length_slider.pack(pady=(0, 15), padx=15, fill="x")

        options_card = ctk.CTkFrame(self, corner_radius=15, fg_color=BG_CARD,
                                     border_width=1, border_color=BORDER)
        options_card.pack(padx=25, pady=10, fill="x")

        ctk.CTkLabel(
            options_card, text="Character Types", font=ctk.CTkFont(size=13, weight="bold"),
            text_color=ACCENT_LIGHT
        ).pack(pady=(15, 8), padx=15, anchor="w")

        self.upper_var = ctk.BooleanVar(value=True)
        self.lower_var = ctk.BooleanVar(value=True)
        self.digits_var = ctk.BooleanVar(value=True)
        self.symbols_var = ctk.BooleanVar(value=True)

        checks = [
            ("Uppercase (A-Z)", self.upper_var),
            ("Lowercase (a-z)", self.lower_var),
            ("Digits (0-9)", self.digits_var),
            ("Symbols (!@#$...)", self.symbols_var),
        ]
        for text, var in checks:
            ctk.CTkCheckBox(
                options_card, text=text, variable=var, command=self.handle_generate,
                fg_color=ACCENT, hover_color=ACCENT_HOVER, border_color=ACCENT_LIGHT,
                checkmark_color=BG_MAIN
            ).pack(pady=4, padx=15, anchor="w")

        ctk.CTkFrame(options_card, height=1, fg_color="transparent").pack(pady=5)

        strength_card = ctk.CTkFrame(self, corner_radius=15, fg_color=BG_CARD,
                                      border_width=1, border_color=BORDER)
        strength_card.pack(padx=25, pady=10, fill="x")

        self.entropy_label = ctk.CTkLabel(
            strength_card, text="Entropy: 0.00 bits", font=ctk.CTkFont(size=13, weight="bold"),
            text_color=ACCENT_LIGHT
        )
        self.entropy_label.pack(pady=(15, 5), padx=15, anchor="w")

        self.strength_bar = ctk.CTkProgressBar(strength_card, height=14, fg_color=BORDER)
        self.strength_bar.pack(pady=(0, 8), padx=15, fill="x")
        self.strength_bar.set(0)

        self.strength_status = ctk.CTkLabel(
            strength_card, text="Security Status: —", font=ctk.CTkFont(size=13, weight="bold")
        )
        self.strength_status.pack(pady=(0, 15), padx=15, anchor="w")

        self.pool_size_label = ctk.CTkLabel(
            self, text="", font=ctk.CTkFont(size=11), text_color=TEXT_MUTED
        )
        self.pool_size_label.pack(pady=(5, 15))

        self.handle_generate()

    def handle_slider_change(self, value):
        length = int(value)
        self.length_label.configure(text=f"Password Length: {length}")
        self.handle_generate()

    def handle_generate(self):
        length = int(self.length_slider.get())
        pool = build_character_pool(
            self.upper_var.get(), self.lower_var.get(),
            self.digits_var.get(), self.symbols_var.get()
        )

        if not pool:
            messagebox.showwarning(
                "No Character Types Selected",
                "Please select at least one character type."
            )
            return

        password = generate_secure_password(length, pool)
        self.history.append(password)

        self.password_display.delete(0, "end")
        self.password_display.insert(0, password)

        entropy = calculate_entropy(length, len(pool))
        self.entropy_label.configure(text=f"Entropy: {entropy:.2f} bits")
        self.pool_size_label.configure(text=f"Character pool size: {len(pool)} unique characters")

        self._update_strength_indicator(entropy)

    def _update_strength_indicator(self, entropy: float):
        normalized = min(entropy / 100, 1.0)
        self.strength_bar.set(normalized)

        if entropy < 60:
            self.strength_bar.configure(progress_color="#E53935")
            self.strength_status.configure(
                text="Security Status: WEAK", text_color="#E53935"
            )
        elif entropy < 80:
            self.strength_bar.configure(progress_color="#FDD835")
            self.strength_status.configure(
                text="Security Status: MEDIUM", text_color="#FDD835"
            )
        else:
            self.strength_bar.configure(progress_color="#43A047")
            self.strength_status.configure(
                text="Security Status: STRONG (Enterprise Grade)", text_color="#43A047"
            )

    def handle_copy(self):
        password = self.password_display.get()
        if password:
            self.clipboard_clear()
            self.clipboard_append(password)
            self.update()
            self._show_toast("✅ Password copied to clipboard!")

    def _show_toast(self, message: str):
        """Shows a small, theme-matching popup that auto-closes — replaces the default messagebox."""
        toast = ctk.CTkToplevel(self)
        toast.overrideredirect(True)
        toast.configure(fg_color=BG_CARD)
        toast.attributes("-topmost", True)

        self.update_idletasks()
        toast_width, toast_height = 280, 55
        x = self.winfo_x() + (self.winfo_width() // 2) - (toast_width // 2)
        y = self.winfo_y() + 40
        toast.geometry(f"{toast_width}x{toast_height}+{x}+{y}")

        border = ctk.CTkFrame(
            toast, corner_radius=12, fg_color=BG_CARD,
            border_width=1, border_color=ACCENT
        )
        border.pack(fill="both", expand=True, padx=2, pady=2)

        ctk.CTkLabel(
            border, text=message, font=ctk.CTkFont(size=13, weight="bold"),
            text_color=ACCENT_LIGHT
        ).pack(expand=True)

        toast.after(1600, toast.destroy)

 
def main():
    app = PasswordGeneratorApp()
    app.mainloop()


if __name__ == "__main__":
    main()
