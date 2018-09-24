import json
import os
from django.conf import settings
import datetime

class GetRoot:
    def __init__(self):
        self.alternative_titles_config_file = os.path.join(settings.CONFIG_FOLDER, "alternative_titles.json")
        self.alternative_values_config_file = os.path.join(settings.CONFIG_FOLDER, "alternative_values.json")
        with open(self.alternative_values_config_file, 'r+') as fp:
            self.alternative_json = json.loads(fp.read())

        with open(self.alternative_titles_config_file, 'r+') as fp:
            self.alternative_titles_json = json.loads(fp.read())

    def get_most_feasible_value(self, json_obj, keyname, list_of_value):
        keyvalues = json_obj[keyname]
        for value in list_of_value:
            if type(value) == type(''): value = value.lower()
            for possible_value, possible_alternative_values in keyvalues.items():
                for alternative_value in possible_alternative_values:
                    if type(value) == type('') and alternative_value.lower().strip() == value.strip():
                        return possible_value
        return list_of_value[0]

    def get_root_word(self, keyname, value):
        keyname = keyname.upper()
        json_obj = self.alternative_json
        if keyname == 'BUY/SELL':
            keyname = 'BUY_SELL'
        if keyname in json_obj:
            if type(value) == type([123]):
                return self.get_most_feasible_value(json_obj, keyname, value)
            if type(value) == type(''): value = value.lower()
            keyvalues = json_obj[keyname]
            for possible_value, possible_alternative_values in keyvalues.items():
                for alternative_value in possible_alternative_values:
                    if type(value) == type('') and alternative_value.lower().strip() == value.strip():
                        return possible_value
        return value

    def match_records(self,keyname,predictedvalue,xonevalue):
        json_obj = self.alternative_json
        alternate_titles_json_obj = self.alternative_titles_json
        keyname = keyname.upper()
        title_properties = alternate_titles_json_obj[keyname]

        try:
            if (title_properties["RoundOff"]):
                rounded_value = round(float(predictedvalue))
                print(rounded_value)
                if rounded_value == xonevalue:
                    return True
                else:
                    return False
        except KeyError:
            if keyname == ("MATURITY_DATE" or "TRADE_DATE"):
                return None
                pass
            if keyname in json_obj:
                root = self.get_root_word(keyname, predictedvalue)
                if root.lower() == xonevalue.lower():
                    return True
                else:
                    return False
    def test(self):
        print(self.alternative_json)
        word = self.get_root_word("CURRENCY","Swiss Francs")
        print(word)
        return word

#
# a = GetRoot()
# a.test()
