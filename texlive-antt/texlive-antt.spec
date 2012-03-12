%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/antt.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/antt.doc.tar.xz

Name: texlive-antt
License: GFSL
Summary: Antykwa Torunska: a Type 1 family of a Polish traditional type
Version: %{tl_version}
Release: %{tl_noarch_release}.2.08.svn18651%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(anttor.sty)
Provides: tex(antyktor.sty)
Requires: texlive-antt-fedora-fonts = %{tl_version}

%description
Antykwa Torunska is a serif font designed by the late Polish
typographer Zygfryd Gardzielewski, reconstructed and digitized
as as Type 1.

date: 2007-08-24 10:36:49 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map antt.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map antt.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for antt
Version: %{tl_version}
Release: %{tl_noarch_release}.2.08.svn18651%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for antt

%package fedora-fonts
Summary: Fonts for antt
Version: %{tl_version}
Release: %{tl_noarch_release}.2.08.svn18651%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-antt = %{tl_version}
BuildArch: noarch

%description fedora-fonts
Antykwa Torunska is a serif font designed by the late Polish
typographer Zygfryd Gardzielewski, reconstructed and digitized
as as Type 1.

date: 2007-08-24 10:36:49 +0200


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gfsl.txt gfsl.txt
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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunska-Bold.otf .
ln -s %{_fontdir}/AntykwaTorunska-Bold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunska-Bold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunska-BoldItalic.otf .
ln -s %{_fontdir}/AntykwaTorunska-BoldItalic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunska-BoldItalic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunska-Italic.otf .
ln -s %{_fontdir}/AntykwaTorunska-Italic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunska-Italic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunska-Regular.otf .
ln -s %{_fontdir}/AntykwaTorunska-Regular.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunska-Regular.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCond-Bold.otf .
ln -s %{_fontdir}/AntykwaTorunskaCond-Bold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCond-Bold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCond-BoldItalic.otf .
ln -s %{_fontdir}/AntykwaTorunskaCond-BoldItalic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCond-BoldItalic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCond-Italic.otf .
ln -s %{_fontdir}/AntykwaTorunskaCond-Italic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCond-Italic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCond-Regular.otf .
ln -s %{_fontdir}/AntykwaTorunskaCond-Regular.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCond-Regular.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCondLight-Italic.otf .
ln -s %{_fontdir}/AntykwaTorunskaCondLight-Italic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCondLight-Italic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCondLight-Regular.otf .
ln -s %{_fontdir}/AntykwaTorunskaCondLight-Regular.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCondLight-Regular.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCondMed-Italic.otf .
ln -s %{_fontdir}/AntykwaTorunskaCondMed-Italic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCondMed-Italic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCondMed-Regular.otf .
ln -s %{_fontdir}/AntykwaTorunskaCondMed-Regular.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCondMed-Regular.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaLight-Italic.otf .
ln -s %{_fontdir}/AntykwaTorunskaLight-Italic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaLight-Italic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaLight-Regular.otf .
ln -s %{_fontdir}/AntykwaTorunskaLight-Regular.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaLight-Regular.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaMed-Italic.otf .
ln -s %{_fontdir}/AntykwaTorunskaMed-Italic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaMed-Italic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaMed-Regular.otf .
ln -s %{_fontdir}/AntykwaTorunskaMed-Regular.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaMed-Regular.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttb.pfb .
ln -s %{_fontdir}/anttb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttbi.pfb .
ln -s %{_fontdir}/anttbi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttbi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcb.pfb .
ln -s %{_fontdir}/anttcb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcbi.pfb .
ln -s %{_fontdir}/anttcbi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcbi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcl.pfb .
ln -s %{_fontdir}/anttcl.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcl.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcli.pfb .
ln -s %{_fontdir}/anttcli.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcli.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcm.pfb .
ln -s %{_fontdir}/anttcm.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcm.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcmi.pfb .
ln -s %{_fontdir}/anttcmi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcmi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcr.pfb .
ln -s %{_fontdir}/anttcr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcri.pfb .
ln -s %{_fontdir}/anttcri.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcri.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttl.pfb .
ln -s %{_fontdir}/anttl.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttl.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttli.pfb .
ln -s %{_fontdir}/anttli.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttli.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttm.pfb .
ln -s %{_fontdir}/anttm.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttm.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttmi.pfb .
ln -s %{_fontdir}/anttmi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttmi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttr.pfb .
ln -s %{_fontdir}/anttr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttri.pfb .
ln -s %{_fontdir}/anttri.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt/anttri.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gfsl.txt
%{_texdir}/texmf-dist/fonts/afm/public/antt/anttb.afm
%{_texdir}/texmf-dist/fonts/afm/public/antt/anttbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/antt/anttcb.afm
%{_texdir}/texmf-dist/fonts/afm/public/antt/anttcbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/antt/anttcl.afm
%{_texdir}/texmf-dist/fonts/afm/public/antt/anttcli.afm
%{_texdir}/texmf-dist/fonts/afm/public/antt/anttcm.afm
%{_texdir}/texmf-dist/fonts/afm/public/antt/anttcmi.afm
%{_texdir}/texmf-dist/fonts/afm/public/antt/anttcr.afm
%{_texdir}/texmf-dist/fonts/afm/public/antt/anttcri.afm
%{_texdir}/texmf-dist/fonts/afm/public/antt/anttl.afm
%{_texdir}/texmf-dist/fonts/afm/public/antt/anttli.afm
%{_texdir}/texmf-dist/fonts/afm/public/antt/anttm.afm
%{_texdir}/texmf-dist/fonts/afm/public/antt/anttmi.afm
%{_texdir}/texmf-dist/fonts/afm/public/antt/anttr.afm
%{_texdir}/texmf-dist/fonts/afm/public/antt/anttri.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/antt-cs.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/antt-ec.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/antt-el.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/antt-ex.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/antt-exp.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/antt-greek.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/antt-mi.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/antt-qx.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/antt-rm.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/antt-sy.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/antt-t2a.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/antt-t2b.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/antt-t2c.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/antt-t5.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/antt-texnansi.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/antt-ts1.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/antt-wncy.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/anttcap-cs.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/anttcap-ec.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/anttcap-qx.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/anttcap-t5.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/antt/anttcap-texnansi.enc
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt-el.map
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt-ex.map
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt-exp.map
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt-greek.map
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt-mi.map
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt-rm.map
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt-sy.map
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt-t2a.map
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt-t2b.map
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt-t2c.map
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt-texnansi.map
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt-wncy.map
%{_texdir}/texmf-dist/fonts/map/dvips/antt/antt.map
%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunska-Bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunska-BoldItalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunska-Italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunska-Regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCond-Bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCond-BoldItalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCond-Italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCond-Regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCondLight-Italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCondLight-Regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCondMed-Italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaCondMed-Regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaLight-Italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaLight-Regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaMed-Italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/antt/AntykwaTorunskaMed-Regular.otf
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttbcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttbicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttcbcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttcbicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttcl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttclcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttcli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttclicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttcm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttcmcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttcmicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttcrcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttcricap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttlcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttlicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttmcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttmicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttrcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/cs-anttricap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttbcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttbicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttcbcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttcbicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttcl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttclcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttcli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttclicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttcm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttcmcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttcmicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttcrcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttcricap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttlcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttlicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttmcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttmicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttrcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ec-anttricap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/el-anttb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/el-anttbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/el-anttcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/el-anttcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/el-anttcl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/el-anttcli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/el-anttcm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/el-anttcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/el-anttcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/el-anttcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/el-anttl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/el-anttli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/el-anttm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/el-anttmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/el-anttr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/el-anttri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ex-anttb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ex-anttcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ex-anttcl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ex-anttcm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ex-anttcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ex-anttl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ex-anttm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ex-anttr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/exp-anttb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/exp-anttbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/exp-anttcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/exp-anttcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/exp-anttcl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/exp-anttcli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/exp-anttcm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/exp-anttcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/exp-anttcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/exp-anttcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/exp-anttl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/exp-anttli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/exp-anttm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/exp-anttmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/exp-anttr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/exp-anttri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/greek-anttb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/greek-anttbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/greek-anttcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/greek-anttcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/greek-anttcl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/greek-anttcli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/greek-anttcm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/greek-anttcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/greek-anttcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/greek-anttcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/greek-anttl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/greek-anttli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/greek-anttm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/greek-anttmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/greek-anttr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/greek-anttri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/mi-anttbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/mi-anttcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/mi-anttcli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/mi-anttcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/mi-anttcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/mi-anttli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/mi-anttmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/mi-anttri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttbcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttbicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttcbcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttcbicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttcl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttclcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttcli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttclicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttcm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttcmcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttcmicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttcrcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttcricap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttlcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttlicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttmcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttmicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttrcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/qx-anttricap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/rm-anttb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/rm-anttbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/rm-anttcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/rm-anttcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/rm-anttcl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/rm-anttcli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/rm-anttcm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/rm-anttcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/rm-anttcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/rm-anttcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/rm-anttl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/rm-anttli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/rm-anttm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/rm-anttmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/rm-anttr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/rm-anttri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/sy-anttbz.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/sy-anttcbz.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/sy-anttclz.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/sy-anttcmz.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/sy-anttcrz.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/sy-anttlz.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/sy-anttmz.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/sy-anttrz.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2a-anttb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2a-anttbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2a-anttcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2a-anttcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2a-anttcl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2a-anttcli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2a-anttcm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2a-anttcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2a-anttcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2a-anttcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2a-anttl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2a-anttli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2a-anttm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2a-anttmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2a-anttr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2a-anttri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2b-anttb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2b-anttbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2b-anttcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2b-anttcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2b-anttcl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2b-anttcli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2b-anttcm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2b-anttcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2b-anttcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2b-anttcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2b-anttl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2b-anttli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2b-anttm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2b-anttmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2b-anttr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2b-anttri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2c-anttb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2c-anttbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2c-anttcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2c-anttcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2c-anttcl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2c-anttcli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2c-anttcm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2c-anttcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2c-anttcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2c-anttcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2c-anttl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2c-anttli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2c-anttm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2c-anttmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2c-anttr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t2c-anttri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttbcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttbicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttcbcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttcbicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttcl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttclcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttcli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttclicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttcm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttcmcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttcmicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttcrcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttcricap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttlcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttlicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttmcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttmicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttrcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/t5-anttricap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttbcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttbicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcbcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcbicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttclcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttclicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcmcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcmicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcrcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttcricap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttlcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttlicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttmcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttmicap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttrcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/texnansi-anttricap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ts1-anttb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ts1-anttbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ts1-anttcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ts1-anttcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ts1-anttcl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ts1-anttcli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ts1-anttcm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ts1-anttcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ts1-anttcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ts1-anttcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ts1-anttl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ts1-anttli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ts1-anttm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ts1-anttmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ts1-anttr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/ts1-anttri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/wncy-anttb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/wncy-anttbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/wncy-anttcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/wncy-anttcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/wncy-anttcl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/wncy-anttcli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/wncy-anttcm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/wncy-anttcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/wncy-anttcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/wncy-anttcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/wncy-anttl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/wncy-anttli.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/wncy-anttm.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/wncy-anttmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/wncy-anttr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/antt/wncy-anttri.tfm
%{_texdir}/texmf-dist/fonts/type1/public/antt/anttb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/antt/anttbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcl.pfb
%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcli.pfb
%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcm.pfb
%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcmi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/antt/anttcri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/antt/anttl.pfb
%{_texdir}/texmf-dist/fonts/type1/public/antt/anttli.pfb
%{_texdir}/texmf-dist/fonts/type1/public/antt/anttm.pfb
%{_texdir}/texmf-dist/fonts/type1/public/antt/anttmi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/antt/anttr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/antt/anttri.pfb
%{_texdir}/texmf-dist/tex/latex/antt/anttor.sty
%{_texdir}/texmf-dist/tex/latex/antt/antyktor.sty
%{_texdir}/texmf-dist/tex/latex/antt/il2antt.fd
%{_texdir}/texmf-dist/tex/latex/antt/il2anttc.fd
%{_texdir}/texmf-dist/tex/latex/antt/il2anttl.fd
%{_texdir}/texmf-dist/tex/latex/antt/il2anttlc.fd
%{_texdir}/texmf-dist/tex/latex/antt/ly1antt.fd
%{_texdir}/texmf-dist/tex/latex/antt/ly1anttc.fd
%{_texdir}/texmf-dist/tex/latex/antt/ly1anttl.fd
%{_texdir}/texmf-dist/tex/latex/antt/ly1anttlc.fd
%{_texdir}/texmf-dist/tex/latex/antt/omlantt.fd
%{_texdir}/texmf-dist/tex/latex/antt/omlanttc.fd
%{_texdir}/texmf-dist/tex/latex/antt/omlanttl.fd
%{_texdir}/texmf-dist/tex/latex/antt/omlanttlc.fd
%{_texdir}/texmf-dist/tex/latex/antt/omsantt.fd
%{_texdir}/texmf-dist/tex/latex/antt/omsanttc.fd
%{_texdir}/texmf-dist/tex/latex/antt/omsanttl.fd
%{_texdir}/texmf-dist/tex/latex/antt/omsanttlc.fd
%{_texdir}/texmf-dist/tex/latex/antt/omxantt.fd
%{_texdir}/texmf-dist/tex/latex/antt/omxanttc.fd
%{_texdir}/texmf-dist/tex/latex/antt/omxanttl.fd
%{_texdir}/texmf-dist/tex/latex/antt/omxanttlc.fd
%{_texdir}/texmf-dist/tex/latex/antt/ot1antt.fd
%{_texdir}/texmf-dist/tex/latex/antt/ot1anttc.fd
%{_texdir}/texmf-dist/tex/latex/antt/ot1anttcm.fd
%{_texdir}/texmf-dist/tex/latex/antt/ot1anttl.fd
%{_texdir}/texmf-dist/tex/latex/antt/ot1anttlc.fd
%{_texdir}/texmf-dist/tex/latex/antt/ot1anttlcm.fd
%{_texdir}/texmf-dist/tex/latex/antt/ot1anttlm.fd
%{_texdir}/texmf-dist/tex/latex/antt/ot1anttm.fd
%{_texdir}/texmf-dist/tex/latex/antt/ot2antt.fd
%{_texdir}/texmf-dist/tex/latex/antt/ot2anttc.fd
%{_texdir}/texmf-dist/tex/latex/antt/ot2anttl.fd
%{_texdir}/texmf-dist/tex/latex/antt/ot2anttlc.fd
%{_texdir}/texmf-dist/tex/latex/antt/ot4antt.fd
%{_texdir}/texmf-dist/tex/latex/antt/ot4anttc.fd
%{_texdir}/texmf-dist/tex/latex/antt/ot4anttl.fd
%{_texdir}/texmf-dist/tex/latex/antt/ot4anttlc.fd
%{_texdir}/texmf-dist/tex/latex/antt/qxantt.fd
%{_texdir}/texmf-dist/tex/latex/antt/qxanttc.fd
%{_texdir}/texmf-dist/tex/latex/antt/qxanttl.fd
%{_texdir}/texmf-dist/tex/latex/antt/qxanttlc.fd
%{_texdir}/texmf-dist/tex/latex/antt/t1antt.fd
%{_texdir}/texmf-dist/tex/latex/antt/t1anttc.fd
%{_texdir}/texmf-dist/tex/latex/antt/t1anttl.fd
%{_texdir}/texmf-dist/tex/latex/antt/t1anttlc.fd
%{_texdir}/texmf-dist/tex/latex/antt/t2aantt.fd
%{_texdir}/texmf-dist/tex/latex/antt/t2aanttc.fd
%{_texdir}/texmf-dist/tex/latex/antt/t2aanttl.fd
%{_texdir}/texmf-dist/tex/latex/antt/t2aanttlc.fd
%{_texdir}/texmf-dist/tex/latex/antt/t2bantt.fd
%{_texdir}/texmf-dist/tex/latex/antt/t2banttc.fd
%{_texdir}/texmf-dist/tex/latex/antt/t2banttl.fd
%{_texdir}/texmf-dist/tex/latex/antt/t2banttlc.fd
%{_texdir}/texmf-dist/tex/latex/antt/t2cantt.fd
%{_texdir}/texmf-dist/tex/latex/antt/t2canttc.fd
%{_texdir}/texmf-dist/tex/latex/antt/t2canttl.fd
%{_texdir}/texmf-dist/tex/latex/antt/t2canttlc.fd
%{_texdir}/texmf-dist/tex/latex/antt/t5antt.fd
%{_texdir}/texmf-dist/tex/latex/antt/t5anttc.fd
%{_texdir}/texmf-dist/tex/latex/antt/t5anttl.fd
%{_texdir}/texmf-dist/tex/latex/antt/t5anttlc.fd
%{_texdir}/texmf-dist/tex/latex/antt/ts1antt.fd
%{_texdir}/texmf-dist/tex/latex/antt/ts1anttc.fd
%{_texdir}/texmf-dist/tex/latex/antt/ts1anttl.fd
%{_texdir}/texmf-dist/tex/latex/antt/ts1anttlc.fd
%{_texdir}/texmf-dist/tex/plain/antt/antt-math.tex

%files doc
%defattr(-,root,root)
%doc gfsl.txt
%{_texdir}/texmf-dist/doc/fonts/antt/AntykwaTorunska-doc-en-2_03.pdf
%{_texdir}/texmf-dist/doc/fonts/antt/AntykwaTorunska-doc-pl-2_03.pdf
%{_texdir}/texmf-dist/doc/fonts/antt/AntykwaTorunska-doc-src-2_03.zip
%{_texdir}/texmf-dist/doc/fonts/antt/GUST-FONT-NOSOURCE-LICENSE.txt
%{_texdir}/texmf-dist/doc/fonts/antt/MANIFEST.txt
%{_texdir}/texmf-dist/doc/fonts/antt/README
%{_texdir}/texmf-dist/doc/fonts/antt/antt-latex-cyr.tex
%{_texdir}/texmf-dist/doc/fonts/antt/antt-latex-math.tex
%{_texdir}/texmf-dist/doc/fonts/antt/antt-latex-pl.tex
%{_texdir}/texmf-dist/doc/fonts/antt/antt-latex-t2a.tex
%{_texdir}/texmf-dist/doc/fonts/antt/antt-latex-t5.tex
%{_texdir}/texmf-dist/doc/fonts/antt/antt-mathtest.tex
%{_texdir}/texmf-dist/doc/fonts/antt/antt-table.tex
%{_texdir}/texmf-dist/doc/latex/antt/README

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/AntykwaTorunska-Bold.otf
%{_fontdir}/AntykwaTorunska-BoldItalic.otf
%{_fontdir}/AntykwaTorunska-Italic.otf
%{_fontdir}/AntykwaTorunska-Regular.otf
%{_fontdir}/AntykwaTorunskaCond-Bold.otf
%{_fontdir}/AntykwaTorunskaCond-BoldItalic.otf
%{_fontdir}/AntykwaTorunskaCond-Italic.otf
%{_fontdir}/AntykwaTorunskaCond-Regular.otf
%{_fontdir}/AntykwaTorunskaCondLight-Italic.otf
%{_fontdir}/AntykwaTorunskaCondLight-Regular.otf
%{_fontdir}/AntykwaTorunskaCondMed-Italic.otf
%{_fontdir}/AntykwaTorunskaCondMed-Regular.otf
%{_fontdir}/AntykwaTorunskaLight-Italic.otf
%{_fontdir}/AntykwaTorunskaLight-Regular.otf
%{_fontdir}/AntykwaTorunskaMed-Italic.otf
%{_fontdir}/AntykwaTorunskaMed-Regular.otf
%{_fontdir}/anttb.pfb
%{_fontdir}/anttbi.pfb
%{_fontdir}/anttcb.pfb
%{_fontdir}/anttcbi.pfb
%{_fontdir}/anttcl.pfb
%{_fontdir}/anttcli.pfb
%{_fontdir}/anttcm.pfb
%{_fontdir}/anttcmi.pfb
%{_fontdir}/anttcr.pfb
%{_fontdir}/anttcri.pfb
%{_fontdir}/anttl.pfb
%{_fontdir}/anttli.pfb
%{_fontdir}/anttm.pfb
%{_fontdir}/anttmi.pfb
%{_fontdir}/anttr.pfb
%{_fontdir}/anttri.pfb

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
