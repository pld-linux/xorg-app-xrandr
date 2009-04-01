Summary:	xrandr application - command-line interface to RandR extension
Summary(pl.UTF-8):	Aplikacja xrandr - interfejs linii poleceń do rozszerzenia RandR
Name:		xorg-app-xrandr
Version:	1.3.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xrandr-%{version}.tar.bz2
# Source0-md5:	616612a15711a4422e71be6acc42ca3c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXrandr-devel >= 1.2.99.3
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-lib-libXrandr >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xrandr is used to set the size, orientation and/or reflection of the
outputs for a screen.

%description -l pl.UTF-8
xrandr służy do ustawiania rozmiaru, orientacji i/lub odbicia wyjścia
ekranu.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xkeystone
%attr(755,root,root) %{_bindir}/xrandr
%{_mandir}/man1/xrandr.1x*
