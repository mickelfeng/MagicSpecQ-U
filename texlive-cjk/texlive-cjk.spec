%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cjk.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cjk.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cjk.source.tar.xz

Name: texlive-cjk
License: GPL+
Summary: CJK language support
Version: %{tl_version}
Release: %{tl_noarch_release}.4.8.2.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-arphic = %{tl_version}
Requires: texlive-cns = %{tl_version}
Requires: texlive-garuda-c90 = %{tl_version}
Requires: texlive-norasi-c90 = %{tl_version}
Requires: texlive-uhc = %{tl_version}
Provides: tex(CJK.sty)
Provides: tex(CJKfntef.sty)
Provides: tex(CJKnumb.sty)
Provides: tex(CJKspace.sty)
Provides: tex(CJKulem.sty)
Provides: tex(CJKutf8.sty)
Provides: tex(CJKvert.sty)
Provides: tex(pshan.sty)
Provides: tex(MULEenc.sty)
Provides: tex(pinyin.sty)
Provides: tex(ruby.sty)
Provides: tex(thaicjk.sty)
Provides: tex(xCJK.sty)
Requires: tex(ulem.sty)
Requires: tex(ifpdf.sty)
Requires: tex(inputenc.sty)
Requires: tex(fontenc.sty)
Requires: tex(graphicx.sty)
Requires: tex(ifxetex.sty)
Requires: tex(fontspec.sty)

%description
CJK is a macro package for LaTeX, providing simultaneous
support for various Asian scripts in many encodings (including
Unicode): - Chinese (both traditional and simplified), -
Japanese, - Korean and - Thai. A special add-on feature is an
interface to the Emacs editor (cjk-enc.el) which gives
simultaneous, easy-to-use support to a bunch of other scripts
in addition to the above: - Cyrillic, - Greek, - Latin-based
scripts, - Russian and - Vietnamese.

date: 2009-09-27 09:50:48 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
:

%postun
if [ $1 == 1 ]; then
  mkdir -p /var/run/texlive
  touch /var/run/run-texhash
else
  %{_bindir}/texhash 2> /dev/null
fi
:

%posttrans
[ -e /var/run/texlive/run-texhash ] && %{_bindir}/texhash 2> /dev/null && rm -f /var/run/texlive/run-texhash
[ -e /var/run/texlive ] && rm -rf /var/run/texlive
:

%package doc
Summary: Documentation for cjk
Version: %{tl_version}
Release: %{tl_noarch_release}.4.8.2.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch
Requires: texlive-arphic-doc
Requires: texlive-cns-doc
Requires: texlive-uhc-doc

%description doc
Documentation for cjk


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

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab/c42goth.fd
%{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab/c42goth.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab/c42maru.fd
%{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab/c42maru.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab/c42min.fd
%{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab/c42min.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab/c52maru.fd
%{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab/c52maru.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab/c52min.fd
%{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab/c52min.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab/c70goth.fd
%{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab/c70goth.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab/c70maru.fd
%{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab/c70maru.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab/c70min.fd
%{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab/c70min.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/Bg5.cap
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/Bg5.chr
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/Bg5.cpx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/Bg5.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/HK.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/c00bkai.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/c00bkai.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/c00bsmi.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/c00bsmi.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/c00bsmir.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/c00bsmir.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/c00cns.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/c00fs.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/c00kai.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/c00kair.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/c00kair.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/c00song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/c01song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/c05song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5/c09song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CEF/c80song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CEF/c81song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CJK.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CJK.sty
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CJKfntef.sty
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CJKnumb.sty
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CJKspace.sty
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CJKulem.sty
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CJKutf8.sty
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CJKvert.sty
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/extended.chr
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/extended.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/pinyin.sty
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/pmC.chr
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/pmCbig.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/pmCsmall.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/ruby.sty
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/standard.bdg
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/standard.chr
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/standard.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/xCJK.sty
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/xpmC.chr
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/xpmC.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CNS/EUC-TW.bdg
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CNS/EUC-TW.chr
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CNS/EUC-TW.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CNS/c31song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CNS/c32song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CNS/c33song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CNS/c34song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CNS/c35song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CNS/c36song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CNS/c37song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/GB/GB.cap
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/GB/GB.cpx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/GB/c10fs.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/GB/c10gbsn.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/GB/c10gbsn.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/GB/c10gkai.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/GB/c10gkai.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/GB/c10song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/GB/c11song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/GB/c19song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/GB/c20song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/GB/c21song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/JIS/EUC-JP.bdg
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/JIS/EUC-JP.chr
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/JIS/EUC-JP.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/JIS/EUC-JPdnp.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/JIS/JIS.cap
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/JIS/JIS.cpx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/JIS/JISdnp.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/JIS/c40song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/JIS/c41song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/JIS/c42song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/JIS/c43song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/JIS/c50song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/HLaTeX.chr
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/KSHL.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63bm.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63dn.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63gr.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63gs.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63gt.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63jgt.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63jmj.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63jnv.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63jsr.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63mj.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63pg.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63pga.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63ph.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63pn.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63sh.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63tz.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63vd.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c63yt.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64bm.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64dn.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64gr.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64gs.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64gt.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64jgt.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64jmj.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64jnv.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64jsr.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64mj.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64pg.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64pga.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64ph.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64pn.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64sh.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64tz.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64vd.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c64yt.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65bm.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65dn.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65gr.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65gs.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65gt.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65jgt.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65jmj.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65jnv.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65jsr.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65mj.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65pg.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65pga.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65ph.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65pn.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65sh.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65tz.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65vd.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/c65yt.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX/pshan.sty
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/KS.chr
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/KS.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c60dr.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c60gr.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c60gs.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c60gt.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c60hgt.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c60hmj.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c60hol.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c60hpg.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c60mj.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c61dr.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c61gr.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c61gs.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c61gt.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c61hgt.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c61hmj.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c61hol.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c61hpg.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c61mj.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/c62song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/hangul.cap
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/hangul.cpx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/hangul2.cap
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/hangul2.cpx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/hanja.cap
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/hanja.cpx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/SJIS/SJIS.bdg
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/SJIS/SJIS.cap
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/SJIS/SJIS.chr
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/SJIS/SJIS.cpx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/SJIS/SJIS.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/SJIS/SJISdnp.chr
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/SJIS/SJISdnp.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/SJIS/c49song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/UTF8.bdg
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/UTF8.chr
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/UTF8.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/c70bkai.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/c70bkai.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/c70bsmi.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/c70bsmi.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/c70gbsn.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/c70gbsn.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/c70gkai.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/c70gkai.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/c70mj.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/c70mj.fdx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/c70song.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/ja.cpx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/ko-Hang.cpx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/ko-Hang2.cpx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/ko-Hani.cpx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/xUTF8.chr
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/xUTF8.enc
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/zh-Hans.cpx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8/zh-Hant.cpx
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/mule/MULEenc.sty
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/thai/c90cmr.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/thai/c90cmss.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/thai/c90cmtt.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/thai/c90enc.def
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/thai/c90gar.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/thai/c90nrsr.fd
%{_texdir}/texmf-dist/tex/latex/cjk/texinput/thai/thaicjk.ldf
%{_texdir}/texmf-dist/tex/latex/cjk/utils/pyhyphen/pinyin.ldf

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/latex/cjk/ChangeLog
%{_texdir}/texmf-dist/doc/latex/cjk/MANIFEST
%{_texdir}/texmf-dist/doc/latex/cjk/Makefile
%{_texdir}/texmf-dist/doc/latex/cjk/README
%{_texdir}/texmf-dist/doc/latex/cjk/TODO
%{_texdir}/texmf-dist/doc/latex/cjk/doc/CEF.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/CJK.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/CJKnumb.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/CJKspace.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/CJKutf8.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/COPYING
%{_texdir}/texmf-dist/doc/latex/cjk/doc/INSTALL
%{_texdir}/texmf-dist/doc/latex/cjk/doc/TDS.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/cjk-enc.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/commands.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/dvidrv.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/fdxfiles.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/fonts.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/hbf2gf.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/history.2_5
%{_texdir}/texmf-dist/doc/latex/cjk/doc/history.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pinyin.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pyhyphen.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/reftex.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/ruby.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/thaifont.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/vertical.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/xCJK.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/chinese/README
%{_texdir}/texmf-dist/doc/latex/cjk/doc/chinese/READMEb5.tex
%{_texdir}/texmf-dist/doc/latex/cjk/doc/chinese/READMEgb.tex
%{_texdir}/texmf-dist/doc/latex/cjk/doc/chinese/emTeXb5.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/chinese/teTeXb5.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/cjk/README
%{_texdir}/texmf-dist/doc/latex/cjk/doc/cjk/READMEb5.cjk
%{_texdir}/texmf-dist/doc/latex/cjk/doc/japanese/README
%{_texdir}/texmf-dist/doc/latex/cjk/doc/japanese/ascii.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/japanese/japanese.jis
%{_texdir}/texmf-dist/doc/latex/cjk/doc/japanese/japanese.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/japanese/jp-fonts.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/japanese/jp-tex.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/japanese/preview.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/japanese/shibuaki.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdf/READMEb5.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdf/READMEgb.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/HOWTO.txt
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/bkai.map
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/cid-x.map
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/cwtb.map
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/dvipdfmx.cfg
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/gen-map.pl
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/map.list
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/updmap.my
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/wcl.sfd
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/texinput/Bg5/c00cwtb.fd
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/texinput/Bg5/c00tmpl.fd
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/texinput/GB/c10tmpl.fd
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/texinput/JIS/c40tmpl.fd
%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/texinput/SJIS/c49tmpl.fd
%{_texdir}/texmf-dist/doc/latex/cjk/examples/Big5.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/Big5vert.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/CEF_test.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/CJKbabel.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/CJKfntef.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/CJKmixed.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/CJKspace.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/CJKutf8.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/GB.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/JIS.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/KS.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/README
%{_texdir}/texmf-dist/doc/latex/cjk/examples/SJIS.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/UTF8.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/muletest.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/py_test.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/rubytest.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/thai.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/xCJK.tex
%{_texdir}/texmf-dist/doc/latex/cjk/examples/cjk/Big5.cjk
%{_texdir}/texmf-dist/doc/latex/cjk/examples/cjk/Big5vert.cjk
%{_texdir}/texmf-dist/doc/latex/cjk/examples/cjk/CEF_test.cjk
%{_texdir}/texmf-dist/doc/latex/cjk/examples/cjk/CJKbabel.cjk
%{_texdir}/texmf-dist/doc/latex/cjk/examples/cjk/SJIS.cjk
%{_texdir}/texmf-dist/doc/latex/cjk/examples/cjk/muletest.cjk
%{_texdir}/texmf-dist/doc/latex/cjk/examples/cjk/rubytest.cjk
%{_texdir}/texmf-dist/doc/latex/cjk/examples/cjk/thai.cjk
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/Big5.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/Big5vert.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/CEF_test.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/CJKbabel.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/CJKfntef.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/CJKmixed.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/CJKspace.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/CJKutf8.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/GB.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/JIS.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/KS.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/SJIS.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/UTF8.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/muletest.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/py_test.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/pytest.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/rubytest.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/thai.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf/xCJK.pdf
%{_texdir}/texmf-dist/doc/latex/cjk/texlive/bin-cjkutils.pl
%{_texdir}/texmf-dist/doc/latex/cjk/texlive/c90.pl
%{_texdir}/texmf-dist/doc/latex/cjk/texlive/cjk-build.pl
%{_texdir}/texmf-dist/doc/latex/cjk/texlive/cjk.pl
%{_texdir}/texmf-dist/doc/latex/cjk/texlive/dnp.pl
%{_texdir}/texmf-dist/doc/latex/cjk/texlive/garuda-c90.pl
%{_texdir}/texmf-dist/doc/latex/cjk/texlive/norasi-c90.pl
%{_texdir}/texmf-dist/doc/latex/cjk/utils/pyhyphen/pytest.tex


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
