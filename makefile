all: fdm.pdf saft.pdf
saft.pdf: saft.dvi
	dvipdfmx -p a4 saft.dvi
saft.dvi: saft.tex setup.eps Evald.eps pulse_echo.eps
	platex saft.tex

fdm.pdf: fdm.dvi
	dvipdfmx -p a4 fdm.dvi
fdm.dvi: fdm.tex fig1.eps fig2.eps fig1.pdf
	#fig2ans.eps fig3ans.eps
	platex fdm.tex
fig1.eps: Figs/fig1.svgz
	inkscape -z -f Figs/fig1.svgz -E Figs/fig1.eps 
fig1.pdf: Figs/fig1.svgz
	inkscape Figs/fig1.svgz --export-pdf=Figs/fig1.pdf --export-text-to-path
fig2.eps: Figs/fig2.svgz
	inkscape -z -f Figs/fig2.svgz -E Figs/fig2.eps 

setup.eps: Figs/setup.svgz
	inkscape -z -f Figs/setup.svgz -E Figs/setup.eps 
Evald.eps: Figs/Evald.svgz
	inkscape -z -f Figs/Evald.svgz -E Figs/Evald.eps 
pulse_echo.eps: Figs/pulse_echo.svgz
	inkscape -z -f Figs/pulse_echo.svgz -E Figs/pulse_echo.eps 


