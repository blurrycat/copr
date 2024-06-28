Name:           mcfly
Version:        0.9.0
Release:        %autorelease
Summary:        Replaces your default ctrl-r shell history search with an intelligent search engine that takes into account your working directory and the context of recently executed commands
License:        MIT

URL:            https://github.com/cantino/mcfly
Source:         https://github.com/cantino/mcfly/archive/refs/tags/v0.9.0.tar.gz

BuildRequires:  cargo

%prep
cargo fetch --locked

%build
cargo build --frozen --release

%install
install -Dm 755 "target/release/mcfly" -t "%{_bindir}/mcfly"

%check
cargo test --frozen

%files
%license LICENSE
%doc README.md
%{_bindir}/mcfly

%changelog
%autochangelog
