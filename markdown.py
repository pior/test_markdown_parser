import re


def convert(markdown_data):
    return '\n'.join(_convert(markdown_data))


RE_ORDERED_LIST_START = re.compile(r'^\d+\.\s')


class FormatError(Exception):
    pass


def _convert(markdown_data):
    """Generator for lines of html"""

    for block in markdown_data.split('\n\n'):
        lines = [l.strip() for l in block.splitlines()]

        if not lines or not len(lines[0]):
            continue

        if lines[0][0] == '#':
            header, content = lines[0].split(' ', 1)
            header_level = len(header)
            yield '<h{level}>{content}</h{level}>'.format(content=content,
                                                          level=header_level)

        elif lines[0][0] == '-':
            yield '<ul>'

            for line in lines:
                token, content = line.split(' ', 1)
                if token != '-':
                    raise FormatError(
                        'Invalid line "%s" in an unordered list' % line)
                content = content.strip()
                yield '<li>%s</li>' % content

            yield '</ul>'

        elif re.match(RE_ORDERED_LIST_START, lines[0]):
            yield '<ol>'

            for line in lines:
                content = line.split(' ', 1)[1]
                content = content.strip()
                yield '<li>%s</li>' % content

            yield '</ol>'

        else:
            content = '\n'.join(lines)
            yield '<p>{content}</p>'.format(content=content)
