%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ucs.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ucs.doc.tar.xz

Name: texlive-ucs
License: LPPL
Summary: Extended UTF-8 input encoding for LaTeX
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17090%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(autofe.sty)
Provides: tex(ucs.sty)
Provides: tex(ucshyper.sty)
Provides: tex(ucsutils.sty)
Requires: tex(fontenc.sty)
Requires: tex(graphicx.sty)
Requires: tex(hyperref.sty)
Requires: tex(keyval.sty)

%description
This bundle provides the ucs package, and utf8x.def, together
with a large number of support files. The utf8x.def definition
file for use with inputenc covers a wider range of Unicode
characters than does utf8.def in the LaTeX distribution. The
ucs package provides facilities for efficient use of large sets
of Unicode characters.

date: 2010-02-19 00:25:14 +0100

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
Summary: Documentation for ucs
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17090%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for ucs


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

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/tex/latex/ucs/UnicodeT.sfd
%{_texdir}/texmf-dist/tex/latex/ucs/autofe.sty
%{_texdir}/texmf-dist/tex/latex/ucs/c00enc.def
%{_texdir}/texmf-dist/tex/latex/ucs/c10enc.def
%{_texdir}/texmf-dist/tex/latex/ucs/c40enc.def
%{_texdir}/texmf-dist/tex/latex/ucs/c42enc.def
%{_texdir}/texmf-dist/tex/latex/ucs/c61enc.def
%{_texdir}/texmf-dist/tex/latex/ucs/cenccmn.tex
%{_texdir}/texmf-dist/tex/latex/ucs/cp1252.enc
%{_texdir}/texmf-dist/tex/latex/ucs/ldvarial.fd
%{_texdir}/texmf-dist/tex/latex/ucs/ldvc2000.fd
%{_texdir}/texmf-dist/tex/latex/ucs/ldvenc.def
%{_texdir}/texmf-dist/tex/latex/ucs/letc2000.fd
%{_texdir}/texmf-dist/tex/latex/ucs/letenc.def
%{_texdir}/texmf-dist/tex/latex/ucs/letgfzem.fd
%{_texdir}/texmf-dist/tex/latex/ucs/letjiret.fd
%{_texdir}/texmf-dist/tex/latex/ucs/lklenc.def
%{_texdir}/texmf-dist/tex/latex/ucs/lklkli.fd
%{_texdir}/texmf-dist/tex/latex/ucs/ltaarial.fd
%{_texdir}/texmf-dist/tex/latex/ucs/ltac2000.fd
%{_texdir}/texmf-dist/tex/latex/ucs/ltaenc.def
%{_texdir}/texmf-dist/tex/latex/ucs/ltgc2000.fd
%{_texdir}/texmf-dist/tex/latex/ucs/ltgenc.def
%{_texdir}/texmf-dist/tex/latex/ucs/ltlcmr.fd
%{_texdir}/texmf-dist/tex/latex/ucs/ltlenc.def
%{_texdir}/texmf-dist/tex/latex/ucs/ltwdsnol.fd
%{_texdir}/texmf-dist/tex/latex/ucs/ltwdsque.fd
%{_texdir}/texmf-dist/tex/latex/ucs/ltwdssin.fd
%{_texdir}/texmf-dist/tex/latex/ucs/ltwenc.def
%{_texdir}/texmf-dist/tex/latex/ucs/lucarial.fd
%{_texdir}/texmf-dist/tex/latex/ucs/lucc2000.fd
%{_texdir}/texmf-dist/tex/latex/ucs/lucenc.def
%{_texdir}/texmf-dist/tex/latex/ucs/mkrenc.def
%{_texdir}/texmf-dist/tex/latex/ucs/mkrezra.fd
%{_texdir}/texmf-dist/tex/latex/ucs/mkrhadas.fd
%{_texdir}/texmf-dist/tex/latex/ucs/mkromega.fd
%{_texdir}/texmf-dist/tex/latex/ucs/mkrrashi.fd
%{_texdir}/texmf-dist/tex/latex/ucs/t2dcmr.fd
%{_texdir}/texmf-dist/tex/latex/ucs/t2denc.def
%{_texdir}/texmf-dist/tex/latex/ucs/tengwarDS.enc
%{_texdir}/texmf-dist/tex/latex/ucs/ucs.sty
%{_texdir}/texmf-dist/tex/latex/ucs/ucsencs.def
%{_texdir}/texmf-dist/tex/latex/ucs/ucshyper.sty
%{_texdir}/texmf-dist/tex/latex/ucs/ucsutils.sty
%{_texdir}/texmf-dist/tex/latex/ucs/utf8x.def
%{_texdir}/texmf-dist/tex/latex/ucs/xscmr.fd
%{_texdir}/texmf-dist/tex/latex/ucs/xsenc.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-0.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-1.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-100.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-101.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-102.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-103.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-104.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-105.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-106.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-107.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-108.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-109.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-110.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-111.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-112.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-113.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-114.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-115.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-116.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-117.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-118.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-119.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-12.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-120.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-121.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-122.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-123.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-124.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-125.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-126.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-127.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-128.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-129.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-130.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-131.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-132.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-133.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-134.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-135.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-136.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-137.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-138.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-139.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-14.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-140.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-141.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-142.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-143.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-144.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-145.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-146.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-147.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-148.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-149.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-150.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-151.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-152.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-153.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-154.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-155.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-156.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-157.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-158.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-159.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-172.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-173.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-174.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-175.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-176.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-177.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-178.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-179.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-18.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-180.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-181.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-182.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-183.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-184.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-185.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-186.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-187.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-188.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-189.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-19.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-190.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-191.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-192.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-193.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-194.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-195.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-196.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-197.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-198.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-199.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-2.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-200.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-201.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-202.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-203.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-204.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-205.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-206.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-207.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-208.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-209.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-210.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-211.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-212.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-213.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-214.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-215.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-24.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-248.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-249.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-250.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-251.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-254.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-255.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-29.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-3.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-30.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-31.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-32.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-33.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-34.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-35.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-3584.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-36.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-37.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-38.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-39.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-4.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-40.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-42.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-46.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-468.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-469.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-47.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-470.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-471.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-48.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-49.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-5.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-50.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-51.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-760.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-761.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-762.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-78.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-79.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-80.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-81.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-82.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-83.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-84.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-85.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-86.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-87.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-88.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-89.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-9.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-90.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-91.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-92.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-93.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-94.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-95.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-96.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-97.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-98.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-99.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uni-global.def
%{_texdir}/texmf-dist/tex/latex/ucs/data/uninames.dat

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/ucs/FAQ
%{_texdir}/texmf-dist/doc/latex/ucs/INSTALL
%{_texdir}/texmf-dist/doc/latex/ucs/LICENSE
%{_texdir}/texmf-dist/doc/latex/ucs/README
%{_texdir}/texmf-dist/doc/latex/ucs/VERSION
%{_texdir}/texmf-dist/doc/latex/ucs/discovermacro.pl
%{_texdir}/texmf-dist/doc/latex/ucs/languages.pdf
%{_texdir}/texmf-dist/doc/latex/ucs/latexout.pl
%{_texdir}/texmf-dist/doc/latex/ucs/ltxmacrs.txt
%{_texdir}/texmf-dist/doc/latex/ucs/makeunidef.pl
%{_texdir}/texmf-dist/doc/latex/ucs/ucs.pdf
%{_texdir}/texmf-dist/doc/latex/ucs/config/ascii.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/boxdraw.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/braille.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/cjk-bg5.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/cjk-gb.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/cjk-globals.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/cjk-hangul.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/cjk-jis.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/combining.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/control.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/ctrlglyphs.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/currency.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/cyrillic.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/devanagari.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/ethiopic.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/geometric.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/greek.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/hebrew.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/ipa.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/klingon.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/latin-a.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/latin-b.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/latin-e-a.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/latin1.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/math.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/mathalpha.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/miscsymb.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/modifier.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/mongolian.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/pifont.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/punct.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/supersub.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/tags.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/telugu.ucf.gz
%{_texdir}/texmf-dist/doc/latex/ucs/config/thai.ucf.gz


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
