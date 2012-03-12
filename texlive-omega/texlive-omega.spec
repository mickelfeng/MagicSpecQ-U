%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/omega.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/omega.doc.tar.xz

Name: texlive-omega
License: GPL+
Summary: A wide-character-set extension of TeX
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-omega-fedora-fonts = %{tl_version}

%description
A development of TeX, which deals in multi-octet Unicode
characters, to enable native treatment of a wide range of
languages without changing character-set. Work on Omega seems,
more or less, to have ceased: its immediate successor was to be
the aleph project (though that too has stalled). Projects
developing Omega (and Aleph) ideas include Omega-2 and LuaTeX.

date: 2009-11-09 23:44:56 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map omega.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map omega.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for omega
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for omega

%package fedora-fonts
Summary: Fonts for omega
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-omega = %{tl_version}
BuildArch: noarch

%description fedora-fonts
A development of TeX, which deals in multi-octet Unicode
characters, to enable native treatment of a wide range of
languages without changing character-set. Work on Omega seems,
more or less, to have ceased: its immediate successor was to be
the aleph project (though that too has stalled). Projects
developing Omega (and Aleph) ideas include Omega-2 and LuaTeX.

date: 2009-11-09 23:44:56 +0100


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gpl.txt gpl.txt
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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omding.pfb .
ln -s %{_fontdir}/omding.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omding.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea1.pfb .
ln -s %{_fontdir}/omsea1.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea1.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea1b.pfb .
ln -s %{_fontdir}/omsea1b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea1b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea2.pfb .
ln -s %{_fontdir}/omsea2.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea2.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea2b.pfb .
ln -s %{_fontdir}/omsea2b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea2b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea3.pfb .
ln -s %{_fontdir}/omsea3.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea3.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea3b.pfb .
ln -s %{_fontdir}/omsea3b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea3b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omseco.pfb .
ln -s %{_fontdir}/omseco.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omseco.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecob.pfb .
ln -s %{_fontdir}/omsecob.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecob.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecobi.pfb .
ln -s %{_fontdir}/omsecobi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecobi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecoi.pfb .
ln -s %{_fontdir}/omsecoi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecoi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecx.pfb .
ln -s %{_fontdir}/omsecx.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecx.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecy.pfb .
ln -s %{_fontdir}/omsecy.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecy.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecyb.pfb .
ln -s %{_fontdir}/omsecyb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecyb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecyi.pfb .
ln -s %{_fontdir}/omsecyi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecyi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsegr.pfb .
ln -s %{_fontdir}/omsegr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsegr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsegrb.pfb .
ln -s %{_fontdir}/omsegrb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsegrb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsegrbi.pfb .
ln -s %{_fontdir}/omsegrbi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsegrbi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsegri.pfb .
ln -s %{_fontdir}/omsegri.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsegri.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omseha.pfb .
ln -s %{_fontdir}/omseha.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omseha.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsehe.pfb .
ln -s %{_fontdir}/omsehe.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsehe.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omseip.pfb .
ln -s %{_fontdir}/omseip.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omseip.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsela.pfb .
ln -s %{_fontdir}/omsela.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omsela.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omselab.pfb .
ln -s %{_fontdir}/omselab.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omselab.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omselabi.pfb .
ln -s %{_fontdir}/omselabi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omselabi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omselai.pfb .
ln -s %{_fontdir}/omselai.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omselai.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omseti.pfb .
ln -s %{_fontdir}/omseti.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omseti.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omssti.pfb .
ln -s %{_fontdir}/omssti.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega/omssti.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/dvips/omega/config.omega
%{_texdir}/texmf-dist/dvips/omega/omega.cfg
%{_texdir}/texmf-dist/fonts/afm/public/omega/omsea1.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omsea1b.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omsea2.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omsea2b.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omsea3.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omsea3b.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omseco.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omsecob.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omsecobi.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omsecoi.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omsecx.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omsecy.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omsegr.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omsegrb.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omsegrbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omsegri.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omseha.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omsehe.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omseip.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omsela.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omselab.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omselabi.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omselai.afm
%{_texdir}/texmf-dist/fonts/afm/public/omega/omseti.afm
%{_texdir}/texmf-dist/fonts/map/dvips/omega/omega.map
%{_texdir}/texmf-dist/fonts/ofm/public/omega/omarab.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/omega/omarabb.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/omega/omlgc.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/omega/omlgcb.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/omega/omlgcbi.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/omega/omlgci.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/omega/ucitt10.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/omega/ucsltt10.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/omega/uctt10.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/omega/uctt12.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/omega/uctt8.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/omega/uctt9.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/omega/ucvtt10.ofm
%{_texdir}/texmf-dist/fonts/ovf/public/omega/omarab.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/omega/omarabb.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/omega/omlgc.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/omega/omlgcb.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/omega/omlgcbi.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/omega/omlgci.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/omega/ucitt10.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/omega/ucsltt10.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/omega/uctt10.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/omega/uctt12.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/omega/uctt8.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/omega/uctt9.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/omega/ucvtt10.ovf
%{_texdir}/texmf-dist/fonts/ovp/public/omega/omarab.ovp
%{_texdir}/texmf-dist/fonts/ovp/public/omega/omarabb.ovp
%{_texdir}/texmf-dist/fonts/ovp/public/omega/omlgc.ovp
%{_texdir}/texmf-dist/fonts/ovp/public/omega/omlgcb.ovp
%{_texdir}/texmf-dist/fonts/ovp/public/omega/omlgcbi.ovp
%{_texdir}/texmf-dist/fonts/ovp/public/omega/omlgci.ovp
%{_texdir}/texmf-dist/fonts/ovp/public/omega/ucitt10.ovp
%{_texdir}/texmf-dist/fonts/ovp/public/omega/ucsltt10.ovp
%{_texdir}/texmf-dist/fonts/ovp/public/omega/uctt10.ovp
%{_texdir}/texmf-dist/fonts/ovp/public/omega/uctt12.ovp
%{_texdir}/texmf-dist/fonts/ovp/public/omega/uctt8.ovp
%{_texdir}/texmf-dist/fonts/ovp/public/omega/uctt9.ovp
%{_texdir}/texmf-dist/fonts/ovp/public/omega/ucvtt10.ovp
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omding.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omsea1.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omsea1b.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omsea2.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omsea2b.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omsea3.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omsea3b.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omseco.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omsecob.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omsecobi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omsecoi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omsecx.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omsecy.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omsegr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omsegrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omsegrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omsegri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omseha.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omseip.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omsela.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omselab.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omselabi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omselai.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omseti.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/omega/omssti.tfm
%{_texdir}/texmf-dist/fonts/type1/public/omega/omding.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea1.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea1b.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea2.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea2b.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea3.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsea3b.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omseco.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecob.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecobi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecoi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecx.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecy.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecyb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsecyi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsegr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsegrb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsegrbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsegri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omseha.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsehe.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omseip.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omsela.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omselab.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omselabi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omselai.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omseti.pfb
%{_texdir}/texmf-dist/fonts/type1/public/omega/omssti.pfb
%{_texdir}/texmf-dist/omega/ocp/char2uni/in646.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/in88591.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/in88592.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/in88593.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/in88594.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/in88595.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/in88596.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/in88597.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/in88598.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/in88599.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/in8859a.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/in8859d.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/in8859e.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/in8859f.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/in8859g.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/inatari.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/inav.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/inbig5.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/incp1250.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/incp1251.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/incp1252.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/incp1253.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/incp1254.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/incp1255.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/incp1256.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/incp1257.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/incp1258.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/incp866.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/incp874.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/inebcdic.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/ingb.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/inkoi8.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/inmac.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/inmsdos.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/inmsdos2.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/innext.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/inov.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/inps2.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/insf1.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/insf2.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/intis620.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/inucode.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/inutf8.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/inviet1.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/inviet2.ocp
%{_texdir}/texmf-dist/omega/ocp/char2uni/inviscii.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/7arb2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/7ber2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/7cyr2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/7hma2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/7in88593.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/7lbe2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/7pap2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/7pas2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/7snd2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/7syr2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/7tbe2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/7urd2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/8mac-arb2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/8mac-cyr2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/apostr2psili.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/cuni2acad.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/cuni2amal.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/cuni2arab.ex.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/cuni2arab.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/cuni2asv.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/cuni2bout.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/cuni2mona.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/cuni2nar.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/cuni2nva.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/cuni2oar-novow.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/cuni2oar.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/cunioara.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/dblquote-point.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/destroy.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/french2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/greek.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/grpo2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/grpotilde2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/inverted-iota-upsilon.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/isogr2uni-verbatim.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/isogr2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/lat2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/lowercase.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/lunatesigma.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/macgr2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/medbeta.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/mixedgreek2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/tarauni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/test1.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/test3.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/tiqwah.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/tiqwah2.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/tsinduni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/turduuni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/uni2cuni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/uni2greek-verbatim.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/uni2greek.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/uni2lat-noffi.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/uni2lat.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/unicuni.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/uppercase-no-accents.ocp
%{_texdir}/texmf-dist/omega/ocp/omega/uppercase.ocp
%{_texdir}/texmf-dist/omega/ocp/uni2char/out88591.ocp
%{_texdir}/texmf-dist/omega/ocp/uni2char/oututf8.ocp
%{_texdir}/texmf-dist/omega/otp/char2uni/in646.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/in88591.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/in88592.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/in88593.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/in88594.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/in88595.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/in88596.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/in88597.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/in88598.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/in88599.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/in8859a.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/in8859d.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/in8859e.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/in8859f.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/in8859g.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/inatari.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/inav.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/inbig5.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/incp1250.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/incp1251.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/incp1252.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/incp1253.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/incp1254.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/incp1255.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/incp1256.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/incp1257.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/incp1258.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/incp866.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/incp874.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/inebcdic.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/ingb.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/inkoi8.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/inmac.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/inmsdos.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/inmsdos2.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/innext.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/inov.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/inps2.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/insf1.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/insf2.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/intis620.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/inucode.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/inutf8.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/inviet1.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/inviet2.otp
%{_texdir}/texmf-dist/omega/otp/char2uni/inviscii.otp
%{_texdir}/texmf-dist/omega/otp/omega/7arb2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/7ber2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/7cyr2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/7hma2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/7in88593.otp
%{_texdir}/texmf-dist/omega/otp/omega/7lbe2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/7pap2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/7pas2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/7snd2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/7syr2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/7tbe2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/7urd2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/8mac-arb2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/8mac-cyr2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/apostr2psili.otp
%{_texdir}/texmf-dist/omega/otp/omega/cuni2acad.otp
%{_texdir}/texmf-dist/omega/otp/omega/cuni2amal.otp
%{_texdir}/texmf-dist/omega/otp/omega/cuni2arab.ex.otp
%{_texdir}/texmf-dist/omega/otp/omega/cuni2asv.otp
%{_texdir}/texmf-dist/omega/otp/omega/cuni2bout.otp
%{_texdir}/texmf-dist/omega/otp/omega/cuni2mona.otp
%{_texdir}/texmf-dist/omega/otp/omega/cuni2nar.otp
%{_texdir}/texmf-dist/omega/otp/omega/cuni2nva.otp
%{_texdir}/texmf-dist/omega/otp/omega/cuni2oar-novow.otp
%{_texdir}/texmf-dist/omega/otp/omega/cuni2oar.otp
%{_texdir}/texmf-dist/omega/otp/omega/dblquote-point.otp
%{_texdir}/texmf-dist/omega/otp/omega/destroy.otp
%{_texdir}/texmf-dist/omega/otp/omega/french2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/grpo2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/grpotilde2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/inverted-iota-upsilon.otp
%{_texdir}/texmf-dist/omega/otp/omega/isogr2uni-verbatim.otp
%{_texdir}/texmf-dist/omega/otp/omega/isogr2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/lat2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/lowercase.otp
%{_texdir}/texmf-dist/omega/otp/omega/lunatesigma.otp
%{_texdir}/texmf-dist/omega/otp/omega/macgr2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/medbeta.otp
%{_texdir}/texmf-dist/omega/otp/omega/mixedgreek2uni.otp
%{_texdir}/texmf-dist/omega/otp/omega/uni2cuni.otp
%{_texdir}/texmf-dist/omega/otp/omega/uni2greek-verbatim.otp
%{_texdir}/texmf-dist/omega/otp/omega/uni2greek.otp
%{_texdir}/texmf-dist/omega/otp/omega/uni2lat-noffi.otp
%{_texdir}/texmf-dist/omega/otp/omega/uni2lat.otp
%{_texdir}/texmf-dist/omega/otp/omega/uppercase-no-accents.otp
%{_texdir}/texmf-dist/omega/otp/omega/uppercase.otp
%{_texdir}/texmf-dist/omega/otp/uni2char/out88591.otp
%{_texdir}/texmf-dist/omega/otp/uni2char/oututf8.otp
%{_texdir}/texmf-dist/tex/generic/encodings/cmbsy.onm
%{_texdir}/texmf-dist/tex/generic/encodings/cmbx.onm
%{_texdir}/texmf-dist/tex/generic/encodings/cmcsc.onm
%{_texdir}/texmf-dist/tex/generic/encodings/cmex.onm
%{_texdir}/texmf-dist/tex/generic/encodings/cmmi.onm
%{_texdir}/texmf-dist/tex/generic/encodings/cmmib.onm
%{_texdir}/texmf-dist/tex/generic/encodings/cmr.onm
%{_texdir}/texmf-dist/tex/generic/encodings/cmr1.onm
%{_texdir}/texmf-dist/tex/generic/encodings/cmsl.onm
%{_texdir}/texmf-dist/tex/generic/encodings/cmsy.onm
%{_texdir}/texmf-dist/tex/generic/encodings/cmti.onm
%{_texdir}/texmf-dist/tex/generic/encodings/cmtt.onm
%{_texdir}/texmf-dist/tex/generic/encodings/ecrm.onm
%{_texdir}/texmf-dist/tex/generic/encodings/euex.onm
%{_texdir}/texmf-dist/tex/generic/encodings/eufb.onm
%{_texdir}/texmf-dist/tex/generic/encodings/eufm.onm
%{_texdir}/texmf-dist/tex/generic/encodings/eurb.onm
%{_texdir}/texmf-dist/tex/generic/encodings/eurm.onm
%{_texdir}/texmf-dist/tex/generic/encodings/eusb.onm
%{_texdir}/texmf-dist/tex/generic/encodings/eusm.onm
%{_texdir}/texmf-dist/tex/generic/encodings/msam.onm
%{_texdir}/texmf-dist/tex/generic/encodings/msbm.onm
%{_texdir}/texmf-dist/tex/generic/omegahyph/bghyph.tex
%{_texdir}/texmf-dist/tex/generic/omegahyph/lthyph.tex
%{_texdir}/texmf-dist/tex/generic/omegahyph/srhyph.tex
%{_texdir}/texmf-dist/tex/plain/omega/grlccode.tex
%{_texdir}/texmf-dist/tex/plain/omega/omega.tex

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/omega/base/doc-1.8.tex
%{_texdir}/texmf-dist/doc/omega/base/torture.ps
%{_texdir}/texmf-dist/doc/omega/base/torture.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/omding.pfb
%{_fontdir}/omsea1.pfb
%{_fontdir}/omsea1b.pfb
%{_fontdir}/omsea2.pfb
%{_fontdir}/omsea2b.pfb
%{_fontdir}/omsea3.pfb
%{_fontdir}/omsea3b.pfb
%{_fontdir}/omseco.pfb
%{_fontdir}/omsecob.pfb
%{_fontdir}/omsecobi.pfb
%{_fontdir}/omsecoi.pfb
%{_fontdir}/omsecx.pfb
%{_fontdir}/omsecy.pfb
%{_fontdir}/omsecyb.pfb
%{_fontdir}/omsecyi.pfb
%{_fontdir}/omsegr.pfb
%{_fontdir}/omsegrb.pfb
%{_fontdir}/omsegrbi.pfb
%{_fontdir}/omsegri.pfb
%{_fontdir}/omseha.pfb
%{_fontdir}/omsehe.pfb
%{_fontdir}/omseip.pfb
%{_fontdir}/omsela.pfb
%{_fontdir}/omselab.pfb
%{_fontdir}/omselabi.pfb
%{_fontdir}/omselai.pfb
%{_fontdir}/omseti.pfb
%{_fontdir}/omssti.pfb

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
