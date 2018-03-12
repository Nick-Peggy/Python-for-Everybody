import xml.etree.ElementTree as ET

data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''  # multi-line string

tree = ET.fromstring(data)  # parse it in
print("Name:", tree.find("name").text)
print("Attribute:", tree.find("email").get("hide"))  # get attributes

