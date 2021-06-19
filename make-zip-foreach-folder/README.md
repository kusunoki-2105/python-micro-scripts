# Make .zip files for each folder at current directory

Before:
``` example-before
target-root-folder
 - target-folder-1
 - target-folder-2
 - target-folder-3
```

After:
``` example-after
target-root-folder
 - target-folder-1
 - target-folder-2
 - target-folder-3
 - target-folder-1.zip
 - target-folder-2.zip
 - target-folder-3.zip
```


## How to use

Put `make_zip_foreach_folder.py` in `target-root-folder`.

And run `python make_zip_foreach_folder.py`.

---

Also, if you using Windows.

`target-root-folder` drop on `RUN_make_zip_foreach_folder.bat`.
