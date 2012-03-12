%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/baskervald.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/baskervald.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/baskervald.source.tar.xz

Name: texlive-baskervald
License: LPPL
Summary: Baskervald ADF fonts collection with TeX/LaTeX support
Version: %{tl_version}
Release: %{tl_noarch_release}.1.016.svn19490%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(baskervald.sty)
Requires: tex(xkeyval.sty)
Requires: tex(fontenc.sty)
Requires: tex(textcomp.sty)
Requires: tex(nfssext-cfr.sty)
Requires: texlive-baskervald-fedora-fonts = %{tl_version}

%description
Baskervald ADF is a serif family with lining figures designed
as a substitute for Baskerville. The family currently includes
upright and italic or oblique shapes in each of regular, bold
and heavy weights. All fonts include the slashed zero and
additional non-standard ligatures. The support package renames
them according to the Karl Berry fontname scheme and defines
two families. One of these primarily provides access to the
"standard" or default characters while the other supports
additional ligatures. The included package files provide access
to these features in LaTeX.

date: 2010-07-14 23:45:16 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map ybv.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map ybv.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for baskervald
Version: %{tl_version}
Release: %{tl_noarch_release}.1.016.svn19490%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for baskervald

%package fedora-fonts
Summary: Fonts for baskervald
Version: %{tl_version}
Release: %{tl_noarch_release}.1.016.svn19490%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-baskervald = %{tl_version}
BuildArch: noarch

%description fedora-fonts
Baskervald ADF is a serif family with lining figures designed
as a substitute for Baskerville. The family currently includes
upright and italic or oblique shapes in each of regular, bold
and heavy weights. All fonts include the slashed zero and
additional non-standard ligatures. The support package renames
them according to the Karl Berry fontname scheme and defines
two families. One of these primarily provides access to the
"standard" or default characters while the other supports
additional ligatures. The included package files provide access
to these features in LaTeX.

date: 2010-07-14 23:45:16 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvb8a.pfb .
ln -s %{_fontdir}/ybvb8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvb8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvbi8a.pfb .
ln -s %{_fontdir}/ybvbi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvbi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvh8a.pfb .
ln -s %{_fontdir}/ybvh8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvh8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvho8a.pfb .
ln -s %{_fontdir}/ybvho8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvho8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvr8a.pfb .
ln -s %{_fontdir}/ybvr8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvr8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvri8a.pfb .
ln -s %{_fontdir}/ybvri8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvri8a.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/afm/arkandis/baskervald/ybvb8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/baskervald/ybvbi8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/baskervald/ybvh8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/baskervald/ybvho8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/baskervald/ybvr8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/baskervald/ybvri8a.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/baskervald/supp-ybv.enc
%{_texdir}/texmf-dist/fonts/map/dvips/baskervald/ybv.map
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvb8s.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvbi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvbi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvbi8s.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvbi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvbiw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvbw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvh8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvh8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvh8s.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvh8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvho8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvho8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvho8s.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvho8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvhow8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvhw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvr8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvr8s.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvri8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvri8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvri8s.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvriw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/ybvrw8t.tfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvb8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvb8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvbi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvbi8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvh8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvh8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvho8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvho8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvr8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvr8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvri8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/ybvri8a.pfm
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvb8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvb8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvbi8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvbi8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvbiw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvbw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvh8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvh8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvho8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvho8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvhow8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvhw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvr8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvr8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvri8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvri8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvriw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/ybvrw8t.vf
%{_texdir}/texmf-dist/tex/latex/baskervald/baskervald.sty
%{_texdir}/texmf-dist/tex/latex/baskervald/t1ybv.fd
%{_texdir}/texmf-dist/tex/latex/baskervald/t1ybvw.fd
%{_texdir}/texmf-dist/tex/latex/baskervald/ts1ybv.fd
%{_texdir}/texmf-dist/tex/latex/baskervald/ts1ybvw.fd

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/baskervald/COPYING
%{_texdir}/texmf-dist/doc/fonts/baskervald/NOTICE.txt
%{_texdir}/texmf-dist/doc/fonts/baskervald/README
%{_texdir}/texmf-dist/doc/fonts/baskervald/baskervaldadf.pdf
%{_texdir}/texmf-dist/doc/fonts/baskervald/baskervaldadf.tex
%{_texdir}/texmf-dist/doc/fonts/baskervald/manifest.txt

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/ybvb8a.pfb
%{_fontdir}/ybvbi8a.pfb
%{_fontdir}/ybvh8a.pfb
%{_fontdir}/ybvho8a.pfb
%{_fontdir}/ybvr8a.pfb
%{_fontdir}/ybvri8a.pfb

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
