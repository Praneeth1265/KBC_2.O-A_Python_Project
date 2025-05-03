import tkinter as tk
from tkinter import Label, Button, StringVar, Checkbutton, Toplevel
from PIL import Image, ImageTk
import pygame
import csv
import os
from random import randint, shuffle
import random

class MemeQuizApp:
    MAX_QUESTIONS = 10
    LEADERBOARD_FILE = "leaderboard.csv"
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        
        self.music_intro = "Music\Instructions.mp3"
        self.music_quiz = "Music\Timer.mp3"
        self.music_leaderboard = "Music\Leaderboard.mp3"
        
        self.play_background_audio(self.music_intro)
        
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.title("Meme Quiz")
        self.current_question = 0
        self.score = 0
        self.cash = 0
        self.name = ""
        self.mode = ""
        
        self.questions = {
            'easy': [
                ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", "Paris"],
                ["Dhoni has '0' centuries outside asia.", "True","False", "True"],
                ["What is the largest mammal on Earth?", "Elephant", "Giraffe", "Blue Whale", "Hippopotamus", "Blue Whale"],
                ["The human skeleton is made up of more than 301 bones.","True","False", "False"],
                ["What is the square root of 64?", "6", "7", "8", "9", "8"],
                ["The Amazon River is the longest river in the world.","True","False", "False"],
                ["The two IPL teams that got banned for spot-fixing till date?","RR & DD","DD & CSK","CSK & RR","MI & CSK","CSK & RR"],
                ["The Great Barrier Reef is the world's 2nd largest coral reef system.","True","False", "False"],
                ["What is the capital of Japan?", "Seoul", "Beijing", "Tokyo", "Bangkok", "Tokyo"],
                ["The currency of South Africa is called the Rand.","True","False", "True"]
            ],
            'moderate': [
                ["The chemical symbol for gold is 'Au'", "True","False", "True"],
                ["Which element has the chemical symbol 'O'?", "Osmium", "Oxygen", "Oganesson", "Oitrogen", "Oxygen"],
                ["Jupiter is the largest planet in our solar system", "True","False", "True"],
                ["Who wrote '1984'?", "George Orwell", "J.R.R. Tolkien", "Aldous Huxley", "Ray Bradbury", "George Orwell",],
                ["The Great Wall of China is visible from space without aid", "True","False", "False"],
                ["What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Arctic Ocean", "Pacific Ocean"],
                ["Alexander Graham Bell is credited with the invention of the telephone", "True","False", "True"],
                ["Who is known as the 'Father of Modern Physics'?", "Isaac Newton", "Albert Einstein", "Niels Bohr", "Galileo Galilei", "Albert Einstein"],
                ["The Earth's atmosphere is composed mostly of nitrogen", "True","False", "True"],
                ["What is the largest desert in the world?", "Gobi Desert", "Arabian Desert", "Sahara Desert", "Antarctica", "Antarctica"]
            ],
            'hard': [
                ["Kohli has won ICC Men's ODI Cricketer of the Decade", "True","False", "True"],
                ["What is the boiling point of water in Fahrenheit?", "212°F", "100°F", "180°F", "32°F", "212°F"],
                ["The star sign Aquarius is represented by a tiger", "True","False", "False"],
                ["In which year did the Titanic sink?", "1910", "1912", "1915", "1918", "1912"],
                ["'A' is the most common letter used in the English language", "True","False", "False"],
                ["What is the speed of light in a vacuum?", "300,000 km/s", "150,000 km/s", "450,000 km/s", "600,000 km/s", "300,000 km/s"],
                ["H&M stands for Hennes & Mauritz", "True","False", "True"],
                ["What is the capital of Canada?", "Ottawa", "Toronto", "Vancouver", "Montreal", "Ottawa"],
                ["In the English language there is no word that rhymes with orange", "True","False", "True"],
                ["In which year did World War II end?", "1943", "1945", "1947", "1950", "1945"]
            ]
        }
        
        
        self.leaderboard_data = []
        self.dice_images = [Image.open(f"Dice_Images/dice_{i}.png") for i in range(1, 7)]
        self.background_music_path = self.music_intro
        self.result_image_label = None 
        self.start_screen()
        
    def play_background_audio(self, file_path):
        pygame.mixer.music.stop()
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Music error: {e}")

    def start_screen(self):
        self.clear_screen()
        label = Label(self.root, text="Welcome to Meme Quiz", font=("Arial", 18))
        label.pack(pady=20)
        score_image = Image.open('Memes/bhidu.jpg')
        width,height=450,400
        score_image.thumbnail((width,height))
        score_photo = ImageTk.PhotoImage(score_image)
        score_image_label = tk.Label(self.root, image=score_photo)
        score_image_label.image = score_photo
        score_image_label.pack(padx=20, pady=20)
        instructions_button = Button(self.root, text="Instructions", command=self.show_instructions)
        instructions_button.config(bg="Black",fg="White")
        instructions_button.pack()
        
    def show_instructions(self):
        self.clear_screen()
        start_image = Image.open('Memes/instructions.png')
        width,height=450,400
        start_image.thumbnail((width,height))
        start_photo = ImageTk.PhotoImage(start_image)
        start_image_label = tk.Label(self.root, image=start_photo)
        start_image_label.image = start_photo
        start_image_label.pack(padx=20, pady=20)
        instructions_label = Label(self.root, text="Instructions", font=("Arial", 20))
        instructions_label.pack(pady=20)
        instruction_label=Label(self.root,text="This is a quiz based on GK in which you will be getting a mode randomly among three modes,\neach will be having 5 MCQ's & 5 True or False questions\nand you will be awarded 1000/- cash for each correct answer untill you mark wrong one\nResults will be displayed along with a meme\n<1> The number on dice decides the mode of questions\n<2> Enter your name so that you will be able to check your standings in leaderboard\n<3> Click on Roll Dice to choose a mode randomly\n<4> Click on Start Quiz to begin the quiz\n<5> Click on Leaderboard to see your stand in bunch of people",font=("Arial", 15),anchor='w')
        instruction_label.pack(pady=20)
        all_label=Label(self.root, text="All The Best",font=("Arial", 15))
        all_label.pack(pady=20)
        start_button = Button(self.root, text="Next", command=self.show_dice_and_name_screen)
        start_button.config(bg="Black",fg="White")
        start_button.pack()
        
    def show_dice_and_name_screen(self):
        self.clear_screen()
        name_label = Label(self.root, text="Enter Your Name:")
        name_label.pack(pady=20)
        name_entry = tk.Entry(self.root)
        name_entry.pack(pady=20)
        start_button = Button(self.root, text="Roll Dice", command=lambda: self.show_dice_page(name_entry.get()))
        start_button.config(bg="Black",fg="White")
        start_button.pack(pady=20)
        
    def show_dice_page(self, name):
        if not name:
            image = Image.open(random.choice(['Memes/Aukaat.jpeg','Memes/jobolavo.jpeg']))
            width,height=450,400
            image.thumbnail((width,height))
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(self.root, image=photo)
            image_label.image = photo
            image_label.pack(padx=20, pady=20)
            return
        self.name = name
        self.clear_screen()
        dice_value = randint(1, 6)
        self.mode = self.get_mode_from_dice_value(dice_value)
        self.show_dice_face(self.dice_images[dice_value - 1])
        mode_map = {
            1: 'Easy',
            2: 'Hard',
            3: 'Moderate',
            4: 'Easy',
            5: 'Hard',
            6: 'Moderate'
        }
        mode_label = Label(self.root, text=f"You'r going to attempt questions from {mode_map.get(dice_value)} mode",font=("Arial", 16))
        mode_label.pack()
        start_button = Button(self.root, text="Start Quiz", command=lambda: self.start_quiz(name))
        start_button.config(bg="Black",fg="White")
        start_button.pack(pady=20)
        
    def get_mode_from_dice_value(self, dice_value):
        mode_mapping = {
            1: 'easy',
            2: 'hard',
            3: 'moderate',
            4: 'easy',
            5: 'hard',
            6: 'moderate'
        }
        return mode_mapping.get(dice_value, 'hard')
    
    def show_dice_face(self, dice_image):
        dice_image = ImageTk.PhotoImage(dice_image)
        dice_label = tk.Label(self.root, image=dice_image)
        dice_label.image = dice_image
        dice_label.pack(pady=20)
        
    def start_quiz(self, name):
        self.name = name
        self.play_background_audio(self.music_quiz)
        self.clear_screen()
        self.show_question_screen()
        
    def show_question_screen(self):
        self.clear_screen()
        question_label = Label(self.root, text=f"Question {self.current_question + 1}", font=("Arial", 16))
        question_label.pack(pady=10)
        question_data = self.questions[self.mode][self.current_question]
        question_text = question_data[0]
        question_label = Label(self.root, text=question_text, font=("Arial", 18))
        question_label.pack(pady=10)
        options = question_data[1:-1]
        self.correct_option = question_data[-1]
        self.wrong_option = question_data[1:-1]
        shuffle(options)
        self.var = StringVar()
        for i, option in enumerate(options):
            option_checkbox = Checkbutton(self.root, text=option, variable=self.var, onvalue=option, offvalue="",command=self.img,font=("Arial", 15))
            option_checkbox.pack()
            
    def img(self):
        selected_option = self.var.get()
        if selected_option == self.correct_option:
            ans_crt_label = Label(self.root, text="Correct Answer!!", font=("Arial", 15))
            ans_crt_label.pack(pady=10)
            self.score += 1
            self.cash +=1000
            image_path = random.choice(['Memes/wah.jpg','Memes/sabaash.jpeg','Memes/acchibaat.webp'])
            score_image = Image.open(image_path)
            width,height=450,400
            score_image.thumbnail((width,height))
            score_photo = ImageTk.PhotoImage(score_image)
            score_image_label = tk.Label(self.root, image=score_photo)
            score_image_label.image = score_photo
            score_image_label.pack(padx=10, pady=10)
        else:
            for ans in self.wrong_option:
                if selected_option == ans :
                    ans_wrng_label = Label(self.root, text="Wrong Answer!!", font=("Arial", 15))
                    ans_wrng_label.pack(pady=10)
                    self.cash = 0
                    image_path = random.choice(['Memes/kyakarrha.jpg','Memes/amitabh.jpg','Memes/bheja.jpg','Memes/modi_maza.webp','Memes/rehnedobeta.webp'])
                    score_image = Image.open(image_path)
                    width,height=450,400
                    score_image.thumbnail((width,height))
                    score_photo = ImageTk.PhotoImage(score_image)
                    score_image_label = tk.Label(self.root, image=score_photo)
                    score_image_label.image = score_photo
                    score_image_label.pack(padx=10, pady=10)
                    ans_label = Label(self.root, text=f"Correct answer is {self.correct_option}", font=("Arial", 15))
                    ans_label.pack(pady=10)
        next_button = Button(self.root, text="Next", command=self.next_question)
        next_button.config(bg='Black',fg='White')
        next_button.pack()
        self.result_image_label = tk.Label(self.root)
        self.result_image_label.pack(pady=10)
        
    def next_question(self):
        self.current_question += 1
        if self.current_question < self.MAX_QUESTIONS:
            self.show_question_screen()
        else:
            if not hasattr(self, 'leaderboard_music_played') or not self.leaderboard_music_played:
                pygame.mixer.music.load(self.music_leaderboard)
                pygame.mixer.music.play()
                self.leaderboard_music_played = True
            self.show_result_screen()
            
    def show_result_screen(self):
        self.clear_screen()
        result_label = Label(self.root, text=f"Your have scored {self.score}", font=("Arial", 16))
        result_label.pack(pady=20)
        cash_label = Label(self.root, text=f"And you have won {self.cash}/- virtual cash", font=("Arial", 16))
        cash_label.pack(pady=20)
        if self.score <= 3:
            image_path = 'Memes/chuna.jpg'
        elif 3<self.score<=6:
            image_path = 'Memes/150rs.webp'
        elif 6<self.cash<=8:
            image_path = 'Memes/ekcrore.webp'
        else:
            image_path = 'Memes/top.png'
        score_image = Image.open(image_path)
        width,height=450,400
        score_image.thumbnail((width,height))
        score_photo = ImageTk.PhotoImage(score_image)
        score_image_label = tk.Label(self.root, image=score_photo)
        score_image_label.image = score_photo
        score_image_label.pack(padx=10, pady=10)
        self.leaderboard_button = Button(self.root, text="Leaderboard", command=self.show_leaderboard)
        self.leaderboard_button.pack(pady=10)
        self.leaderboard_button.config(bg="Black",fg="White")
        MemeQuizApp.save_to_csv(self.name, self.score, self.cash)
        
    def show_result_image(self, image_path):
        result_image = Image.open(image_path)
        result_photo = ImageTk.PhotoImage(result_image)
        self.result_image_label.configure(image=result_photo)
        self.result_image_label.image = result_photo
        
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
        
    def on_closing(self):
        pygame.mixer.music.stop()
        self.root.destroy()
        
    @staticmethod
    def save_to_csv(name, score,cash):
        csv_file_path = 'leaderboard.csv'
        if not os.path.exists(csv_file_path):
            with open(csv_file_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['Name', 'Score','Cash'])
        with open(csv_file_path, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([name, score,cash])
            
    def show_leaderboard(self):
        leaderboard_data = self.get_leaderboard_data()
        self.display_leaderboard(leaderboard_data)
        
    def get_leaderboard_data(self):
        csv_file_path = 'leaderboard.csv'
        if not os.path.exists(csv_file_path):
            return []
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)
            data = [row for row in csv_reader]
        sorted_data = sorted(data, key=lambda x: int(x[1]), reverse=True)
        return sorted_data
    
    def display_leaderboard(self, leaderboard_data):
        leaderboard_window = Toplevel(self.root)
        leaderboard_window.title("Leaderboard")
        name_label = Label(leaderboard_window, text="Name", font=("Arial", 14, "bold"))
        name_label.grid(row=0, column=0, padx=10, pady=5)
        score_label = Label(leaderboard_window, text="Score", font=("Arial", 14, "bold"))
        score_label.grid(row=0, column=1, padx=10, pady=5)
        cash_label = Label(leaderboard_window, text="Cash", font=("Arial", 14, "bold"))
        cash_label.grid(row=0, column=2, padx=10, pady=5)
        for index, (name, score,cash) in enumerate(leaderboard_data, start=1):
            name_label = Label(leaderboard_window, text=name, font=("Arial", 12))
            name_label.grid(row=index, column=0, padx=10, pady=5)
            score_label = Label(leaderboard_window, text=score, font=("Arial", 12))
            score_label.grid(row=index, column=1, padx=10, pady=5)
            cash_label = Label(leaderboard_window, text=cash, font=("Arial", 12))
            cash_label.grid(row=index, column=2, padx=10, pady=5)

if __name__ == "__main__":
    quiz_app = MemeQuizApp()
    quiz_app.run()