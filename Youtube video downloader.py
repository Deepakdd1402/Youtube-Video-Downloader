from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""


def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose  the Folder(OR)Path!!",fg="red")



def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste the Link again!!",fg="red")



    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")



root = Tk()
root.title("Youtube video Downloader")
root.geometry("650x700")
root.columnconfigure(0,weight=1)


ytdLabel = Label(root,text="Enter/paste the URL of the Video to Download",font=("jost",15,"bold"))
ytdLabel.grid()


ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()


ytdError = Label(root,text="Error ",fg="red",font=("jost",10))
ytdError.grid()


saveLabel = Label(root,text="Select the file path to save the video",font=("jost",15,"bold"))
saveLabel.grid()


saveEntry = Button(root,width=15,bg="red",fg="white",text="Choose the Path",command=openLocation)
saveEntry.grid()


locationError = Label(root,text="Error",fg="red",font=("jost",10))
locationError.grid()


ytdQuality = Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()

choices = ["720p","420p","AUDIO(MP3,128k)"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()


downloadbtn = Button(root,text="Download",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

developerlabel = Label(root,text="YOUTUBE  VIDEO  DOWNLOADER ",font=("jost",20,"bold"),fg="blue")
developerlabel.grid()
root.mainloop()