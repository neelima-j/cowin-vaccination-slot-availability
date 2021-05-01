import requests
import json
import requests
import datetime as dt
 
 
#api_request = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/states")
#api = json.loads(api_request.content)
#print(api)

#kerala_code = 17

#api_request = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(kerala_code))
#api = json.loads(api_request.content)
#print(api)

district_map = {
    301:'Alapuzha',
    307:'Ernakulam',
    298:'Kollam',
    304:'Kottayam',
    296:'Trivandrum',
    303:'Thrissur',
    306:'Idukki',
    297:'Kannur',
    295:'Kasargod',
    302:'Malappuram',
    308:'Palakkad',
    300:'Pathanmthitta',
    299:'Wayanad',
    544:'Kanyakumari'
    }
districts_of_interest = [301, 307, 298, 304, 296, 303 ] #Kerala
#districts_of_interest = [544]   #Kanyakumari

 
date = dt.datetime.today()
date_str = date.strftime("%d-%m-%Y")


for district in districts_of_interest:
        print('***',district_map[district],'***')
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(district,date_str)

        api_request = requests.get(URL)
        if api_request.ok:
            api = json.loads(api_request.content)
            if api["centers"]:
                for center in api["centers"]:
                        print(center['sessions'][0]['date'],'\t',center['name'],center['block_name'],end='')
                        print('\t',center['sessions'][0]['available_capacity'],"slots",'\t',"Age:",center['sessions'][0]['min_age_limit'] )
                        
                #else:
     

