Name:		manslide
Summary:	Graphical slideshow creation program
Version:	2.0.3
Release:	5
Source0:	http://www.mandrivalinux-online.eu/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.kde-apps.org/content/show.php?content=72739
Group:		Graphics
License:	GPLv2+

BuildRequires:	qt4-devel
Requires:	sox
Requires:	imagemagick
Requires:	mencoder
Requires:	mplayer

%description
Manslide is a slideshow creation application which makes it easy to
produce attractive slideshows with optional background music. Manslide
uses the QT4 toolkit.

%prep
%setup -q

%build
%qmake_qt4
%make

%install
install -m755 Manslide -D %{buildroot}%{_datadir}/%{name}/%{name}
install -m644 *.qm %{buildroot}%{_datadir}/%{name}/
install -m644 *.ts %{buildroot}%{_datadir}/%{name}/
cp -R Interface %{buildroot}%{_datadir}/%{name}/
cp -R BIB_ManSlide %{buildroot}%{_datadir}/%{name}/
install -d %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Manslide
Comment=Slideshow generator
Exec=%{_bindir}/%{name} 
Icon=image_processing_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Graphics;Qt;Photography;X-MandrivaLinux-CrossDesktop;
EOF

%files
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
