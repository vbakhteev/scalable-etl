import os
import time

from celery import Celery

from filtering import filter_text

time.sleep(10)

task_queue = Celery('CorpusExtraction', broker=os.getenv('BROKER_URL'))


@task_queue.task(bind=True, name='cleanTask')
def clean(self, src, src_lang, dst, dst_lang, output):
    src_clean = filter_text(src)
    dst_clean = filter_text(dst)

    task_queue.send_task(
        'alignTask',
        kwargs={'src': src_clean, 'src_lang': src_lang, 'dst': dst_clean, 'dst_lang': dst_lang, 'output': output},
    )
