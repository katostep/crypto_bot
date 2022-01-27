import getpass
import cryptocode

# ターミナルで入力した文字をパスワードで暗号化してファイル保存する
def encrypto_save(file_path):
	if not file_path:
		print("Please filename!!!")
		return
	data = getpass.getpass("api secret:")
	password = getpass.getpass('password:')
	
	cipher = cryptocode.encrypt(data, password)

	with open(file_path, 'w') as f:
		f.write(cipher)

# 複号化する
def decrypto(file_path):
	password = getpass.getpass('password:')
	f = open(file_path, 'r' , encoding='UTF-8')
	decoded = cryptocode.decrypt(f.read(),password)

	return decoded

if __name__ == "__main__":
	file_path = 'bitflyer.txt'	
	encrypto_save(file_path)
	#print(decrypto(file_path))
