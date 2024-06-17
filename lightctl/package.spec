# Generated by rust2rpm 26
%bcond_without check

# prevent library files from being installed
%global cargo_install_lib 0

Name:           lightctl
Version:        0.1.1
Release:        %autorelease
Summary:        Simple utility to control backlight devices on Linux through logind
License:        MIT
URL:            https://github.com/blurrycat/lightctl
Source:         https://github.com/blurrycat/lightctl/archive/refs/tags/v0.1.1.tar.gz
BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n lightctl-%{version} -p1
%{__cargo} vendor
%{__mkdir} -p .cargo
cat > .cargo/config.toml << EOF
[profile.rpm]
inherits = "release"
opt-level = %{rustflags_opt_level}
codegen-units = %{rustflags_codegen_units}
debug = %{rustflags_debuginfo}
strip = "none"

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%cargo_build

%install
%cargo_install

%files
%license LICENSE
%doc README.md
%{_bindir}/lightctl

%changelog
%autochangelog
