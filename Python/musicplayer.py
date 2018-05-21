from tkinter import *
import tkinter.messagebox
import urllib.parse
import urllib.request
import json
import mp3play

music_name = ""
list_music_url = []
list_music_name = []
# 搜索音乐
def get_music():
    global music_name
    music_name = music_int.get().encode("utf-8")
    if not music_name:
        tkinter.messagebox.showinfo("提示：", "无此音乐")
        return
    music_name = urllib.parse.quote(music_name) # 将输入的中文名转码
    # 网易云音乐链接
    html = urllib.request.urlopen('http://s.music.163.com/search/get/?type=1&s=%s&limit=9' % music_name).read()
    music_list = json.loads(html)
    list_music = music_list['result']['songs']
    global list_music_url
    global list_music_name
    listbox.delete(0, listbox.size())
    for i in list_music:
        listbox.insert(END, i['name'] + "(" + i['artists'][0]['name'] + ")")
        list_music_url.append(i['audio'])
        list_music_name.append(i['name'])

def play_music(*args):
    global mp3
    sy = listbox.curselection()[0]
    mp3 = mp3play.load(list_music_url[sy])
    mp3.play()
    var.set("正在播放")
    urllib.request.urlretrieve(list_music_url[sy], list_music_name[sy] + '.mp3')

win = Tk()
win.title('zhx')
win.geometry('+630+100')
music_int = Entry(win, font=('宋体', 20))
music_int.grid(row=0, column=1)
listbox = Listbox(win, width=50)
listbox.bind('<Double-Button-1>', play_music)
listbox.grid(column=1)
button = Button(win, text='搜索音乐', font=('宋体', 20), fg='blue', bg='green', command=get_music)
button.grid(row=2, column=1)
var = StringVar()
var.set('已准备就绪')
label = Label(win, font=('宋体', 15), fg='red', textvariable=var)
label.grid(row=3, column=1)
win.mainloop()
