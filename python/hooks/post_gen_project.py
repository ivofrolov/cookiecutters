import os

DOTFILES = ["envrc", "gitignore"]

for path in DOTFILES:
    os.rename("_" + path, "." + path)
