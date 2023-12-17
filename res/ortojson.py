import json
import re
import PyPDF2

def preprocess(text):

    text = re.sub(r"  ", " ", text)
    text = re.sub(r' \n', '\n', text)
    text = re.sub(r"Ergänzung des Schweizerischen Zivilgesetzbuches. BG\n\d+ / \d+ \d+", "" ,text)
    text = re.sub(r"\nObligationenrecht\n\d+ / \d+ \d+","", text)
    text = re.sub(r"(Art\..*)\n",r"</content>\n<article>\n\1\n</article>\n<content>\n", text)

    return text



def write(filename, content):
    fh = open(filename, "w", encoding='utf8')
    fh.write(content)

   

def pdfToJson():

    pdfFileObj = open('./fedlex-data-admin-ch-eli-cc-27-317_321_377-20230209-de-pdf-a-1.pdf', 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    content = ""
    size = (len(pdfReader.pages))
    
    
    print("load pdf started")    
    for i in range(size):        
        content += pdfReader.pages[i].extract_text()


    print("load pdf finished")    

    print("preprocess started")    
    content = preprocess(content)
    write("./ocr.txt", content)

    print("preprocess finihsed")



    print("parsing started")
    items = parse(content)

    print("parsing finished")

    result = []
    for item in items:
        result.append({
            "article": item[0],
            "content": item[1],
        })


    fh = open("ocr.json", "w", encoding='utf8')
    fh.write(json.dumps(result, ensure_ascii=False))


def parse(content):
    pattern_art = r'<article>\n(.*?)\n</article>\n<content>\n(.*?)\n</content>'
    return re.findall(pattern_art, content,  re.DOTALL)



def main():
    pdfToJson()


if __name__ == "__main__":
    main()

# closing the pdf file object