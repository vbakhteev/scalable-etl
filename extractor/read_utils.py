from lxml import etree


def extract_segments(file_path):
    for event, element in etree.iterparse(file_path, tag='tu'):
        tuv1, tuv2 = element.xpath('tuv')
        src, src_lang = extract_text_and_lang(tuv1)
        dst, dst_lang = extract_text_and_lang(tuv2)

        yield src, src_lang, dst, dst_lang


def extract_text_and_lang(tuv_element: etree._Element):
    text = tuv_element[0].text
    lang = tuv_element.attrib.values()[0]
    return text, lang
