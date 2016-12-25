import orm 
import asyncio

from models import User, Blog, Comment

@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop, user='www-data', password='www-data',db='awesome')

    u = User(name='Test2', email='test2@example.com', passwd='1234567890', image='about:lank')

    yield from u.save()
    yield from orm.destory_pool()

    # for x in test():
    #     pass


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()