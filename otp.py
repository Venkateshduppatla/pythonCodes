# Program to send OTP and Authenticate the OTP and then to run the program.

# import requests
# import random

# otp = random.randint(1000,9999)
# url = "https://www.fast2sms.com/dev/bulkV2"
# querystring = {"authorization":"LP7Uow41RrEDMGd23JbQBih0Fgt8xvqyXV59eYWnuSNOlZTaCcVxsu231aYhPSJtD0L5iWgRZojKAFrG","variables_values": str(otp),"route":"otp","numbers": '7989783116'}
# headers = {'cache-control': "no-cache"}
# response = requests.request("GET", url, headers=headers, params=querystring)
# print('Otp sent to XXXXXX3116!')
# while 1:
# 	if input("Enter the otp: ") == str(otp):
# 		print("Authentication Successfull!")
# 		break
# 	else:
# 		print("Enter the Correct Otp!")


# Program to send OTP and Authenticate the OTP.

import requests
import random

otp = random.randint(1000,9999)
def sendOtp(mobileNumber):
	url = "https://www.fast2sms.com/dev/bulkV2"
	querystring = {"authorization":"LP7Uow41RrEDMGd23JbQBih0Fgt8xvqyXV59eYWnuSNOlZTaCcVxsu231aYhPSJtD0L5iWgRZojKAFrG","variables_values": str(otp),"route":"otp","numbers": mobileNumber}
	headers = {'cache-control': "no-cache"}
	response = requests.request("GET", url, headers=headers, params=querystring)
	print('Otp sent!')
def validateOtp():
	mobileNumber = input("Enter the UserName/Mobile Number: ")
	sendOtp(mobileNumber)
	while 1:
		if input("Enter the otp: ") == str(otp):
			print("Authentication Successfull!")
			break
		else:
			print("Enter the Correct Otp!")