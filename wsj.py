import random
import time
from datetime import datetime
import json

import requests
from bs4 import BeautifulSoup

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.wsj.com/search?query=apple&dateRange=30d",
    "sec-ch-device-memory": "8",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-arch": "\"arm\"",
    "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"135.0.7049.114\", \"Not-A.Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"135.0.7049.114\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
cookies = {
    "datadome": "WksFQq8jNbNj5bT_i_uWVqhD5W1nAJUUaOcnAS8uGX0vc5GhTaS6_3wWOAknsVsRYuBuWpA5Cgj3WLnbCOAHpVyyhP1QC7FS7obyhY~VgIyCmZMICX1gGSGhS23HFETF",
    "usr_prof_v2": "eyJpYyI6MX0%3D",
    "ab_uuid": "5519210a-2413-40de-b1ff-39a1a59e1510",
    "_lr_geo_location_state": "00",
    "_lr_geo_location": "PH",
    "ca_r": "www.wsj.com",
    "_pubcid": "63daa707-7c31-4249-b895-f9751a5432e2",
    "_pubcid_cst": "DCwOLBEsaQ%3D%3D",
    "_lr_retry_request": "true",
    "_lr_env_src_ats": "false",
    "_sp_su": "false",
    "pbjs-unifiedid": "%7B%22TDID%22%3A%22e8571eea-568e-41db-9d26-9b2795e1481f%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222025-04-25T08%3A45%3A21%22%7D",
    "pbjs-unifiedid_cst": "CyzZLLwsaQ%3D%3D",
    "__gads": "ID=71293a4c9283957b:T=1745570721:RT=1745570721:S=ALNI_Mbo6TeYvnYa8iPTQ2ndRYPvri--oA",
    "__gpi": "UID=000010b0aeae455a:T=1745570721:RT=1745570721:S=ALNI_MaTkGdDVfGyg1AmsKP92yY7nnud9Q",
    "__eoi": "ID=c5d0c9f8ba6d5d6f:T=1745570721:RT=1745570721:S=AA-AfjbD7UA3M2Lrlw-seE-BxrF2",
    "_ncg_domain_id_": "cf3845c1-fe1a-4341-9d55-c916e33b6973.0.1745570721.1777106721",
    "utag_main": "v_id:01966c1f700b00169e9a169e671b05075003406d00b3b$_sn:1$_se:1$_ss:1$_st:1745572521804$ses_id:1745570721804%3Bexp-session$_pn:1%3Bexp-session$_prevpage:WSJ%20ResearchTools%20Search%3Bexp-1745574321807$vapi_domain:wsj.com",
    "AMCV_CB68E4BA55144CAA0A4C98A5%40AdobeOrg": "1585540135%7CMCIDTS%7C20204%7CvVersion%7C4.4.0"
}
page = 1

keywords = {


    "GOOGL": [
        "waymo"
    ]
}

def parse_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    formatted_date = date_obj.strftime("%Y-%m-%d")
    return formatted_date

def find_parent_company(keyword):
    for parent_company, keywords_list in keywords.items():
        if keyword.lower() in [k.lower() for k in keywords_list]:  
            return parent_company
    return None  # if no parent company found

sleep_time = random.randint(10, 60)

result = []
for company, items in keywords.items():
    for item in items:
        print(f"- {item}")
        for i in range(1, 999):
            print('right now is the No' + str(i) + "page")
            url = "https://www.wsj.com/search"
            params = {
                "query": str(item),
                "dateRange": "30d",
                "page": str(i)
            }
            response = requests.get(url, headers=headers, cookies=cookies, params=params)
            time.sleep(5)
            # parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # find the <script> tag with id="__NEXT_DATA__"
            script_tag = soup.find('script', {'id': '__NEXT_DATA__'})
            if script_tag:
                json_data = script_tag.string.strip()  # .strip() removes leading/trailing whitespace
                # print(json_data)
                js = json.loads(json_data)
                # print(js)
                props = js['props']
                if props and isinstance(props, dict):
                    pageProps = props.get('pageProps', {})
                    mostPopularDatas = props.get('pageProps', {}).get('mostPopularData') if props else None
                    symbol = find_parent_company(item)
                searchResults = props['pageProps']['searchResults']
                if searchResults == []:
                    break
                # if searchResults == []:
                #     break
                else:
                    for searchResult in searchResults:
                        headline = searchResult.get('headline')
                        summary = searchResult.get('summary')
                        timestamp = searchResult.get('timestamp')
                        print(symbol, headline,timestamp, summary)
                        result.append({
                            "company": symbol,
                            "title": headline,
                            "date": str(timestamp).split("T")[0],
                            "summary": summary
                        })
    # with open(f"./json/{item}.json", "w") as outfile:
    #             # outfile.write(str(result))
    #     json.dump(result, outfile, indent=4, ensure_ascii=False)
            # for mostPopularData in mostPopularDatas:
            #     headline = mostPopularData['headline']
            #     summary = mostPopularData['summary']
            #     timestamp = mostPopularData['timestamp']
            #     print(companyDatas['companyName'], headline, str(timestamp), summary)