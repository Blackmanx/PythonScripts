# PythonScripts

A collection of python scripts I made with different applications.

## CopyPDF

Script that asks for a pdf, then appends all its pages into the destination pdf.

Usage:

```
python copypdf.py
```

```
python copypdf.py source_pdf destination_pdf
```

## FusionPDF

Script that asks for a folder and fuses all the pdfs inside it into one.

Usage:

```
python fusionpdf.py
```

```
python fusionpdf.py --folder=/path/to/folder --output=filename.pdf
```

## ExcelClient

Tool to find and retrieve data from an excel and print it in text files.

Usage:

```
python excelclient.py
```

```
python excelclient.py /path/to/excelfile
```

Then use the prompt menu.

## LineSplitter

Script that asks for a text file, then splits all its lines into different files inside the selected file's folder.

Usage:

```
python linesplitter.py
```

```
python linesplitter.py /path/to/file
```


## PathGrepper

Script that asks for a folder and a string to grep recursively inside that folder, including binaries.  It will print the paths where string is found in a file of your naming.

Usage:

```
python pathgrepper.py
```

```
python pathgrepper.py /path/to/folder <string>
```


## StringCommonizer

Script that asks for two text files and extracts common lines between them in a new file.

Usage:

```
python stringcommonizer.py
```

```
python stringcommonizer.py /path/to/file1 /path/to/file2
```
