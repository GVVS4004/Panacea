from website import crete_app
app=crete_app.create_app()

if __name__=='__main__':
    app.run(debug=True)
    