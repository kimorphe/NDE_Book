all: fdm.pdf saft.pdf
saft.pdf: saft.dvi
	dvipdfmx -p a4 saft.dvi
saft.dvi: saft.tex
	platex saft.tex

fdm.pdf: fdm.dvi
	dvipdfmx -p a4 fdm.dvi
fdm.dvi: fdm.tex fig1.eps fig2.eps
	#fig2ans.eps fig3ans.eps
	platex fdm.tex
fig1.eps: Figs/fig1.svgz
	inkscape -z -f Figs/fig1.svgz -E Figs/fig1.eps 
fig2.eps: Figs/fig2.svgz
	inkscape -z -f Figs/fig2.svgz -E Figs/fig2.eps 


