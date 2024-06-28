Name:           lightctl
Version:        0.1.1
Release:        %autorelease
Summary:        Simple utility to control backlight devices on Linux through logind
License:        MIT
URL:            https://github.com/blurrycat/lightctl
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo

%description 
Simple utility to control backlight devices on Linux through logind

%prep
%autosetup
cargo fetch --locked

%build
cargo build --frozen --release

%install
install -Dm 755 "target/release/lightctl" -t "%{buildroot}/%{_bindir}/"

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
