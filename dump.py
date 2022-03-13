import os, sys,platform,time
if __name__ == "__main__":
	if len(sys.argv) == 2:
		if sys.argv[1] == "remove":
			os.system("rm -f .__apikey__.txt")
			exit(" [!] Succesfull Deleted")
		else:
			print(" [?] Wellcome : ")
			exit(" [!] Run : python jssl.py remove")
	from time import sleep
	import requests
	bit = platform.architecture()[0]
	if bit == 'd64bit':
		from f64 import main
		print("\n Congratulations! Your device supported!\n")
		time.sleep(3)
		main()
	elif bit == 'd32bit':
		from f32 import main
		print("\n Congratulations! Your device supported!\n")
		time.sleep(3)
		main()
