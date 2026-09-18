Name:           hunspell-sv
Version:        2026.09.17
Release:        1%{?dist}
Summary:        Swedish dictionary for Hunspell
License:        LGPL-3.0-only
URL:            https://github.com/yeager/hunspell-sv
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/hunspell-sv-%{version}.tar.gz
Source1:        COPYING.LESSER
Source2:        COPYING
BuildArch:      noarch
BuildRequires:  python3
BuildRequires:  hunspell
Requires:       hunspell-filesystem

%description
Swedish spelling dictionary with affix and compound rules, including
vocabulary for software, information technology and modern Swedish.
The main sv_SE dictionary is installed for Hunspell-compatible applications.
The historical supplementary dictionary is included as example data.

%prep
%setup -q
cp -p %{SOURCE1} COPYING.LESSER
cp -p %{SOURCE2} COPYING

%build
python3 build.py --no-tm --output rebuilt.dic
cmp sv_SE.dic rebuilt.dic

%install
install -d %{buildroot}%{_datadir}/hunspell
install -m 0644 sv_SE.aff sv_SE.dic %{buildroot}%{_datadir}/hunspell/
install -d %{buildroot}%{_docdir}/%{name}/examples
install -m 0644 sv_SE_expanded.aff sv_SE_expanded.dic %{buildroot}%{_docdir}/%{name}/examples/

%check
python3 -m unittest discover -s tests -v

%files
%license LICENSE COPYING.LESSER COPYING
%doc README.md
%{_datadir}/hunspell/sv_SE.aff
%{_datadir}/hunspell/sv_SE.dic
%dir %{_docdir}/%{name}/examples
%{_docdir}/%{name}/examples/sv_SE_expanded.aff
%{_docdir}/%{name}/examples/sv_SE_expanded.dic

%changelog
* Thu Sep 17 2026 Daniel Nylander <github@danielnylander.se> - 2026.09.17-1
- Package upstream release with validated Swedish dictionaries
- Install supplementary dictionary as example data
