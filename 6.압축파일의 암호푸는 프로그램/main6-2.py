import itertools
import zipfile

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zFile = zipfile.ZipFile(r'6.압축파일의 암호푸는 프로그램\비밀번호는 123.zip')

for len in range(1, 6):
    to_attempt = itertools.product(passwd_string, repeat = len)
    for attempt in to_attempt:
        passwd = ''.join(attempt) #공백이 없는 문자열로 변환해줌
        print(passwd)
        try:
            zFile.extractall(pwd = passwd.encode()) # 압축을 푸는 기능
            print(f"비밀번호는 {passwd} 입니다.")
            break
        except:
            pass