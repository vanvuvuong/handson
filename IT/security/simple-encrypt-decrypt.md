# Simple encryption & decryption for saving sensitive file in Linux

## I. Prerequisites

-   `gpg`: installation guide in [here](https://gnupg.org/download/)

---

## II. Step by step guide:

---

### **1. Create & export private/public key pair:**

-   Please follow detail guide in [here](https://gnupg.org/documentation/guides.html).

-   Run this command & answer all the prompt (suppose we create key name `sample`)

    ```
    gpg --full-gen-key
    ```

-   Export key public & private files

    ```
    gpg --armor --export sample > sample_public.gpg
    gpg --armor --export-secret-keys sample > sample_private.gpg
    ```

-   Import key public & private files (in other machine)

    ```
    gpg --import sample_public.gpg
    gpg --import sample_private.gpg
    ```

    After that you need to trust the key to use it without any errors

    ```
    gpg --edit sample
    gpg> trust
    [...]
    Please decide how far you trust this user to correctly verify other users' keys
    (by looking at passports, checking fingerprints from different sources, etc.)

      1 = I don't know or won't say
      2 = I do NOT trust
      3 = I trust marginally
      4 = I trust fully
      5 = I trust ultimately
      m = back to the main menu

    Your decision? 5
    Do you really want to set this key to ultimate trust? (y/N) y
    [...]
    gpg>quit
    ```

---

### **2. Setup simple encrypt, decrypt shell functions:**

-   Openning preference shell configuration file, suppose you use **zsh**, open file `~/.zshrc` and adding thess 2 functions:

    ```
    # encrypt files in current folder
    function eccf() {
        for file in ./*; do
            if [[ "$file" == *.asc ]] || [[ "$file" == *.md ]]; then
                continue
            fi
            gpg --batch --yes --armor --encrypt-files --recipient "$1" "$file" 2>/dev/null
        done
    }

    # decrypt files in current folder
    function dccf() {
        for file in ./*; do
            if [[ "$file" == *.asc ]]; then
                gpg --batch --yes --armor --decrypt-files --recipient "$1" "$file" 2>/dev/null
            fi
            continue
        done
    }
    ```

-   Close your current shell & reopen it to make sure the function is working

---

### **3. Sample encryption, decryption command**

-   Please remember that `sample` after `eccf` is the public/private key name that we setup before. These commands will **encrypt all files** in folder **`folder-has-files-that-want-to-encrypt`**:

    ```
    cd folder-has-files-that-want-to-encrypt
    eccf sample
    ```

-   These commands will **decrypt all files** with extension **\*.asc** in folder **`folder-has-files-that-want-to-decrypt`**:

    ```
    cd folder-has-files-that-want-to-decrypt
    dccf sample
    ```
