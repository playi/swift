# This program checks various localized feeds for consistency.
# It assumes most fields should be the same, except for fields specified
# in IGNORE_FIELDS
#
# If you pass a locale as the source locale (-s), which is often `en` in
# our usage, it will update the other feeds to match.  There's no safety
# checking, so your feeds should be in source control, in case this
# program trashes your feeds.

import argparse
import json

def compare_documents(source_docs, target_docs):
    IGNORE_FIELDS = ["title", "overviewSubtitle", "detailSubtitle",  "description", "additionalInformation"]
    return_docs = []
    dirty = False
    for doc in target_docs:
        source_doc = None
        for x in source_docs:
            if doc["url"] == x["url"]:
                source_doc = x
        if source_doc:
            for i in doc:
                if i not in IGNORE_FIELDS and doc[i] != source_doc[i]:
                    print(i + ": " + doc[i] + " does not match " + source_doc[i] + ", Replacing.")
                    dirty = True
                    doc[i] = source_doc[i]
        else:
            print("Error: could not find source doc for " + doc)

        return_docs.append(doc)
    if dirty:
        return return_docs

def scan_locales(source_locale):
    source_feed = None
    with open('locales.json', 'r') as locale_file:
        feeds = json.load(locale_file)
        if source_locale:
            with open(feeds[source_locale]) as source_feed_file:
                source_feed = json.load(source_feed_file)

        for i in feeds:
            print("locale :" + i + ", file :" + feeds[i])
            dirty = False
            feed = None
            with open(feeds[i], 'r') as feed_file:
                feed = json.load(feed_file)
                for j in feed:
                    if source_feed:
                        if j != "documents":
                            if (feed[j] != source_feed[j]):
                                dirty = True
                                print(j + ": " + feed[j] + " does not match " + source_feed[j] + ", Replacing.")
                                feed[j] = source_feed[j]
                        else:
                            updated_docs = compare_documents(source_feed[j], feed[j])
                            if updated_docs:
                                dirty = True
                                feed[j] = updated_docs
            if feed and dirty:
                with open(feeds[i], 'w') as feed_file:
                    json.dump(feed, feed_file, indent=4, separators=(',', ': '))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-s', '--source', action='store', dest='source')
    args = parser.parse_args()
    scan_locales(args.source)
