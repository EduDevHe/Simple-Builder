# Simple-Builder

## Dowload Repository:
`git clone https://github.com/EduDevHe/Simple-Builder.git`

## Install:
```bash
cp simple_builder.py /usr/local/bin/
```
```bash
chmod +x /usr/local/bin/simple_builder.py
```
## How to use:
- Initializes the simple builder and creates the simple_builder.json configuration file
```bash
simple_builder.py -i
```
- Compile a file written in c
```bash
simple_builder.py -f Hello.c
```
## Config File:
```json
{
 "lang": "c", // Language supported by gcc
 "compiler": "gcc", // Compiler
  "run": "false", // Run after compile
  "dist": "./bin" // Executable directory
}
```
