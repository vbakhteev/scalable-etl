import os

from celery import Celery

from filtering import filter_text

task_queue = Celery(
    'CorpusExtraction',
    broker=os.getenv('BROKER_URL'),
)


@task_queue.task(name='node.cleanTask')
def clean(src, src_lang, dst, dst_lang, output):
    src_clean = filter_text(src)
    dst_clean = filter_text(dst)

    task_queue.send_task(
        'master.writeTask',
        kwargs={'src': src_clean, 'src_lang': src_lang, 'dst': dst_clean, 'dst_lang': dst_lang, 'output': output},
        queue='masterq',
    )


@task_queue.task(name='node.alignTask')
def align(src, src_lang, dst, dst_lang, output):
    sentences_aligned = True

    if sentences_aligned:
        task_queue.send_task(
            'master.writeTask',
            kwargs={'src': src, 'src_lang': src_lang, 'dst': dst, 'dst_lang': dst_lang, 'output': output},
            queue='masterq',
        )
