Name:           usbredir
Version:        0.3.3
Release:        2%{?dist}
Summary:        USB network redirection protocol libraries
Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://spice-space.org/page/UsbRedir
Source0:        http://spice-space.org/download/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:  libusb1-devel >= 1.0.9

%description
usbredir is a protocol for redirection USB traffic from a single USB device,
to a different (virtual) machine then the one to which the USB device is
attached. This package contains a number of libraries to help implementing
support for usbredir:

usbredirparser:
A library containing the parser for the usbredir protocol

usbredirhost:
A library implementing the usb-host side of a usbredir connection.
All that an application wishing to implement an usb-host needs to do is:
* Provide a libusb device handle for the device
* Provide write and read callbacks for the actual transport of usbredir data
* Monitor for usbredir and libusb read/write events and call their handlers


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        server
Summary:        Simple usb-host tcp server
Group:          System Environment/Daemons
License:        GPLv2+
Requires:       %{name} = %{version}-%{release}

%description    server
A simple usb-host tcp server, using libusbredirhost.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/libusbredir*.la


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING.LIB README TODO 
%{_libdir}/libusbredir*.so.*

%files devel
%defattr(-,root,root,-)
%doc usb-redirection-protocol.txt README.multi-thread
%{_includedir}/usbredir*.h
%{_libdir}/libusbredir*.so
%{_libdir}/pkgconfig/libusbredir*.pc

%files server
%defattr(-,root,root,-)
%doc COPYING
%{_sbindir}/usbredirserver


%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 0.3.3-2
- 为 Magic 3.0 重建

* Thu Jan 12 2012 Hans de Goede <hdegoede@redhat.com> - 0.3.3-1
- Update to upstream 0.3.3 release

* Tue Jan  3 2012 Hans de Goede <hdegoede@redhat.com> 0.3.2-1
- Update to upstream 0.3.2 release

* Wed Aug 24 2011 Hans de Goede <hdegoede@redhat.com> 0.3.1-1
- Update to upstream 0.3.1 release

* Thu Jul 14 2011 Hans de Goede <hdegoede@redhat.com> 0.3-1
- Initial Fedora package
