# revision 25523
# category Package
# catalog-ctan /macros/latex/contrib/l3experimental
# catalog-date 2012-02-26 23:34:26 +0100
# catalog-license lppl1.3
# catalog-version SVN 3471

%{!?_texdir: %global _texdir %{_datadir}/texlive}
%define _texmfdistdir %{_texdir}/texmf-dist

Name:		texlive-l3experimental
Version:	2011
Release:	2%{?dist}
Summary:	Experimental LaTeX3 concepts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/l3experimental
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3experimental.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3experimental.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3experimental.source.tar.xz
BuildArch:	noarch

%description
The l3experimental packages are a collection of experimental
implementations for aspects of the LaTeX3 kernel, dealing with
higher-level ideas such as the Designer Interface. Some of them
work as stand alone packages, providing new functionality, and
can be used on top of LaTeX2e with no changes to the existing
kernel. The present release includes: - l3dt: kernel support
for data tables; - l3galley: kernel support for xgalley; -
l3regex: kernel support for regular expression search and
replace operations; - l3sort: kernel support for sorting
sequences, token lists or comma-lists, according to user-
specified comparison criteria; - l3str: kernel support for
string manipulation; - xcoffins, which allows the alignment of
boxes using a series of 'handle' positions, supplementing the
simple TeX reference point; and - xgalley, which controls boxes
receiving text for typesetting. All the files of the bundle are
also available in the Subversion (SVN) repository of the LaTeX3
Project. The bundle on CTAN is based on a snapshot of the SVN
repository on 2012-01-19.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/l3experimental/l3dt/l3dt.sty
%{_texmfdistdir}/tex/latex/l3experimental/l3sort/l3sort.sty
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3flag.sty
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3regex-trace.sty
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3regex.sty
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str.sty
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3tl-analysis.sty
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3tl-build.sty
%{_texmfdistdir}/tex/latex/l3experimental/xcoffins/xcoffins.sty
%{_texmfdistdir}/tex/latex/l3experimental/xgalley/l3galley.sty
%{_texmfdistdir}/tex/latex/l3experimental/xgalley/xgalley.sty
%doc %{_texmfdistdir}/doc/latex/l3experimental/README
%doc %{_texmfdistdir}/doc/latex/l3experimental/l3dt/l3dt.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/l3sort/l3sort.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/l3str/l3flag.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/l3str/l3regex.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/l3str/l3str.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/l3str/l3tl-analysis.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/l3str/l3tl-build.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/xcoffins/xcoffins.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/xgalley/l3galley.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/xgalley/xgalley.pdf
#- source
%doc %{_texmfdistdir}/source/latex/l3experimental/l3dt/l3dt.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/l3dt/l3dt.ins
%doc %{_texmfdistdir}/source/latex/l3experimental/l3sort/l3sort.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/l3sort/l3sort.ins
%doc %{_texmfdistdir}/source/latex/l3experimental/l3str/l3flag.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/l3str/l3regex.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/l3str/l3str.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/l3str/l3str.ins
%doc %{_texmfdistdir}/source/latex/l3experimental/l3str/l3tl-analysis.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/l3str/l3tl-build.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/xcoffins/xcoffins.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/xcoffins/xcoffins.ins
%doc %{_texmfdistdir}/source/latex/l3experimental/xgalley/l3galley.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/xgalley/xgalley.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/xgalley/xgalley.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> SVN3471-2
+ Revision: 783481
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> SVN3471-1
+ Revision: 783033
- Update to latest release.

* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> SVN3341-1
+ Revision: 779590
- Update to latest release.

* Wed Feb 08 2012 Paulo Andrade <pcpa@mandriva.com.br> SVN3331-1
+ Revision: 772112
- Update to latest release.

* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> SVN3209-1
+ Revision: 770205
- Update to latest upstream package

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> SVN3109-1
+ Revision: 762635
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> SVN3036-2
+ Revision: 753069
- Rebuild to reduce used resources

* Sat Dec 17 2011 Paulo Andrade <pcpa@mandriva.com.br> SVN3036-1
+ Revision: 743255
- texlive-l3experimental

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> SVN2966-1
+ Revision: 739796
- texlive-l3experimental

* Sun Nov 06 2011 Paulo Andrade <pcpa@mandriva.com.br> SVN2900-1
+ Revision: 722015
- texlive-l3experimental
- texlive-l3experimental
- texlive-l3experimental
- texlive-l3experimental
- texlive-l3experimental

