%global gem_name rspec

Summary: Behaviour driven development (BDD) framework for Ruby
Name: rubygem-%{gem_name}
Version: 2.11.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://rspec.info
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(rspec-core) >= %{version}
Requires: rubygem(rspec-mocks) >= %{version}
Requires: rubygem(rspec-expectations) >= %{version}
Requires: ruby(abi)  = 1.9.1
BuildRequires: rubygems-devel
BuildRequires: ruby(abi) = 1.9.1
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
RSpec is a behaviour driven development (BDD) framework for Ruby.  

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}

%files
%doc %{gem_docdir}
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/License.txt
%{gem_instdir}/README.md
%exclude %{gem_cache}
%{gem_spec}

%changelog
* Thu Oct 11 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.11.0-1
- Update to Rspec 2.11.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 05 2012 Vít Ondruch <bkabrda@redhat.com> - 2.8.0-1
- Update to RSpec 2.8.0.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Mar 09 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3.1-1
- Update from Marek Goldmann <mgoldman@redhat.com>
  - Updated to 1.3.1
  - Patch to make it work with Rake >= 0.9.0.beta.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 16 2010 Michael Stahnke <stahnma@fedpraproject.org> - 1.3.0-2
- Removed 404 URL in the description (bug 515042)

* Fri Apr 09 2010 Michael Stahnke <stahnma@fedpraproject.org> - 1.3.0-1
- Updated to 1.3.0

* Wed Dec 09 2009 Michael Stahnke <stahnma@fedoraproject.org> - 1.2.9-1
- New Version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Michael Stahnke <stahnma@fedoraproject.org> - 1.2.7-1
- New Version

* Fri Mar 27 2009 Michael Stahnke <stahnma@fedoraproject.org> - 1.2.2-1
- New Version 

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 08 2008 Michael Stahnke <stahnma@fedoraproject.org> - 1.1.11-1
- New Version

* Mon Nov 03 2008 Michael Stahnke <stahnma@fedoraproject.org> - 1.1.8-3
- Updating to require ruby(abi)

* Mon Oct 13 2008 Michael Stahnke <stahnma@fedoraproject.org> - 1.1.8-1
- New version

* Wed May 14 2008 Michael Stahnke <stahnma@fedoraproject.org> - 1.1.3-1
- Initial package
