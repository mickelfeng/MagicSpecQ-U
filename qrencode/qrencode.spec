Name:           qrencode
Version:        3.2.0
Release:        1%{?dist}
Summary:        Generate QR 2D barcodes

Group:          Applications/Engineering
License:        LGPLv2+
URL:            http://megaui.net/fukuchi/works/qrencode/index.en.html
Source0:        http://megaui.net/fukuchi/works/qrencode/%{name}-%{version}.tar.gz

BuildRequires:  libpng-devel chrpath


%description
Qrencode is a utility software using libqrencode to encode string data in
a QR Code and save as a PNG image.

%package        devel
Summary:        QR Code encoding library - Development files
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The qrencode-devel package contains libraries and header files for developing
applications that use qrencode.

%prep
%setup -q


%build
%configure --with-tests
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -rf $RPM_BUILD_ROOT%{_libdir}/libqrencode.la
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/qrencode

%check
cd ./tests
sh test_all.sh


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc ChangeLog COPYING NEWS README TODO
%{_bindir}/qrencode
%{_mandir}/man1/qrencode.1.*
%{_libdir}/libqrencode.so.*

%files devel
%{_includedir}/qrencode.h
%{_libdir}/libqrencode.so
%{_libdir}/pkgconfig/libqrencode.pc


%changelog
* Sun Jan 15 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 3.2.0-1
- update to 3.2.0
- remove BuildRoot tag in spec file
- remove "rm -rf $RPM_BUILD_ROOT" at the beginning of %%install section
- remove %%clean section
- remove %%defattr lines
- add a joker for libqrencode.so.* files

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.1.1-6
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 13 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 3.1.1-4
- Fixed the rpath problem.

* Mon Jul 12 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 3.1.1-3
- Fixed some small spec mistakes.

* Mon Jul 12 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 3.1.1-2
- Fixed some small errors.

* Thu Jul 08 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 3.1.1-1
- Initial build.
