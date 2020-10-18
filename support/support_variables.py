BACKUPS_DIR = '/storage/emulated/0/theme-backups'
APK_DIR = '/data/openpilot/apk/ai.comma.plus.offroad.apk'
BACKUP_OPTIONS = []

# =============  get_user_theme() vars ============= ##
CONTRIB_THEMES = 'contributed-themes'
EXCLUDED_THEMES = ['Example', 'ignoreme']
MIN_SIM_THRESHOLD = 0.25  # user's input needs to be this percent or higher similar to a theme to select it

# ==============  Auto Installer Vars ============== ## - see DEVREADME
IS_AUTO_INSTALL = False     #Do Auto Install
DESIRED_AUTO_VER = '1'      #Desired theme version, add 1 to update users theme.
AUTO_INSTALL_CONF = {'auto_selected_theme': 'Arne', 'install_3T_logo': True, 'install_Leo_logo': True, 'install_anim': True,
                     'ani_color': ''}

# =================  Welcome Texts ================= ##
WELCOME_TEXT = ['Created By: Colton (Brandon) S. EndLine \\n',
                'Special Thanks to @ShaneSmiskol for all the help!!!',
                'Free to use! Free to Edit! Free to integrate!',
                'Design and contribute your themes today!',
                '(See the developer folder in this repo)',
                'It\'s your EON, do what you want!']
AUTO_WELCOME_TEXT = ['Created By: Colton (Brandon) S. EndLine \\n',
                'Special Thanks to @ShaneSmiskol for all the help!!!',
                'Free to use! Free to Edit! Free to integrate!',
                'Design and contribute your themes today!',
                '(See the developer folder in this repo)',
                'It\'s your EON, do what you want!',
                '*NOTE* THIS IS AN AUTO INSTALL PROGRAM',
                'This is a minimal installer and only made to',
                'auto install the theme the user of this program',
                'has decided on and will not work if you want to',
                'manually install another theme',
                'clone https://github.com/Coltonton/eon-custom-themes.git',
                'to cd /data to use the full program!']
RESTORE_WELCOME_TEXT = ['Created By: Colton (Brandon) S. EndLine \\n',
                'Special Thanks to @ShaneSmiskol for all the help!!!',
                'Free to use! Free to Edit! Free to integrate!',
                'Design and contribute your themes today!',
                '(See the developer folder in this repo)',
                'It\'s your EON, do what you want!',
                ' ',
                '*NOTE* this it the backup restore program']
