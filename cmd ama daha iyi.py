#komut tanımlama
import subprocess
print('cmd ama daha iyi mertfsmal')
while True:
    try:
        print('----------------------------')
        cmdKomut=input()
        cmdKomut = cmdKomut.lower()
        yeniCmdKomut1 = cmdKomut.replace("ı", "i")
        yeniCmdKomut2 = yeniCmdKomut1.replace("ş", "s")
        yeniCmdKomut3 = yeniCmdKomut2.replace("ç", "c")
        yeniCmdKomut4 = yeniCmdKomut3.replace("ğ", "g")
        yeniCmdKomut5 = yeniCmdKomut4.replace("ö", "o")
        yeniCmdKomut = yeniCmdKomut5.replace("ü", "u")
        print(f"yeni string: {yeniCmdKomut}")
        if yeniCmdKomut == 'normal cmd':
            while True:
                try:
                    normalCmd = input()
                    if normalCmd == 'cikis':
                        break
                    if normalCmd != 'cikis':
                        subprocess.call(normalCmd, shell=True)
                except Exception as e:
                    print(e)
        if yeniCmdKomut == 'yardim':
            print('Buraya baya şey yazcam şimdilik boş')
        if yeniCmdKomut == 'baslat':
            subprocess.call('start', shell=True)
        if yeniCmdKomut == 'gecmis':
            subprocess.call('doskey /history', shell=True)
        if yeniCmdKomut == 'dizin':
            subprocess.call('dir', shell=True)
        if yeniCmdKomut == 'baslik':
            sa = input()
            subprocess.call(f'title {sa}', shell=True)
        if yeniCmdKomut == 'agac':
            subprocess.call('tree', shell=True)
        if yeniCmdKomut == 'temizle':
            subprocess.call('cls', shell=True)
        if yeniCmdKomut == 'ip bilgileri':
            subprocess.call('ipconfig', shell=True)
        if yeniCmdKomut == 'wifi bilgileri':
            subprocess.call('netsh wlan show profiles', shell=True)
        if yeniCmdKomut == 'wifi sifreleri':
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
            for i in profiles:
                try:
                    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                    try:
                        print ("{:<30}|  {:<}".format(i, results[0]))
                    except IndexError:
                        print ("{:<30}|  {:<}".format(i, ""))
                except subprocess.CalledProcessError:
                    print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
    except Exception as e:
        print('Bu kod programa kayıtlı değildir. Lütfen tekrar deneyin.', e)
        pass
        #İngilizce kodları da açmayı ve string split