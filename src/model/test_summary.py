import os
import json
import src.model.summary as summary
import unittest


# def json_of_response(response):
#     """Decode json from response"""
#     return json.loads(response.data.decode('utf8'))
#
# def json_request(self, url, data):
#     return self.app.post(url,
#                          data=json.dumps(data),
#                          content_type='application/json')
#
# def build_summary(client, text):
#     """Records a message"""
#     rv = json_request(client, '/api/summary_from_text', {'text': text})
#     # if text:
#     #     assert b'Your message was recorded' in rv.data
#     return rv

class SummaryestCase(unittest.TestCase):
    def test_build(self):
        input = "Text like this. Fastering test"
        text = summary.build(input)
        expected = "Fastering test\n\nText like this."
        self.assertEqual(text, expected)

if __name__ == '__main__':
    unittest.main()
