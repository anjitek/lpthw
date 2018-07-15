import sys
script, input_encoding, error = sys.argv
#need three arguments when running python ex23.py

#bytes.decode(encoding="utf-8", errors="strict")
#Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，
#这个 bytes 对象可以由 str.encode() 来编码返回。
#http://www.runoob.com/python3/python3-string-decode.html
#encoding -- 要使用的编码，如"UTF-8"。
#errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。
#其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    #strip():delete spaces before and after lines
    raw_bytes = next_lang.encode(encoding, errors=errors)
    #encode(编码)：按照某种规则将“文本”转换为“字节流”。
    #python 3中表示：unicode变成str
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    #decode(解码)：将“字节流”按照某种规则转换成“文本”。
    #python3中表示：str变成unicode

    print(raw_bytes, "<<<=======>>>", cooked_string)

languages = open("languages.txt", encoding = "utf-8")

main(languages, input_encoding, error)
