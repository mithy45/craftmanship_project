import unittest
import requests
class TestFlask(unittest.TestCase):

    def test_story1_put_correct_response(self):
        payload = {
                    "word":"key-hello",
                    "translations":[
                        {"language":"en", "translation":"hello"},
                        {"language":"fr", "translation":"bonjour"},
                        {"language":"it", "translation":"ciao"}
                    ]
                }
        response = requests.put(url="http://localhost:8080/api/words", json=payload)

        expected = payload
        expected["url"] = "http://localhost:8080/api/words/key-hello"
        self.assertEqual(response.json(), expected)
        self.assertEqual(response.status_code, 201)

    def test_story1_put_incorrect_format_response(self):
        payload = {
                    "shitwords":"key-hello",
                    "shittranslations":[
                        {"language":"en", "translation":"hello"},
                        {"language":"fr", "translation":"bonjour"},
                        {"language":"it", "translation":"ciao"}
                    ]
                }
        response = requests.put(url="http://localhost:8080/api/words", data=payload)
        self.assertEqual(response.status_code, 406)

    def test_story1_put_no_payload_response(self):
        response = requests.put(url="http://localhost:8080/api/words")
        self.assertEqual(response.status_code, 406)
    


if __name__ == "__main__":
    unittest.main()