%define debug_package %{nil}
%define upstreamversion 0.9.5

Name:    jsonnet
Version: 0.9.5
Release: 1%{?dist}
Summary: Jsonnet - The data templating language
License: ASL 2.0
URL:     http://jsonnet.org

Source0: https://github.com/google/jsonnet/releases/download/v%{upstreamversion}/jsonnet-%{upstreamversion}.tar.gz

%description

Jsonnet is a domain specific configuration language that
helps you define JSON data. Jsonnet lets you compute fragments
of JSON within the structure, bringing the same benefit to
structured data that templating languages bring to plain text.

%prep
%setup

%build
make

%install
mkdir -vp %{buildroot}/usr/bin
install -m 755 jsonnet %{buildroot}/usr/bin/jsonnet

%files
%defattr(-,root,root,-)
/usr/bin/jsonnet
