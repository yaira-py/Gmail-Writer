import tkinter as tk
from tkinter import scrolledtext

class EmailWriter:
    def __init__(self,root):
        self.root=root
        self.root.title('New Message')
        self.root.geometry('500x600')

        self.to_label=tk.Label(self.root,text='To:')
        self.to_label.pack(anchor='w',padx=10,pady=(10,2))

        self.to_entry=tk.Entry(self.root,width=50)
        self.to_entry.pack(padx=10,pady=(0,10))

        self.sub_label=tk.Label(self.root,text='Subject:')
        self.sub_label.pack(anchor='w',padx=10,pady=(5,2))

        self.sub_entry=tk.Entry(self.root,width=50)
        self.sub_entry.pack(padx=10,pady=(0,10))

        self.bottom_frame=tk.Frame(self.root,bg='#f2f2f2')
        self.bottom_frame.pack(side='bottom',fill='x',padx=15,pady=15)

        self.send_btn=tk.Button(self.bottom_frame,text='Send',bg='#1a73e8',fg='white',font=('Arial',10,'bold'),
                                command=self.send_email)
        self.send_btn.pack(side='left')

        self.status_label=tk.Label(self.bottom_frame,text='',bg='#f2f2f2',font=('Arial',9))
        self.status_label.pack(side='left',padx=10)

        self.body_label=tk.Label(self.root,text="Body:",font=('Arial',9,'bold'),bg='#f2f2f2',fg='#5f6368')
        self.body_label.pack(anchor='w',padx=10,pady=(5,2))

        self.body_text=scrolledtext.ScrolledText(self.root,font=('Arial',10),bd=1,relief='solid')
        self.body_text.pack(fill='both',expand='True',padx=10,pady=(0,10))


    def send_email(self):
        recipient=self.to_entry.get()
        if recipient:
            self.status_label.config(text=f'Message sent to {recipient}!')

        else:
            self.status_label.config(text='Please enter a recipient!',fg='red')












if __name__=="__main__":
    window=tk.Tk()
    app=EmailWriter(window)
    window.mainloop()
