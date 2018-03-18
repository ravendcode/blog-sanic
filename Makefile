dev:
	nodemon --watch blog_sanic --exec python3.6 blog_sanic/app.py -e js,hbs,pug,py

prod:
	python3.6 blog_sanic/app.py -env=production -port=80
