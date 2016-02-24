Summary:	xrandr application - command-line interface to RandR extension
Summary(pl.UTF-8):	Aplikacja xrandr - interfejs linii poleceń do rozszerzenia RandR
Name:		xorg-app-xrandr
Version:	1.5.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xrandr-%{version}.tar.bz2
# Source0-md5:	ebffac98021b8f1dc71da0c1918e9b57
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXrandr-devel >= 1.5
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	xorg-lib-libXrandr >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xrandr is used to set the size, orientation and/or reflection of the
outputs for a screen.

%description -l pl.UTF-8
xrandr służy do ustawiania rozmiaru, orientacji i/lub odbicia wyjścia
ekranu.

%package -n xorg-app-xkeystone
Summary:	xkeystone application to help setting keystone effect correction
Summary(pl.UTF-8):	Aplikacja xkeystone pomagająca ustawić korekcję efektu trapezu
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nickle-cairo

%description -n xorg-app-xkeystone
xkeystone application to help setting keystone effect correction.

%description -n xorg-app-xkeystone -l pl.UTF-8
Aplikacja xkeystone pomagająca ustawić korekcję efektu trapezu.

%prep
%setup -q -n xrandr-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__sed} -i -e '1s,/usr/bin/env nickle,/usr/bin/nickle,' $RPM_BUILD_ROOT%{_bindir}/xkeystone

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xrandr
%{_mandir}/man1/xrandr.1*

%files -n xorg-app-xkeystone
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xkeystone
