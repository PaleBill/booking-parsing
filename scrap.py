import requests, json
from bs4 import BeautifulSoup

cookies = {
    'px_init': '0',
    'cors_js': '1',
    'bkng_sso_session': 'e30',
    'OptanonAlertBoxClosed': '2024-01-13T17:37:32.830Z',
    'pcm_consent': 'consentedAt%3D2024-01-13T17%3A37%3A33.262Z%26countryCode%3DCZ%26expiresAt%3D2024-07-11T17%3A37%3A33.262Z%26implicit%3Dfalse%26regionCode%3D10%26regulation%3Dgdpr%26legacyRegulation%3Dgdpr%26consentId%3D84e2a828-1ec8-4ae3-93b3-3948e03c6131%26analytical%3Dfalse%26marketing%3Dfalse',
    'BJS': '-',
    '11_srd': '%7B%22features%22%3A%5B%7B%22id%22%3A16%7D%5D%2C%22score%22%3A3%2C%22detected%22%3Afalse%7D',
    'bkng_sso_auth': 'CAIQsOnuTRpmfotH/vCDVIfJGfA3YCN+eUB3aoArQrFCGBYPziETIOPROwO8qvFK4XBvTvvR/lSPow3OAf/1URgwMWVtnHdlKB3Ri8cDECPkSshTyw1ChMLaXFYk2UVEdxpMIc0kjj97UheYd/Rb',
    'b': '%7B%22countLang%22%3A4%7D',
    '_gcl_au': '1.1.2012221482.1707504340',
    'bkng_expired_hint': 'eyJib29raW5nX2dsb2JhbCI6W3sibG9naW5faGludCI6MjA5NjY1NjcxOX1dfQ',
    'bkng_sso_ses': 'e30',
    'pxcts': '86237f2f-c78f-11ee-8190-28e349f59b33',
    '_pxvid': '8623640e-c78f-11ee-8190-55291895593a',
    '_ga': 'GA1.1.332210299.1707514729',
    'esadm': '02UmFuZG9tSVYkc2RlIyh9YbxZGyl9Y5%2BPXwOi6jFGQ0RbZZSmxzi1XS7lYm1aAOXjDbH%2FoZ%2FVsu8%3D',
    '_ga_G0GLDX0JXR': 'GS1.1.1707514728.1.1.1707514788.0.0.0',
    '_px3': '162d1d511678e38810002c5adf5ce64f9b89450e6c25bee083694ca460a671f7:V5IrJe7ZswDRIuLq6EhrhtGDxV/1MuPTQna56hrr4k+awPWmQt/vnwor9aZGOecVkb4Nq4A9ZKYN4C1J1qP/9Q==:1000:3fcWqsufQ1McSB2Nc3DcVCnI0tEYDSGXQvZh/H3/m8bmUkCwl7VsuYFWwPgxW2YXYq53sCRWkGC4+lvcAQ7wNjq0RsDiotWcfcWsCxQDP0bN7vWFVYmR6MKt6Xl0en3YKvKri3PWdWjKK/iF4DjAv78i8mBawZMVME2OL/bd0+vTBdNXSrad5gy91U8Au1OBJFHonTiCx6eBx0AL0mJKDyfjO3cidIubA+CVnzi7QnA=',
    '_pxde': '4e06c6bee2ab60d615b62d1934c74f26c47a9d6f113424641f564e3ef43bf991:eyJ0aW1lc3RhbXAiOjE3MDc1MTUyMjc5NjksImZfa2IiOjAsImlwY19pZCI6W119',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Feb+09+2024+22%3A48%3A41+GMT%2B0100+(%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=1f991a87-728b-43c9-b367-75789910f32f&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0004%3A0&implicitConsentCountry=GDPR&implicitConsentDate=1705167450946&backfilled_at=1705167453262&backfilled_seed=1&geolocation=CZ%3B10&AwaitingReconsent=false',
    'bkng': '11UmFuZG9tSVYkc2RlIyh9YSvtNSM2ADX0BnR0tqAEmjvkTfFBLA7M%2B%2FovGBr%2B9svXEoc59zwuc%2BG%2BwIh9XslvzN6MteshZHFivLIBRuMiOoaacDPCNIz7sb%2FX%2Fx6fj0GNIRFaWWfX8CWYbdlFHx04sfYvkrCSjZ0bKpteye6PwQ9e014%2FcduK1dXWR17SxHzFSriDgSX3xMZGuoVid0%2Bo2g%3D%3D',
    'lastSeen': '0',
    'aws-waf-token': '0ba63e1a-bb4d-4082-92e2-b6626aec51e6:CQoAnzyZpM0BAAAA:IrQe71u2y3JHM5UKp55EGrlHCnMGZd8MxCrgF16qFPPsVF3cL0tbKSgtKrtU+INkstGV1PIuh62Dk8i76qdkXNUHPIFkH6ZDkUrR61TlcqIDnRiA9OtC1g3GwNYmPs4OSh8y2wS4Wg2IYOrXwuc2++CCT5Fi1/Jlr6LdAPD5bkI0L5HjRvZ9wEORwPxs0VqtWbMHYL4Ref0FwvCNdW6ilZCECdw+TiVCdIB8S87CW75D6dsYB4QwNVDss9QYbDON9jKwi2oP',
}

headers = {
    'authority': 'www.booking.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'referer': 'https://www.booking.com/searchresults.html?aid=397594&label=gog235jc-1FCAEY7wcoggI46AdIM1gDaDqIAQGYAQW4ARfIAQzYAQHoAQH4AQyIAgGoAgO4Ap26mq4GwAIB0gIkNDU1YmU3M2EtNTVlZS00YjA0LWFlODMtYmVhYzJiMzc0MzVi2AIG4AIB&sid=16277eb615b30350f154e0e5297bc45e&checkin=2024-02-18&checkout=2024-02-19&dest_id=-542184&dest_type=city&srpvid=6c8099119d0601d9&track_hp_back_button=1&lang=en-us&soz=1&lang_changed=1',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

params = {
        'label': 'gog235jc-1FCAEY7wcoggI46AdIM1gDaDqIAQGYAQW4ARfIAQzYAQHoAQH4AQyIAgGoAgO4Ap26mq4GwAIB0gIkNDU1YmU3M2EtNTVlZS00YjA0LWFlODMtYmVhYzJiMzc0MzVi2AIG4AIB',
        'sid': '16277eb615b30350f154e0e5297bc45e',
        'aid': '397594',
        'ss': 'France',
        'lang': 'en-us',
        'src': 'searchresults',
        'dest_type': 'country',
        'ac_position': '0',
        'ac_click_type': 'b',
        'ac_langcode': 'en',
        'ac_suggestion_list_length': '5',
        'search_selected': 'true',
        'search_pageview_id': '96ec994e22c90088',
        'ac_meta': 'GhA5NmVjOTk0ZTIyYzkwMDg4IAAoATICZW46BmZyYW5jZUAASgBQAA==',
        'checkin': '2024-02-13',
        'checkout': '2024-02-14',
        'group_adults': '2',
        'no_rooms': '1',
        'group_children': '0',
        'nflt': 'privacy_type=3;ht_id=201;class=1;class=2;class=3;ht_id=204',
        'checkin': '2024-02-13',
        'checkout':'2024-02-14',
        'offset': '0'
    }

def try_text(obj, slice = 0):
    try:
        return obj.text.strip()[slice:]
    except:
        return None

def get_links(countries):

    countries_data = {}

    for country in countries:

        country_hotels = []
        params['ss'] = country
        params['offset'] = 0

        response = requests.get(url= "https://www.booking.com/searchresults.en-us.html", headers=headers, cookies = cookies, params = params)    
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        page_number = soup.find('ol', class_="ef2dbaeb17").find_all('li')[-1].text 


        print(page_number, ' pages in ', country)

        for offset in range(int(page_number)):

            params['offset'] = offset*25
            response = requests.get(url= "https://www.booking.com/searchresults.en-us.html", headers=headers, cookies = cookies, params = params)
            
            data = response.text

            soup = BeautifulSoup(data, "html.parser")
            cards = soup.find_all("div", {"data-testid": "property-card"})
            
            for card in cards:

                country_hotels.append({
                    'name': try_text(card.find('div', {"data-testid":"title"})),
                    'link': card.find('a',{'data-testid':"title-link"}).get('href'),
                    'type': try_text(card.select_one('div.c19beea015 > div > div > div > h4')),
                    'rating': try_text(card.select_one('div.a3b8729ab1.d86cee9b25')),
                    'price': try_text(card.select_one('span.f6431b446c.fbfd7c1165.e84eb96b1f'),2),
                    'country': country,
                    'city': try_text(card.find('span', {'data-testid':"address"})),
                    'image': card.find('img', {'data-testid':"image"}).get('src')
                })

                print(len(country_hotels),country_hotels[-1]['name'], '\n' )

            print('*'*10, '\n', 'Page: ', offset+1)

        countries_data[country] = country_hotels

        print(country, ' - ', 'done ', len(country_hotels))
            
    return countries_data


def main():
    countries = ["Iceland","Italy","Finland","Estonia","Denmark","Ukraine"]
    
    countries_data = get_links(countries)

    with open('Hotels_full.json', 'a') as file:
        json.dump(countries_data, file, indent=4, ensure_ascii= True)


if __name__ == "__main__":
    main()