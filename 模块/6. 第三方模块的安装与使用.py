import schedule
import time
def job(a):
    print('我正在做{0}工作'.format(a))

job('编程')
schedule.every(5).seconds.do(job,'编程')
while True:
    schedule.run_pending()
    time.sleep(10)