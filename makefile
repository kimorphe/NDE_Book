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
fdm.dvi: fdm.tex Figs/fig1.pdf Figs/fig2.pdf 
	platex fdm.tex
Figs/fig1.pdf: Figs/fig1.svgz
	inkscape Figs/fig1.svgz --export-pdf=Figs/fig1.pdf --export-text-to-path
Figs/fig2.pdf: Figs/fig2.svgz
	inkscape Figs/fig2.svgz --export-pdf=Figs/fig2.pdf --export-text-to-path

Figs/measurement.pdf: Figs/measurement.svgz
	#inkscape -z -f Figs/measurement.svgz -E Figs/measurement.eps 
	inkscape Figs/measurement.svgz --export-pdf=Figs/measurement.pdf -D --export-text-to-path
Figs/cloud.pdf: Figs/cloud.svgz
	inkscape Figs/cloud.svgz --export-pdf=Figs/cloud.pdf -D --export-text-to-path
Figs/wvfm2.pdf: Figs/wvfm2.svgz
	inkscape Figs/wvfm2.svgz --export-pdf=Figs/wvfm2.pdf -D --export-text-to-path
Figs/locii.pdf: Figs/locii.svgz
	inkscape Figs/locii.svgz --export-pdf=Figs/locii.pdf -D --export-text-to-path
Figs/saftM2.pdf: Figs/saftM2.svgz
	inkscape Figs/saftM2.svgz --export-pdf=Figs/saftM2.pdf -D --export-text-to-path
Figs/blind_sum.pdf: Figs/blind_sum.svgz
	inkscape Figs/blind_sum.svgz --export-pdf=Figs/blind_sum.pdf -D --export-text-to-path
Figs/psf_pulse.pdf: Figs/psf_pulse.svgz
	inkscape Figs/psf_pulse.svgz --export-pdf=Figs/psf_pulse.pdf -D --export-text-to-path
Figs/psf_profile.pdf: Figs/psf_profile.svgz
	inkscape Figs/psf_profile.svgz --export-pdf=Figs/psf_profile.pdf -D --export-text-to-path
Figs/psf_aptlim.pdf: Figs/psf_aptlim.svgz
	inkscape Figs/psf_aptlim.svgz --export-pdf=Figs/psf_aptlim.pdf -D --export-text-to-path
Figs/psf_cont.pdf: Figs/psf_cont.svgz
	inkscape Figs/psf_cont.svgz --export-pdf=Figs/psf_cont.pdf -D --export-text-to-path
Figs/psf_profile_cont.pdf: Figs/psf_profile_cont.svgz
	inkscape Figs/psf_profile_cont.svgz --export-pdf=Figs/psf_profile_cont.pdf -D --export-text-to-path
Figs/psf_cont_delay.pdf: Figs/psf_cont_delay.svgz
	inkscape Figs/psf_cont_delay.svgz --export-pdf=Figs/psf_cont_delay.pdf -D --export-text-to-path
Figs/1D_prb.pdf: Figs/1D_prb.svgz
	inkscape Figs/1D_prb.svgz --export-pdf=Figs/1D_prb.pdf -D --export-text-to-path
Figs/setup.pdf: Figs/setup.svgz
	inkscape Figs/setup.svgz --export-pdf=Figs/setup.pdf -D --export-text-to-path
Figs/Evald.pdf: Figs/Evald.svgz
	inkscape Figs/Evald.svgz --export-pdf=Figs/Evald.pdf -D --export-text-to-path
Figs/pulse_echo.pdf: Figs/pulse_echo.svgz
	inkscape Figs/pulse_echo.svgz --export-pdf=Figs/pulse_echo.pdf -D --export-text-to-path


