# git-walk

Walk up and down in revisions of a [Git](https://git-scm.com/) repository.


## API

Checkout the last or latest commit:

```
git walk (last|latest)
```

Checkout the first or oldest commit:

```
git walk (first|oldest)
```

Walk down and checkout the previous commit:

```
git walk prev [n_commits]
```

Walk up and checkout the next commit:

```
git walk next [n_commits]
```


## Installation

Clone the repository and register the new command locally:

```bash
git clone https://github.com/nok/git-walk.git && cd ./git-walk && bash ./install.sh
```


## License

The extension is Open Source Software released under the [MIT](license.txt) license.
