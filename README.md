# Swift Playgrounds Subscription Feeds

Subscription feed for Swift Playgrounds

This repo contains the subscription feeds, and can accessed with the Swift Playgrounds app at https://playi.github.com/swift/locales.json  Note that this repo was intentionally created with a shorter name, since that url needs to be typed into Swift Playgrounds for testing.

For future updates, copy (make sure you copy, and not just drag and drop an alias) the playgroundbook builds from the DashBook repo into the appropriate `Content` folder, then update the feeds.  Usually this means updating the 'lastUpdatedDate', as well as the 'sha512'.  You can get the `sha512` on macOS by running:
    `openssl dgst -sha512 <filename>`

There is a python script that can help update the different localized feeds, although the `additionalInformation` fields still need to be manually updated.

While public, this repos's github page is intended for testing.  The official release is at https://swiftplaygrounds.makewonder.com/locales.json
