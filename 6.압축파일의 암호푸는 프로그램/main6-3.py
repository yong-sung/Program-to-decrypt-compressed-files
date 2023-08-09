import itertools # 반복 가능한 객체를 조합하거나 순열을 생성하기 위한 itertools 모듈을 임포트
import zipfile

def un_zip(passwd_string, min_len, max_len, zFile):
    for len in range(min_len, max_len+1):
        to_attempt = itertools.product(passwd_string, repeat = len)
        for attempt in to_attempt:
            passwd = ''.join(attempt) #공백이 없는 문자열로 변환해줌
            print(passwd)
            try:
                zFile.extractall(pwd = passwd.encode()) # 압축을 푸는 기능
                print(f"비밀번호는 {passwd} 입니다.")
                return 1
            except:
                pass

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" # 비밀번호로 시도할 문자열

zFile = zipfile.ZipFile(r'6.압축파일의 암호푸는 프로그램\비밀번호는 123.zip')

# 시도할 비밀번호의 길이 범위를 정의
min_len = 1
max_len = 5

unzip_result = un_zip(passwd_string, min_len, max_len, zFile)

if unzip_result == 1:
    print("암호찾기에 성공하였습니다.")
else:
    print("암호찾기에 실패하였습니다.")