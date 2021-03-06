from sanic import Sanic
from sanic.response import json

'''
This is a trivial asynchronous IO-centric Python webapplication. 

Run build.sh to use Packeto to build an image 

You can then run it using: 

docker run -p 8888:8888  python-asyncio-web 
'''

app = Sanic('greetings-service')


@app.route("/")
async def test(request):
    return json({"hello": "world"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
