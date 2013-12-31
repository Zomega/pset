Pset - Version 0.3
==================

This repo contains my Personal Pset Management setup and compile scripts. My Psets are in LaTeX by default; I use a Makefile to expedite common tasks.

Dependencies
------------

* (http://jinja.pocoo.org/ "Jinja2") for constructing new psets out of templates.

How to Use
----------

Since (for now) this is Makefile based, there is no install process. Instead for each new pset do the following steps

1. Pull this repository into the folder the pset will be made in.
2. `cd` to the pset and run `make init`.
3. Complete the interactive prompt (if you're looking to develop, this is based in `.config/config.py`).
4. Complete your pset (hopefully, this is the hard part) in the `.tex.part` files and supporting files. For instance, write LaTeX for part (2)(a)(iv) in `problem.2.a.iv.tex.part`. If a part is incomplete, tag it with the string TODO.
5. At any time, run `make` to create PDFs of the pset.
6. Before turning in, it's a good idea to run `make check` to check for the string TODO in relevant documents.

Pull Request Policy
-------------------

If you submit a pull request, please make an effort to remove _pset specific_ files before you submit it (e.g. your third 18.100 pset should not be part of the request). In addition, it would be wonderful if you rebased these files out of history.

License
-------

This software is licensed, appropriately enough, under the MIT License. For the full text of the license, see the `LICENSE` file. You should have received this file with the software.

TL;DR, do what you want with this software. If it can help you, either for it's original purpose or as an example, I'm glad.
