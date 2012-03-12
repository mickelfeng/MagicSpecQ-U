%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/presentations.doc.tar.xz

Name: texlive-presentations-doc
License: LPPL
Summary: Documentation for presentations
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17172%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description
Documentation for presentations


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lppl.txt lppl.txt
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}/texmf-dist
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
%{_texdir}/texmf-dist/doc/latex/presentations/01-01-1.ltx2crop
%{_texdir}/texmf-dist/doc/latex/presentations/01-01-2.ltx2ps
%{_texdir}/texmf-dist/doc/latex/presentations/01-01-3.ltx2
%{_texdir}/texmf-dist/doc/latex/presentations/01-01-4.ltx2
%{_texdir}/texmf-dist/doc/latex/presentations/01-01-5.ltx2ps
%{_texdir}/texmf-dist/doc/latex/presentations/01-01-6.ltx2
%{_texdir}/texmf-dist/doc/latex/presentations/01-02-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/01-03-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/01-03-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/01-03-3.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/01-03-4.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/01-03-4.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/01-03-5.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/01-04-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/01-04-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/01-04-3.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/01-04-4.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/01-04-5.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/01-05-1.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/01-05-2.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/01-05-3.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/02-01-1.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-01-2.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-01-3.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-02-1.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-03-1.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-03-2.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-03-3.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-03-4.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-04-1.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-04-2.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-04-3.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-04-4.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-04-5.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-04-6.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-04-7.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-05-1.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-06-1.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-06-2.ltxps
%{_texdir}/texmf-dist/doc/latex/presentations/02-07-1.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-08-1.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-09-1.ltxps
%{_texdir}/texmf-dist/doc/latex/presentations/02-10-1.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-10-2.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-10-3.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-10-4.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-10-5.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-10-6.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-11-1.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-12-1.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-12-2.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-13-1.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-13-2.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-13-3.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-1.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-10.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-11.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-12.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-13.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-14.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-15.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-16.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-17.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-18.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-2.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-3.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-4.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-5.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-6.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-7.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-8.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/02-14-9.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/03-01-1.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/03-02-1.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/03-03-1.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/03-03-2.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/03-03-3.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/04-01-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-01-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-01-3.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-01-4.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-03-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-03-2.ltx2
%{_texdir}/texmf-dist/doc/latex/presentations/04-04-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-05-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-06-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-06-10.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-06-11.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-06-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-06-3.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-06-4.ltxbps
%{_texdir}/texmf-dist/doc/latex/presentations/04-06-5.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-06-6.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-06-7.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-06-8.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-06-9.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-07-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-08-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-09-1.ltxbps
%{_texdir}/texmf-dist/doc/latex/presentations/04-11-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-11-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-11-3.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-12-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-12-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-13-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-13-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-14-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-15-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-15-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-16-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-16-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-16-3.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-17-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-18-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-18-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-19-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-19-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-20-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-20-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-20-3.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-20-4.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-20-5.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-21-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-21-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-21-3.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-21-4.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-22-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-22-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-22-3.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-23-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-23-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-24-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-24-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-10.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-11.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-12.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-13.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-14.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-15.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-16.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-17.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-18.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-19.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-20.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-21.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-22.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-23.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-24.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-25.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-26.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-27.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-28.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-29.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-3.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-30.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-31.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-32.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-33.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-34.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-35.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-36.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-37.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-4.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-5.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-6.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-7.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-8.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-25-9.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-10.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-11.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-12.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-13.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-14.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-15.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-16.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-17.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-18.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-19.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-20.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-21.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-22.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-23.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-24.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-25.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-26.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-27.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-28.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-29.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-3.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-30.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-31.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-32.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-33.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-34.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-35.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-36.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-37.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-4.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-5.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-6.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-7.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-8.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/04-26-9.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/05-00-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/05-01-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/05-02-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/05-03-1.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/05-03-2.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/06-01-1.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/06-01-2.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/06-01-3.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/06-01-4.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/06-01-5.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/06-01-6.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/06-01-7.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/06-02-1.ltxps
%{_texdir}/texmf-dist/doc/latex/presentations/06-02-2.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/06-04-1.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/06-04-2.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/06-04-3.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/06-05-1.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/07-03-1.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/07-03-2.ltx
%{_texdir}/texmf-dist/doc/latex/presentations/07-03-3.ltxpd
%{_texdir}/texmf-dist/doc/latex/presentations/07-03-4.ltxb
%{_texdir}/texmf-dist/doc/latex/presentations/07-05-1.ltxbps
%{_texdir}/texmf-dist/doc/latex/presentations/07-05-2.ltxbps
%{_texdir}/texmf-dist/doc/latex/presentations/README
%{_texdir}/texmf-dist/doc/latex/presentations/Textdemo.tex
%{_texdir}/texmf-dist/doc/latex/presentations/beamer-demo.tex
%{_texdir}/texmf-dist/doc/latex/presentations/beamer-demo2.tex
%{_texdir}/texmf-dist/doc/latex/presentations/pd-demo-default.tex
%{_texdir}/texmf-dist/doc/latex/presentations/pd-demo.tex
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/FULogo.png
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/FULuft.jpg
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/FUbib.jpg
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/FUlogo.pdf
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/TU.jpg
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/TeX.pdf
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/beamer0.pdf
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/beamer1.pdf
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/beamer2.pdf
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/beamernavbar.png
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/beamernavsymbols.pdf
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/beamernavsymbols.tex
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/fu-berlin-air.pdf
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/fu-berlin.pdf
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/geo.jpg
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/ligaturen.png
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/multimedia.jpg
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/multimedia.png
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/multimedia.tex
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/silberlaube.jpg
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/silberlaube2.jpg
%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer/zedat.pdf
%{_texdir}/texmf-dist/doc/latex/presentations/images/pd/FULogo.eps
%{_texdir}/texmf-dist/doc/latex/presentations/images/pd/FULogo2.eps
%{_texdir}/texmf-dist/doc/latex/presentations/images/pd/FULogoRGB.eps
%{_texdir}/texmf-dist/doc/latex/presentations/images/pd/FULogo_RGB.eps
%{_texdir}/texmf-dist/doc/latex/presentations/images/pd/FUbib.eps
%{_texdir}/texmf-dist/doc/latex/presentations/images/pd/fuBIB10.eps
%{_texdir}/texmf-dist/doc/latex/presentations/images/pd/fuBIB10.pdf
%{_texdir}/texmf-dist/doc/latex/presentations/images/pd/logofbbw.eps
%{_texdir}/texmf-dist/doc/latex/presentations/images/pd/silberlaube.eps
%{_texdir}/texmf-dist/doc/latex/presentations/images/pd/silberlaube2.eps
%{_texdir}/texmf-dist/doc/latex/presentations/images/pd/wieesgeht.eps
%{_texdir}/texmf-dist/doc/latex/presentations/images/pd/zedat2.eps
%{_texdir}/texmf-dist/doc/latex/presentations/images/pdfscreen/Tore3d.pdf
%{_texdir}/texmf-dist/doc/latex/presentations/images/pdfscreen/mp.pdf
%{_texdir}/texmf-dist/doc/latex/presentations/images/pdfscreen/mpgraph.mps
%{_texdir}/texmf-dist/doc/latex/presentations/images/pdfscreen/pst.pdf
%{_texdir}/texmf-dist/doc/latex/presentations/images/pdfscreen/tex.png


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
