from hello_world.formater import plain_text_upper_case, format_to_xml
import unittest


class TestFormater(unittest.TestCase):
    def test_plain_uppercase(self):
        r = plain_text_upper_case("wwww", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())
    def test_format_to_xml(self):
        r = format_to_xml("wwww", "EEEMSG")
        assert(r == ("<greetings>\n\t<name>wwww</name>\n\t<msg>EEEMSG</msg>\n</greetings>"))
