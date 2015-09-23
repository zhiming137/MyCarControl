import web
        
urls = (
    '/(.*)', 'index'
)
app = web.application(urls, globals())
render = web.template.render('templates/',cache=False)

class index:        
    def GET(self, name):
        return render.index()

if __name__ == "__main__":
    app.run()
