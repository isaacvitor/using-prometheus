import asyncio
from random import randint
# import sys

from aiohttp import web

import prometheus_metrics

port = None
count = 1
region = 'td-us-1'
cluster_name = 'cluster_xpto'


async def slow(request):
    global port
    global count
    m = f'Hello, running a SLOW FUNCTION in: {port} - #{count}!'
    print(m)
    sleep_time = randint(1, 3)
    print(f'Sleeping for {sleep_time} seconds...')
    await asyncio.sleep(sleep_time)
    count+=1
    return web.Response(text=m)


async def fast(request):
    global port
    global count    
    m = f'Hello, running a FAST FUNCTION in: {port} - #{count}!'
    print(m)
    count+=1
    return web.Response(text=m)


async def metrics(request):
    global port
    global count
    m = f'Returning some metrics!'
    print(m)
    return web.Response(text=m)


app = web.Application()
app.add_routes([web.get('/slow', slow)])
app.add_routes([web.get('/fast', fast)])
app.add_routes([web.get('/metrics', metrics)])


def main(p):
    global port
    global region

    # args = list(sys.argv)
    # port = int(args[1]) if len(args) >= 2 else SERVER_PORT
    try:
        port = int(p)
        web.run_app(app, host='0.0.0.0', port=port)
    except KeyboardInterrupt:
        pass
