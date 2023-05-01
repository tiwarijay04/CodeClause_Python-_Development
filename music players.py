from tkinter import *
from tkinter import filedialog
from pygame.mixer import mixer
import os

mixer.init()

def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))
    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()

def stop_song(status: StringVar):
    mixer.music.stop()

def load(listbox):
    os.chdir(filedialog.askdirectory(title='Open a songs directory'))

    tracks = os.listdir()

    for track in tracks:
        listbox.insert(END, track)

def pause_song(status: StringVar):
    mixer.music.pause()

def resume_song(status: StringVar):
    mixer.music.unpause()

root = Tk()
root.geometry('400x430')
root.title('Music Player in Python')
root.resizable(0, 0)

song_frame = LabelFrame(root, text='Now Playing', width=400, height=90)
song_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='',width=400, height=120)
button_frame.place(x=0, y=90)

listbox_frame = LabelFrame(root, text='My Playlist')
listbox_frame.place(x=0, y=210, height=210, width=400)

current_song = StringVar(root, value='*Please Select a Song*')
song_status = StringVar(root, value='<Not Available>')
playlist = Listbox(listbox_frame, font=('Helvetica', 11))

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=playlist.yview)
playlist.pack(fill=BOTH, padx=5, pady=5)
Label(song_frame, font=('Times', 10, 'bold')).place(x=10, y=10)

song_lbl = Label(song_frame, textvariable=current_song,bg='white',font=("Times", 10), width=40)
song_lbl.place(x=60, y=17.5)

pause_btn = Button(button_frame, text='Pause',   width=7,command=lambda: pause_song(song_status))
pause_btn.place(x=150, y=10)

play_btn = Button(button_frame, text='Play',  width=7,command=lambda: play_song(current_song, playlist, song_status))
play_btn.place(x=15, y=10)

resume_btn = Button(button_frame, text='Resume',  width=7,command=lambda: resume_song(song_status))
resume_btn.place(x=285, y=10)

load_btn = Button(button_frame, text='Add your Playlist',  width=35,command=lambda: load(playlist))
load_btn.place(x=60, y=60)

root.update()
root.mainloop()