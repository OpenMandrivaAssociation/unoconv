Summary:	Tool to convert between any document format supported by LibreOffice

Name:		unoconv
Version:	0.6
Release:	4
License:	GPLv2
Group:		File tools
URL:		http://dag.wieers.com/home-made/unoconv/
Source0:	http://dag.wieers.com/home-made/%{name}/%{name}-%{version}.tar.gz
BuildArch:	noarch

Requires:	libreoffice-common
Requires:	libreoffice-pyuno

%description
unoconv converts between any document format that LibreOffice understands.
It uses LibreOffice's UNO bindings for non-interactive conversion of
documents.

Supported document formats include Open Document Format (.odf), MS Word (.doc),
MS Office Open/MS OOXML (.xml), Portable Document Format (.pdf), HTML, XHTML,
RTF, Docbook (.xml), and more.

%prep
%setup -q
%apply_patches

%build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING README.asciidoc WISHLIST tests/
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


