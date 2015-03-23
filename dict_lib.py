# -*- coding: utf-8 -*-
__author__ = 'sergy'

import httplib, urllib
import xml.etree.ElementTree as ET

class yandex_dict:
    base_url = r'https://dictionary.yandex.net/api/v1/dicservice/lookup'
    post_url = r'/api/v1/dicservice/lookup'

    def __init__(self, cur_api_key):
        self.api_key = cur_api_key

    def get_result_post(self, text_in, c_lang):
        params = urllib.urlencode({'key': self.api_key, 'text': text_in, 'lang': c_lang})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = httplib.HTTPSConnection("dictionary.yandex.net")
        conn.request("POST", self.post_url, params, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        print(data)
        conn.close()
        return data


    def check_text(self, text_in, c_lang):
        result_xml = self.get_result_post(text_in, c_lang)
        root = ET.fromstring(result_xml)
        translations = root.findall("./def")
        words = []
        for translation in translations:
            c_word = translation.find("./tr/text").text
            words.append(c_word)
        return words


