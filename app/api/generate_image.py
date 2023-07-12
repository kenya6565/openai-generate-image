from http.server import BaseHTTPRequestHandler
import json, os, requests

class handler(BaseHTTPRequestHandler):
  def do_POST(self):
    content_length = int(self.headers['Content-Length'])
    post_data = self.rfile.read(content_length)
    request_data = json.loads(post_data)

    text = request_data.get('text', '')

    headers = {
        'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}',
        'Content-Type': 'application/json'
    }

    data = {
        "text": text
    }

    response = requests.post('https://api.openai.com/v1/images', headers=headers, data=json.dumps(data))

    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps({"generated_image": response.json()["generated_image"]}).encode())
    return
