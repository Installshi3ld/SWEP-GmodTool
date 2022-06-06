import re
import os
import io
import shutil

import random



MAIN_FILE: str = "lua"

weaponFileName = "Default"
weaponName = "Default"
weaponPrimaryDamage = 10
weaponPrimaryClipSize = 10
weaponPrimaryAmmoType = "pistol"

weaponOnlyAdmin = "false"
weaponSpawnable = "false"
weaponCategory = "Other"

weaponModel3D = "Default"
weaponAuthor ="Default"
weaponInstruction = "default"
weaponPrimaryAutomatic = "true"

canThrowGrenade = "false"
throwGrenadeProbability = "0"

canShotgun = "false"
shotGunProbability = "0"

canJumpShot = "false"
probabilityJumpShot = "0"

canTeleport = "false"
teleportProbability = "0"

canBounce = "true"
probabilityBounce = "0"

#create the file at a certain location in the src directory will overide any existing file with the same path
def vim(path: str) -> io.FileIO:

    path: str = MAIN_FILE + '/' + path
    os.makedirs(os.path.dirname(path), mode=0o777, exist_ok=True)
    file = io.open(path, mode="w", encoding="utf-8")
    return file



try:
    shutil.rmtree("main")
except:
    pass




def RandomWeapon():

    readTemplate = io.open("Templates/weapon.template", mode="r", encoding="utf-8")

    theTemplate = readTemplate.read()

    dico = {

            "weaponName" : str(weaponName),
            "weaponAuthor" : str(weaponAuthor),
            "weaponInstruction" : str(weaponInstruction),

            "weaponSpawnable" : str(weaponSpawnable),
            "weaponOnlyAdmin" : str(weaponOnlyAdmin),
            "weaponCategory" : str(weaponCategory),

            "weaponPrimaryDamage" : str(weaponPrimaryDamage),
            "weaponPrimaryClipSize" : str(random.randrange(100)),
            "weaponPrimaryRecoil" : str(random.randrange(10) / 10),
            "weapon3DModel" : weaponModel3D,

            "weaponPrimaryClipSize" : str(weaponPrimaryClipSize),
            "weaponPrimaryAmmoType" : str(weaponPrimaryAmmoType),
            "weaponPrimaryAutomatic" : str(weaponPrimaryAutomatic),

            ##Skill--------------------------------------------------------

            "canThrowGrenade" : str(canThrowGrenade),
            "throwGrenadeProbability" : str(throwGrenadeProbability),

            "canShotgun" : str(canShotgun),
            "shotgunProbability" : str(shotGunProbability),

            "canTeleport" : str(canTeleport),
            "teleportProbability" : str(teleportProbability),

            "canBounce" : str(canBounce),
            "probabilityBounce" : str(probabilityBounce),

            "canJumpShot" : str(canJumpShot),
            "probabilityJumpShot" : str(probabilityJumpShot),
    }


    getList = re.findall(r"\$[^$]*\$", theTemplate)

    for j in getList:
        j: str
        ii = j.replace('$', "")
        if ii in dico:
            theTemplate = theTemplate.replace(j, dico[ii])

            # theTemplate= theTemplate.replace(j,dico[ii])

    createExample = vim("weapons/" + weaponFileName + ".lua")
    createExample.write(theTemplate)
    createExample.close()


