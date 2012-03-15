# revision 25525
# category Package
# catalog-ctan /macros/latex/contrib/l3kernel
# catalog-date 2012-02-26 23:34:26 +0100
# catalog-license lppl1.3
# catalog-version SVN 3471

%{!?_texdir: %global _texdir %{_datadir}/texlive}
%define _texmfdistdir %{_texdir}/texmf-dist

Name:		texlive-l3kernel
Version:	2011
Release:	2%{?dist}
Summary:	LaTeX3 programming conventions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/l3kernel
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel.source.tar.xz
BuildArch:	noarch

%description
The l3kernel bundle provides an implementation of the LaTeX3
programmers' interface, as a set of packages that run under
LaTeX 2e. The interface provides the foundation on which the
LaTeX3 kernel and other future code are built: it is an API for
TeX programmers. The packages are set up so that the LaTeX3
conventions can be used with regular LaTeX 2e packages. All the
files of the bundle are also available in the Subversion (SVN)
repository of the LaTeX3 Project. The bundle on CTAN is based
on a snapshot of the SVN repository on 2012-02-26.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/l3kernel/l3doc.ist
%{_texmfdistdir}/tex/latex/l3kernel/expl3.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3basics.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3bootstrap.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3box.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3clist.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3coffins.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3color.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3doc.cls
%{_texmfdistdir}/tex/latex/l3kernel/l3expan.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3file.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3fp.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3int.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3keys.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3luatex.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3msg.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3names.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3prg.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3prop.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3quark.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3seq.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3skip.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3tl.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3token.sty
%doc %{_texmfdistdir}/doc/latex/l3kernel/README
%doc %{_texmfdistdir}/doc/latex/l3kernel/expl3.pdf
%doc %{_texmfdistdir}/doc/latex/l3kernel/interface3.pdf
%doc %{_texmfdistdir}/doc/latex/l3kernel/interface3.tex
%doc %{_texmfdistdir}/doc/latex/l3kernel/l3styleguide.pdf
%doc %{_texmfdistdir}/doc/latex/l3kernel/l3styleguide.tex
%doc %{_texmfdistdir}/doc/latex/l3kernel/l3syntax-changes.pdf
%doc %{_texmfdistdir}/doc/latex/l3kernel/l3syntax-changes.tex
%doc %{_texmfdistdir}/doc/latex/l3kernel/source3.pdf
%doc %{_texmfdistdir}/doc/latex/l3kernel/source3.tex
%doc %{_texmfdistdir}/doc/latex/l3kernel/source3body.tex
#- source
%doc %{_texmfdistdir}/source/latex/l3kernel/expl3.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3alloc.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3basics.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3bootstrap.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3box.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3clist.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3coffins.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3color.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3doc.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3drivers.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3expan.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3file.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3final.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3fp.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3int.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3keys.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3luatex.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3msg.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3names.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3prg.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3prop.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3quark.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3seq.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3skip.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3tl.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3token.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3tree.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:SVN3471-2
+ Revision: 783481
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:SVN3471-1
+ Revision: 783035
- Update to latest release.

* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:SVN3341-1
+ Revision: 779591
- Update to latest release.

* Wed Feb 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:SVN3331-1
+ Revision: 772113
- Update to latest release.

* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 3209-1
+ Revision: 770206
- Update to latest upstream package

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 3109-1
+ Revision: 762636
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 3036-2
+ Revision: 753070
- Rebuild to reduce used resources

* Sat Dec 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 3036-1
+ Revision: 743256
- texlive-l3kernel

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 2966-1
+ Revision: 739798
- texlive-l3kernel
- texlive-l3kernel

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2900-1
+ Revision: 718797
- texlive-l3kernel
- texlive-l3kernel
- texlive-l3kernel
- texlive-l3kernel

