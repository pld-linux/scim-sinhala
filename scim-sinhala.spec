Summary:	SCIM IMEngine module for Sinhala input
Summary(pl.UTF-8):	Silnik IM SCIM dla metody wprowadzania znaków syngaleskich
Name:		scim-sinhala
Version:	0.1.0
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://osdn.jp/projects/scim-imengine/releases/p4040
Source0:	http://dl.osdn.jp/scim-imengine/16666/%{name}-%{version}.tar.gz
# Source0-md5:	180f11e667b7998e612364a405d73b87
Patch0:		%{name}-no-rpath.patch
URL:		https://osdn.jp/projects/scim-imengine/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	scim-devel >= 1.0
Requires:	scim >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCIM IMEngine module for Sinhala input.

%description -l pl.UTF-8
Silnik IM SCIM dla metody wprowadzania znaków syngaleskich.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.la

# empty translations only (as of 0.1.0)
#find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
# -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/sinhala.so
%{_datadir}/scim/icons/scim-sinhala.png
