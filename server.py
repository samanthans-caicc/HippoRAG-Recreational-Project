import http.server
import socketserver

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        return super().do_GET()

def main():
    Handler = CustomHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        
        # Optional: open browser automatically
        #webbrowser.open(f"http://localhost:{PORT}")
        
        httpd.serve_forever()


if __name__ == '__main__':
    main()
