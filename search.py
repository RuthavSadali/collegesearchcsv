import xml.etree.ElementTree as ET 
import dateutil.parser

class Search:
    
    def round_dictionary(self, dict, decimals=2):
        """
        HELPER METHOD IGNORE
        """
        for key in dict:
            dict[key] = round(dict[key], 2)
        return dict 

    def amount_spent(self, category):
        """
        Returns the amount spent in category
        """
        tree = ET.parse('sales-data.xml')
        root = tree.getroot()

        total = 0

        for item in root.findall('people/person'):
            if item.findall('category') == category:
                total = total + item.findall('amount')
        return total
            
    def spent_by_gender(self):
        """
        Returns a dictionary with a M and F key and the
        amount spent by each gender
        """
        tree = ET.parse('sales-data.xml')
        root = tree.getroot()

        totalM = 0
        totalF = 0

        for item in root.findall('people/person'):
            if item.findall('gender') == 'M':
                totalM = totalM + item.findall('amount')
            else:
                totalF = totalF + item.findall('amount')

        return {'M': totalM, 'F' : totalF}
        
    def all_categories(self):
        """
        Returns a dictionary with amounts spent in each
        category. The category should be the key, the
        sum of all sales in that category is the value
        """
        tree = ET.parse('sales-data.xml')
        root = tree.getroot()

        dictionary =  {}

        for item in root.findall('people/person'):
            s = item.findall('category')
            if item.findall('category') in dictionary:
                None
            else:
                dictionary[s] = 0
        
        for item in root.findall('people/person'):
            s = item.findall('category')
            p = item.findall('amount')

            dictionary[s] = dictionary[s] + p

        dictionary = round_dictionary(dictionary, 2)
        return dictionary

    def spent_between(self, start_date, end_date):
        """
        Returns the sum of all sales between start_date
        and end_date, inclusive
        """
        tree = ET.parse('sales-data.xml')
        root = tree.getroot()

        total = 0

        for item in root.findall('people/person'):
            if start_date < dateutil.parser.parse(item.findall('timestamp')):
                if end_date > dateutil.parser.parse(item.findall('timestamp')):
                    total = total + item.findall('amount')
        return total

    
