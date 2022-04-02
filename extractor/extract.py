import argparse
import os

from celery import Celery
from lxml import etree


def parse_args():
    parser = argparse.ArgumentParser(
        description='Extracts corpus TMX, cleans data and produces parallel file structure')
    parser.add_argument('--tmx-file', dest='tmx_file', type=str, required=True,
                        help='Path to TMX file being processed')
    parser.add_argument('--output', type=str, default='out/',
                        help='The path to the folder where the extracted corpus will be located')

    return parser.parse_args()


def main():
    args = parse_args()
    task_queue = Celery('CorpusExtraction', broker=os.getenv('BROKER_URL'))

    for src, src_lang, dst, dst_lang in extract_segments(args.tmx_file):
        task_queue.send_task(
            'cleanTask',
            kwargs={'src': src, 'src_lang': src_lang, 'dst': dst, 'dst_lang': dst_lang, 'output': args.output},
        )


def extract_segments(file_path):
    for event, element in etree.iterparse(file_path, tag='tu'):
        src, src_lang = extract_text_and_lang(element[4])
        dst, dst_lang = extract_text_and_lang(element[5])

        yield src, src_lang, dst, dst_lang


def extract_text_and_lang(tuv_element: etree._Element):
    text = tuv_element[0].text
    lang = tuv_element.attrib.values()[0]
    return text, lang


if __name__ == '__main__':
    main()
