# git-walk

`git walk` allows you to walk up and down in revisions of a git repository.


## API

Checkout the latest commit:

```
git walk last
```

Checkout the first commit:

```
git walk first
```

Walk down and checkout the previous commit:

```
git walk prev
```

Walk up and checkout the next commit:

```
git walk next
```


## Installation

Clone the repository and register the new command globally:

```bash
git clone https://github.com/nok/git-walk.git
cp ./git-walk/script.py ~/.git-walk.py
git config --global alias.walk '!python ~/.git-walk.py'
rm -rf ./git-walk
```


## License

The extension is Open Source Software released under the [MIT](license.txt) license.
