from lxml import etree


def extract_segments(file_path):
    for event, element in etree.iterparse(file_path, tag='tu'):
        src, src_lang = extract_text_and_lang(element[4])
        dst, dst_lang = extract_text_and_lang(element[5])

        yield src, src_lang, dst, dst_lang


def extract_text_and_lang(tuv_element: etree._Element):
    text = tuv_element[0].text
    lang = tuv_element.attrib.values()[0]
    return text, lang
