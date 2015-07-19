%define debug_package %{nil}

Name: kfileaudiopreview
Version: 4.99.0
Release: 5
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: Plugin interface for audio previews
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Phonon4Qt5)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Service)
BuildRequires: ninja

%description
Plugin interface for audio previews

%prep
%setup -q
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files
%{_libdir}/plugins/*.so
