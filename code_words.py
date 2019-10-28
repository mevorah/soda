import sys
import re

# Extensions must be in a format ready for python
extensions = [
    "c",
    "c\+\+",
    "css",
    "go",
    "html",
    "java",
    "js",
    "kt",
    "md",
    "objc",
    "py",
    "rs",
    "ruby",
    "swift",
    "xml",
    "yaml",
    "yml"
]
pattern_path_str = "^.*\/(.*)\.({}).*$".format('|'.join(extensions))
pattern_alone_str = "^(.*)\.({}).*$".format('|'.join(extensions))
pattern_path = re.compile(pattern_path_str)
pattern_alone = re.compile(pattern_alone_str)

def getCamelCaseWords(word):
    words = []
    current_word = ""
    for char in filename_no_ext:
        if char.isupper():
            words.append(current_word)
            current_word = ""
        current_word += char
    words.remove("")

    words.append(current_word)
    return words

def getSnakeCaseWords(word):
    words = []
    current_word = ""
    for char in filename_no_ext:
        if char is "_":
            words.append(current_word)
            current_word = ""
            continue
        current_word += char

    words.append(current_word)
    return words


title = sys.argv[1]
path_result = pattern_path.search(title)
alone_result = pattern_alone.search(title)

filename_no_ext = None
if path_result:
    filename_no_ext = path_result.group(1)
elif alone_result:
    filename_no_ext = alone_result.group(1)

if filename_no_ext:
    words = []
    if "_" in filename_no_ext:
        words = getSnakeCaseWords(filename_no_ext)
    elif filename_no_ext.islower():
        words = getSnakeCaseWords(filename_no_ext)
    else:
        words = getCamelCaseWords(filename_no_ext)
    print(",".join(words))