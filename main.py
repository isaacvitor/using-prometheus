import asyncio
import multiprocessing as mp

import worker

workers = []

async def create_worker(port):
    return mp.Process(target=worker.main, args=(port,))

async def create_workers():
    global workers
    global qu
    port_list = [3000, 3001]
    for i in port_list:
        p = await create_worker(i)
        p.start()
        workers.append({'process': p, 'port': i})
        print(f'{p.pid} - is alive: {p.is_alive()}')
    return workers

async def close_workers(app):
    global workers
    try:
        for p in workers:
            p['process'].close()
        workers = []
    except Exception as e:
        print(e)

async def main():
    await create_workers()
    

if __name__ == '__main__':
    try:  
        asyncio.run(main())
    except KeyboardInterrupt:
        try:
            for p in workers:
                p.terminate()
        except:
            pass
    