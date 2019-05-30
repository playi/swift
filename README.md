# Swift Playgrounds Subscription Feeds

Subscription feed for Swift Playgrounds

This repo contains the subscription feeds, and can accessed with the Swift Playgrounds app at https://playi.github.com/swift/locales.json  Note that this repo was intentionally created with a shorter name, since that url needs to be typed into Swift Playgrounds for testing.

For future updates:

1. Copy (make sure you copy, and not just drag and drop an alias) the playgroundbook builds from the DashBook repo into the appropriate `Content` folder.
2. Delete the previous zipped version of the playgroundbook.
3. Zip the new playgroundbook.  You can do this in Finder with the right-click menu "Compress" option on the playgroundbook file.
4. Delete the pre-zip playgroundbook, it's not necessary.
5. Get the SHA512 for the playgroundbook zip that you just created.
        `openssl dgst -sha512 Content/Dash/dashbook.playgroundbook.zip`
        `openssl dgst -sha512 Content/DashTemplate/DashTemplate.playgroundbook.zip`
6. Update `Feeds/en_lproj/feed.json`.  Make sure you find the appropriate section, either for `dashbook` or `DashTemplate`.  You must update the `sha512`.  You probably should update the `lastUpdatedDate`.
7. There's a python script that takes the changes from `Feeds/en_lproj/feed.json` and attempts to propagate them to the various localized copies of the feed.  Run it with `en` as the source feed.  Note that anything in `additionalInformation` fields don't get propagated by this script (TODO: propagate `additionalInformation.version`)
        `python check_feeds.py -s en`
8. Commit all the changes.  At this point, the feed should then be available at https://playi.github.io/swift/locales.json
9. If all goes well, publish to our official feed at S3.
        `aws s3 sync . s3://swiftplaygrounds.makewonder.com`
   If uploaded successfully, the feed should now be at the official location: https://swiftplaygrounds.makewonder.com/locales.json
