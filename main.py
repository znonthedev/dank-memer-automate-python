import sched
from dank_memer_actions import *

s = sched.scheduler(time.time, time.sleep)


def start_bot():
    fish()
    hunt()
    post_memes()
    search()
    beg()
    dep()
    s.enter(35, 0, start_bot)


s.enter(1, 0, start_bot)
s.run()
