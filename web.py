from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<html>
    <body>
     <h1 align="center">About the System</h1>
        <table border="1" cellpadding="5" align="center">
            <tr>
                <th>SYSTEM CONFIGURATION</th><th>DESCRIPTION</th>
            </tr>
            <tr>
                <td>Processor</td>
                <td>13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</td>
            </tr>
            <tr>
                <td>Primary Memory</td>
                <td>Ram-16GB</td>
            </tr>
            <tr>
                <td>Secondary Memory</td>
                <td>Rom-512GB</td>
            </tr>
            <tr>
                <td>O.S</td>
                <td>Windows 11</td>
            </tr>
            
        </table>
    </body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()