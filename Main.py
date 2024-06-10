# Credits to Vexels, Vector Stock, Flaticon, and Tales of the Rays for their images used in this game.
# Import the modules that are used in this game.

import tkinter 
import time 
import random
from tkinter import messagebox
from PIL import Image, ImageTk

root = tkinter.Tk()
root.geometry("1000x1000")
root.title("Arts of Melee")
root.resizable(False, False)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# Attribute Variables

maxHealth = 100 # This can be altered using items ingame.
maxDefense = 50 # This can be altered using items ingame.
maxMana = 100 # This can be altered using items ingame.
maxStamina = 100 # This can be altered using items ingame.

normalWeapons = {
    "Knife": "Images/Knife.png",
    "Sword": "Images/Sword.png",
    "Spear": "Images/Spear.png",
    "Bat": "Images/Bat.png",
    "Crowbar": "Images/Crowbar.png"
}

specialWeapons = {
    "Fireaxe": "Images/Fireaxe.png",
    "Karambit": "Images/Karambit.png",
    "Spiked Bat": "Spiked Bat.png",
    "Machete": "Machete.png",
    "Chainsaw": "Chainsaw.png"
}

uniqueWeapons = {
    "Pumpkin Launcher": "Pumpkin Launcher.png",
    "Infernal Blade": "Infernal Blade.png",
    "Scythe": "Scythe.png",
    "Trident": "Trident.png",
    "Cryo Gauntlet": "Cryo Gauntlet.png"
}

# Tkinter Variables

def player(health, defense, mana, stamina):
    healthLabel = tkinter.Label(root, text=f"Health: {health}")
    healthLabel.grid(row=0,column=0)
    defenseLabel = tkinter.Label(root, text=f"Defense: {defense}")
    healthLabel.grid(row=1,column=0)
    manaLabel = tkinter.Label(root, text=f"Mana: {mana}")
    manaLabel.grid(row=2,column=0)
    staminaLabel = tkinter.Label(root, text=f"Stamina: {stamina}")
    staminaLabel.grid(row=3,column=0)
    attackButton = tkinter.Button(root, text="Attack")
    attackButton.grid(row=4,column=0)
    healButton = tkinter.Button(root, text="Heal")
    healButton.grid(row=5,column=0)

def enemy(name, health, defense):
    enemyName = tkinter.Label(root, text="Name:")
    enemyHealth = tkinter.Label(root, text="Health:")
    enemyDefense = tkinter.Label(root, text="Defense:")

def playerAttack():
    print("Hello")

def playerHeal():
    print("Hello")

def enemyAttack():
    print("Hello")

# End of the code. This is where everything is created.

player(15, 5, 15, 15)

root.mainloop()