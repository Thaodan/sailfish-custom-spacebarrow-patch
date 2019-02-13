Name:       sailfishos-patch-custom-spacebarrow

BuildArch: noarch

Summary:    A patch to add ! , ? to SpacebarRow as accents to the . button
Version:    0.1
Release:    1
Group:      Qt/Qt
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
BuildRequires: shpp

%description
A patch to add ! , ? to SpacebarRow as accents to the . button

%prep
%setup -q -n %{name}-%{version}

%build
make
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%{name}
