# MathTranslate
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/SUSYUSTC/MathTranslate/blob/main/README.md)
[![zh](https://img.shields.io/badge/lang-zh-yellow.svg)](https://github.com/SUSYUSTC/MathTranslate/blob/main/README.zh.md)

<p align="center">
  <a href="https://github.com/SUSYUSTC/MathTranslate">
    <img width=30% src="logo.jpg">
  </a>
</p>


This is a project to provide translation of scientific papers with heavy math symbols from any language to any language while keeping the math symbols unchanged. In most translation softwares you wouldn't be able to keep equations and it would annoy you.
This project is based on the following two tools:
1. [mathpix](https://mathpix.com/): it provides an interface to convert text+equation images to latex code. Unfortunately it is not totally free. The price can be seen at  https://mathpix.com/pricing.
2. [translate-shell](https://github.com/soimort/translate-shell): it provides a terminal interface to google translate

The main work in this project is to translate a latex file from one language to another and to develop an interface of the above two tools.

Here's an example of what you get finally.
<p float="left">
<img src="https://user-images.githubusercontent.com/30529122/225237425-9341b03e-25b5-4617-b606-5e3813de3ec2.png" width="260">
<img src="https://user-images.githubusercontent.com/30529122/225234174-78af1e5f-aeff-4dd8-9f4c-d948edc35318.png" width="400">
</p>

Although it is currently a small project, we are aware that this project has received much more attention that we expected. We are planning more developments for better user experience.

## Requirements
1. Only works for Linux temporarily. For windows user you can use Windows Subsystem for Linux (WSL). We will soon
2. A [mathpix](https://mathpix.com/) account. Unfortunatedly it is totally free. The current price is free for 100 screenshots (requires an educational email in registeration) and $5 per month for 5000 screenshots.
3. translate-shell: `sudo apt-get install translate-shell`
4. texlive (or any other tool to generate pdf from tex): `sudo apt-get install texlive-full`

## Usage
1. Download mathpix. In the Settings-Formatting, change "Inline math delimiters" and "Block mode delimiters" to "\( ... \)" and "\[ ... \]", respectively.
2. Add directory `MathTranslate/scripts` to PATH
3. Use mathpix to screenshot what you want to translate, copy the output latex code and save in a tex file. Let's say the filename is old.tex.
4. Run `translate_tex.py old.tex new.tex` in this folder (you could change "new" to anything you like). You will get a translated tex file new.tex and a corresponding pdf file in case `xelatex` is installed on your machine.
5. Since this project is small, sometimes you need to slightly change the final tex file for compilation.
6. The default code is translating English into Chinese. If you want to translate from/to other languages, you just need to change `language_from` and `language_to` in `MathTranslate/scripts/translate_tex.py`

## Examples
In the example directory, you can see `english.tex` which is the mathpix output of a part of a recent paper. Run `translate_tex.py english.tex chinese.tex` and you would expect to get the same output with the existing `chinese.tex` and `chinese.pdf`.

## Further developments
1. Support for different operating systems.
2. Automatically extract images from pdf, process images in a batch and output a single translated pdf by one click!
3. A more user-friendly interface.

If you are interested in making contribution, please contact me by susyustc@gmail.com or Wechat account sunjiace2262.
