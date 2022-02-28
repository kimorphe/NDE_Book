all: fdm.pdf saft.pdf
saft.pdf: saft.dvi
	dvipdfmx -p a4 saft.dvi
saft.dvi: saft.tex\
       	Figs/measurement.eps Figs/cloud.eps Figs/wvfm2.eps Figs/locii.eps\
       	Figs/saftM2.eps Figs/psf_pulse.eps Figs/1D_prb.eps Figs/setup.eps\
       	Figs/Evald.eps Figs/pulse_echo.eps Figs/blind_sum.eps Figs/psf_aptlim.eps\
       	Figs/psf_profile.eps Figs/psf_cont.eps Figs/psf_profile_cont.eps Figs/psf_cont_delay.eps
	platex saft.tex

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

Figs/measurement.eps: Figs/measurement.svgz
	inkscape -z -f Figs/measurement.svgz -E Figs/measurement.eps 
Figs/cloud.eps: Figs/cloud.svgz
	inkscape -z -f Figs/cloud.svgz -E Figs/cloud.eps 
Figs/wvfm2.eps: Figs/wvfm2.svgz
	inkscape -z -f Figs/wvfm2.svgz -E Figs/wvfm2.eps 
Figs/locii.eps: Figs/locii.svgz
	inkscape -z -f Figs/locii.svgz -E Figs/locii.eps 
Figs/saftM2.eps: Figs/saftM2.svgz
	inkscape -z -f Figs/saftM2.svgz -E Figs/saftM2.eps 
Figs/blind_sum.eps: Figs/blind_sum.svgz
	inkscape -z -f Figs/blind_sum.svgz -E Figs/blind_sum.eps 
Figs/psf_pulse.eps: Figs/psf_pulse.svgz
	inkscape -z -f Figs/psf_pulse.svgz -E Figs/psf_pulse.eps 
Figs/psf_profile.eps: Figs/psf_profile.svgz
	inkscape -z -f Figs/psf_profile.svgz -E Figs/psf_profile.eps 
Figs/psf_aptlim.eps: Figs/psf_aptlim.svgz
	inkscape -z -f Figs/psf_aptlim.svgz -E Figs/psf_aptlim.eps 
Figs/psf_cont.eps: Figs/psf_cont.svgz
	inkscape -z -f Figs/psf_cont.svgz -E Figs/psf_cont.eps 
Figs/psf_profile_cont.eps: Figs/psf_profile_cont.svgz
	inkscape -z -f Figs/psf_profile_cont.svgz -E Figs/psf_profile_cont.eps 
Figs/psf_cont_delay.eps: Figs/psf_cont_delay.svgz
	inkscape -z -f Figs/psf_cont_delay.svgz -E Figs/psf_cont_delay.eps 
Figs/1D_prb.eps: Figs/1D_prb.svgz
	inkscape -z -f Figs/1D_prb.svgz -E Figs/1D_prb.eps 
Figs/setup.eps: Figs/setup.svgz
	inkscape -z -f Figs/setup.svgz -E Figs/setup.eps 
Figs/Evald.eps: Figs/Evald.svgz
	inkscape -z -f Figs/Evald.svgz -E Figs/Evald.eps 
Figs/pulse_echo.eps: Figs/pulse_echo.svgz
	inkscape -z -f Figs/pulse_echo.svgz -E Figs/pulse_echo.eps 


