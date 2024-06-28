%global forgeurl https://git.sr.ht/~kennylevinsen/poweralertd

Name:           poweralertd
Version:        0.3.0
Release:        1%{?dist}
Summary:        UPower-powered power alerter

License:        GPL-3.0-only
URL:            https://sr.ht/~kennylevinsen/poweralertd
Source:         https://git.sr.ht/~kennylevinsen/poweralertd/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires: upower

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(systemd)

%description
%{summary}.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_userunitdir}/%{name}.service


%changelog
%autochangelog

