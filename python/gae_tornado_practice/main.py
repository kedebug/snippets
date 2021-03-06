import os
import tornado.web
import tornado.wsgi
import wsgiref.handlers
import handlers

settings = {
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
}

def main():
    application = tornado.wsgi.WSGIApplication([
        (r'/', handlers.PostListHandler),
        (r'/new', handlers.NewPostHandler),
    ], **settings)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
    main()
