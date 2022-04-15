all: fdm.pdf wavebook.pdf
wavebook.pdf: wavebook.dvi
	dvipdfmx -p a4 wavebook.dvi
wavebook.dvi: wavebook.tex saft.tex adj.tex poffis.tex\
       	Figs/measurement.pdf Figs/cloud.pdf Figs/wvfm2.pdf Figs/locii.pdf\
       	Figs/saftM2.pdf Figs/psf_pulse.pdf Figs/1D_prb.pdf Figs/setup.pdf\
       	Figs/Evald.pdf Figs/pulse_echo.pdf Figs/blind_sum.pdf Figs/psf_aptlim.pdf\
       	Figs/psf_profile.pdf Figs/psf_cont.pdf Figs/psf_profile_cont.pdf Figs/psf_cont_delay.pdf
	uplatex wavebook.tex

fdm.pdf: fdm.dvi
	dvipdfmx -p a4 fdm.dvi
fdm.dvi: fdm.tex Figs/fig1.eps Figs/fig2.eps Figs/fig1.pdf
	platex fdm.tex
Figs/fig1.eps: Figs/fig1.svgz
	inkscape -z -f Figs/fig1.svgz -E Figs/fig1.eps 
Figs/fig1.pdf: Figs/fig1.svgz
	inkscape Figs/fig1.svgz --export-pdf=Figs/fig1.pdf --export-text-to-path
Figs/fig2.eps: Figs/fig2.svgz
	inkscape -z -f Figs/fig2.svgz -E Figs/fig2.eps 

#Figs/measurement.eps: Figs/measurement.svgz
Figs/measurement.pdf: Figs/measurement.svgz
	#inkscape -z -f Figs/measurement.svgz -E Figs/measurement.eps 
	inkscape Figs/measurement.svgz --export-pdf=Figs/measurement.pdf -D --export-text-to-path
Figs/cloud.pdf: Figs/cloud.svgz
	#inkscape -z -f Figs/cloud.svgz -E Figs/cloud.eps 
	inkscape Figs/cloud.svgz --export-pdf=Figs/cloud.pdf -D --export-text-to-path
Figs/wvfm2.pdf: Figs/wvfm2.svgz
	#inkscape -z -f Figs/wvfm2.svgz -E Figs/wvfm2.eps 
	inkscape Figs/wvfm2.svgz --export-pdf=Figs/wvfm2.pdf -D --export-text-to-path
Figs/locii.pdf: Figs/locii.svgz
	#inkscape -z -f Figs/locii.svgz -E Figs/locii.eps 
	inkscape Figs/locii.svgz --export-pdf=Figs/locii.pdf -D --export-text-to-path
Figs/saftM2.pdf: Figs/saftM2.svgz
	#inkscape -z -f Figs/saftM2.svgz -E Figs/saftM2.eps 
	inkscape Figs/saftM2.svgz --export-pdf=Figs/saftM2.pdf -D --export-text-to-path

Figs/blind_sum.pdf: Figs/blind_sum.svgz
	#inkscape -z -f Figs/blind_sum.svgz -E Figs/blind_sum.eps 
	inkscape Figs/blind_sum.svgz --export-pdf=Figs/blind_sum.pdf -D --export-text-to-path
Figs/psf_pulse.pdf: Figs/psf_pulse.svgz
	#inkscape -z -f Figs/psf_pulse.svgz -E Figs/psf_pulse.eps 
	inkscape Figs/psf_pulse.svgz --export-pdf=Figs/psf_pulse.pdf -D --export-text-to-path
Figs/psf_profile.pdf: Figs/psf_profile.svgz
	#inkscape -z -f Figs/psf_profile.svgz -E Figs/psf_profile.eps 
	inkscape Figs/psf_profile.svgz --export-pdf=Figs/psf_profile.pdf -D --export-text-to-path
Figs/psf_aptlim.pdf: Figs/psf_aptlim.svgz
	#inkscape -z -f Figs/psf_aptlim.svgz -E Figs/psf_aptlim.eps 
	inkscape Figs/psf_aptlim.svgz --export-pdf=Figs/psf_aptlim.pdf -D --export-text-to-path
Figs/psf_cont.pdf: Figs/psf_cont.svgz
	#inkscape -z -f Figs/psf_cont.svgz -E Figs/psf_cont.eps 
	inkscape Figs/psf_cont.svgz --export-pdf=Figs/psf_cont.pdf -D --export-text-to-path
Figs/psf_profile_cont.pdf: Figs/psf_profile_cont.svgz
	#inkscape -z -f Figs/psf_profile_cont.svgz -E Figs/psf_profile_cont.eps 
	inkscape Figs/psf_profile_cont.svgz --export-pdf=Figs/psf_profile_cont.pdf -D --export-text-to-path
Figs/psf_cont_delay.pdf: Figs/psf_cont_delay.svgz
	#inkscape -z -f Figs/psf_cont_delay.svgz -E Figs/psf_cont_delay.eps 
	inkscape Figs/psf_cont_delay.svgz --export-pdf=Figs/psf_cont_delay.pdf -D --export-text-to-path
Figs/1D_prb.pdf: Figs/1D_prb.svgz
	#inkscape -z -f Figs/1D_prb.svgz -E Figs/1D_prb.eps 
	inkscape Figs/1D_prb.svgz --export-pdf=Figs/1D_prb.pdf -D --export-text-to-path
Figs/setup.pdf: Figs/setup.svgz
	#inkscape -z -f Figs/setup.svgz -E Figs/setup.eps 
	inkscape Figs/setup.svgz --export-pdf=Figs/setup.pdf -D --export-text-to-path
Figs/Evald.pdf: Figs/Evald.svgz
	#inkscape -z -f Figs/Evald.svgz -E Figs/Evald.eps 
	inkscape Figs/Evald.svgz --export-pdf=Figs/Evald.pdf -D --export-text-to-path
Figs/pulse_echo.pdf: Figs/pulse_echo.svgz
	#inkscape -z -f Figs/pulse_echo.svgz -E Figs/pulse_echo.eps 
	inkscape Figs/pulse_echo.svgz --export-pdf=Figs/pulse_echo.pdf -D --export-text-to-path


