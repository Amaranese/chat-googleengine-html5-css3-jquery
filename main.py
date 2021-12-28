
















import wsgiref.handlers
from chinwag import handlers
from chinwag.handlers import messages, rooms, authorizations, ping
from google.appengine.ext import webapp

def main():
      application = webapp.WSGIApplication([
      ('/', handlers.HomeHandler),
      ('/ping/(\d+)/?', ping.PingHandler),
      ('/rooms/?', rooms.RoomCollectionHandler),
      ('/rooms/(\d+)/?', rooms.RoomHandler),
      ('/rooms/(\d+)/edit/?', rooms.EditRoomHandler),
      ('/rooms/(\d+)/messages/?', messages.MessageCollectionHandler),
      ('/rooms/(\d+)/authorizations/?', authorizations.AuthorizationCollectionHandler),
    ], debug=True)
  wsgiref.handlers.CGIHandler().run(handlers.MockHTTPMethodMiddleware(application))

if __name__ == '__main__':
  main()