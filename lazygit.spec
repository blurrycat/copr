%global debug_package %{nil}

Name:           lazygit
Version:        0.42.0
Release:        %autorelease
Summary:        Simple terminal UI for git commands
License:        MIT
URL:            https://github.com/jesseduffield/lazygit
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  golang
BuildRequires:  git-core

%description
Simple terminal UI for git commands

%prep
%autosetup

%build
go get
go build \
    -ldflags "-X main.version=%{version}" \
    -o %{name}.bin

%install
install -Dpm 0755 %{name}.bin %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc docs/ README.md
%{_bindir}/%{name}

%changelog
%autochangelog
