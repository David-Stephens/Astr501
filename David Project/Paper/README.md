# NuGrid Paper Repo

The [NuGrid Paper Repo](https://github.com/NuGrid/Paper) is available
from [GitHub NuGrid organization](https://github.com/NuGrid)

## Intro

This directory contains the new NuGrid paper Latex template.  It is
based on the layout created by Ed Brown for the MESA paper.  It is
provided so that NuGrid papers can be written by an author team, using
the same Latex style and thereby leading to an internally consistent
manuscript. New papers can re-use the .bib files and macros from
existing papers so that there is further consistency.

This repo contains `paper_resources` directory which contains a macros
and a bib diredctory. These contain latex macro files and `*.bib`
files and should be used for each paper. Additions should be made to
these shared macro and bib files.  For MNRAS and AAS journals there
are separate *template* directories, `paper_mnras` and `paper_aas`. Each 
contains a ready-to-use `paper.tex` template that imports the
resources from `paper_resources`. 

## Quickstart

Make sure you are insude the `Paper` repo, and that you have mounted the CANFAR VOspace if you want to use the figure example:
```
getCert
mountvofs --readonly --cache_dir=/tmp/vosCache --cache_limit=2000 --mountpoint=/tmp/nugrid --vospace=vos:nugrid
cd paper_template/figs/figure_template/
jupyter notebook example_figures.ipynb
```
In the notebook use the _Cell_ $\rightarrow$ _Run All_ menu option to execute the notebook and make the image files. Then 
```
cd ../..
./mk
```
This should produce the pdf file `paper.pdf`.


## Additional information

1. Clone the Paper repo and start writing in the `paper_template` dir using the `paper.tex` template. 
2. Rename Paper repo to some project name and associate with appropriate remote repository to share with collaborators. 
3. It is recommended to keep the `paper_resources` dir with your paper repo until the paper is finished,
and then add any useful changes you may have made to the `paper_resources` to the Paper repo.  When starting a new paper, always start
with a new copy of Paper repo.
3. **Data:** Data pertaining to the paper should be deposited  on the NuGrid CANFAR VOspace, ideally associated with a DOI. The DOI can be requested from CANFAR, by emailing to them (cc fherwig@uvic.ca). 
4. **Figures:** It is recommended to keep the final notebook that generates a figure to be shown in the paper in a directory with the Paper repo. An example is available: `paper_template/figs/figure_template`. In this way anyone, including yourself (!) can later reproduce these plots, or make similar ones with little effort.
4. **Bibliography:**   All references should go into one of the .bib files. `*.bib` files can be found and maintained in `paper_resources/bib`.
   ADS gives access to the bibtex record for every article.
5. **Symbols, units, etc.:** are standardized in the  `paper_resources/macros` directory. Rather than adding new commands to individual LaTeX files, please put all definitions in. Note that for many things there are
   already macros. In particular note the way we write isotopes (see
   nuclides.tex). The point of the NuGrid Latex framework is to
   homogenize the Latex document appearance, and using only one macro
   for each task is the most important way in which to enable efficient collaborative writing.
6. **Notes:** for material not destined for the text of the paper, such as planning documents, use the `paper_template/notes` directory.
7. There is a Makefile and/or basic compile scripts (mk and clean) 
   to construct the paper from sources and to clean up the auxiliary 
   files.

## Resources

* Check the [AASTeX v6.1 Authors Guide](http://journals.aas.org/authors/aastex/aasguide61.html)  for details and the more complete example in `paper_template/aastex_v611/sample61.tex` as well as the comments and .
* [MNRAS for authors](http://www.oxfordjournals.org/our_journals/mnrasl/for_authors/)

## Acknowledgements
Thank you to Ed Brown for permission to use the initial version of
this template, and to Aaron Dotter for adopting it for to the NuGrid
collaboration.  Updates by Ondrea Clarkson. Updates by Falk Herwig to aastex v6.11.

