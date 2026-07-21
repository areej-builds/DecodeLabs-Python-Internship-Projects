import customtkinter as ctk
import random
import json
import os


class ModernQuizApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Configuration
        self.title("Quiz Application")
        self.geometry("1100x700")
        self.minsize(900, 600)

        # Theme Colors
        self.bg_color = "#0B0E1E"
        self.accent_purple = "#8B5CF6"
        self.text_main = "#FFFFFF"
        self.text_muted = "#9CA3AF"
        self.input_bg = "#1F2937"
        self.success_color = "#10B981"
        self.error_color = "#EF4444"
        self.warning_color = "#F59E0B"

        self.configure(fg_color=self.bg_color)

        # Font Configuration
        self.font_main = ("Segoe UI", 36, "bold")
        self.font_sub = ("Segoe UI", 16, "italic")
        self.font_btn = ("Segoe UI", 16, "bold")
        self.font_metrics = ("Segoe UI", 14, "bold")

        # High score persistence
        self.highscore_file = "quiz_highscore.json"
        self.high_score = self.load_high_score()

        # Application State
        self.score = 0
        self.current_q_index = 0
        self.time_left = 0
        self.timer_job = None
        self.timer_duration = 15  # seconds allowed per question
        self.review_log = []       # Stores per-question review data for the review screen
        self.answer_locked = False  # Prevents double submission while feedback is showing

        self.base_questions = [
            {
                "q": "What is the capital of France?",
                "a": "paris",
                "fact": "Did you know? The Eiffel Tower, located in this famous city, can grow by up to 15 centimeters during the summer due to thermal expansion."
            },
            {
                "q": "Which planet is known as the Red Planet?",
                "a": "mars",
                "fact": "Did you know? A year on this planet is almost twice as long as a year on Earth, lasting 687 Earth days."
            },
            {
                "q": "What is the hardest natural substance on Earth?",
                "a": "diamond",
                "fact": "Did you know? This incredibly hard material is actually made of pure carbon that has been subjected to immense heat and pressure over billions of years."
            },
            {
                "q": "Which programming language is known for its readability?",
                "a": "python",
                "fact": "Did you know? The creator of this language started developing it as a hobby project during the Christmas holidays in 1989."
            },
            {
                "q": "What is the largest ocean on Earth?",
                "a": "pacific",
                "fact": "Did you know? This ocean is so vast that it covers more surface area than all of Earth's landmasses combined."
            }
        ]

        self.questions = list(self.base_questions)

        # ==========================================
        # 1. PRE-BUILD ALL FRAMES (To Prevent Flickering)
        # ==========================================
        self.start_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.quiz_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.result_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.review_frame = ctk.CTkFrame(self, fg_color="transparent")

        self.build_start_screen()
        self.build_quiz_screen()
        self.build_result_screen()
        self.build_review_screen()

        # Show Start Screen Initially
        self.show_frame(self.start_frame)

    def show_frame(self, frame_to_show):
        # Hide all frames
        self.start_frame.place_forget()
        self.quiz_frame.place_forget()
        self.result_frame.place_forget()
        self.review_frame.place_forget()
        # Show only the requested frame
        frame_to_show.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

    # ==========================================
    # HIGH SCORE PERSISTENCE
    # ==========================================
    def load_high_score(self):
        # Load the saved high score from disk, defaulting to 0 if missing or invalid
        if os.path.exists(self.highscore_file):
            try:
                with open(self.highscore_file, "r") as f:
                    data = json.load(f)
                    return data.get("high_score", 0)
            except (json.JSONDecodeError, OSError):
                return 0
        return 0

    def save_high_score(self):
        # Persist the current high score to disk
        try:
            with open(self.highscore_file, "w") as f:
                json.dump({"high_score": self.high_score}, f)
        except OSError:
            pass  # Fail silently if the file cannot be written

    # ==========================================
    # 2. UI BUILDING METHODS (Run Only Once)
    # ==========================================
    def build_start_screen(self):
        center_frame = ctk.CTkFrame(self.start_frame, fg_color="transparent")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        lbl_title = ctk.CTkLabel(center_frame, text="Welcome to the Quiz Game", font=self.font_main, text_color=self.text_main)
        lbl_title.pack(pady=(0, 5))

        lbl_sub = ctk.CTkLabel(center_frame, text="test your knowledge", font=self.font_sub, text_color=self.accent_purple)
        lbl_sub.pack(pady=(0, 20))

        # High score display, refreshed every time the quiz finishes
        self.lbl_highscore = ctk.CTkLabel(center_frame, text=f"High Score: {self.high_score}", font=self.font_metrics, text_color=self.success_color)
        self.lbl_highscore.pack(pady=(0, 30))

        lbl_ready = ctk.CTkLabel(center_frame, text="Are You Ready for the Quiz?", font=("Segoe UI", 20), text_color=self.text_main)
        lbl_ready.pack(pady=(0, 30))

        btn_go = ctk.CTkButton(center_frame, text="Let's Go!", font=self.font_btn, fg_color=self.accent_purple, hover_color="#7C3AED", corner_radius=20, width=200, height=50, command=self.start_quiz)
        btn_go.pack()

    def build_quiz_screen(self):
        # Metrics Bar
        top_frame = ctk.CTkFrame(self.quiz_frame, fg_color="transparent")
        top_frame.place(relx=0.5, rely=0.08, anchor="center", relwidth=0.9)

        lbl_badge = ctk.CTkLabel(top_frame, text="  QUIZ GAME  ", font=self.font_metrics, text_color=self.accent_purple, fg_color="#1E1B4B", corner_radius=8)
        lbl_badge.pack(side="left", padx=10)

        self.lbl_score = ctk.CTkLabel(top_frame, text="Current Score: 0", font=self.font_metrics, text_color=self.success_color)
        self.lbl_score.pack(side="left", padx=30)

        # Countdown timer label
        self.lbl_timer = ctk.CTkLabel(top_frame, text="Time: 15s", font=self.font_metrics, text_color=self.warning_color)
        self.lbl_timer.pack(side="left", padx=30)

        self.lbl_counter = ctk.CTkLabel(top_frame, text="Question 1 of 4", font=self.font_metrics, text_color=self.text_main)
        self.lbl_counter.pack(side="right", padx=10)

        self.progress_bar = ctk.CTkProgressBar(self.quiz_frame, width=800, height=8, progress_color=self.accent_purple, fg_color=self.input_bg)
        self.progress_bar.place(relx=0.5, rely=0.15, anchor="center")

        # Center Content
        center_frame = ctk.CTkFrame(self.quiz_frame, fg_color="transparent")
        center_frame.place(relx=0.5, rely=0.42, anchor="center")

        self.lbl_question = ctk.CTkLabel(center_frame, text="", font=("Segoe UI", 28, "bold"), text_color=self.text_main, wraplength=800)
        self.lbl_question.pack(pady=(0, 25))

        self.ans_entry = ctk.CTkEntry(center_frame, font=("Segoe UI", 20), width=350, height=55, fg_color=self.input_bg, border_color=self.accent_purple, border_width=2, text_color=self.text_main, corner_radius=12, justify="center")
        self.ans_entry.pack()
        # Pressing Enter submits the answer, same as clicking Next/Submit
        self.ans_entry.bind("<Return>", lambda event: self.evaluate_and_next())

        # Feedback label shown briefly after each answer (correct / wrong / skipped / timed out)
        self.lbl_feedback_inline = ctk.CTkLabel(center_frame, text="", font=("Segoe UI", 16, "bold"))
        self.lbl_feedback_inline.pack(pady=(15, 0))

        # Bottom Controls
        btn_frame = ctk.CTkFrame(self.quiz_frame, fg_color="transparent")
        btn_frame.place(relx=0.5, rely=0.78, anchor="center")

        btn_quit = ctk.CTkButton(btn_frame, text="Quit", font=self.font_btn, fg_color="transparent", hover_color="#451A22", border_color=self.error_color, border_width=2, text_color=self.error_color, corner_radius=20, width=140, height=45, command=self.confirm_quit)
        btn_quit.grid(row=0, column=0, padx=20)

        self.btn_next = ctk.CTkButton(btn_frame, text="Next", font=self.font_btn, fg_color=self.accent_purple, hover_color="#7C3AED", corner_radius=20, width=140, height=45, command=self.evaluate_and_next)
        self.btn_next.grid(row=0, column=1, padx=20)

        self.btn_skip = ctk.CTkButton(btn_frame, text="Skip this Question", font=self.font_btn, fg_color="transparent", hover_color="#1F2937", border_color=self.text_muted, border_width=1, text_color=self.text_muted, corner_radius=20, width=180, height=45, command=self.skip_question)
        self.btn_skip.grid(row=0, column=2, padx=20)

        # Fact Label
        self.lbl_fact = ctk.CTkLabel(self.quiz_frame, text="", font=("Segoe UI", 14, "italic"), text_color=self.text_muted, wraplength=700)
        self.lbl_fact.place(relx=0.5, rely=0.94, anchor="center")

    def build_result_screen(self):
        center_frame = ctk.CTkFrame(self.result_frame, fg_color="transparent")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.lbl_feedback = ctk.CTkLabel(center_frame, text="", font=("Segoe UI", 32, "bold"))
        self.lbl_feedback.pack(pady=(0, 20))

        self.lbl_result = ctk.CTkLabel(center_frame, text="", font=("Segoe UI", 22), text_color=self.text_main, justify="center")
        self.lbl_result.pack(pady=(0, 15))

        # New high score badge, hidden unless earned this round
        self.lbl_new_highscore = ctk.CTkLabel(center_frame, text="", font=("Segoe UI", 16, "bold"), text_color=self.success_color)
        self.lbl_new_highscore.pack(pady=(0, 25))

        self.final_progress = ctk.CTkProgressBar(center_frame, width=400, height=10, fg_color=self.input_bg)
        self.final_progress.pack(pady=(0, 35))

        btn_row = ctk.CTkFrame(center_frame, fg_color="transparent")
        btn_row.pack()

        btn_review = ctk.CTkButton(btn_row, text="Review Answers", font=self.font_btn, fg_color=self.accent_purple, hover_color="#7C3AED", corner_radius=20, width=180, height=45, command=self.show_review_screen)
        btn_review.grid(row=0, column=0, padx=10)

        btn_replay = ctk.CTkButton(btn_row, text="Play Again", font=self.font_btn, fg_color="transparent", hover_color="#1F2937", border_color=self.accent_purple, border_width=1, text_color=self.text_main, corner_radius=20, width=160, height=45, command=self.start_quiz)
        btn_replay.grid(row=0, column=1, padx=10)

        btn_exit = ctk.CTkButton(btn_row, text="Close Game", font=self.font_btn, fg_color="transparent", hover_color="#1F2937", border_color=self.text_muted, border_width=1, text_color=self.text_main, corner_radius=20, width=160, height=45, command=self.destroy)
        btn_exit.grid(row=0, column=2, padx=10)

    def build_review_screen(self):
        # Scrollable frame so any number of questions can be reviewed without overflow
        outer = ctk.CTkFrame(self.review_frame, fg_color="transparent")
        outer.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.85, relheight=0.85)

        lbl_title = ctk.CTkLabel(outer, text="Answer Review", font=("Segoe UI", 28, "bold"), text_color=self.text_main)
        lbl_title.pack(pady=(0, 15))

        self.review_scroll = ctk.CTkScrollableFrame(outer, fg_color=self.input_bg, corner_radius=12)
        self.review_scroll.pack(fill="both", expand=True, pady=(0, 20))

        btn_back = ctk.CTkButton(outer, text="Back to Results", font=self.font_btn, fg_color=self.accent_purple, hover_color="#7C3AED", corner_radius=20, width=180, height=45, command=lambda: self.show_frame(self.result_frame))
        btn_back.pack()

    # ==========================================
    # 3. DYNAMIC UPDATING LOGIC (No Destroying)
    # ==========================================
    def start_quiz(self):
        self.score = 0
        self.current_q_index = 0
        self.review_log = []
        # Shuffle the question order every time the quiz starts, for replay variety
        self.questions = random.sample(self.base_questions, len(self.base_questions))
        self.load_question()
        self.show_frame(self.quiz_frame)

    def load_question(self):
        q_data = self.questions[self.current_q_index]
        total_q = len(self.questions)

        self.answer_locked = False
        self.lbl_feedback_inline.configure(text="")

        # Update existing widgets instead of recreating them (Flicker-Free!)
        self.lbl_score.configure(text=f"Current Score: {self.score}")
        self.lbl_counter.configure(text=f"Question {self.current_q_index + 1} of {total_q}")
        self.progress_bar.set(self.current_q_index / total_q)

        self.lbl_question.configure(text=q_data["q"])
        self.lbl_fact.configure(text=q_data["fact"])

        self.ans_entry.configure(state="normal")
        self.ans_entry.delete(0, 'end')
        self.ans_entry.focus()

        self.btn_next.configure(state="normal")
        self.btn_skip.configure(state="normal")

        # Dynamic button text
        if self.current_q_index == total_q - 1:
            self.btn_next.configure(text="Submit")
        else:
            self.btn_next.configure(text="Next")

        self.start_timer()

    # ==========================================
    # COUNTDOWN TIMER LOGIC
    # ==========================================
    def start_timer(self):
        # Cancel any timer left over from the previous question
        if self.timer_job is not None:
            self.after_cancel(self.timer_job)

        self.time_left = self.timer_duration
        self.update_timer_label()
        self.tick_timer()

    def tick_timer(self):
        if self.time_left <= 0:
            self.timer_job = None
            self.handle_timeout()
            return

        self.time_left -= 1
        self.update_timer_label()
        self.timer_job = self.after(1000, self.tick_timer)

    def update_timer_label(self):
        color = self.error_color if self.time_left <= 5 else self.warning_color
        self.lbl_timer.configure(text=f"Time: {self.time_left}s", text_color=color)

    def handle_timeout(self):
        # Treat a timeout the same as an unanswered question
        if self.answer_locked:
            return
        self.log_review(user_answer="(no answer - time ran out)", is_correct=False)
        self.lock_answer_controls()
        self.show_inline_feedback("Time's up!", self.error_color)
        self.after(900, self.advance_question)

    # ==========================================
    # ANSWER EVALUATION
    # ==========================================
    def evaluate_and_next(self):
        if self.answer_locked:
            return  # Prevent double submission while feedback is showing

        self.stop_timer()

        user_answer = self.ans_entry.get().strip().lower()
        correct_answer = self.questions[self.current_q_index]["a"]
        is_correct = user_answer == correct_answer

        if is_correct:
            self.score += 1
            self.show_inline_feedback("Correct!", self.success_color)
        else:
            self.show_inline_feedback(f"Wrong! Correct answer: {correct_answer.title()}", self.error_color)

        self.log_review(user_answer=user_answer if user_answer else "(no answer)", is_correct=is_correct)
        self.lock_answer_controls()
        self.lbl_score.configure(text=f"Current Score: {self.score}")

        # Brief pause so the user can see the feedback before moving on
        self.after(900, self.advance_question)

    def skip_question(self):
        if self.answer_locked:
            return

        self.stop_timer()
        self.log_review(user_answer="(skipped)", is_correct=False)
        self.lock_answer_controls()
        self.show_inline_feedback("Skipped", self.text_muted)
        self.after(700, self.advance_question)

    def stop_timer(self):
        if self.timer_job is not None:
            self.after_cancel(self.timer_job)
            self.timer_job = None

    def lock_answer_controls(self):
        self.answer_locked = True
        self.ans_entry.configure(state="disabled")
        self.btn_next.configure(state="disabled")
        self.btn_skip.configure(state="disabled")

    def show_inline_feedback(self, message, color):
        self.lbl_feedback_inline.configure(text=message, text_color=color)

    def log_review(self, user_answer, is_correct):
        q_data = self.questions[self.current_q_index]
        self.review_log.append({
            "question": q_data["q"],
            "user_answer": user_answer,
            "correct_answer": q_data["a"],
            "is_correct": is_correct
        })

    def advance_question(self):
        self.current_q_index += 1
        self.route_next_screen()

    def route_next_screen(self):
        if self.current_q_index < len(self.questions):
            self.load_question()  # Just load new text!
        else:
            self.update_and_show_result()

    # ==========================================
    # QUIT CONFIRMATION (custom themed popup, not the default OS dialog)
    # ==========================================
    def confirm_quit(self):
        self.stop_timer()

        # Small modal window styled to match the app's dark theme
        popup = ctk.CTkToplevel(self)
        popup.title("Quit Quiz")
        popup.geometry("420x220")
        popup.resizable(False, False)
        popup.configure(fg_color=self.bg_color)
        popup.transient(self)   # Keep the popup on top of the main window
        popup.grab_set()        # Block interaction with the main window until closed

        # Center the popup relative to the main window
        self.update_idletasks()
        pos_x = self.winfo_x() + (self.winfo_width() // 2) - 210
        pos_y = self.winfo_y() + (self.winfo_height() // 2) - 110
        popup.geometry(f"+{pos_x}+{pos_y}")

        card = ctk.CTkFrame(popup, fg_color=self.input_bg, corner_radius=16)
        card.pack(expand=True, fill="both", padx=15, pady=15)

        lbl_title = ctk.CTkLabel(card, text="Quit Quiz?", font=("Segoe UI", 20, "bold"), text_color=self.text_main)
        lbl_title.pack(pady=(25, 10))

        lbl_message = ctk.CTkLabel(card, text="Are you sure you want to quit?\nYour progress will be lost.", font=("Segoe UI", 14), text_color=self.text_muted, justify="center")
        lbl_message.pack(pady=(0, 25))

        btn_row = ctk.CTkFrame(card, fg_color="transparent")
        btn_row.pack()

        def on_yes():
            popup.destroy()
            self.destroy()

        def on_no():
            popup.destroy()
            self.start_timer()  # Resume the timer since the user decided to stay

        btn_yes = ctk.CTkButton(btn_row, text="Yes, Quit", font=self.font_btn, fg_color=self.error_color, hover_color="#B91C1C", corner_radius=20, width=140, height=42, command=on_yes)
        btn_yes.grid(row=0, column=0, padx=10)

        btn_no = ctk.CTkButton(btn_row, text="No, Stay", font=self.font_btn, fg_color=self.accent_purple, hover_color="#7C3AED", corner_radius=20, width=140, height=42, command=on_no)
        btn_no.grid(row=0, column=1, padx=10)

        # Also resume the timer if the popup is closed via the window's X button
        popup.protocol("WM_DELETE_WINDOW", on_no)

    # ==========================================
    # RESULT SCREEN
    # ==========================================
    def update_and_show_result(self):
        total = len(self.questions)
        percentage = (self.score / total) * 100

        if self.score == total:
            feedback_msg = "Excellent! You are a genius. 🎉"
            msg_color = self.success_color
        elif self.score >= total * 0.75:
            feedback_msg = "Good job! Keep it up. 👍"
            msg_color = self.accent_purple
        elif self.score >= total * 0.5:
            feedback_msg = "Not bad, but you can improve. 📚"
            msg_color = self.warning_color
        else:
            feedback_msg = "Better luck next time! 🔄"
            msg_color = self.error_color

        self.lbl_feedback.configure(text=feedback_msg, text_color=msg_color)

        result_text = f"You have scored {self.score} out of {total},\nwhich makes your percentage {int(percentage)}%"
        self.lbl_result.configure(text=result_text)

        # Check and persist a new high score
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
            self.lbl_new_highscore.configure(text="New High Score!")
            self.lbl_highscore.configure(text=f"High Score: {self.high_score}")
        else:
            self.lbl_new_highscore.configure(text="")

        self.final_progress.configure(progress_color=self.success_color)
        self.final_progress.set(1.0)

        self.populate_review_screen()
        self.show_frame(self.result_frame)

    # ==========================================
    # REVIEW SCREEN
    # ==========================================
    def populate_review_screen(self):
        # Clear any review entries left over from a previous playthrough
        for widget in self.review_scroll.winfo_children():
            widget.destroy()

        for index, entry in enumerate(self.review_log, start=1):
            row = ctk.CTkFrame(self.review_scroll, fg_color=self.bg_color, corner_radius=10)
            row.pack(fill="x", padx=10, pady=8)

            status_color = self.success_color if entry["is_correct"] else self.error_color
            status_text = "Correct" if entry["is_correct"] else "Incorrect"

            lbl_q = ctk.CTkLabel(row, text=f"{index}. {entry['question']}", font=("Segoe UI", 16, "bold"), text_color=self.text_main, anchor="w", justify="left", wraplength=700)
            lbl_q.pack(fill="x", padx=15, pady=(12, 4))

            lbl_status = ctk.CTkLabel(row, text=status_text, font=("Segoe UI", 14, "bold"), text_color=status_color, anchor="w")
            lbl_status.pack(fill="x", padx=15)

            lbl_user = ctk.CTkLabel(row, text=f"Your answer: {entry['user_answer']}", font=("Segoe UI", 13), text_color=self.text_muted, anchor="w")
            lbl_user.pack(fill="x", padx=15)

            lbl_correct = ctk.CTkLabel(row, text=f"Correct answer: {entry['correct_answer'].title()}", font=("Segoe UI", 13), text_color=self.text_muted, anchor="w")
            lbl_correct.pack(fill="x", padx=15, pady=(0, 12))

    def show_review_screen(self):
        self.show_frame(self.review_frame)


# Execution entry point
if __name__ == "__main__":
    app = ModernQuizApp()
    app.mainloop()
