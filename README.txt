This is the Python 3 implementation of Andre Brown's behavioral syntax code: https://github.com/aexbrown/Behavioural_Syntax

I have three grades that I will give to the code:
a) 50%: started but unfinished
b) 80%: mostly finished
c) 100%: runs as expected and is easy to read

The following have been very useful resources:
1) http://mathesaurus.sourceforge.net/matlab-numpy.html
2) http://www.cert.org/flocon/2011/matlab-python-xref.pdf

I now have access to a Python interpreter as I managed to borrow a laptop from the university. (My laptop's screen broke)

These Python programs are for discretizing worm behaviour using a series of template postures and then using the posture sequences to discover interesting patterns of behaviour and for comparing worm strains to each other.  Details can be found in the following manuscript (please cite it if you use any of this code for a publication):

Roland F. Schwarz, Robyn Branicky, Laura J. Grundy, William R. Schafer, André E.X. Brown (2015) Changes in postural syntax characterize sensory modulation and natural variation of C. elegans locomotion. PLOS Computational Biology, accepted.
Preprint: http://dx.doi.org/10.1101/017707

The 'demo' subfolder contains scripts organised by figure.  Running these scripts should reproduce most the figures of the paper (up to differences based on random numbers used in the code).  Some pre-processing is required (for example, to extract angle arrays from the feature data and to convert these angle arrays to state sequences using template postures).  There are scripts for these tasks included in the repository.

The data used in this paper are mostly available from this ftp site:
ftp://ftp.mrc-lmb.cam.ac.uk/pub/tjucikas/wormdatabase/results-12-06-08/Laura Grundy/

Please e-mail me for any data not available from that address.  We are still (slowly) working to make an improved database that will include original videos for re-analysis.

If you find any bugs or have any questions, please e-mail me at andre.brown@csc.mrc.ac.uk or aexbrown@gmail.com.


The MIT License

Copyright (c)  Medical Research Council 2015

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
