%define name		manslide
%define origname	Manslide
%define	version		1.6
%define	release		%mkrel 1

Name:		%{name}
Summary:	Graphical slideshow creation program
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.kde-apps.org/content/show.php/Manslide?content=52227
Group:		Graphics
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2+

BuildRequires:	libqt4-devel
Requires:	sox
Requires:	ImageMagick
Requires:	mencoder
Requires:	mplayer

%description
Manslide is a slideshow creation application which makes it easy to
produce attractive slideshows with optional background music. Manslide
uses the QT4 toolkit.

%prep
%setup -q -n %origname-%version

%build
PATH=/usr/lib/qt4/bin:$PATH qmake
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" %make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install Manslide %{buildroot}%{_bindir}/manslide

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Manslide
Comment=Slideshow generator
Exec=%{_bindir}/%{name} 
Icon=image_processing_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Graphics;Qt;Photography;
EOF

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
