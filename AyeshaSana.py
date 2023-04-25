try:
	import requests
except ImportError:
	os.system('pip install requests')


ses = requests.Session()

id = []
ok = []
cp =[]
loop = 0
pwx = []
method = []


##______COLORS____ARE________######
pwx=[]
W = '\33[97;1m'
R = '\33[91;1m'
G = '\33[92;1m'
Y = '\33[93;1m'
B = '\33[94;1m'
P = '\33[95;1m'
S = '\33[96;1m'
N = '\1b[0m'
#________________________________________#
def clear():
	os.system("clear")

def line():
	print(52*'-')
def p(x):
	print(x)

def logo():
	logo = (f'''\33[1;97m                                    
@@@@@@@   @@@  @@@       @@@  @@@  @@@@@@@  @@@@@@@@  
@@@@@@@@  @@@  @@@       @@@  @@@  @@@@@@@  @@@@@@@@  
@@!  @@@  @@!  @@!       @@!  @@@    @@!    @@!       
\33[1;96m!@!  @!@  !@!  !@!       !@!  @!@    !@!    !@!       
@!@  !@!  !!@  @!!       @!@  !@!    @!!    @!!!:!    
\33[1;97m!@!  !!!  !!!  !!!       !@!  !!!    !!!    !!!!!:    
!!:  !!!  !!:  !!:       !!:  !!!    !!:    !!:       
:!:  !:!  :!:   :!:      :!:  !:!    :!:    :!:       
 :::: ::   ::   :: ::::  ::::: ::     ::     :: ::::  
:: :  :   :    : :: : :   : :  :      :     : :: ::   
[<>] The Original Codes are Written by Dilute Codes
---------------------------------------------------
  Author    : Dilute Codes( Aqib Ali )
  Github    : https://github.com/Dilute Codes
  Facebook  : Dilute Codes
  Version   : DC Extreme [1.2]
    \33[1;96mNaam Ki Dosti Kaam ki Yaari\\Dosron Ki Tarah ! Adat Nhi Hamari \33[1;97m
---------------------------------------------------''')
	p(logo)


ua3 = "YAHN APNY 3RD USER AGENT LGANY HE "



ua2 = ' YH 2ND USERAGENTS LGALO METHOD 2 KY LIYE'

# USER AGENT FUNCTION UA 1 METHOD 1
def iAmAndroidUa():
	# YHN APNY ESE ANDROID KY UA LGANY HE MNE EXAMPLE KY LIYE IPHONE KY LGAY
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G ace Build/RZKS31.Q3-45-16-9-11)","Dalvik/2.1.0 (Linux; U; Android 9; AFTWMST22 Build/PS7633.3445N)","Dalvik/2.1.0 (Linux; U; Android 10; 7LC1 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; X88pro10.r.de.6330.d4.software Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 11; PX1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 5.0.0; View Prime Build/v12bn [FBAN/FB4A;FBAV/353.0.0.27.492;FBBV/558626621;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/558626621;FBMF/Wiko;FBBD/Wiko;FBPN/com.facebook.orca;FBDV/View Prime;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 5.1; Archos 50 Cobalt Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ2A.230405.003.A2)","Dalvik/2.1.0 (Linux; U; Android 13; PHP110 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; V2238 Build/TP1A.220624.014_NONFCMOD1)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-T818 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 12; TECNO Mobile CH9n Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; T96R Build/LMY49F)","Dalvik/2.1.0 (Linux; U; Android 7.0; Moto C Build/NRD90M.041)","Dalvik/2.1.0 (Linux; U; Android 13; SH-M24 Build/S3162)","Dalvik/2.1.0 (Linux; U; Android 10.0; T9212A Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 11; AiPlus2K Build/RTM3.211215.123)","Dalvik/2.1.0 (Linux; U; Android 9; SA 2K TV Build/PTO7.211209.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g32 Build/S2SNS32.34-60-6)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SF550 Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A536N Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/TQ2A.230305.008.C1)","Dalvik/2.1.0 (Linux; U; Android 9; Viva_1003G Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 12; ZTE A2322G Build/SKQ1.220213.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G (2022) Build/S1SDS32.56-81-10)","Dalvik/2.1.0 (Linux; U; Android 9; coral Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A3460 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; V2239 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; S1 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ2A.230405.003)","Dalvik/2.1.0 (Linux; U; Android 13; Bengal for arm64 Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 7.0; X12 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2465 Build/RKQ1.211119.001)","Dalvik/2.1.0 (Linux; U; Android 11; Q9.r1.00.6330_642.d4 Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 11; hatch Build/R112-15359.45.0)","Dalvik/2.1.0 (Linux; U; Android 13; Subsystem for Android(TM) Build/TQ2A.230305.008.C1)","Dalvik/2.1.0 (Linux; U; And
