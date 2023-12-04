import tkinter as tk
from tkinter import messagebox
from login import Login

class CGUI:
    def __init__(self):
        self.mainWindow = None
        self.loginFrame = None

    def openLoginFrame(self):
        self.loginFrame = tk.Frame(self.mainWindow)
        self.loginFrame.pack(padx=10, pady=10)

        usernameLabel = tk.Label(self.loginFrame, text='Username')
        passwordLabel = tk.Label(self.loginFrame, text='Password')

        usernameEntry = tk.Entry(self.loginFrame)
        passwordEntry = tk.Entry(self.loginFrame, show='*')

        loginButton = tk.Button(self.loginFrame, text='Login', command=lambda: self.handleLogin(usernameEntry.get(), passwordEntry.get()))

        usernameLabel.grid(row=0, column=0, padx=5, pady=5)
        passwordLabel.grid(row=1, column=0, padx=5, pady=5)
        usernameEntry.grid(row=0, column=1, padx=5, pady=5)
        passwordEntry.grid(row=1, column=1, padx=5, pady=5)
        loginButton.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def handleLogin(self, username, password):
        resultLogin = Login.Guilogin(username, password)

        if resultLogin == 2:
            messagebox.showinfo('Login Successful', f'Welcome {username}')
        elif resultLogin == -1:
            messagebox.showerror('Access Denied', 'You have exceeded the maximum login attempts')
        else:
            messagebox.showerror('Login Failed', 'Invalid username or password')

    def openMainWindow(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.attributes('-fullscreen', True)

    def run(self):
        self.openMainWindow()
        self.openLoginFrame()
        self.mainWindow.mainloop()

if __name__ == "__main__":
    app = CGUI()
    app.run()
