# git-walk

Walk up and down in revisions of a [Git](https://git-scm.com/) repository.


## API

Checkout the last or latest commit:

```bash
git walk (last|latest)
```

Checkout the first or oldest commit:

```bash
git walk (first|oldest)
```

Walk down and checkout the previous commit:

```bash
git walk prev [n_commits]
```

Walk up and checkout the next commit:

```bash
git walk next [n_commits]
```


## Installation

Clone the repository and register the new command locally:

```bash
git clone https://github.com/nok/git-walk.git && cd ./git-walk && bash ./install.sh
```


## License

The extension is Open Source Software released under the [MIT](license.txt) license.
