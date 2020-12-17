# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 12:21:15 2020

@author: Dawid
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PyPDF2 import PdfFileMerger
import popout


def main_window(parent):
        screen_x = int(parent.winfo_screenwidth())
        screen_y = int(parent.winfo_screenheight())
        window_x = parent.winfo_width()
        window_y = parent.winfo_height()
        posX = int(round((screen_x/2) - (window_x/2), 0))
        posY = int(round((screen_y/2) - (window_y/2), 0))
        geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
        parent.minsize(window_x, window_y)
        parent.maxsize(1800, 1000)
        parent.geometry(geo)

class interactive_list:
    def __init__(self, parent):
        self.parent = parent
        self.listbox = tk.Listbox(self.parent, width=50, height=10)
        self.listbox.grid(row=0, column=0, padx=5, pady=5)
        
        vsb = ttk.Scrollbar(parent,
                            orient='vertical',
                            command=self.listbox.yview)
        vsb.grid(row=0, column=1, sticky='ns', pady=5)
        hsb = ttk.Scrollbar(parent,
                            orient='horizontal',
                            command=self.listbox.xview)
        hsb.grid(row=1, column=0, sticky='we', padx=5)
        self.listbox.configure(yscrollcommand=vsb.set)
        self.listbox.configure(xscrollcommand=hsb.set)
        
        #Frame with buttons
        frame = tk.Frame(parent, padx=5, pady=10)
        frame.grid(row=0, column=2, sticky=tk.N)
        
        #Width of the buttons
        width = 10
        
        #Add - adds new pdf file at the beginning of the list
        but_add = tk.Button(frame,
                            text='Add',
                            command=self.add,
                            width=width)
        but_add.grid(row=0, column=0, sticky=tk.W)
        
        #Del - deletes the selected file
        but_del = tk.Button(frame,
                            text='Delete',
                            command=self.delete,
                            width=width)
        but_del.grid(row=1, column=0, sticky=tk.W)
        
        #Top - puts the selected file at the top of the list
        but_top = tk.Button(frame,
                            text='To top',
                            command=self.totop,
                            width=width)
        but_top.grid(row=2, column=0, sticky=tk.W)
        
        #Bot - puts the selected file at the bottom of the list
        but_bot = tk.Button(frame,
                            text='To bottom',
                            command=self.tobottom,
                            width=width)
        but_bot.grid(row=3, column=0, sticky=tk.W)
        
        #Mer - merges the pdf files in the order in the list
        but_mer = tk.Button(frame,
                            text='Merge pdfs',
                            command=self.merge,
                            width=width)
        but_mer.grid(row=4, column=0)
        
        parent.update()
        main_window(parent)
        
    def add(self, initialdir=''):
        title = 'Please select a file'
        filepath = filedialog.askopenfilename(parent=self.parent,
                                                title=title,
                                                initialdir=initialdir)
        if filepath is None or filepath == '':
            return
        self.listbox.insert(0, filepath)
        
    def delete(self):
        try:
            self.listbox.delete(self.listbox.curselection())
        except:
            pass
        
    def totop(self):
        current_selection = self.listbox.get(tk.ACTIVE)
        if current_selection is None or current_selection == '':
            return
        self.listbox.delete(self.listbox.curselection())
        self.listbox.insert(0, current_selection)
        
    def tobottom(self):
        current_selection = self.listbox.get(tk.ACTIVE)
        if current_selection is None or current_selection == '':
            return
        self.listbox.delete(self.listbox.curselection())
        self.listbox.insert(tk.END, current_selection)
        
    def merge(self):
        merger = PdfFileMerger()
        pdfs = self.listbox.get(0, last=tk.END)
        if len(pdfs) < 2:
            #Check if enough files to merge
            msg = 'There must be more than one file to merge'
            popout.Warning(self.parent, msg)
            return
        filepath = filedialog.asksaveasfilename(defaultextension='.pdf',
                                                initialdir='')
        if filepath is None or filepath == '':
            #Check if filepath empty
            msg = 'You must choose a file name'
            popout.Warning(self.parent, msg)
            return
        
        #Merging process
        for pdf in pdfs:
            merger.append(pdf)
        merger.write(filepath)
        merger.close()
        
        #Message with confirmation
        msg = 'Files have been successfully merged'
        popout.Warning(self.parent, msg)
        
root = tk.Tk()
root.title('PDF File Merger')
content = interactive_list(root)
root.mainloop()