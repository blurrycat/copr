Name:           mise
Version:        2024.6.6
Release:        %autorelease
Summary:        The front-end to your dev env
License:        MIT
URL:            https://github.com/jdx/mise
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo
BuildRequires:  pkgconfig(openssl)

%description
The front-end to your dev env

%prep
%autosetup
cargo fetch --locked

%build
cargo build --frozen --release

%install
install -Dm 755 "target/release/%{name}" -t "%{buildroot}/%{_bindir}/"
install -Dm 644 "man/man1/%{name}.1" -t "%{buildroot}/%{_mandir}/man1/"
install -Dm 644 "completions/%{name}.bash" "%{buildroot}/usr/share/bash-completion/completions/%{name}"

%files
%license LICENSE
%doc README.md
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
/usr/share/bash-completion/completions/%{name}

%changelog
%autochangelog
