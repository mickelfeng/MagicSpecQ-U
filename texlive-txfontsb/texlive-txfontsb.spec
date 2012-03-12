%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/txfontsb.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/txfontsb.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/txfontsb.source.tar.xz

Name: texlive-txfontsb
License: GPL+
Summary: Extensions to txfonts, using GNU Freefont
Version: %{tl_version}
Release: %{tl_noarch_release}.1.00.svn19513%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(txfontsb.sty)
Requires: tex(txfonts.sty)
Requires: texlive-txfontsb-fedora-fonts = %{tl_version}

%description
A set of fonts that extend the txfonts bundle with small caps
and old style numbers, together with Greek support. The
extensions are made with modifications of the GNU Freefont.

date: 2010-01-21 01:12:12 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map gptimes.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map gptimes.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for txfontsb
Version: %{tl_version}
Release: %{tl_noarch_release}.1.00.svn19513%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for txfontsb

%package fedora-fonts
Summary: Fonts for txfontsb
Version: %{tl_version}
Release: %{tl_noarch_release}.1.00.svn19513%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-txfontsb = %{tl_version}
BuildArch: noarch

%description fedora-fonts
A set of fonts that extend the txfonts bundle with small caps
and old style numbers, together with Greek support. The
extensions are made with modifications of the GNU Freefont.

date: 2010-01-21 01:12:12 +0100


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifb-SmallCaps.pfb .
ln -s %{_fontdir}/FreeSerifb-SmallCaps.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifb-SmallCaps.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifb-SmallCapsAlt.pfb .
ln -s %{_fontdir}/FreeSerifb-SmallCapsAlt.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifb-SmallCapsAlt.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifb.pfb .
ln -s %{_fontdir}/FreeSerifb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifbBold.pfb .
ln -s %{_fontdir}/FreeSerifbBold.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifbBold.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifbBoldItalic.pfb .
ln -s %{_fontdir}/FreeSerifbBoldItalic.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifbBoldItalic.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifbItalic.pfb .
ln -s %{_fontdir}/FreeSerifbItalic.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifbItalic.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/txfontsb/FreeSerifb-SmallCaps.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfontsb/FreeSerifb-SmallCapsAlt.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfontsb/FreeSerifb.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfontsb/FreeSerifbBold.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfontsb/FreeSerifbBoldItalic.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfontsb/FreeSerifbItalic.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/txfontsb/gptimes.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/txfontsb/gptimesy.enc
%{_texdir}/texmf-dist/fonts/map/dvips/txfontsb/gptimes.map
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesb6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesb6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesbi6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesbi6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesg6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesi6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesi6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesrg6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimessc6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimessc6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimessco6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimessco6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesyb6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesyb6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesybi6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesybi6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesyg6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesyi6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesyi6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesyrg6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesysc6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesysc6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesysco6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/gtimesysco6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/timessc6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/timessc6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/timessco6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/timessco6r.tfm
%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifb-SmallCaps.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifb-SmallCapsAlt.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifbBold.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifbBoldItalic.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/FreeSerifbItalic.pfb
%{_texdir}/texmf-dist/fonts/vf/public/txfontsb/gtimesb6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfontsb/gtimesbi6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfontsb/gtimesi6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfontsb/gtimesrg6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfontsb/gtimessc6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfontsb/gtimessco6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfontsb/gtimesyb6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfontsb/gtimesybi6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfontsb/gtimesyi6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfontsb/gtimesyrg6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfontsb/gtimesysc6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfontsb/gtimesysco6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfontsb/timessc6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfontsb/timessco6a.vf
%{_texdir}/texmf-dist/tex/latex/txfontsb/lgrtxr.fd
%{_texdir}/texmf-dist/tex/latex/txfontsb/lgrtxrc.fd
%{_texdir}/texmf-dist/tex/latex/txfontsb/lgrtxry.fd
%{_texdir}/texmf-dist/tex/latex/txfontsb/lgrtxryc.fd
%{_texdir}/texmf-dist/tex/latex/txfontsb/ot1txrc.fd
%{_texdir}/texmf-dist/tex/latex/txfontsb/ot1txryc.fd
%{_texdir}/texmf-dist/tex/latex/txfontsb/txfontsb.sty

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/fonts/txfontsb/README
%{_texdir}/texmf-dist/doc/fonts/txfontsb/txfontsb.pdf
%{_texdir}/texmf-dist/doc/fonts/txfontsb/txfontsb.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/FreeSerifb-SmallCaps.pfb
%{_fontdir}/FreeSerifb-SmallCapsAlt.pfb
%{_fontdir}/FreeSerifb.pfb
%{_fontdir}/FreeSerifbBold.pfb
%{_fontdir}/FreeSerifbBoldItalic.pfb
%{_fontdir}/FreeSerifbItalic.pfb

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
