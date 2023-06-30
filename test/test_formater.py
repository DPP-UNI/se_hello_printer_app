from hello_world.formater import plain_text_upper_case, format_to_xml
import unittest
from lxml import etree


class TestFormater(unittest.TestCase):
    def test_plain_uppercase(self):
        r = plain_text_upper_case("wwww", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())
    def test_format_to_xml(self):
        r = format_to_xml("wwww", "EEEMSG")
        root = etree.Element("greetings")
        etree.SubElement(root, "name").text = "EEEMSG"
        etree.SubElement(root, "msg").text = "wwww"
        self.assertTrue(r == etree.tostring(root, pretty_print=True))
