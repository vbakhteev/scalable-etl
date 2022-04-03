import os

from celery import Celery

from read_utils import extract_segments

task_queue = Celery(
    'CorpusExtraction',
    broker=os.getenv('BROKER_URL'),
)


@task_queue.task(name='master.startTask')
def start(tmx_file, output):
    for src, src_lang, dst, dst_lang in extract_segments(tmx_file):
        task_queue.send_task(
            'node.cleanTask',
            kwargs={'src': src, 'src_lang': src_lang, 'dst': dst, 'dst_lang': dst_lang, 'output': output},
            queue='nodeq',
        )


@task_queue.task(name='master.writeTask')
def write(src, src_lang, dst, dst_lang, output):
    with open(output, 'a') as f:
        f.write('<>'.join([src_lang, dst_lang, src, dst]) + '\n')
