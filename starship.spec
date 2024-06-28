Name:           starship
Version:        1.19.0
Release:        %autorelease
Summary:        The minimal, blazing-fast, and infinitely customizable prompt for any shell!
License:        ISC
URL:            https://github.com/starship/starship
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(openssl)

%description
The minimal, blazing-fast, and infinitely customizable prompt for any shell!

  - Fast: it's fast - really really fast!
  - Customizable: configure every aspect of your prompt.
  - Universal: works on any shell, on any operating system.
  - Intelligent: shows relevant information at a glance.
  - Feature rich: support for all your favorite tools.
  - Easy: quick to install - start using it in minutes.


%prep
%autosetup
cargo fetch --locked

%build
cargo build --frozen --release

%install
install -Dm 755 "target/release/%{name}" -t "%{buildroot}/%{_bindir}/"

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
%autochangelog
