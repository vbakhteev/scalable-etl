import argparse
import os

from celery import Celery


def parse_args():
    parser = argparse.ArgumentParser(
        description='Extracts corpus TMX, cleans data and produces parallel file structure')
    parser.add_argument('--tmx-file', dest='tmx_file', type=str, required=True,
                        help='Path to TMX file being processed')
    parser.add_argument('--output', type=str, default='resources/output.txt',
                        help='The path to the file where the extracted corpus will be located')

    return parser.parse_args()


def main():
    args = parse_args()
    task_queue = Celery(
        'CorpusExtraction',
        broker=os.getenv('BROKER_URL'),
    )

    if os.path.exists(args.output):
        os.remove(args.output)

    task_queue.send_task(
        'master.startTask', kwargs={'tmx_file': args.tmx_file, 'output': args.output},
        queue='masterq',
    )


if __name__ == '__main__':
    main()
