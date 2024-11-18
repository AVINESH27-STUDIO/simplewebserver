from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <body>
        <h1 align="center"> laptop specification avinesh.B (24013574)</h1>
        <ol type="I" start="1">
            <li>device name DESKTOP-NBGBHVC </li>
            <li>processor 13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</li>
            <li>installed ram 16.0 GB (15.7 GB usable)</li>
            <li>device id EC6787BC-B8F4-4A61-86FC-95F8B82EB53F</li>
            <li>product id 00342-42709-15979-AAOEM</li>
            <li>system type 64-bit operating system, x64-based processor</li>
            <li>pen and touch  No pen or touch input is available for this display</li>
        </ol>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()