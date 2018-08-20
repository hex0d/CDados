#! /usr/bin/python3

def main():
	msg = str(input("Mensagem: "))
	bin_msg = [format(ord(c), 'b').zfill(8) for c in msg]
	print('Mensagem em binario: ' + ''.join(bin_msg) )

if __name__ == "__main__":
	main()
