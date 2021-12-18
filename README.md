# StrucTree
A parser for XML and JSON files that shows the structure of the file similar to the Linux tree command.

## Usage
tbd

## Purpose
This tool is great to get an overview of the structure of your XML or JSON files. 
It is not only helpful for programming and further processing of the files but also for documentation. For example, its output can be included in LaTeX listing environments:
```
\usepackage{listings}

\begin{lstlisting}
./test.{json/xml}
   └─movies
      ├─movie
      │  ├─name
      │  └─year
      └─movie
         ├─name
         └─year
\end{lstlisting}

```
