Name:       @NAME@

BuildArch: noarch

Summary:    @SUMMARY@
Version:    @VER@
Release:    1
Group:      Qt/Qt
License:    @LICENSE@
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
#\\ifdef SFOS_VERSION
Requires: sailfish-version == @SFOS_VERSION@
#\\endif

%description
@DESCRIPTION@

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/patchmanager/patches/%Name
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/%Name

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/%Name ]; then
/usr/sbin/patchmanager -u %Name || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/%Name ]; then
/usr/sbin/patchmanager -u %Name || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%Name
