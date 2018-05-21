from xml.parsers.expat import ParserCreate
import re

class defaultsax(object):
    def __init__(self):
        self.weather = {}
    def start_element(self, name, attrs):
        self.weather['na'] = name
        self.weather['attr'] = attrs
        if self.weather['na'] == 'yweather:location':
            print('国家：%s\t城市:%s' % (attrs['country'],attrs['city']))

        if self.weather['na'] == 'yweather:wind':
            print('今日温度：%s°C\t风向：%s°\t风速：%skm/h' % (attrs['chill'],attrs['direction'],attrs['speed']))

        if self.weather['na'] == 'yweather:atmosphere':
            print('湿度：%s\t能见度：%s\t气压:%-10s' % (attrs['humidity'],attrs['visibility'],attrs['pressure']))

        if self.weather['na'] == 'yweather:astronomy':
            print('日出：%s\t日落：%s' % (attrs['sunrise'],attrs['sunset']))

#        if self.weather['na'] == 'yweather:condition':
#            print('天气状况：%s,日期：%s' % (attrs['text'],attrs['date']))

        if self.weather['na'] == 'yweather:forecast':
            if int(re.search('[\d]{2}', attrs['date']).group()) - self.weather['days'] == 0:
                print('---今日天气状况---\n日期:%s\n天气：%s\n最低温度:%s\n最高温度：%s°' % (attrs['date'],attrs['text'],attrs['low'],attrs['high']))
            if int(re.search('[\d]{2}', attrs['date']).group()) - self.weather['days'] == 1:
                print('---明日天气状况---\n日期：%s\n天气：%s\n最低温度:%s\n最高温度：%s°' % (attrs['date'],attrs['text'],attrs['low'],attrs['high']))

    def end_element(self, name):
        self.weather['end_ele'] = name
        if self.weather['end_ele'] == 'pubDate':
            dy = re.search('[\d]{2}', self.weather['ch_da'])
            self.weather['days'] = int(dy.group())
        pass

    def char_data(self, text):
        self.weather['ch_da'] = text
        #print('sax:char_data: %s' % text)
        pass

xml = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''
handler = defaultsax()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)