%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/arabi.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/arabi.doc.tar.xz

Name: texlive-arabi
License: LPPL
Summary: (La)TeX support for Arabic and Farsi, compliant with Babel
Version: %{tl_version}
Release: %{tl_noarch_release}.1.1.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(PPRarabic.sty)
Provides: tex(arabic.sty)
Provides: tex(arabicfnt.sty)
Provides: tex(arabicore.sty)
Provides: tex(arabiftoday.sty)
Provides: tex(arabnovowel.sty)
Provides: tex(arfonts.sty)
Provides: tex(ARfonts.sty)
Provides: tex(calendrierfpar.sty)
Provides: tex(calendrierfpmodified.sty)
Provides: tex(farsi.sty)
Provides: tex(farsifnt.sty)
Provides: tex(fmultico.sty)
Provides: tex(fnum.sty)
Provides: tex(frfonts.sty)
Provides: tex(FRfonts.sty)
Provides: tex(haparabica.sty)
Provides: tex(HAPArabica.sty)
Provides: tex(lagally.sty)
Provides: tex(poetry.sty)
Provides: tex(translit.sty)
Requires: tex(amssymb.sty)
Requires: tex(inputenc.sty)
Requires: tex(ifthen.sty)
Requires: tex(pstricks.sty)
Requires: tex(pst-3d.sty)
Requires: tex(multido.sty)
Requires: tex(fp.sty)
Requires: tex(pst-key.sty)
Requires: tex(babel.sty)
Requires: tex(pst-grad.sty)
Requires: tex(pifont.sty)
Requires: texlive-arabi-fedora-fonts = %{tl_version}

%description
The package provides the Arabic and Farsi script support for
TeX without the need of any external pre-processor. The bi-
directional capability supposes that the user has a TeX engine
that knows the four primitives \beginR, \endR, \beginL and
\endL. That is the case in both the TeX--XeT and e-TeX engines.
Arabi will accept input in several 8-bit encodings, including
UTF-8. Arabi can make use of a wide variety of Arabic and Farsi
fonts; PDF files generated using Arabi may be searched, and
text may be copied from them and pasted elsewhere.

date: 2007-02-23 23:22:37 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map arabi.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map arabi.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  %{_bindir}/texhash 2> /dev/null
  %{_bindir}/updmap-sys --nohash --quiet &> /dev/null
else
  mkdir -p /var/run/texlive
  touch /var/run/texlive/run-texhash
  touch /var/run/texlive/run-updmap
fi
:

%posttrans
[ -e /var/run/texlive/run-texhash ] && %{_bindir}/texhash 2> /dev/null && rm -f /var/run/texlive/run-texhash
[ -e /var/run/texlive/run-updmap ] && %{_bindir}/updmap-sys --nohash --quiet &> /dev/null && rm -f /var/run/texlive/run-updmap
[ -e /var/run/texlive ] && rm -rf /var/run/texlive
:

%package doc
Summary: Documentation for arabi
Version: %{tl_version}
Release: %{tl_noarch_release}.1.1.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for arabi

%package fedora-fonts
Summary: Fonts for arabi
Version: %{tl_version}
Release: %{tl_noarch_release}.1.1.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-arabi = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The package provides the Arabic and Farsi script support for
TeX without the need of any external pre-processor. The bi-
directional capability supposes that the user has a TeX engine
that knows the four primitives \beginR, \endR, \beginL and
\endL. That is the case in both the TeX--XeT and e-TeX engines.
Arabi will accept input in several 8-bit encodings, including
UTF-8. Arabi can make use of a wide variety of Arabic and Farsi
fonts; PDF files generated using Arabi may be searched, and
text may be copied from them and pasted elsewhere.

date: 2007-02-23 23:22:37 +0100


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lppl.txt lppl.txt
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}/texmf-dist
xz -dc %{SOURCE1} | tar x -C %{buildroot}%{_texdir}/texmf-dist
# nuke useless tlmgr packaging stuff and doc droppings
rm -rf %{buildroot}%{_texdir}/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf-dist/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/*.pdf
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/info/dir

# link installed fonts with Fedora
install -d -m 0755 %{buildroot}%{_fontdir}
pushd %{buildroot}%{_fontdir}
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_albattar.pfb .
ln -s %{_fontdir}/ae_albattar.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_albattar.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almateen.pfb .
ln -s %{_fontdir}/ae_almateen.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almateen.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almohanad_bold.pfb .
ln -s %{_fontdir}/ae_almohanad_bold.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almohanad_bold.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almohanad_boldItalitalic.pfb .
ln -s %{_fontdir}/ae_almohanad_boldItalitalic.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almohanad_boldItalitalic.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almohanad_thin.pfb .
ln -s %{_fontdir}/ae_almohanad_thin.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almohanad_thin.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almohanad_xxbold.pfb .
ln -s %{_fontdir}/ae_almohanad_xxbold.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almohanad_xxbold.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almothnna.pfb .
ln -s %{_fontdir}/ae_almothnna.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almothnna.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_alyermook.pfb .
ln -s %{_fontdir}/ae_alyermook.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_alyermook.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_arab.pfb .
ln -s %{_fontdir}/ae_arab.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_arab.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_cortoba.pfb .
ln -s %{_fontdir}/ae_cortoba.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_cortoba.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_dimnah.pfb .
ln -s %{_fontdir}/ae_dimnah.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_dimnah.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_furat.pfb .
ln -s %{_fontdir}/ae_furat.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_furat.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_granada.pfb .
ln -s %{_fontdir}/ae_granada.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_granada.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_graph.pfb .
ln -s %{_fontdir}/ae_graph.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_graph.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_hani.pfb .
ln -s %{_fontdir}/ae_hani.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_hani.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_hor.pfb .
ln -s %{_fontdir}/ae_hor.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_hor.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_kayrawan.pfb .
ln -s %{_fontdir}/ae_kayrawan.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_kayrawan.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_khalid.pfb .
ln -s %{_fontdir}/ae_khalid.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_khalid.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_mashq.pfb .
ln -s %{_fontdir}/ae_mashq.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_mashq.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_metal.pfb .
ln -s %{_fontdir}/ae_metal.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_metal.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_nada.pfb .
ln -s %{_fontdir}/ae_nada.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_nada.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_nagham.pfb .
ln -s %{_fontdir}/ae_nagham.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_nagham.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_nice.pfb .
ln -s %{_fontdir}/ae_nice.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_nice.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_ostorah.pfb .
ln -s %{_fontdir}/ae_ostorah.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_ostorah.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_ouhod.pfb .
ln -s %{_fontdir}/ae_ouhod.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_ouhod.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_petra.pfb .
ln -s %{_fontdir}/ae_petra.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_petra.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_rehan.pfb .
ln -s %{_fontdir}/ae_rehan.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_rehan.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_salem.pfb .
ln -s %{_fontdir}/ae_salem.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_salem.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_shado.pfb .
ln -s %{_fontdir}/ae_shado.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_shado.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_sharjah.pfb .
ln -s %{_fontdir}/ae_sharjah.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_sharjah.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_sindibad.pfb .
ln -s %{_fontdir}/ae_sindibad.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_sindibad.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_tarablus.pfb .
ln -s %{_fontdir}/ae_tarablus.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_tarablus.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_tholoth.pfb .
ln -s %{_fontdir}/ae_tholoth.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_tholoth.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/farsiweb/homa.pfb .
ln -s %{_fontdir}/homa.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/farsiweb/homa.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/farsiweb/nazli.pfb .
ln -s %{_fontdir}/nazli.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/farsiweb/nazli.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/farsiweb/nazlib.pfb .
ln -s %{_fontdir}/nazlib.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/farsiweb/nazlib.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/farsiweb/titr.pfb .
ln -s %{_fontdir}/titr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/farsiweb/titr.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/afm/arabi/arabeyes/ae_almohanad_boldItalitalic.afm
%{_texdir}/texmf-dist/fonts/afm/arabi/arabeyes/ae_almohanad_thin.afm
%{_texdir}/texmf-dist/fonts/afm/arabi/arabeyes/ae_almohanad_xxbold.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/arabi/ararabeyes.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/arabi/ardtpnaskh.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/arabi/ardtpthuluth.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/arabi/armonotype.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/arabi/aromega.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/arabi/arsimplified.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/arabi/arunicode.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/arabi/farsitex.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/arabi/farsiwebencoding.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/arabi/frmonotype.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/arabi/frsimple.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/arabi/frsimplified.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/arabi/frunicode.enc
%{_texdir}/texmf-dist/fonts/map/dvips/arabi/arabi.map
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/ae_almohanad_xxbold.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/ae_alyermook.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/ae_arab.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/ae_tholoth.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aealbattar.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aealmateen.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aealmohanadb.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aealmohanadbolditalic.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aealmothnna.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aealyermook.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aearab.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aecortoba.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aedimnah.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aefurat.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aegranada.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aegraph.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aehani.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aehor.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aekayrawan.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aekhalid.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aemashq.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aemetal.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aenada.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aenagham.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aenice.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aeostorah.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aeouhod.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aepetra.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aerehan.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aesalem.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aeshado.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aesharjah.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aesindibad.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aetarablus.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes/aetholoth.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/farsiweb/homa.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/farsiweb/nazli.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/farsiweb/nazlib.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/farsiweb/nazlibout.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/farsiweb/nazliout.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/farsiweb/titr.tfm
%{_texdir}/texmf-dist/fonts/tfm/arabi/farsiweb/titrout.tfm
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_albattar.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almateen.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almohanad_bold.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almohanad_boldItalitalic.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almohanad_thin.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almohanad_xxbold.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almothnna.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_alyermook.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_arab.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_cortoba.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_dimnah.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_furat.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_granada.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_graph.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_hani.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_hor.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_kayrawan.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_khalid.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_mashq.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_metal.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_nada.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_nagham.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_nice.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_ostorah.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_ouhod.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_petra.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_rehan.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_salem.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_shado.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_sharjah.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_sindibad.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_tarablus.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_tholoth.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/farsiweb/homa.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/farsiweb/nazli.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/farsiweb/nazlib.pfb
%{_texdir}/texmf-dist/fonts/type1/arabi/farsiweb/titr.pfb
%{_texdir}/texmf-dist/tex/latex/arabi/8859-6.def
%{_texdir}/texmf-dist/tex/latex/arabi/PPRarabic.sty
%{_texdir}/texmf-dist/tex/latex/arabi/arabi4ht.cfg
%{_texdir}/texmf-dist/tex/latex/arabi/arabic.cfg
%{_texdir}/texmf-dist/tex/latex/arabi/arabic.ldf
%{_texdir}/texmf-dist/tex/latex/arabi/arabicfnt.sty
%{_texdir}/texmf-dist/tex/latex/arabi/arabicore.sty
%{_texdir}/texmf-dist/tex/latex/arabi/arabiftoday.sty
%{_texdir}/texmf-dist/tex/latex/arabi/arabnovowel.sty
%{_texdir}/texmf-dist/tex/latex/arabi/arfonts.sty
%{_texdir}/texmf-dist/tex/latex/arabi/calendrierfpar.sty
%{_texdir}/texmf-dist/tex/latex/arabi/calendrierfpmodified.sty
%{_texdir}/texmf-dist/tex/latex/arabi/cp1256.def
%{_texdir}/texmf-dist/tex/latex/arabi/farsi.ldf
%{_texdir}/texmf-dist/tex/latex/arabi/farsifnt.sty
%{_texdir}/texmf-dist/tex/latex/arabi/fmultico.sty
%{_texdir}/texmf-dist/tex/latex/arabi/fnum.sty
%{_texdir}/texmf-dist/tex/latex/arabi/frfonts.sty
%{_texdir}/texmf-dist/tex/latex/arabi/haparabica.sty
%{_texdir}/texmf-dist/tex/latex/arabi/laeaealbattar.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaealmateen.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaealmohanadb.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaealmothnna.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaealyermook.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaearab.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaecortoba.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaedimnah.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaefurat.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaegranada.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaegraph.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaehani.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaehor.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaekayrawan.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaekhalid.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaemashq.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaemetal.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaenada.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaenagham.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaenice.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaeostorah.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaeouhod.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaepetra.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaerehan.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaesalem.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaeshado.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaesharjah.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaesindibad.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaetarablus.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeaetholoth.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeandlso.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeararial.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laearcour.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laearomega.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laearsimpo.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeartimes.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeasv.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laecmr.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laecmss.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laecmtt.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laedthuluth.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laedtpn.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laedtpnsp.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laeenc.def
%{_texdir}/texmf-dist/tex/latex/arabi/laeenc.dfu
%{_texdir}/texmf-dist/tex/latex/arabi/laekacstbook.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laemaghribi.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laenaskhi.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laereqaa.fd
%{_texdir}/texmf-dist/tex/latex/arabi/laetraditionalarabic.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lagally.sty
%{_texdir}/texmf-dist/tex/latex/arabi/lfecmr.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lfecmss.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lfecmtt.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lfeelham.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lfeenc.def
%{_texdir}/texmf-dist/tex/latex/arabi/lfefandlso.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lfefarsismpl.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lfefrarial.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lfefrtimes.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lfeftraditionalarabic.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lfehoma.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lfekoodak.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lfenazli.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lfenazliout.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lferoya.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lfesmplarabic.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lfeterafik.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lfetitr.fd
%{_texdir}/texmf-dist/tex/latex/arabi/lfetitrout.fd
%{_texdir}/texmf-dist/tex/latex/arabi/mosq.def
%{_texdir}/texmf-dist/tex/latex/arabi/poetry.sty
%{_texdir}/texmf-dist/tex/latex/arabi/puenc-ar.def
%{_texdir}/texmf-dist/tex/latex/arabi/transcmr.fd
%{_texdir}/texmf-dist/tex/latex/arabi/translit.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/arabi/README
%{_texdir}/texmf-dist/doc/latex/arabi/bblopts.cfg
%{_texdir}/texmf-dist/doc/latex/arabi/big2.pdf
%{_texdir}/texmf-dist/doc/latex/arabi/big2.tex
%{_texdir}/texmf-dist/doc/latex/arabi/fontchart_arabic.pdf
%{_texdir}/texmf-dist/doc/latex/arabi/fontchart_farsi.pdf
%{_texdir}/texmf-dist/doc/latex/arabi/lion.pdf
%{_texdir}/texmf-dist/doc/latex/arabi/lppl.tex
%{_texdir}/texmf-dist/doc/latex/arabi/samplebook.css
%{_texdir}/texmf-dist/doc/latex/arabi/samplebook.html
%{_texdir}/texmf-dist/doc/latex/arabi/samplebook.pdf
%{_texdir}/texmf-dist/doc/latex/arabi/samplebook.tex
%{_texdir}/texmf-dist/doc/latex/arabi/test_beamer.pdf
%{_texdir}/texmf-dist/doc/latex/arabi/testplaintex.pdf
%{_texdir}/texmf-dist/doc/latex/arabi/testplaintex.tex
%{_texdir}/texmf-dist/doc/latex/arabi/user_guide.pdf

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/ae_albattar.pfb
%{_fontdir}/ae_almateen.pfb
%{_fontdir}/ae_almohanad_bold.pfb
%{_fontdir}/ae_almohanad_boldItalitalic.pfb
%{_fontdir}/ae_almohanad_thin.pfb
%{_fontdir}/ae_almohanad_xxbold.pfb
%{_fontdir}/ae_almothnna.pfb
%{_fontdir}/ae_alyermook.pfb
%{_fontdir}/ae_arab.pfb
%{_fontdir}/ae_cortoba.pfb
%{_fontdir}/ae_dimnah.pfb
%{_fontdir}/ae_furat.pfb
%{_fontdir}/ae_granada.pfb
%{_fontdir}/ae_graph.pfb
%{_fontdir}/ae_hani.pfb
%{_fontdir}/ae_hor.pfb
%{_fontdir}/ae_kayrawan.pfb
%{_fontdir}/ae_khalid.pfb
%{_fontdir}/ae_mashq.pfb
%{_fontdir}/ae_metal.pfb
%{_fontdir}/ae_nada.pfb
%{_fontdir}/ae_nagham.pfb
%{_fontdir}/ae_nice.pfb
%{_fontdir}/ae_ostorah.pfb
%{_fontdir}/ae_ouhod.pfb
%{_fontdir}/ae_petra.pfb
%{_fontdir}/ae_rehan.pfb
%{_fontdir}/ae_salem.pfb
%{_fontdir}/ae_shado.pfb
%{_fontdir}/ae_sharjah.pfb
%{_fontdir}/ae_sindibad.pfb
%{_fontdir}/ae_tarablus.pfb
%{_fontdir}/ae_tholoth.pfb
%{_fontdir}/homa.pfb
%{_fontdir}/nazli.pfb
%{_fontdir}/nazlib.pfb
%{_fontdir}/titr.pfb

%changelog
* Mon Aug 23 2010 Jindrich Novy <jnovy@redhat.com> 2010-9
- rpmlint fixes

* Sat Jul 17 2010 Jindrich Novy <jnovy@redhat.com> 2010-8
- depend on the new texlive-base noarch package
- ship licenses with documentation
- sync with upstream

* Mon May 31 2010 Jindrich Novy <jnovy@redhat.com> 2010-7
- switch to "tlpretest" source tree
- add lua and ruby dependencies to packages requiring them
- generate global package database "texlive.tlpdb" directly from
tlpobj files shipped with each package

* Wed May 19 2010 Jindrich Novy <jnovy@redhat.com> 2010-6
- update to the latest frozen development TeX Live
- add svn to noarch versions according to guildelines

* Fri Apr 30 2010 Jindrich Novy <jnovy@redhat.com> 2010-5
- add dependencies resolution among biblatex files
- another %%postun scriplets fix

* Wed Apr 21 2010 Jindrich Novy <jnovy@redhat.com> 2010-4
- fix and tighten dependencies in %%post* scriptlets
- extract dependencies also from .cls and .ldf files
- speed up build by skipping some bits in __os_install_post

* Mon Apr 19 2010 Jindrich Novy <jnovy@redhat.com> 2010-3
- speed up installation/updating by running updmap/fmtutil
and texhash post-transaction once

* Sat Apr 03 2010 Jindrich Novy <jnovy@redhat.com> 2010-0.1
- bump version to 2010
- reduce total number of packages from 3580 to 3440 by removal
of dummy ones not shipping actually anything
- add style dependencies from packages reecently added
(were previously blacklisted)
- do not ship koma-script sources

* Tue Nov 10 2009 Jindrich Novy <jnovy@redhat.com> 2009-4
- info and man pages are now part of main packages, not -doc
- use fedora-compliant license codes for License in spec
- fix fedora-fonts packages generation
- add dummy description if packages misses any
- package bdf fonts

* Tue Nov 10 2009 Jindrich Novy <jnovy@redhat.com> 2009-2
- install man and info pages into proper locations visible
by man and info
- update scriptlets
- remove xindy bits

* Mon Nov 09 2009 Jindrich Novy <jnovy@redhat.com> 2009-1
- official TeX Live 2009 release

* Tue Aug 25 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.3
- make TeX Live TrueType and OpenType fonts accessible by
other Fedora apps

* Thu Aug 20 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.2
- don't package generated pdfs from man pages

* Wed Aug 12 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.1
- initial packaging for TeX Live 2009
