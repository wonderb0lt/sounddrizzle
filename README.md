# SoundDrizzle

This is nothing more than a simple downloader for SoundCloud so that you can listen to your favorite tracks offline. You'll have to create a SoundCloud app and put the id into sounddrizzle.py (if installed via pip, you'll have to find it in your filesystem)

**It is your responsibility to check whether or not the track has rights reserved, and if you're allowed to download**

You can use the script against SoundCloud URLs...

```bash
$ drizzle https://soundcloud.com/wearecc/dublabs-cc10-mix
```

or perform a search on the API:

```bash
$ drizzle "dublabs #cc10"
```

For more options, call `drizzle --help`
