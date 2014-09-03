__author__ = 'danielby'
import tornado.web
import tornado.gen
import tornado.httpclient
import tornado.ioloop
import datetime

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http_client = tornado.httpclient.AsyncHTTPClient()
        http_client.fetch("http://friendfeed-api.com/v2/feed/bret", callback=self.handle_request)

    def handle_request(self, response):
        if response.error: raise tornado.web.HTTPError(500)
        json = tornado.escape.json_decode(response.body)
        self.write("Fetched " + str(len(json["entries"])) + " entries "
                   "from the FriendFeed API")
        self.finish()


application = tornado.web.Application([
    (r'/', MainHandler)
])

application.listen(8888)
tornado.ioloop.IOLoop.instance().start()