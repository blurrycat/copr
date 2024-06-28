Name:           mcfly
Version:        0.9.0
Release:        %autorelease
Summary:        Fly through your shell history.
License:        MIT
URL:            https://github.com/cantino/mcfly
Source:         https://github.com/cantino/mcfly/archive/refs/tags/v0.9.0.tar.gz
BuildRequires:  cargo

%description
McFly replaces your default ctrl-r shell history search with an intelligent search engine
that takes into account your working directory and the context of recently executed commands.
McFly's suggestions are prioritized in real time with a small neural network.

%prep
%autosetup -n mcfly-%{version} -p1
cargo fetch --locked

%build
cargo build --frozen --release

%install
install -Dm 755 "target/release/mcfly" -t "%{buildroot}/%{_bindir}/mcfly"

%check
cargo test --frozen

%files
%license LICENSE
%doc README.md
%{_bindir}/mcfly

%changelog
%autochangelog
