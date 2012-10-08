%global githash 726325d
%global gitdate 20100625
#global posttag .%{?gitdate}git%{?githash}

Name:		qoauth
Version:	1.0.1
Release:	4%{?posttag}%{?dist}
Summary:	Qt-based C++ library for OAuth authorization scheme
Group:		System Environment/Libraries
License:	LGPLv2+
URL:		http://github.com/ayoy/qoauth
Source0:	http://files.ayoy.net/qoauth/release/%{version}/src/%{name}-%{version}-src.tar.bz2
BuildRequires:	qt4-devel qca2-devel doxygen
BuildRequires:	qca-ossl
Requires:	qca-ossl%{?_isa}

%description
QOAuth is a Qt-based C++ implementation of an interface to services using
OAuth authorization scheme.

%package devel
Summary:	Development files for the Qt OAuth support library
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	qt4-devel%{?_isa}
Requires:	qca2-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries, header files and documentations 
for developing applications that use QOAuth library. 

%prep
%setup -q -n %{name}-%{version}-src
sed -i -e '/^ *docs \\$/d' \
       -e "s!\(\$\${INSTALL_PREFIX}\)/lib.*!%{_libdir}!" src/src.pro
sed -i -e 's\/lib\/%{_lib}\g' src/pcfile.sh

%build
export PATH=%{_qt4_bindir}:$PATH
%{_qt4_qmake} PREFIX="%{_prefix}"
make %{?_smp_mflags}

doxygen Doxyfile
# fix the time stamp
for file in doc/html/*; do
	touch -r Doxyfile $file
done

%install
make install INSTALL="install -p" INSTALL_ROOT=%{buildroot}
magic_rpm_clean.sh

%check
make check || :

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README CHANGELOG LICENSE
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc doc/html doc/examples
%{_libdir}/*.so
%{_libdir}/*.prl
%{_libdir}/pkgconfig/*.pc
%{_qt4_prefix}/mkspecs/features/*.prf
%{_includedir}/*

%changelog
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 08 2010 Chen Lei <supercyper@163.com> - 1.0.1-1
- Update to 1.0.1

* Fri Jun 25 2010 Chen Lei <supercyper@163.com> - 1.0.1-0.3.20100625git726325d
- New upstream version

* Tue Jun 22 2010 Chen Lei <supercyper@163.com> - 1.0.1-0.2.20100622git7f69e33
- New upstream version
- Add %%check section

* Tue May 25 2010 Chen Lei <supercyper@163.com> - 1.0.1-0.1.20100525gitec7e4d5
- initial rpm build
