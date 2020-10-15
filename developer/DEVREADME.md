
# Check Back here soon! Still working on developer documentation!!!!


---
---
---
---
---
---
---
---

# EON-Custom-Themes
Upgrade your EON/Leon/Two's Looks!!! This is a pretty all inclusive guide to modify your device themingly, if you are wanting a simpler to the point guide [you can find that here!](https://github.com/Coltonton/EON-Custom-Themes/blob/master/GetANewTheme.md) It's your own device! You own it, do with it as you please despite what someeee people may say, which is ironic ain't it?.....

This is a new project, find any errors? submit an issue, or make a pull request! This is not my project but our project!! * **Soviet national anthem plays** *

Table of Contents
=======================
* [What is this?](#what-is-this)
* [Setting Up FileZilla](#Setting-Up-FileZilla)

### 3T-EON Boot Logo Instructions
* [Retrive 3T Boot Logo](#Retrive-3T-Boot-Logo)
* [Modifying 3T Files](#Modifying-3T-Files)
* [Uploading Modified 3T Logo/Custom Logo:](#Uploading-Modified-3T-Logo/Custom-Logo)


### LEON/TWO Boot Logo Instructions HALP ME!!!
* [HELP WANTED!!!!](#Help-Wanted)
* [Find The LEON/TWO logo.bin:](#Find-The-LEON/TWO-logo.bin)


### Boot Animation & OP Loading Screen
*  [Boot Animation:](#Boot-Animation)
*  [OpenPilot Loading Screen:](#OpenPilot-Loading-Screen)

### Themes

*  [How To Use:](#How-To-Use)
*  [List of themes:](#List-Of-Themes)
*  [Contribute Your Work!](#Contribute-Your-Work)


---
### Boot Logo Information:
* [General Information](#Boot-Logo-Information)
* [Making a Boot Logo](Making-a-Boot-Logo)
* * [For OnePlus 3T EONs](#Making-For-OnePlus-EONs)
* * [For LeEco EONs](#Making-For-LeEco-EONs)
* [Creating The Boot Logo Package](#Creating-The-Boot-Logo-Package)
* [How To Install The Boot Logo](#How-To-Install-The-Boot-Logo)
* * [The Easy Way](#The-Easy-Way)
* * [The Manual Way](#The-Manual-Way)



# Boot Logo Information
The boot logo is really a simple part of an android device; it lives as part of the bootloader. Saying that means I have to give a big WARNING! Make sure you use the proper command if manually replacing the boot logo!! The OnePlus EON and LeEco EON have different paths for the boot logo. Using the wrong command / replacing the wrong file may lead to a corrupted bootloader!!!! requiring you to reinstall the bootloader.... If the file is dammaged or wrong then you should be okay but you will see a linux penguin as the boot logo. 

But now back to your regualar sceduled information; you need not read this unless you want to "learn you sumthin" or currious; just skip to the sub-sections below!!!! Anyhow... since the bootloader is a very "simple" program; tasked with getting android up and running; that means its not that complex. Everything you see up to the android boot animation is from the bootloader, such as the boot logo, the screen that appears when your battery does not have enough juice and is charging and some other things. All it does is displays a 1080*1920 image it's that simple! These images are built into a "partition" file of sorts. In the case of the OnePlus 3T it is the `sde17` (Aka logo) partition file located in `/dev/block` and for the LeEco LePro it is `sde32` (Aka splash) in `/dev/block`. In the case of the LeEco due to some funny buisness you need to actually replace `/dev/block/bootdevice/by-name/splash` but its all the same, just symlinks anyway. See the sub-sections bellow for more information! Particularly [Making a Boot Logo](#Making-a-Boot-Logo).

## Making a Boot Logo

 Using your favorite image creation program ex. Photoshop/Gimp create a canvas 1920*1080 and create your design). Once finished you will need to rotate the asset positive 90 degrees  (so its vertical - we are dealing with a phone afterall) and export as a png and replace the desired asset in the applicable boot logo maker tool outlined bellow.

### Making For OnePlus EONs:
- Clone or download this project to your Windows PC (yes... it is unfortunatly required) then navigate to where you cloned/downloaded this and go to `./Boot-Logo-Tools/OnePlus3TBootLogoMaker/`
- Here lies all the files you need, all the PNG files in this directory are all the possible 'bootloader' displays!
- - `fhd_oppo_1080_1920_result.raw` Is the main boot logo.
- - `fhd_charger_1080_1920_result.raw` Is the screen that shows up when your EONs battery is dead but charging
- - `fhd_lowpower_1080_1920_result.raw` (never appears) is supposed to be the "EON is dead, please plug in" display
- - `fhd_fastboot_1080_1920_result.raw` (never appears) but is the fastboot splash screen
- - `fhd_battery_1080_1920_result.raw` Is a battery error message
- Edit these files in your prefered image creator/editor (gimp/photoshop/etc) to your hearts desire then export as a png and overwrite the desired asset. 
- I have made new horizontal assets for the EON to match its orientation. These are free for you to use :) All the assets that are in the folder need to stay there, if you want to remove one for whatever reason just make it a full black image.
- Proceed to [Create the boot logo package](#Creating-the-boot-logo-package)

### Making For LeEco EONs:
- Clone or download this project to your Windows PC (yes... it is unfortunatly required) then navigate to where you cloned/downloaded this and go to `./Boot-Logo-Tools/LeEcoBootLogoMaker/pics/`
- Here lies all the files you need, all the PNG files in this directory are all the possible 'bootloader' displays! These are more self explanatory as to what they do but the LeEco has a special trick up its sleeve. You will notice there are 3 files `logo1`, `logo2`, and `logo3` these all are the main boot logo! The device will display these three images alternately!
- Edit these files in your prefered image creator/editor (gimp/photoshop/etc) to your hearts desire then export as a png and overwrite the desired asset. 
- I have made new horizontal assets for the EON to match its orientation. These are free for you to use :) All the assets that are in the folder need to stay there, if you want to remove one for whatever reason just make it a full black image.
- Proceed to [Create the boot logo package](#Creating-the-boot-logo-package)

## Creating the boot logo package:
- Once you have all the assets you desire edited how you want all you need to do is run the `CREATE_LOGO` batch script and the provided tools (not created by me) will package up the logo automagically! 
- - The OnePlus3T tool a new file will appear (or overwite) called `modified.logo.bin`, go ahead and rename this to LOGO removing the extention (ensure '[show file name extentions](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)' is turned on for your machine to do this).
- - The LeEco tool it will appear in `/output/splash.img`, go ahead and rename this to SPLASH removing the extention (ensure '[show file name extentions](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)' is turned on for your machine to do this).

## How To Install The Boot Logo:
### The Easy Way!
- The easiest most convienient way to get your boot logo on your device is by forking this project and creating your own theme folder in `eon-custom-themes/contributed-themes` follow the guide HERE for information on how to properly structure your theme folder so the program recognizes it. You do not need to modify any code, just create your folder as outlined, clone your fork to your device, and run. If you did everything right it will show up and work! The program scans `contributed-themes` and thats how it populates available themes!
- Going this route allows for easyier future changes, automagic backuping, and no fiddling with commands/android stuff/filezilla. but you have to be somewhat familiar with git. 
### The Manual Way:
- Okay... Okay... its not as bad as it seems to go this route. You need to use ADB or Filezilla (click for guide) to upload your LOGO or SPLASH to /sdcard then run the respective command from SSH below. SECOND WARNING!!! Be careful doing this next step, replaacing the wrong file or using the wrong script may lead to a curropted bootloader!!!! 

To Backup (Recomended but optional): 
- - For OnePlus3T EONs run `if=/dev/block/sde17 of=/sdcard/LOGO.backup`
- - For LeEco EONs run `if=/dev/block/bootdevice/by-name/splash of=/sdcard/SPLASH.backup`

To install:
- - For OnePlus3T EONs run `if=/sdcard/LOGO of=/dev/block/sde17`
- - For LeEco EONs run `if=sdcard/SPLASH of=/dev/block/bootdevice/by-name/splash`

If you see a linux penguin on next reboot something is wrong with your file. you uploaded

# Boot Animation Information
The Android boot animation is also a pretty "simple" and non complex as well. It is Androids loading screen to tell the user... well... it's loading... Basicly its an "un-zipped gif" by what I mean you provide all of the "frames" of the animation, then the device does the rest! The "frames" consist of 1920*1080 jpg files. To Start the boot animation is a non-compression zip folder containing a desc.txt, then folders for each 'part' of the animation. Most common and what comma uses is the 3 part animation (part0, part1, part2). part0 is the first part and is only played once this typically is used to transiston from the boot logo then fade in the main boot animation to make the boot visual process look cleaner. part1 is the main animation that will play on loop until Android fully boots then finishes its current animation. part2 plays once as well and is used as an out-transistion



# OpenPilot Spinner Information

# Auto Installer Information 










---
---
---

## What is this?

Thanks for asking young one! This is a project dedicated to de-comma-ing your EON! Wether you dont like Comma.ai the company or want to personalize your EON, I gotchu fam!

Included in this repository is all the info you need to start hacking around! This is also a community project so here you can find boot logos, boot animations, and OpenPilot loading annimations for your device! Created by myself and other community members, free to use!!! Made your own and want to share it with the world? Wonderful! check [Contribute Your Work!](#Contribute-Your-Work!)


## Setting Up FileZilla:
0. [Download Filezilla](https://filezilla-project.org/download.php?type=client)
1. Install FileZilla
2. Open Site Manager (Top leftmost icon - looks like 3 server racks)
3. Create a new site and call it EON
4. For Protocol select SFTP
5. Enter the IP adress of your eon in Host
6. Port: 8022
7. Login Type: Key File
8. User: root
9. Key File: choose eonkey.pem from root in this repo

3T-EON Instructions:
=======================

## 3T Boot Logo:
### Retrive 3T Boot Logo

1. Connect with FileZilla
2. and go to `/dev/block`
3. In the left handed pannel choose where you want to save.
4. Doubble click the file sde17 to transfer and backup

### Modifying 3T Files:
(Windows Required)

#### Extracting 3T Boot Images:
If you want to create your own boot logo(s) you can use the provided files in OnePlus3T assets folder, and can skip this section, use this section only if you wish to modify an existing bootlogo set.

1. Download this repo.
2. If you wish to modify a 3T boot logo, take it and replplace the sde17.bin file in `Boot Logo Tools\OnePlus3TInjector` with it, being sure to add the .bin extention 
4. Doubble click `Extractor.cmd`
5. All the files will extract and replace into the `Boot Logo Tools\OnePlus3TInjector` folder.

#### Editing 3T Boot Images
This is not a Photoshop or Gimp tutorial. 
Although there are a few files that get extracted you only need to worry about 3 of them (edit the others as you like, I have already made new horizontal themes, that you are free to use use).

* FHD_Charger... is the low battery screen shown while it is pluged in.
* FHD_lowpower... is the low battery screen shown while not pluged in.
* FHD_oppo... is the main boot logo.
0. Download this repo if you haven't.
1. GENTLEMEN! START... YOUR.... ENG..oh...favorite image editors...
2. Remember were dealing with a phone. So you can set your canvas to 1920w x 1080h  but you will need to rotate the image +90 degrees once done editing.
3. Do not go extravagant with the boot logo there is not alot of program memory for anything crazy.
4. Once you have made your logo(s), again remember to rotate it +90 degrees and export as a png file using the EXACT name as the file you want to change, and replace it in the `Boot Logo Tools\OnePlus3TInjector` directory that you are changing.
#### Reinjecting 3T Boot Images

0. Download this repo if you haven't.
1. Doubble click `Injector.cmd`
3. This will create a file called modified.logo.bin, rename it to sde17 (with no file extention)
4. FIN! You can now [Upload your modified 3T logo](#Uploading-modified/custom-3T-Logo:)

### Uploading modified/custom 3T Logo:
0. Make sure you are NOT about to follow these steps to install on a LeEco Based EON (LEON,GOLD,TWO) THIS IS ONLY FOR OP3T EON's, YOUR DEVICE WILL BE HARD BRICKED! DEAD! CAPUT! JEFFREY EPSTEIN'ED!!!!!
1. Connect with FileZilla.
2. Go to `/dev/block`
3. In the left pane area in FileZilla, navigate to the boot logo you want to use.
4. Right click and choose upload, then overwrite.

Reboot and enjoy! If EON shows a Linux penguin you done screwed sumthin' up! (Or somebody else did) Try again!


LEON/TWO_Instructions
=======================

## DO NOT DON NOT!!!!! TRY TO PUT A OP3T BOOT LOGO ON YOUR LEECO EON

## HELP WANTED!!

I do not have a LEON and I need your help! 
If you want to send in a LEON/Two logo.bin it would be much appriciated! 
Email it to Cole@endoflinetech.com and I will get a working! It would be appricieated if you would help verify my work is working
I'm also C-ton#2169 on discord if you want help / want to chat!



## Installing ADB (Windows):
1. [Download ADB](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)
2. Extract zip to c:\ADB

## Find The LEON/TWO logo.bin:

0. [Install ADB](#Installing-ADB-(Windows):)
1. SSH Into Eon
2. Run `am start -a android.settings.SETTINGS`
3. Find Developer Options and verify/enable *ADB over Network*
4. Open windows command prompt and navigate to cd /ADB/platform-tools 
5. `adb connect YOUR_EON_IP:5555`
6. `adb shell`
7. `su`
8. `cd /dev/block/bootdevice/byname`
9. `ls -all`
10. You will need to look through the list and detrimine where LOGO is; on the 3T-ON
    it is /dev/block/sde17
11. Save to sdard memory making sure if=/location_of_LOGO ex: `dd if=/dev/block/sde17 of=/sdcard/logo.img`
12. Exit from shell (ctl+D) `adb pull /sdcard/logo.bin C:\ADB` (Or wherever you like)
13. Email to to Cole@endoflinetech.com including name/github/other info to be credited! 


Boot Animation & OP Loading Screen
=======================
## Boot Animation:
(Universal Method For OP3T EONS and LeEco Eons (Gold/TWO))
1. Download this repo to your computer.
2. SSH into EON and run `mount -o remount,rw /system`.
3. SSH into EON with FileZilla, navigate to your downloads  in the left section (your computer) and `/system/media` on the EON Side.
4. Doubble click bootanimation.zip on the eon side to backup the stock Comma boot animation.
5. With FileZilla, navigate to this downloaded repo in the left section (your computer) and `/system/media` on the EON Side.
6. Doubble click bootanimation.zip in your desired theme folder in the left section, and choose to overwrite.
7. Reboot and enjoy!

## OpenPilot Loading Screen:
* Not Available yet sorry :(



Community-Files:
=======================

## How To Use:

Looking to theme your EON? This is the place see [List Of Themes](#List-of-themes:) to see contributed themes! Just Clone/download this repo, and follow the guide relevant to you from the below list  

* [3T Boot Logo Upload Instructions](#Uploading-Modified-3T-Logo/Custom-Logo:)
* [LEON Boot Logo Upload Instructions](#null:) 
* [EON Boot Animation Instructions](#Boot-Animation:)
* Or the info/instructions provided by the author for other custom files.

## List Of Themes: 
| Theme Number | Theme Name            |Boot Logo?(3T)| Boot Logo? (LeEco) | Boot Animation? | Custom OP Files?                 | Contributor/ Author|
|----------- | ----------------------| -------------| ------------------ | ----------------| ---------------------------------| -------------------|
|  1         | Acura                 | Yes          | No                 | No              | No                               | Colton             |
|  2         | Android               | Yes          | No                 | Yes             | No                               | Colton             |
|  3         | Apple                 | Yes          | No                 | No              | No                               | Colton             |
|  4         | Arne-Pilot            | Yes          | No                 | Yes             | No                               | Colton             |
|  5         | Chevy                 | Yes          | No                 | No              | No                               | Colton             |
|  6         | Colton-HooeyPilot     | Yes          | No                 | No              | Elements, & Sounds               | Colton             |
|  n/a       | Comma-Stock           | Yes          | No                 | Yes             | No                               | Comma.ai           |
|  7         | CommunityPilot        | Yes          | No                 | No              | No                               | Colton             |
|  8         | DragonPilot           | Yes          | No                 | Yes             | No                               | Colton             |
|  9         | A General Theme       | Yes          | No                 | Yes             | No                               | Colton             |
| 10         | Honda                 | Yes          | No                 | Yes             | No                               | Colton             |
| 11         | Hyundai               | Yes          | No                 | No              | No                               | Colton             |
| 12         | Kia                   | Yes          | No                 | No              | No                               | Colton             |
| 13         | Lexus                 | Yes          | No                 | No              | No                               | Colton             |
| 14         | OnePlus               | Yes          | No                 | No              | No                               | Colton             |
| 15         | Subaru                | Yes          | No                 | Yes             | No                               | Colton             |
| 16         | Toyota                | Yes          | No                 | Yes             | No                               | Colton             |

This is the default linup, I will be finishing up whats here, with maybe a coupple others. Happy to hear suggestions for others!!! 
I still need your help, to make LEON boot logos. Want to help? See [HELP WANTED!!!!](#Help-Wanted)

## Donations accepted and very much not required!:
I also hate to ask but I've put quite an ammount of time in to this project. If you like what I've done and do want to help you can buy me a bee....coffee! by donating on [PayPal](https://paypal.me/dattech?locale.x=en_US). Just a coupple dollary doo's will mean alot, plese dont feel overly generous I did this for my fun and the community!!

## Contribute Your Work!:

### How To Contribute:
Just Fork this repo, and clone it, add in youre theme following the example theme, looking at others, and the 
Looking to theme your EON? This is the place see [Directory Structure](#Directory-Structure:) You can add whatever you like! Made a custom boot logo? boot Animation? Wonderful!!! Did you edit UI.c? spinner.c? Spinner assets? OP assets? or make your own APK? You can also share your work!! share, you can do that too!!! Just leave instructions in your folder letting them know what to do!

Requirements To Contribute:
* Logo/animation/etc must be in the correct orientation.
* You must follow the directory structure/ how files & folders should be names.
* Inside `Other Files` is free rein.
* No Pornographic/Obscene/GreyLine content will we accepted - Keep it clean.
* No "off-color" or controversial content of any kind.
* You are willing to accept responsibility for your theme, I will not maintain your themes.
* You accept legal responsibility over anything in your theme folder, if I receive a copyright notice, I will take down your theme and forward the notice to you until you resolve the issue.
* Some form of contact is required either in `Contrib.txt`, or shared privately with me. 

Ready to submit? Create a pull request, I will reveiw and merge in!

### Directory Structure:

How to format your theme folder, only use what you need

    .
    └──Theme Name                 # Name Of your Theme
        |──APK                    #Your OP APK
        ├──Assets                 #OP/selfdrive/assets folder
        |──Other Files            #Edited UI.C or spinenr.c?
        |──Bootanimation.zip      # Android Boot Animation
        |──Contrib.txt            # Add your info here,
        |──Screenshots            # Place screenshots here so people can see what it looks like!!
        |──LEONLogo               # LEON/GOLD/TWO Boot Logo folder
        └──OP3TLogo               # 3T-EON Boot Logo folder - place the sde17 file in here
        
        
        
                                  