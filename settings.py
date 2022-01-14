#Do not make any vars equal numbers. True or False are fine and "" are fine.

#If True system will not remove files after encrypt and decrypt. Will remove files if set to False.
do_not_remove=False
#Do not disable failsafe unless needed! Trust me. Don't disable it.
fail_safe=True
#Required python version to run program.
required_version='3.10.0'
#Application version. Just for show.
program_version='0.3.1'
#Drive letter to store hash.aes file on root directory. Letter must be Uppercase. Windows only.
drive_letter='E'
#Drive name to store hash.aes file on root directory. Linux only.
drive_name='Computer'
#Operating System or OS. Can be macos, windows or linux. Must be lowercase.
system='macos'
#Filters bad words that people should not be using. Not currently active.
profanity_filter=True
#Disable profanity filter for admin.
disable_filter_admin=False
#A backup password in case the other is forgotten.
global_password=True
#Don't load save file. True: Skip save file -- False: Load defualt file not save file.
dont_load_save=False
#Automatically optimize on start up. USE AT YOUR OWN RISK. Currently in development phase.
optimize_on_startup=False
#Enable automated history_file for functions
auto_history_record=True
#App version control --(Disable if needed)--
app_version_control=False
#Only allow set operating system. Change system variable to your choice.
set_operating_system=False
#Allowed windows versions. You can choose 7, 8, 10, 11. Only works if system setting is set to windows.
allow_windows_version='10'
#If a record prior what's asked is a duplicate, system will then ignore the task given.
skip_history_copy=True
#Enable automated history_file for functions. 
auto_error_record=True
#Quit app if one or more settings are incorrect. For safety purposes do not disable.
quit_ifIncorrect=True
#Record a more informed description of a item in history.txt
advanced_history=True
#Automatically check inputs for profanity. May use more CPU power than normal.
auto_filter_profanity=True
#Attempt to speed up the search on inputs by using a smaller version of profanity.txt. Only works if auto_filter_profanity is set to True.
auto_filter_profanity_speedBoost=False
#An attempt to use more than one cpu core.
multi_process=False
#Assign Digit number to history item for a more depth look into the item. And create a database to handle all the data for each assigned item.
assign_digit_forHistory=True
#How many digits are allowed to be used to store history. Max 30.
allowed_digists_forHistory=8
#Will still check for incorrect settings if quit_ifIncorrect is True, but won't display anything.
show_incorrect_settings=True
#Will deny the program from saving. No matter what. Will cause problems for long term.
disable_save=False
#min and max password lengths, and allowed characters
min_length=5
max_length=16
allowedPassword_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890*()#'
#Passwords have to meet the requirments set above.
strict_password=True

#Settings coming soon. Do not change unless your a dare devil.
#No settings are pending. Send a request on GitHub for ideas.
#If a setting is missing, not present, or not there, skip it.
skip_missing_settings=False
#When you start the database a backup will be made.
backupOn_StartUp=False
#Allowed permissions to create, remove, edit backups.
allowed_backupPermissions=['admin','teacher']

#Remove if you aren't using my custom application.
#Settings for application.
show_background=True
button_color='white'
bg_color='#80a8e8'
text_color='#494b4d'
button_height=2
button_width=15
text_font=30
entry_background_color='White'
entry_text_color='Black'