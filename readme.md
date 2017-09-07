# git-walk

Walk up and down in revisions of a [Git](https://git-scm.com/) repository.


## API

Checkout the last or latest commit:

```bash
git walk last
```

```bash
git walk latest
```

Checkout the first or oldest commit:

```bash
git walk first
```

```bash
git walk oldest
```

Walk down and checkout the previous commit:

```bash
git walk prev
```

Walk up and checkout the next commit:

```bash
git walk next
```


## Installation

Clone the repository and register the new command locally:

```bash
git clone https://github.com/nok/git-walk.git && cd ./git-walk && bash ./install.sh
```


## License

The extension is Open Source Software released under the [MIT](license.txt) license.
