### When `pip` isn't installed
  * on mac / linux - `sudo easy_install pip`
  * on windows (cmd as admin) - `easy_install pip`

### Installing XGBoost on Windows if `pip` and `anaconda` install commands fail
  * Download xgboost whl file from http://www.lfd.uci.edu/~gohlke/pythonlibs/
  * Use `pip install <downloaded-whl-file-path>`
  * If install fails due to missing dependencies, install them first and retry. Almost all `whl` packages can be found online if facing issues with installing a particular package

### Upgrading all installed python packages on windows
  * `pip freeze > requirements.txt`
  * `pip install -r requirements.txt --upgrade`
    
### Compilers and unhandled dependencies
  * Some packages are installed with the help of compilers like gcc, cmake, etc. And not each package will indicate/handle the dependency. For e.g., Installing gcc solved the problem of installing word2vec on the machine. Always, always stick to 64 bit version of everything.

### Jupyter notebook wordwrap for code
Add this to jupyter config, the config file is usually present at `.jupyter\jupyter_notebook_config` in the user folder. If not available `jupyter notebook --generate-config` will generate a default one.
```json
{
  "MarkdownCell": {
    "cm_config": {
      "lineWrapping": true
    }
  },
  "CodeCell": {
    "cm_config": {
      "lineWrapping": true
    }
  }
}
```

### Using different Jupyter notebook startup folder
  * `jupyter notebook <path-to-desired-folder>` 

### Install a python package without using cache for the package and it's dependencies
  * `pip --no-cache-dir install <package-name>`

### `cl.exe missing` error during a package installation
  * This executable is under `Program Files > Microsoft Visual Studio > VC > bin` Adding the folder to the `PATH` environment variable should fix the issue
