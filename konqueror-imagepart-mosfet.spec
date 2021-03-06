%define		_name	mosfet-imagepart
Summary:	pixieplus - image viewer for KDE
Summary(pl.UTF-8):	pixieplus - przeglądarka obrazków dla KDE
Name:		konqueror-imagepart-mosfet
Version:	0.2.1
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.mosfet.org/%{_name}/%{_name}-%{version}.tar.gz
# Source0-md5:	bad62081abec0d1279ac2577fdc95a61
URL:		http://www.mosfet.org/mosfet-imagepart/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	qt-devel >= 6:3.1
BuildRequires:	libtool
BuildRequires:	libltdl-devel
Requires:	kdelibs >= 3.1
Requires:	qt >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
Pixie is designed to allow you to efficently browse, manage, and view
large numbers of images as well as do basic editing such as adjust
contrast/brightness, scale, and apply effects. For Windows users, you
can think of it as a combination of ACDSee(TM) and Paint Shop Pro(TM).

%description -l pl.UTF-8
Pixie jest narzędziem służącym do przeglądania i zarządzania dużą
ilością plików graficznych umożliwiającym prostą edycję obrazów
(poziomy jasności i kontrastu, skalowanie oraz efekty dodatkowe).

%prep
%setup -q -n %{_name}-%{version}

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CFLAGS="%{rpmcflags}" CXXFLAGS="%{rpmcflags}"
#%%{__make} -f Makefile.cvs
%configure	\
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mosfetwallpaper
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_datadir}/services/mosfetimage.desktop
