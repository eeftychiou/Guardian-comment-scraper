from scrapeComments import scrapeComments
import argparse
import os
import json
import csv

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()

def saveComments(format, comments):
    print format
    fileName = 'comments-{%i}.%s'%(len(comments[0]),format)
    outFile = open(fileName, 'wb')

    if format=='csv':
        keys = comments[0][0].keys()
        w = csv.DictWriter(outFile, keys)
        w.writeheader()

    for i, comment in enumerate(comments):
        if format == 'json' or format is None:

            json.dump(comment, outFile, indent=4)
            outFile.close()
        elif format == 'csv':
            w.writerows(comment)


fileOrUrl = args.source
fileName, fileExtension = os.path.splitext(fileOrUrl)
comments = []

if fileExtension == '.txt':
    lines = [line.rstrip('\n') for line in open(fileOrUrl)]
    for line in lines:
        output = scrapeComments(line)
        comments.append(output)
else:
    output = scrapeComments(fileName)
    comments.append(output)

saveComments(args.output, comments)

