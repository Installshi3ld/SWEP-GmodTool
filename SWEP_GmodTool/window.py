
from asyncio.windows_events import NULL
from select import select
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

import re
import Main
import list
import randomString
import tkinter as tk


window = tk.Tk()
window.geometry('1000x800')

basicWeaponLabelFrame = LabelFrame(window, text="Basic Weapon creation", padx=10, pady=10)
basicWeaponLabelFrame.grid(row= 1, column=1)

randomWeaponLabelFrame = LabelFrame(window, text="Random Weapon creation", padx=10, pady=10)
randomWeaponLabelFrame.grid(row= 1, column=1)

#MenuBar
def alert():
    showinfo("alerte", "Bravo!")

#For Basic Weapon Label Frame----------------------------------
def ShowBasicWeaponLabelFrame():

    randomWeaponLabelFrame.grid_remove()
    basicWeaponLabelFrame.grid()

#For random Weapon Label Frame----------------------------------
    
def ShowRandomWeaponLabelFrame():

    basicWeaponLabelFrame.grid_remove()
    randomWeaponLabelFrame.grid()

#########################################################################################################


   

WeaponInformationLabelFrame = LabelFrame(basicWeaponLabelFrame, text="Weapon Information", padx=10, pady=10)
WeaponInformationLabelFrame.grid(row= 1, column=1)

#Weapon information ----------------------------------------------------------------------
#Weapon name in game
Label(WeaponInformationLabelFrame, text=' Weapon Name (In game) :', borderwidth=1).grid(row=1, column=1)
weaponNameEntry = Entry(WeaponInformationLabelFrame, width = 20)
weaponNameEntry.grid(row=1, column=2)

#Weapon name file
Label(WeaponInformationLabelFrame, text=' Weapon Name (File):', borderwidth=1).grid(row=2, column=1)
weaponNameFileEntry = Entry(WeaponInformationLabelFrame, width = 20)
weaponNameFileEntry.grid(row=2, column=2)

#Weapon name file
Label(WeaponInformationLabelFrame, text=' Weapon Author:', borderwidth=1).grid(row=1, column=3)
weaponAuthorEntry = Entry(WeaponInformationLabelFrame, width = 20)
weaponAuthorEntry.grid(row=1, column=4)

#Weapon name file
Label(WeaponInformationLabelFrame, text=' Weapon Instruction:', borderwidth=1).grid(row=2, column=3)
weaponInstructionEntry = Entry(WeaponInformationLabelFrame, width = 20)
weaponInstructionEntry.grid(row=2, column=4)

#Weapon Information randomize
def randomizeWeaponInformation():
    weaponNameEntry.delete(0, 'end')
    weaponNameEntry.insert(0, randomString.randomString())

    weaponNameFileEntry.delete(0, 'end')
    weaponNameFileEntry.insert(0, randomString.randomString())

    weaponAuthorEntry.delete(0, 'end')
    weaponAuthorEntry.insert(0, randomString.randomString())

    weaponInstructionEntry.delete(0, 'end')
    weaponInstructionEntry.insert(0, randomString.randomString())

Button(WeaponInformationLabelFrame, text="Randomize weapon information",command=randomizeWeaponInformation).grid(row=3, column=4)

#---------------------------------------------------------------------------------------------
#WEAPON SPAWN INFORMATION

WeaponSpawnInformationLabelFrame = LabelFrame(basicWeaponLabelFrame, text="Weapon Spawn Information", padx=10, pady=10)
WeaponSpawnInformationLabelFrame.grid(row= 2, column=1)

#Only admin check box
onlyAdmin = tk.IntVar()
Label(WeaponSpawnInformationLabelFrame, text='Admin only:', borderwidth=1).grid(row=1, column=1)
checkboxAdminOnly = Checkbutton(WeaponSpawnInformationLabelFrame, variable=onlyAdmin, onvalue= 1, offvalue=0)
checkboxAdminOnly.grid(row=1, column= 2)

#Weapon spawnable
weaponSpawnable = tk.IntVar()
Label(WeaponSpawnInformationLabelFrame, text=' Spawnable:', borderwidth=1).grid(row=1, column=3)
checkboxSpawnable = Checkbutton(WeaponSpawnInformationLabelFrame, variable=weaponSpawnable, onvalue= 1, offvalue=0)
checkboxSpawnable.select()
checkboxSpawnable.grid(row=1, column= 4)
    
#Weapon category
Label(WeaponSpawnInformationLabelFrame, text=' Weapon Category:', borderwidth=1).grid(row=1, column=5)
weaponCategoryEntry = Entry(WeaponSpawnInformationLabelFrame, width = 20)
weaponCategoryEntry.grid(row=1, column=6)



#---------------------------------------------------------------------------------------------
#WEAPON PRIMARY ATTACK

#Enable/ disable Primary Attack
varPrimaryLabelFrame = tk.IntVar()
def enable_DisableWeaponPrimaryAttackLabelFrame():
    if(varPrimaryLabelFrame.get() == 1):
        weaponPrimaryAttackLabelFrame.grid()
    elif(varPrimaryLabelFrame.get() == 0):
        weaponPrimaryAttackLabelFrame.grid_remove()

#CheckBox enable/disable Primary Attack

weaponPrimaryAttackCheckBox = Checkbutton(basicWeaponLabelFrame,text= "Weapon Primary Attack",variable = varPrimaryLabelFrame, onvalue=1, offvalue=0, command=enable_DisableWeaponPrimaryAttackLabelFrame)
weaponPrimaryAttackCheckBox.select()
weaponPrimaryAttackCheckBox.grid(row=1, column=2)

#Define Primary Attack Label Frame
weaponPrimaryAttackLabelFrame = LabelFrame(basicWeaponLabelFrame, text="Weapon Primary Attack", padx=10, pady=10)
weaponPrimaryAttackLabelFrame.grid(row= 2, column=2)

#Primary damage
Label(weaponPrimaryAttackLabelFrame, text='Weapon Primary Damage:', borderwidth=1).grid(row=1, column=1)
weaponPrimaryDamageEntry = Spinbox(weaponPrimaryAttackLabelFrame, from_=0, to= 1000)
weaponPrimaryDamageEntry.grid(row=1, column=2)

#Primary clip size
Label(weaponPrimaryAttackLabelFrame, text='Weapon Clip size:', borderwidth=1).grid(row=2, column=1)
weaponPrimaryAttackClipSize = Spinbox(weaponPrimaryAttackLabelFrame, from_=0, to= 1000)
weaponPrimaryAttackClipSize.grid(row=2, column=2)

#Primary ammo type
Label(weaponPrimaryAttackLabelFrame, text='Ammo type:', borderwidth=1).grid(row=3, column=1)
weaponPrimaryAmmoType = tk.StringVar(weaponPrimaryAttackLabelFrame)
weaponPrimaryAmmoType.set(list.weaponAmmoType[2])
weaponAmmoTypeMenu = tk.OptionMenu(weaponPrimaryAttackLabelFrame, weaponPrimaryAmmoType, *list.weaponAmmoType)
weaponAmmoTypeMenu.grid(row=3, column=2)

#Primary automatic 
varPrimaryAutomatic = tk.IntVar()
Label(weaponPrimaryAttackLabelFrame, text='Automatic:', borderwidth=1).grid(row=4, column=1)
weaponPrimaryAutomaticCheckBox = Checkbutton(weaponPrimaryAttackLabelFrame,variable = varPrimaryAutomatic, onvalue=1, offvalue=0)
weaponPrimaryAutomaticCheckBox.grid(row=4, column=2)




def updateModel3DMenu(self):
    
    #If choose file is choose
    if(model3DType.get() == chooseFile):
        model3DFilePath = askopenfilename(title="Choose a 3D model",filetypes=[('mdl files','.mdl'),('all files','.*')])

        #if filepath != NULL
        if(model3DFilePath != ""):
            model3DList.insert(len(model3DList)-1, model3DFilePath)

            removeModel3Dmenu = model3DMenu["menu"]
            removeModel3Dmenu.delete(0, "end")

            for string in model3DList:
                    removeModel3Dmenu.add_command(label=string, 
                                    command=lambda value=string: model3DMenu.set(value))


#Model3D
chooseFile = "Choose file..."
Label(basicWeaponLabelFrame, text='3D model:', borderwidth=1).grid(row=5, column=1)
model3DList = ["pistol", "357", "shotgun", "crossbow", chooseFile]
model3DType = tk.StringVar(basicWeaponLabelFrame)
model3DType.set("Pistol")
model3DMenu = tk.OptionMenu(basicWeaponLabelFrame, model3DType, *model3DList)
model3DMenu.grid(row=5, column=2)


##THROW GRENADE -------------------------------------------------------------------------------------------------------------------------------------------------

#Enable/ disable Throw grenade skill
varcanThrowGrenadeCheckBox = tk.IntVar()
def enable_DisablePrimaryThrowGrenadeLabelFrame():
    if(varcanThrowGrenadeCheckBox.get() == 1):
        weaponThrowGrenadeLabelFrame.grid()
    elif(varcanThrowGrenadeCheckBox.get() == 0):
        weaponThrowGrenadeLabelFrame.grid_remove()

#can throw grenade
weaponCanThrowGrenadeCheckBox = Checkbutton(basicWeaponLabelFrame,text= "Throw grenade",variable = varcanThrowGrenadeCheckBox, onvalue=1, offvalue=0, command=enable_DisablePrimaryThrowGrenadeLabelFrame)
weaponCanThrowGrenadeCheckBox.select()
weaponCanThrowGrenadeCheckBox.grid(row=6, column=1)

#Define Throw Grenade Label Frame
weaponThrowGrenadeLabelFrame = LabelFrame(basicWeaponLabelFrame, text="Throw grenade", padx=10, pady=10)
weaponThrowGrenadeLabelFrame.grid(row= 7, column=1)

#Get throw grenade probability
weaponThrowGrenadeScale = Scale(weaponThrowGrenadeLabelFrame, orient= 'horizontal', from_=0, to=100, tickinterval=10, length=350, label='Probability')
weaponThrowGrenadeScale.grid(row=1, column=1)


##SHOTGUN SHOOT-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Enable/ disable Shotgun shot
varcanShotgunShotCheckBox = tk.IntVar()
def enable_DisableShotgunShootLabelFrame():
    if(varcanShotgunShotCheckBox.get() == 1):
        weaponShotgunShotLabelFrame.grid()
    elif(varcanShotgunShotCheckBox.get() == 0):
        weaponShotgunShotLabelFrame.grid_remove()

#Can shotgun shot
weaponCanShotgunShotCheckBox = Checkbutton(basicWeaponLabelFrame,text= "ShotgunShot",variable = varcanShotgunShotCheckBox, onvalue=1, offvalue=0, command=enable_DisableShotgunShootLabelFrame)
weaponCanShotgunShotCheckBox.select()
weaponCanShotgunShotCheckBox.grid(row=6, column=2)

#Define Shotgun shot Label Frame
weaponShotgunShotLabelFrame = LabelFrame(basicWeaponLabelFrame, text="ShotgunShot", padx=10, pady=10)
weaponShotgunShotLabelFrame.grid(row= 7, column=2)

#Shotgun shot probability
weaponShotgunShotScale = Scale(weaponShotgunShotLabelFrame, orient= 'horizontal', from_=0, to=100, tickinterval=10, length=350, label='Probability')
weaponShotgunShotScale.grid(row=1, column=1)

##BOUNCE SHOT----------------------------------------------------------------------------------------------------------------------------------------------

#Enable/ disable Bounce shot
varcanBounceShotCheckBox = tk.IntVar()
def enable_DisableBounceShotLabelFrame():
    if(varcanBounceShotCheckBox.get() == 1):
        weaponBounceShotLabelFrame.grid()
    elif(varcanBounceShotCheckBox.get() == 0):
        weaponBounceShotLabelFrame.grid_remove()

#Can bounce shoot
weaponCanBounceShotCheckBox = Checkbutton(basicWeaponLabelFrame,text= "Bounce shot",variable = varcanBounceShotCheckBox, onvalue=1, offvalue=0, command=enable_DisableBounceShotLabelFrame)
weaponCanBounceShotCheckBox.select()
weaponCanBounceShotCheckBox.grid(row=8, column=1)

#Define Bounce shot Label Frame
weaponBounceShotLabelFrame = LabelFrame(basicWeaponLabelFrame, text="Bounce shot", padx=10, pady=10)
weaponBounceShotLabelFrame.grid(row= 9, column=1)

#get bounce shoot probability
weaponBounceShotScale = Scale(weaponBounceShotLabelFrame, orient= 'horizontal', from_=0, to=100, tickinterval=10, length=350, label='Probability')
weaponBounceShotScale.grid(row=1, column=1)

##Teleport SHOT----------------------------------------------------------------------------------------------------------------------------------------------

#Enable/ disable Bounce shot
varcanTeleportShotCheckBox = tk.IntVar()
def enable_DisableBounceShotLabelFrame():
    if(varcanTeleportShotCheckBox.get() == 1):
        weaponTeleportShotLabelFrame.grid()
    elif(varcanTeleportShotCheckBox.get() == 0):
        weaponTeleportShotLabelFrame.grid_remove()

#Can bounce shoot
weaponCanTeleportShotCheckBox = Checkbutton(basicWeaponLabelFrame,text= "Teleport shot",variable = varcanTeleportShotCheckBox, onvalue=1, offvalue=0, command=enable_DisableBounceShotLabelFrame)
weaponCanTeleportShotCheckBox.select()
weaponCanTeleportShotCheckBox.grid(row=8, column=2)

#Define Bounce shot Label Frame
weaponTeleportShotLabelFrame = LabelFrame(basicWeaponLabelFrame, text="Teleport shot", padx=10, pady=10)
weaponTeleportShotLabelFrame.grid(row= 9, column=2)

#get bounce shoot probability
weaponTeleportShotScale = Scale(weaponTeleportShotLabelFrame, orient= 'horizontal', from_=0, to=100, tickinterval=10, length=350, label='Probability')
weaponTeleportShotScale.grid(row=1, column=1)

##Jump SHOT----------------------------------------------------------------------------------------------------------------------------------------------

#Enable/ disable Bounce shot
varcanJumpShotCheckBox = tk.IntVar()
def enable_DisableBounceShotLabelFrame():
    if(varcanJumpShotCheckBox.get() == 1):
        weaponJumpShotLabelFrame.grid()
    elif(varcanJumpShotCheckBox.get() == 0):
        weaponJumpShotLabelFrame.grid_remove()

#Can bounce shoot
weaponCanJumpShotCheckBox = Checkbutton(basicWeaponLabelFrame,text= "Jump shot",variable = varcanJumpShotCheckBox, onvalue=1, offvalue=0, command=enable_DisableBounceShotLabelFrame)
weaponCanJumpShotCheckBox.select()
weaponCanJumpShotCheckBox.grid(row=10, column=1)

#Define Bounce shot Label Frame
weaponJumpShotLabelFrame = LabelFrame(basicWeaponLabelFrame, text="Jump shot", padx=10, pady=10)
weaponJumpShotLabelFrame.grid(row= 11, column=1)

#get bounce shoot probability
weaponJumpShotScale = Scale(weaponJumpShotLabelFrame, orient= 'horizontal', from_=0, to=100, tickinterval=10, length=350, label='Probability')
weaponJumpShotScale.grid(row=1, column=1)


##-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def startGeneration():
    error = []

    if(weaponNameEntry.get() == ""):
        askokcancel('Compilation error', "Weapon name need at least 1 character")
        error.append(True)
    else:
        Main.weaponName = weaponNameEntry.get()
        error.append(False)

    #Weapon File Name--------------------------------------------------------------------------------------------------
    weaponNameFileWrongCharacter = re.findall(r"\\|\/|\:|\*|\?|\"|\<|\>|\|", weaponNameFileEntry.get())
    if(len(weaponNameFileWrongCharacter) > 0):
        askokcancel('Compilation error', 'A file cannot contain the following characters : \ / : * " < > |')
        error.append(True)
    else:
        Main.weaponFileName = weaponNameFileEntry.get()
        error.append(False)


    Main.weaponInstruction = weaponInstructionEntry.get()
    Main.weaponAuthor = weaponAuthorEntry.get()


    #Admin only----------------------------------------------------------------
    if(onlyAdmin.get() == 1): Main.weaponOnlyAdmin = "true"
    else : Main.weaponOnlyAdmin = "false"

    if(weaponSpawnable.get() == 1): Main.weaponSpawnable = "true"
    else : Main.weaponSpawnable = "false"

    #weapon category-----------------------------------------------------------
    if(weaponCategoryEntry.get() == ""):
        askokcancel('Compilation error', "Weapon category need at least 1 character")
        error.append(True)
    else:
        Main.weaponCategory = weaponCategoryEntry.get()
        error.append(False)


    #Primary attack damage---------------------------------------------------
    if(weaponPrimaryDamageEntry.get().isdigit()):
        Main.weaponPrimaryDamage = weaponPrimaryDamageEntry.get()
        error.append(False)
    else:
        askokcancel('Compilation error', "Weapon primary damage isn't a number")
        weaponPrimaryDamageEntry.delete(0, 'end')
        error.append(True)

    Main.weaponPrimaryClipSize = weaponPrimaryAttackClipSize.get()
    Main.weaponPrimaryAmmoType = weaponPrimaryAmmoType.get()

    if(varPrimaryAutomatic.get() == 1): Main.weaponPrimaryAutomatic = "true"
    else : Main.weaponPrimaryAutomatic = "false"


    #3D model
    Main.weaponModel3D = model3DType.get()

##------------------------------------------------------------------------------------
    if(varcanThrowGrenadeCheckBox.get() == 1): Main.canThrowGrenade = "true"
    else : Main.canThrowGrenade = "false"

    Main.throwGrenadeProbability = weaponThrowGrenadeScale.get()
##------------------------------------------------------------------------------------
    if(varcanShotgunShotCheckBox.get() == 1): Main.canShotgun = "true"
    else : Main.canShotgun = "false"

    Main.shotGunProbability = weaponShotgunShotScale.get()
##------------------------------------------------------------------------------------
    if(varcanBounceShotCheckBox.get() == 1): Main.canBounce = "true"
    else : Main.canBounce = "false"

    Main.probabilityBounce = weaponBounceShotScale.get()
##------------------------------------------------------------------------------------
    if(varcanTeleportShotCheckBox.get() == 1): Main.canTeleport = "true"
    else : Main.canTeleport = "false"

    Main.teleportProbability = weaponTeleportShotScale.get()

##------------------------------------------------------------------------------------
    if(varcanJumpShotCheckBox.get() == 1): Main.canJumpShot = "true"
    else : Main.canJumpShot = "false"

    Main.probabilityJumpShot = weaponJumpShotScale.get()

##------------------------------------------------------------------------------------



    #if any error
    for i in range(len(error)):
        if(error[i] == True):
            return None

    Main.RandomWeapon()

#########################################################################################################


menubar = Menu(window)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Basic weapon", command=ShowBasicWeaponLabelFrame)
menu1.add_command(label="Random Weapon", command=ShowRandomWeaponLabelFrame)
menu1.add_separator()
menu1.add_command(label="Quit", command=window.quit)
menubar.add_cascade(label="Weapon", menu=menu1)



Button(basicWeaponLabelFrame, text='Execute', borderwidth=1, command=startGeneration).grid(row=12, column=1)
window.title("Garry's mod Weapon kit creation ")
window.config(menu=menubar)
window.mainloop()





"""
def mesCouille():
    model3DList.append("1")
    removeModel3Dmenu = model3DMenu["menu"]
    removeModel3Dmenu.delete(0, "end")

    for string in model3DList:
        removeModel3Dmenu.add_command(label=string, 
            command=lambda value=string: model3DMenu.set(value))

    print(removeModel3Dmenu.get())
    
update_button = tk.Button(window, text='Update option menu', command=mesCouille)
update_button.grid(column=1, row=12)

#piou[1:-1] \/[^./]*\.

"""


