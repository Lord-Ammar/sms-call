import os,sys,time,requests,bs4,json
import subprocess
try:
   import requests
except ImportError:
   print(' \n\x1b[97m[\x1b[91m!\x1b[97m] Module requests not Installed')
   print('     \x1b[97mSilahkan Install Dulu Ketik \x1b[91m: \x1b[93mpip2 install requests\n')
   sys.exit()

os.system("clear")

IP = requests.get('https://api.ipify.org').text
localtime = time.asctime(time.localtime(time.time()))
y = ("ehegheisgdhskwuvecrcdjswiugrgd177")

#Untuk Clear
def loken():
	os.system("clear")
	print ("""
\033[1;95m╦  \033[1;97m┌─┐┌─┐┬┌┐┌ 
\033[1;95m║  \033[1;97m│ ││ ┬││││ 
\033[1;95m╩═╝\033[1;97m└─┘└─┘┴┘└┘ 

Download Token : \033[1;96mhttps://drive.google.com/file/d
/16FfFjzYl0UfoDbBoRA_R21mci4BiGyhX/view?usp=drivesdk
""")
	print ("")
	login()

#login Password
def login():
          pasw = input("\033[1;97m[\033[1;90m•\033[1;97m] Token:\033[1;92m ")
          if pasw ==y:
              print ("Sukses Login Ke Tools")
              time.sleep(2)
              main()
          else:
              print ("Failed Login Tools")
              time.sleep(2)
              login()


#Target
def target():
	print ("\033[1;90m    ! \033[1;97mExample: \033[1;96m8xx")
	print("")
	no = input("\033[1;96m    [\033[1;90m•\033[1;96m] \033[1;97mNomor Target: ")
	ammar = ("0"+no)
	hah = requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={'phone':no}).text
	req = requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={'phone':no}).text
	if 'terkirim' in req and hah:
		print ('\033[1;95m{\033[1;97m√\033[1;95m} \033[1;93mSpam Success')
	else:
		print ('\033[1;95m{\033[1;97mx\033[1;95m} \033[1;93mSpam Failed')


#Donasi
def donasi():
	print ("""╭─「 Donasi • Pulsa 」
│ • XL [087708773367]
│ • Smartfren [088229683561]
╰────
╭─「 Hubungi 」
│ > Ingin donasi? wa.me/6288229683561
╰────""")

#Spam Matahari
def matahari():
	os.system("python2 spm.py")

#logo
def logo():
	banner = ("""
\33[31;1m   ─▄────▄▄▄▄▄▄▄────▄─  \033[1;95m╔═╗\033[1;97m┌┬┐┌─┐   \033[1;95m╔═╗\033[1;97m┌─┐┬  ┬
\33[31;1m   ▀▀▄─▄█████████▄─▄▀▀  \033[1;95m╚═╗\033[1;97m│││└─┐───\033[1;95m║  \033[1;97m├─┤│  │
\33[31;1m   ────██─▀███▀─██────  \033[1;95m╚═╝\033[1;97m┴ ┴└─┘   \033[1;95m╚═╝\033[1;97m┴ ┴┴─┘┴─┘
\33[31;1m   ──▄─▀████▀████▀─▄──  \033[1;97m[\033[1;0m\033[1;41mCoded By AmmarBN & Sanz\033[1;0m]
\33[31;1m   ▀█────██▀█▀██────█▀  """)
	print (banner)
	print("")
	print ("          \033[1;90m• \033[1;97mCreator : \033[1;92mAmmarBN")
	print ("          \033[1;90m• \033[1;97mYou Ip : \033[1;92m"+IP)
	print ("          \033[1;90m• \033[1;97mTime Local : \033[1;92m"+localtime)
	print ("          \033[1;90m• \033[1;97mKlik \033[1;92mCTRL z \033[1;97m(Untuk Berhenti)")
	print ("")
	print (""" \033[1;93m     1 \033[1;97mGass Spam \33[31;1m(\033[1;96msms,call\33[31;1m)""")
	print (""" \033[1;93m     2 \033[1;97mSMS Unlimited Matahari (\033[1;92mActive\033[1;97m)""")
	print (""" \033[1;93m     3 \033[1;97mDonasi Buat Creator""")

#Buat Input Main
def main():
	os.system("clear")
	print ("")
	logo()
	Gan = input("      Input Menu Gan \33[31;1m~> ")
	if Gan == "1":
		target()
	if Gan == "2":
		matahari()
	if Gan == "3":
		donasi()
	else:
		print ("Input salah Login Ulang....")
		time.sleep(5)
		main()

#Buat Start Program
loken()

if __name__ == "__main__":
       login()
