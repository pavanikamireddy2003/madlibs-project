from tkinter import *  
def Story11(win):  
  def final(tl: Toplevel, user_name, sports, City, playeruser_name, drinkuser_name, snacks):  
    text1 = f''''' 
       We decided to play a {sports} game in {City} one day with our friend {user_name}. 
But we were unable to play. Consequently, we attended the game to watch our favourite player, {playeruser_name}. 
We consumed {drinkuser_name} and some {snacks} as well. 
It was great fun for us! We are eager to visit once more and have fun. 
'''  
    tl.geometry(newGeometry='500x550')  
    Label(tl, text='Story:',  wraplength=tl.winfo_width()).place(x=160, y=310)  
    Label(tl, text=text1,wraplength=tl.winfo_width()).place(x=0, y=330)  
  NewScreen11 = Toplevel(win, bg='yellow')  
  NewScreen11.title("A Memorable Day")  
  NewScreen11.geometry('500x500')  
  Label(NewScreen11, text=' A Memorable Day').place(x=100, y=0)  
  Label(NewScreen11, text='User_name:').place(x=0, y=35)  
  Label(NewScreen11, text='Enter a game:').place(x=0, y=70)  
  Label(NewScreen11, text='Enter a city:').place(x=0, y=110)  
  Label(NewScreen11, text='Enter the user_name of a player:').place(x=0, y=150)  
  Label(NewScreen11, text='Enter the user_name of a drink:').place(x=0, y=190)  
  Label(NewScreen11, text='Enter the user_name of a snack:').place(x=0, y=230)  
  User_name = Entry(NewScreen11, width=11)  
  User_name.place(x=200, y=35)  
  game = Entry(NewScreen11, width=11)  
  game.place(x=200, y=70)  
  city = Entry(NewScreen11, width=11)  
  city.place(x=200, y=105)  
  player = Entry(NewScreen11, width=11)  
  player.place(x=200, y=150)  
  drink = Entry(NewScreen11, width=11)  
  drink.place(x=200, y=190)  
  snack = Entry(NewScreen11, width=11)  
  snack.place(x=200, y=230)  
  SubmitButton1  = Button(NewScreen11, text="Submit", background="Brown", font=('Calibri', 12), command=lambda:final(NewScreen11, User_name.get(), game.get(), city.get(), player.get(), drink.get(), snack.get()))  
  SubmitButton1.place(x=150, y=270)  
  NewScreen11.mainloop()  
def Story22(win):  
    def final(tl: Toplevel, path, pronoun, emotional, emotion, adverb):  
            text1 = f''''' 
            When I was younger, I wanted to be a {path}, but as I got older, I became interested in the {pronoun} and decided to become an engineer. Then I started working at a job where I was not {emotional}. 
I decided to pursue my passion after experiencing {emotion} 
Despite receiving less {adverb} than I did in my prior employment. 
I'm very sensitive. '''  
#let us set the geometry of the project  
            tl.geometry(newGeometry='500x550')  
            Label(tl, text='Story:',  wraplength=tl.winfo_width()).place(x=160, y=310)  
            Label(tl, text=text1,wraplength=tl.winfo_width()).place(x=0, y=330)  
    NewScreen11 = Toplevel(win, bg='red')  
    NewScreen11.title("Career")  
    NewScreen11.geometry('500x500')  
    Label(NewScreen11, text='Career').place(x=150, y=0)  
    Label(NewScreen11, text='Your Childhood dream:').place(x=0, y=35)  
    Label(NewScreen11, text='Your current interest:').place(x=0, y=70)  
    Label(NewScreen11, text='Enter a emotion:').place(x=0, y=110)  
    Label(NewScreen11, text='Enter a negative emotion:').place(x=0, y=150)  
    Label(NewScreen11, text='Enter a adverb:').place(x=0, y=190)  
    Path = Entry(NewScreen11, width=15)  
    Path.place(x=200, y=35)  
    Pronoun = Entry(NewScreen11, width=15)  
    Pronoun.place(x=200, y=70)  
    Emotional = Entry(NewScreen11, width=15)  
    Emotional.place(x=200, y=110)  
    Emotion= Entry(NewScreen11, width=15)  
    Emotion.place(x=200, y=150)  
    Adverb = Entry(NewScreen11, width=15)  
    Adverb.place(x=200, y=190)  
    SubmitButton1  = Button(NewScreen11, text="Submit", background="Brown", font=('Calibri', 12), command=lambda:final(NewScreen11, Path.get(), Pronoun.get(), Emotional.get(), Emotion.get(), Adverb.get()))  
    SubmitButton1.place(x=150, y=270)  
Screen11 = Tk()  
Screen11.title(" Mad Libs Generator")  
Screen11.geometry('400x400')  
Screen11.config(bg="pink")  
Label(Screen11, text=' Mad Libs Generator').place(x=100, y=20)  
Story111Button = Button(Screen11, text='A memorable day', font=("Calibri New Roman", 13),command=lambda: Story11(Screen11),bg='Brown')  
Story111Button.place(x=140, y=90)  
Story222Button = Button(Screen11, text='Career', font=("Calibri New Roman", 13),command=lambda: Story22(Screen11), bg='Brown')  
Story222Button.place(x=150, y=150)  
Screen11.update()  
Screen11.mainloop()  