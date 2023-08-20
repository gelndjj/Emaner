import tkinter as tk, os, re
from tkinter import ttk, filedialog

class FileRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Renamer")
        self.root.geometry("830x300")
        self.selected_extension = "All extensions"  # Default selection

        # Left Frame
        self.left_frame = tk.Frame(self.root, bg='#3A7FF6', width=220)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        label_title = ("Welcome to Emaner")

        label_text = ("Emaner renames your files \n"
                      "according to your will.\n\n"
                      "Simply type the text\n"
                      "to see the change\n"
                      "and click on Rename Files.\n\n"
                      )

        self.left_label_title = tk.Label(self.left_frame, text=label_title, justify=tk.LEFT, bg='#3A7FF6', fg='white', font=("Arial-BoldMT", int(18.0)))
        self.left_label_title.place(x=4,y=20)

        self.left_label = tk.Label(self.left_frame, text=label_text, justify=tk.LEFT, bg='#3A7FF6', fg='white', font=("Georgia", int(14.0)))
        self.left_label.place(x=4,y=80)

        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.extension_combobox = ttk.Combobox(self.right_frame, values=[], state="readonly", width=12)
        self.extension_combobox.place(x=260, y=235)
        self.extension_combobox.bind("<<ComboboxSelected>>", self.update_extension_listbox)

        self.replace_file_list = []
        self.replace_include_subfolders = tk.IntVar(value=0)
        self.replace_use_regex = tk.IntVar(value=0)
        self.replace_preserve_extensions = tk.IntVar(value=0)
        self.replace_string = tk.StringVar(value="")
        self.replace_new_string = tk.StringVar(value="")

        self.replace_select_button = tk.Button(self.root, text="Select Folder", command=self.replace_select_folder)
        self.replace_select_button.pack(pady=10)

        self.replace_listbox = tk.Listbox(self.right_frame, selectmode=tk.MULTIPLE, width=40, height=12)
        self.replace_listbox.place(x=28, y=12)

        self.replace_subfolder_checkbox = tk.Checkbutton(self.root, text="Include Subfolders",
                                                         variable=self.replace_include_subfolders,
                                                         command=self.update_replace_listbox)
        self.replace_subfolder_checkbox.pack()

        self.replace_regex_checkbox = tk.Checkbutton(self.root, text="Regular Expression",
                                                     variable=self.replace_use_regex,
                                                     command=self.update_replace_listbox)
        self.replace_regex_checkbox.pack()

        self.replace_preserve_ext_checkbox = tk.Checkbutton(self.root, text="Preserve Extensions",
                                                            variable=self.replace_preserve_extensions,
                                                            command=self.update_replace_listbox)
        self.replace_preserve_ext_checkbox.pack()

        self.replace_label = tk.Label(self.root, text="Replace:")
        self.replace_label.pack()

        self.replace_entry = tk.Entry(self.root, textvariable=self.replace_string)
        self.replace_entry.pack()

        self.replace_new_label = tk.Label(self.root, text="New:")
        self.replace_new_label.pack()

        self.replace_new_entry = tk.Entry(self.root, textvariable=self.replace_new_string)
        self.replace_new_entry.pack()

        self.replace_rename_button = tk.Button(self.root, text="Rename Files", command=self.rename_replace_files)
        self.replace_rename_button.pack(pady=10)

        self.replace_re_button = tk.Button(self.root, text="?", command=self.show_ins)
        self.replace_re_button.place(x=393,y=68)

        self.replace_string.trace("w", self.update_replace_listbox)
        self.replace_new_string.trace("w", self.update_replace_listbox)

    def update_extension_combobox(self):
        extensions = set()
        extensions.add("All extensions")  # Add "All extensions" as the first option
        for file_path in self.replace_file_list:
            _, extension = os.path.splitext(file_path)
            extensions.add(extension)
        self.extension_combobox["values"] = sorted(list(extensions))  # Sort the extensions

    def update_extension_listbox(self, event=None):
        self.selected_extension = self.extension_combobox.get()
        self.update_replace_listbox()
        selected_extension = self.extension_combobox.get()
        self.replace_listbox.delete(0, tk.END)
        replace_text = self.replace_string.get()
        new_text = self.replace_new_string.get() or ""

        for file_path in self.replace_file_list:
            _, extension = os.path.splitext(file_path)
            if selected_extension == "All extensions" or extension == selected_extension:
                old_file_name = os.path.basename(file_path)
                new_file_name = old_file_name
                if replace_text:
                    if self.replace_preserve_extensions.get():
                        file_name, file_extension = os.path.splitext(old_file_name)
                        if self.replace_use_regex.get():
                            new_file_name = re.sub(replace_text, new_text, file_name) + file_extension
                        else:
                            new_file_name = file_name.replace(replace_text, new_text) + file_extension
                    else:
                        if self.replace_use_regex.get():
                            new_file_name = re.sub(replace_text, new_text, old_file_name)
                        else:
                            new_file_name = old_file_name.replace(replace_text, new_text)
                self.replace_listbox.insert(tk.END, new_file_name)

    def replace_select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.replace_folder_path = folder_path
            self.replace_include_subfolders.set(0)
            self.replace_use_regex.set(0)
            self.replace_preserve_extensions.set(0)
            self.extension_combobox.set("")
            self.update_replace_listbox()

    def update_replace_file_list(self):
        self.replace_file_list = []
        if self.replace_include_subfolders.get():
            for root_dir, _, files in os.walk(self.replace_folder_path):
                for filename in files:
                    self.replace_file_list.append(os.path.join(root_dir, filename))
        else:
            self.replace_file_list = [os.path.join(self.replace_folder_path, filename) for filename in
                                      os.listdir(self.replace_folder_path) if
                                      os.path.isfile(os.path.join(self.replace_folder_path, filename))]

    def update_replace_listbox(self, *args):
        self.update_replace_file_list()
        self.update_extension_combobox()
        replace_text = self.replace_string.get()
        new_text = self.replace_new_string.get() or ""
        use_regex = self.replace_use_regex.get()
        preserve_extensions = self.replace_preserve_extensions.get()
        self.replace_listbox.delete(0, tk.END)
        for file_path in self.replace_file_list:
            _, extension = os.path.splitext(file_path)
            if self.selected_extension == "All extensions" or extension == self.selected_extension:
                old_file_name = os.path.basename(file_path)
                if preserve_extensions:
                    file_name, file_extension = os.path.splitext(old_file_name)
                    new_file_name = file_name
                    if use_regex:
                        new_file_name = re.sub(replace_text, new_text, new_file_name)
                    else:
                        new_file_name = new_file_name.replace(replace_text, new_text)
                    new_file_name += file_extension
                else:
                    new_file_name = old_file_name
                    if use_regex:
                        new_file_name = re.sub(replace_text, new_text, new_file_name)
                    else:
                        new_file_name = new_file_name.replace(replace_text, new_text)
                self.replace_listbox.insert(tk.END, new_file_name)

    def rename_replace_files(self):
        old_string = self.replace_string.get()
        new_string = self.replace_new_string.get() or " "
        use_regex = self.replace_use_regex.get()
        preserve_extensions = self.replace_preserve_extensions.get()
        selected_extension = self.extension_combobox.get()

        if old_string:
            for file_path in self.replace_file_list:
                file_dir, old_file_name = os.path.split(file_path)
                _, extension = os.path.splitext(old_file_name)

                if selected_extension and extension != selected_extension:
                    continue

                if preserve_extensions:
                    file_name, file_extension = os.path.splitext(old_file_name)
                    new_file_name = file_name
                    if use_regex:
                        new_file_name = re.sub(old_string, new_string, new_file_name)
                    else:
                        new_file_name = new_file_name.replace(old_string, new_string)
                    new_file_name += file_extension
                else:
                    new_file_name = old_file_name
                    if use_regex:
                        new_file_name = re.sub(old_string, new_string, new_file_name)
                    else:
                        new_file_name = new_file_name.replace(old_string, new_string)
                new_file_path = os.path.join(file_dir, new_file_name)
                os.rename(file_path, new_file_path)
                print(f"Renamed {old_file_name} to {new_file_name}")

            self.update_extension_combobox()  # Update the extensions in the ComboBox
            self.update_replace_listbox()  # Update the Listbox after renaming

    def show_ins(self):
        re_exp = tk.Toplevel(self.root)
        re_exp.title('Regular Expressions Examples')
        re_exp.geometry('480x300')
        re_exp.resizable(0, 0)

        re_exp_listbox = tk.Listbox(re_exp,
                                    width=50,
                                    height=20,
                                    borderwidth=1,
                                    background='#e8e6e6')
        re_exp_listbox.pack()
        re_exp_listbox.insert(tk.END, '. - Matches any single character except newline.\n',
                              '^ - Matches the start of a string.\n',
                              '$ - Matches the end of a string.\n',
                              '* - Matches zero or more occurrences of the previous character or group.\n',
                              '+ - Matches one or more occurrences of the previous character or group.\n',
                              '? - Matches zero or one occurrence of the previous character or group.\n',
                              '{n} - Matches exactly n occurrences of the previous character or group.\n',
                              '{n,} - Matches n or more occurrences of the previous character or group.\n',
                              '{n,m} - Matches at least n and at most m occurrences of the previous character or group.\n',
                              '[abc] - Matches any one of the characters a, b, or c.\n',
                              '[^abc] - Matches any character except a, b, or c.\n',
                              '| - Matches either the expression before or after the vertical bar.\n',
                              '\d - Matches any digit (0-9).\n',
                              '\D - Matches any character that is not a digit.\n',
                              '\w - Matches any word character (a-z, A-Z, 0-9, and underscore).\n',
                              '\W - Matches any character that is not a word character.\n',
                              '\s - Matches any whitespace character (space, tab, newline, etc.).\n',
                              '\S - Matches any non-whitespace character.')

if __name__ == "__main__":
    root = tk.Tk()
    app = FileRenamerApp(root)
    root.mainloop()