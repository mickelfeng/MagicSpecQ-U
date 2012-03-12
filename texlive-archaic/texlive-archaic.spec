%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/archaic.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/archaic.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/archaic.source.tar.xz

Name: texlive-archaic
License: LPPL
Summary: A collection of archaic fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(aramaic.sty)
Provides: tex(cypriot.sty)
Provides: tex(etruscan.sty)
Provides: tex(greek4cbc.sty)
Provides: tex(greek6cbc.sty)
Provides: tex(hieroglf.sty)
Provides: tex(linearb.sty)
Provides: tex(nabatean.sty)
Provides: tex(oands.sty)
Provides: tex(oldprsn.sty)
Provides: tex(phoenician.sty)
Provides: tex(protosem.sty)
Provides: tex(runic.sty)
Provides: tex(sarabian.sty)
Provides: tex(ugarite.sty)
Provides: tex(viking.sty)
Requires: texlive-archaic-fedora-fonts = %{tl_version}

%description
The collection contains fonts to represent Aramaic, Cypriot,
Etruscan, Greek of the 6th and 4th centuries BCE, Egyptian
hieroglyphics, Linear A, Linear B, Nabatean old Persian, the
Phaistos disc, Phoenician, proto-Semitic, runic, South Arabian
Ugaritic and Viking scripts. The bundle also includes a small
font for use in phonetic transcription of the archaic writings.
The bundle's own directory includes a font installation map
file for the whole collection.

date: 2006-11-08 11:10:08 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map archaicprw.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map archaicprw.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for archaic
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for archaic

%package fedora-fonts
Summary: Fonts for archaic
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-archaic = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The collection contains fonts to represent Aramaic, Cypriot,
Etruscan, Greek of the 6th and 4th centuries BCE, Egyptian
hieroglyphics, Linear A, Linear B, Nabatean old Persian, the
Phaistos disc, Phoenician, proto-Semitic, runic, South Arabian
Ugaritic and Viking scripts. The bundle also includes a small
font for use in phonetic transcription of the archaic writings.
The bundle's own directory includes a font installation map
file for the whole collection.

date: 2006-11-08 11:10:08 +0100


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/aram10.pfb .
ln -s %{_fontdir}/aram10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/aram10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/copsn10.pfb .
ln -s %{_fontdir}/copsn10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/copsn10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/cugar10.pfb .
ln -s %{_fontdir}/cugar10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/cugar10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/cypr10.pfb .
ln -s %{_fontdir}/cypr10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/cypr10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/etr10.pfb .
ln -s %{_fontdir}/etr10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/etr10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/fut10.pfb .
ln -s %{_fontdir}/fut10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/fut10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/givbc10.pfb .
ln -s %{_fontdir}/givbc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/givbc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/gvibc10.pfb .
ln -s %{_fontdir}/gvibc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/gvibc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/linb10.pfb .
ln -s %{_fontdir}/linb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/linb10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/nab10.pfb .
ln -s %{_fontdir}/nab10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/nab10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/oandsi10.pfb .
ln -s %{_fontdir}/oandsi10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/oandsi10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/oandsu10.pfb .
ln -s %{_fontdir}/oandsu10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/oandsu10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/phnc10.pfb .
ln -s %{_fontdir}/phnc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/phnc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/pmhg.pfb .
ln -s %{_fontdir}/pmhg.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/pmhg.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/proto10.pfb .
ln -s %{_fontdir}/proto10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/proto10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/sarab10.pfb .
ln -s %{_fontdir}/sarab10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic/sarab10.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/afm/public/archaic/aram10.afm
%{_texdir}/texmf-dist/fonts/afm/public/archaic/copsn10.afm
%{_texdir}/texmf-dist/fonts/afm/public/archaic/cugar10.afm
%{_texdir}/texmf-dist/fonts/afm/public/archaic/cypr10.afm
%{_texdir}/texmf-dist/fonts/afm/public/archaic/etr10.afm
%{_texdir}/texmf-dist/fonts/afm/public/archaic/fut10.afm
%{_texdir}/texmf-dist/fonts/afm/public/archaic/givbc10.afm
%{_texdir}/texmf-dist/fonts/afm/public/archaic/gvibc10.afm
%{_texdir}/texmf-dist/fonts/afm/public/archaic/linb10.afm
%{_texdir}/texmf-dist/fonts/afm/public/archaic/nab10.afm
%{_texdir}/texmf-dist/fonts/afm/public/archaic/oandsi10.afm
%{_texdir}/texmf-dist/fonts/afm/public/archaic/oandsu10.afm
%{_texdir}/texmf-dist/fonts/afm/public/archaic/phnc10.afm
%{_texdir}/texmf-dist/fonts/afm/public/archaic/pmhg.afm
%{_texdir}/texmf-dist/fonts/afm/public/archaic/proto10.afm
%{_texdir}/texmf-dist/fonts/afm/public/archaic/sarab10.afm
%{_texdir}/texmf-dist/fonts/map/dvips/archaic/aramaic.map
%{_texdir}/texmf-dist/fonts/map/dvips/archaic/archaicprw.map
%{_texdir}/texmf-dist/fonts/map/dvips/archaic/cypriot.map
%{_texdir}/texmf-dist/fonts/map/dvips/archaic/etruscan.map
%{_texdir}/texmf-dist/fonts/map/dvips/archaic/fut10.map
%{_texdir}/texmf-dist/fonts/map/dvips/archaic/greek4cbc.map
%{_texdir}/texmf-dist/fonts/map/dvips/archaic/greek6cbc.map
%{_texdir}/texmf-dist/fonts/map/dvips/archaic/hieroglf.map
%{_texdir}/texmf-dist/fonts/map/dvips/archaic/linearb.map
%{_texdir}/texmf-dist/fonts/map/dvips/archaic/nabatean.map
%{_texdir}/texmf-dist/fonts/map/dvips/archaic/oands.map
%{_texdir}/texmf-dist/fonts/map/dvips/archaic/oldprsn.map
%{_texdir}/texmf-dist/fonts/map/dvips/archaic/phoenician.map
%{_texdir}/texmf-dist/fonts/map/dvips/archaic/protosem.map
%{_texdir}/texmf-dist/fonts/map/dvips/archaic/sarabian.map
%{_texdir}/texmf-dist/fonts/map/dvips/archaic/ugarite.map
%{_texdir}/texmf-dist/fonts/source/public/archaic/copsn10.mf
%{_texdir}/texmf-dist/fonts/source/public/archaic/givbc10.mf
%{_texdir}/texmf-dist/fonts/source/public/archaic/gvibc10.mf
%{_texdir}/texmf-dist/fonts/source/public/archaic/sarab10.mf
%{_texdir}/texmf-dist/fonts/source/public/archaic/vik10.mf
%{_texdir}/texmf-dist/fonts/source/public/archaic/vikglyph.mf
%{_texdir}/texmf-dist/fonts/source/public/archaic/viktitle.mf
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/aram10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/copsn10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/cugar10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/cypr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/etr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/fut10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/givbc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/gvibc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/linb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/nab10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/oandsi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/oandsu10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/phnc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/pmhg.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/proto10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/sarab10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/archaic/vik10.tfm
%{_texdir}/texmf-dist/fonts/type1/public/archaic/aram10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/archaic/copsn10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/archaic/cugar10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/archaic/cypr10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/archaic/etr10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/archaic/fut10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/archaic/givbc10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/archaic/gvibc10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/archaic/linb10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/archaic/nab10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/archaic/oandsi10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/archaic/oandsu10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/archaic/phnc10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/archaic/pmhg.pfb
%{_texdir}/texmf-dist/fonts/type1/public/archaic/proto10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/archaic/sarab10.pfb
%{_texdir}/texmf-dist/tex/latex/archaic/aramaic.sty
%{_texdir}/texmf-dist/tex/latex/archaic/cypriot.sty
%{_texdir}/texmf-dist/tex/latex/archaic/etruscan.sty
%{_texdir}/texmf-dist/tex/latex/archaic/greek4cbc.sty
%{_texdir}/texmf-dist/tex/latex/archaic/greek6cbc.sty
%{_texdir}/texmf-dist/tex/latex/archaic/hieroglf.sty
%{_texdir}/texmf-dist/tex/latex/archaic/linearb.sty
%{_texdir}/texmf-dist/tex/latex/archaic/nabatean.sty
%{_texdir}/texmf-dist/tex/latex/archaic/oands.sty
%{_texdir}/texmf-dist/tex/latex/archaic/oldprsn.sty
%{_texdir}/texmf-dist/tex/latex/archaic/ot1aram.fd
%{_texdir}/texmf-dist/tex/latex/archaic/ot1copsn.fd
%{_texdir}/texmf-dist/tex/latex/archaic/ot1cugar.fd
%{_texdir}/texmf-dist/tex/latex/archaic/ot1cypr.fd
%{_texdir}/texmf-dist/tex/latex/archaic/ot1etr.fd
%{_texdir}/texmf-dist/tex/latex/archaic/ot1fut.fd
%{_texdir}/texmf-dist/tex/latex/archaic/ot1givbc.fd
%{_texdir}/texmf-dist/tex/latex/archaic/ot1gvibc.fd
%{_texdir}/texmf-dist/tex/latex/archaic/ot1nab.fd
%{_texdir}/texmf-dist/tex/latex/archaic/ot1oands.fd
%{_texdir}/texmf-dist/tex/latex/archaic/ot1phnc.fd
%{_texdir}/texmf-dist/tex/latex/archaic/ot1pmhg.fd
%{_texdir}/texmf-dist/tex/latex/archaic/ot1proto.fd
%{_texdir}/texmf-dist/tex/latex/archaic/ot1sarab.fd
%{_texdir}/texmf-dist/tex/latex/archaic/ot1vik.fd
%{_texdir}/texmf-dist/tex/latex/archaic/phoenician.sty
%{_texdir}/texmf-dist/tex/latex/archaic/protosem.sty
%{_texdir}/texmf-dist/tex/latex/archaic/runic.sty
%{_texdir}/texmf-dist/tex/latex/archaic/sarabian.sty
%{_texdir}/texmf-dist/tex/latex/archaic/t1aram.fd
%{_texdir}/texmf-dist/tex/latex/archaic/t1copsn.fd
%{_texdir}/texmf-dist/tex/latex/archaic/t1cugar.fd
%{_texdir}/texmf-dist/tex/latex/archaic/t1cypr.fd
%{_texdir}/texmf-dist/tex/latex/archaic/t1etr.fd
%{_texdir}/texmf-dist/tex/latex/archaic/t1fut.fd
%{_texdir}/texmf-dist/tex/latex/archaic/t1givbc.fd
%{_texdir}/texmf-dist/tex/latex/archaic/t1gvibc.fd
%{_texdir}/texmf-dist/tex/latex/archaic/t1linb.fd
%{_texdir}/texmf-dist/tex/latex/archaic/t1nab.fd
%{_texdir}/texmf-dist/tex/latex/archaic/t1oands.fd
%{_texdir}/texmf-dist/tex/latex/archaic/t1phnc.fd
%{_texdir}/texmf-dist/tex/latex/archaic/t1pmhg.fd
%{_texdir}/texmf-dist/tex/latex/archaic/t1proto.fd
%{_texdir}/texmf-dist/tex/latex/archaic/t1sarab.fd
%{_texdir}/texmf-dist/tex/latex/archaic/t1vik.fd
%{_texdir}/texmf-dist/tex/latex/archaic/ugarite.sty
%{_texdir}/texmf-dist/tex/latex/archaic/viking.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/archaic/README.PRW
%{_texdir}/texmf-dist/doc/fonts/archaic/aramaic-README
%{_texdir}/texmf-dist/doc/fonts/archaic/aramaic.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/asamples.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/asamples.tex
%{_texdir}/texmf-dist/doc/fonts/archaic/cypriot-README
%{_texdir}/texmf-dist/doc/fonts/archaic/cypriot.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/etruscan-README
%{_texdir}/texmf-dist/doc/fonts/archaic/etruscan.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/greek4cbc-README
%{_texdir}/texmf-dist/doc/fonts/archaic/greek4cbc-trygivbc.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/greek4cbc-trygivbc.tex
%{_texdir}/texmf-dist/doc/fonts/archaic/greek4cbc.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/greek6cbc-README
%{_texdir}/texmf-dist/doc/fonts/archaic/greek6cbc-trygvibc.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/greek6cbc-trygvibc.tex
%{_texdir}/texmf-dist/doc/fonts/archaic/greek6cbc.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/hieroglf-README
%{_texdir}/texmf-dist/doc/fonts/archaic/hieroglf-trypmhg.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/hieroglf-trypmhg.tex
%{_texdir}/texmf-dist/doc/fonts/archaic/hieroglf.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/linearb-README
%{_texdir}/texmf-dist/doc/fonts/archaic/linearb.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/nabatean-README
%{_texdir}/texmf-dist/doc/fonts/archaic/nabatean.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/oands-README
%{_texdir}/texmf-dist/doc/fonts/archaic/oands.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/oldprsn-README
%{_texdir}/texmf-dist/doc/fonts/archaic/oldprsn.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/phoenician-README
%{_texdir}/texmf-dist/doc/fonts/archaic/phoenician-tryphnc.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/phoenician-tryphnc.tex
%{_texdir}/texmf-dist/doc/fonts/archaic/phoenician.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/protosem-README
%{_texdir}/texmf-dist/doc/fonts/archaic/protosem.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/runic-README
%{_texdir}/texmf-dist/doc/fonts/archaic/runic.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/sarabian-README
%{_texdir}/texmf-dist/doc/fonts/archaic/sarabian.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/tryaramaic.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/tryaramaic.tex
%{_texdir}/texmf-dist/doc/fonts/archaic/trycypriot.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/trycypriot.tex
%{_texdir}/texmf-dist/doc/fonts/archaic/tryetruscan.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/tryetruscan.tex
%{_texdir}/texmf-dist/doc/fonts/archaic/trylinearb.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/trylinearb.tex
%{_texdir}/texmf-dist/doc/fonts/archaic/trynabatean.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/trynabatean.tex
%{_texdir}/texmf-dist/doc/fonts/archaic/tryoands.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/tryoands.tex
%{_texdir}/texmf-dist/doc/fonts/archaic/tryoldprsn.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/tryoldprsn.tex
%{_texdir}/texmf-dist/doc/fonts/archaic/tryprotosem.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/tryprotosem.tex
%{_texdir}/texmf-dist/doc/fonts/archaic/tryrunic.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/tryrunic.tex
%{_texdir}/texmf-dist/doc/fonts/archaic/trysarabian.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/trysarabian.tex
%{_texdir}/texmf-dist/doc/fonts/archaic/tryugarite.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/tryugarite.tex
%{_texdir}/texmf-dist/doc/fonts/archaic/ugarite-README
%{_texdir}/texmf-dist/doc/fonts/archaic/ugarite.pdf
%{_texdir}/texmf-dist/doc/fonts/archaic/viking-README
%{_texdir}/texmf-dist/doc/fonts/archaic/viking-try_vik.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/aram10.pfb
%{_fontdir}/copsn10.pfb
%{_fontdir}/cugar10.pfb
%{_fontdir}/cypr10.pfb
%{_fontdir}/etr10.pfb
%{_fontdir}/fut10.pfb
%{_fontdir}/givbc10.pfb
%{_fontdir}/gvibc10.pfb
%{_fontdir}/linb10.pfb
%{_fontdir}/nab10.pfb
%{_fontdir}/oandsi10.pfb
%{_fontdir}/oandsu10.pfb
%{_fontdir}/phnc10.pfb
%{_fontdir}/pmhg.pfb
%{_fontdir}/proto10.pfb
%{_fontdir}/sarab10.pfb

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
