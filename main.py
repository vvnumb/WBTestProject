from config import settings


if __name__ == "__main__":
    if settings.IS_SELF_SERVER_IMPL:
        from presentation.self_server_impl import SelfImplementedHTTPServer
        from http.server import HTTPServer
        
        webServer = HTTPServer((settings.HOSTNAME, settings.PORT), SelfImplementedHTTPServer)
        print("Server started http://%s:%s" % (settings.HOSTNAME, settings.PORT))
        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass

        webServer.server_close()
    else:
        from presentation.fastapi_impl import app
        import uvicorn
        uvicorn.run(app, port=settings.PORT)
