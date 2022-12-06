%global plugin_name googlechat

%global commit0 b6b824a4764b51316f7be325492575684647e021
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20221106

Name: purple-%{plugin_name}
Version: 0
Release: 1.%{date}git%{shortcommit0}%{?dist}
Epoch: 0

License: GPLv3+
Summary: Google Chat plugin for libpurple
URL: https://github.com/EionRobb/%{name}
Source0: %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
#https://github.com/EionRobb/purple-googlechat/archive/b6b824a4764b51316f7be325492575684647e021.zip

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libprotobuf-c)
BuildRequires: pkgconfig(purple)

BuildRequires: gcc
BuildRequires: make

Provides: purple-hangouts = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: purple-hangouts < %{?epoch:%{epoch}:}%{version}-%{release}

%package -n pidgin-%{plugin_name}
Summary: Google Chat (Hangouts replacement) pictures, emojis andicons for Pidgin
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: pidgin

%description
Adds support for Google Chat to Pidgin, Adium, Finch and other messengers based
on libpurple.

%description -n pidgin-%{plugin_name}
Adds pixmaps, icons and smileys for Hangouts protocol implemented by
hangouts-purple.

%prep
%autosetup -n %{name}-%{commit0}

%build
%set_build_flags
%make_build

%install
%make_install
chmod 755 %{buildroot}%{_libdir}/purple-2/lib%{plugin_name}.so

%files
%{_libdir}/purple-2/lib%{plugin_name}.so
%license LICENSE
%doc README.md

%files -n pidgin-%{plugin_name}
%{_datadir}/pixmaps/pidgin/protocols/*/%{plugin_name}.png

%changelog
* Tue Dec 06 2022 Marcus Müller <marcus@hostalia.de> - 0:0-1.20221106gitb6b824a
- Make this package supersede purple-hangouts, provide it

* Tue Dec 06 2022 Marcus Müller <marcus@hostalia.de> - 0:0-0.20221106gitb6b824a
- First SPEC version, heavily based on purple-hangouts SPEC
