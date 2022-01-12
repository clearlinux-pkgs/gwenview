#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : gwenview
Version  : 21.12.1
Release  : 38
URL      : https://download.kde.org/stable/release-service/21.12.1/src/gwenview-21.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.12.1/src/gwenview-21.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.12.1/src/gwenview-21.12.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: gwenview-bin = %{version}-%{release}
Requires: gwenview-data = %{version}-%{release}
Requires: gwenview-lib = %{version}-%{release}
Requires: gwenview-license = %{version}-%{release}
Requires: gwenview-locales = %{version}-%{release}
Requires: cfitsio
Requires: libkdcraw
BuildRequires : baloo-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : cfitsio-dev
BuildRequires : exiv2-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : kactivities-dev
BuildRequires : kfilemetadata-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libkdcraw-dev
BuildRequires : libkipi-dev
BuildRequires : libpng-dev
BuildRequires : phonon-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(lcms2)
BuildRequires : purpose-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : tiff-dev

%description
The Independent JPEG Group's JPEG software
==========================================

%package bin
Summary: bin components for the gwenview package.
Group: Binaries
Requires: gwenview-data = %{version}-%{release}
Requires: gwenview-license = %{version}-%{release}

%description bin
bin components for the gwenview package.


%package data
Summary: data components for the gwenview package.
Group: Data

%description data
data components for the gwenview package.


%package doc
Summary: doc components for the gwenview package.
Group: Documentation

%description doc
doc components for the gwenview package.


%package lib
Summary: lib components for the gwenview package.
Group: Libraries
Requires: gwenview-data = %{version}-%{release}
Requires: gwenview-license = %{version}-%{release}

%description lib
lib components for the gwenview package.


%package license
Summary: license components for the gwenview package.
Group: Default

%description license
license components for the gwenview package.


%package locales
Summary: locales components for the gwenview package.
Group: Default

%description locales
locales components for the gwenview package.


%prep
%setup -q -n gwenview-21.12.1
cd %{_builddir}/gwenview-21.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641949927
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1641949927
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gwenview
cp %{_builddir}/gwenview-21.12.1/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/gwenview/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/gwenview-21.12.1/COPYING %{buildroot}/usr/share/package-licenses/gwenview/a21ac62aee75f8fcb26b1de6fc90e5eea271854c
cp %{_builddir}/gwenview-21.12.1/COPYING.DOC %{buildroot}/usr/share/package-licenses/gwenview/1bd373e4851a93027ba70064bd7dbdc6827147e1
pushd clr-build
%make_install
popd
%find_lang gwenview

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gwenview
/usr/bin/gwenview_importer

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.gwenview.desktop
/usr/share/gwenview/color-schemes/fullscreen.colors
/usr/share/gwenview/cursors/zoom.png
/usr/share/gwenview/images/background.png
/usr/share/icons/hicolor/128x128/actions/document-share.png
/usr/share/icons/hicolor/128x128/apps/gwenview.png
/usr/share/icons/hicolor/16x16/actions/document-share.png
/usr/share/icons/hicolor/16x16/apps/gwenview.png
/usr/share/icons/hicolor/22x22/actions/document-share.png
/usr/share/icons/hicolor/22x22/apps/gwenview.png
/usr/share/icons/hicolor/32x32/actions/document-share.png
/usr/share/icons/hicolor/32x32/apps/gwenview.png
/usr/share/icons/hicolor/48x48/actions/document-share.png
/usr/share/icons/hicolor/48x48/apps/gwenview.png
/usr/share/icons/hicolor/64x64/actions/document-share.png
/usr/share/icons/hicolor/64x64/apps/gwenview.png
/usr/share/kconf_update/gwenview-imageview-alphabackgroundmode-update.pl
/usr/share/kconf_update/gwenview.upd
/usr/share/kservices5/gvpart.desktop
/usr/share/metainfo/org.kde.gwenview.appdata.xml
/usr/share/qlogging-categories5/gwenview.categories
/usr/share/solid/actions/gwenview_importer.desktop
/usr/share/solid/actions/gwenview_importer_camera.desktop

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/gwenview/browse_mode.png
/usr/share/doc/HTML/ca/gwenview/index.cache.bz2
/usr/share/doc/HTML/ca/gwenview/index.docbook
/usr/share/doc/HTML/ca/gwenview/modified-bar.png
/usr/share/doc/HTML/ca/gwenview/start-page.png
/usr/share/doc/HTML/ca/gwenview/view_mode.png
/usr/share/doc/HTML/de/gwenview/browse_mode.png
/usr/share/doc/HTML/de/gwenview/fullscreen_mode.png
/usr/share/doc/HTML/de/gwenview/index.cache.bz2
/usr/share/doc/HTML/de/gwenview/index.docbook
/usr/share/doc/HTML/de/gwenview/view_mode.png
/usr/share/doc/HTML/en/gwenview/browse_mode.png
/usr/share/doc/HTML/en/gwenview/fullscreen-browse.png
/usr/share/doc/HTML/en/gwenview/fullscreen-view.png
/usr/share/doc/HTML/en/gwenview/importer-picking-root-folder.png
/usr/share/doc/HTML/en/gwenview/importer.png
/usr/share/doc/HTML/en/gwenview/index.cache.bz2
/usr/share/doc/HTML/en/gwenview/index.docbook
/usr/share/doc/HTML/en/gwenview/modified-bar.png
/usr/share/doc/HTML/en/gwenview/start-page.png
/usr/share/doc/HTML/en/gwenview/view_mode.png
/usr/share/doc/HTML/es/gwenview/index.cache.bz2
/usr/share/doc/HTML/es/gwenview/index.docbook
/usr/share/doc/HTML/id/gwenview/index.cache.bz2
/usr/share/doc/HTML/id/gwenview/index.docbook
/usr/share/doc/HTML/it/gwenview/browse_mode.png
/usr/share/doc/HTML/it/gwenview/fullscreen-browse.png
/usr/share/doc/HTML/it/gwenview/fullscreen-view.png
/usr/share/doc/HTML/it/gwenview/importer-picking-root-folder.png
/usr/share/doc/HTML/it/gwenview/importer.png
/usr/share/doc/HTML/it/gwenview/index.cache.bz2
/usr/share/doc/HTML/it/gwenview/index.docbook
/usr/share/doc/HTML/it/gwenview/modified-bar.png
/usr/share/doc/HTML/it/gwenview/start-page.png
/usr/share/doc/HTML/it/gwenview/view_mode.png
/usr/share/doc/HTML/nl/gwenview/index.cache.bz2
/usr/share/doc/HTML/nl/gwenview/index.docbook
/usr/share/doc/HTML/pt/gwenview/index.cache.bz2
/usr/share/doc/HTML/pt/gwenview/index.docbook
/usr/share/doc/HTML/pt_BR/gwenview/index.cache.bz2
/usr/share/doc/HTML/pt_BR/gwenview/index.docbook
/usr/share/doc/HTML/sr/gwenview/index.cache.bz2
/usr/share/doc/HTML/sr/gwenview/index.docbook
/usr/share/doc/HTML/sv/gwenview/index.cache.bz2
/usr/share/doc/HTML/sv/gwenview/index.docbook
/usr/share/doc/HTML/uk/gwenview/browse_mode.png
/usr/share/doc/HTML/uk/gwenview/fullscreen-browse.png
/usr/share/doc/HTML/uk/gwenview/fullscreen-view.png
/usr/share/doc/HTML/uk/gwenview/importer-picking-root-folder.png
/usr/share/doc/HTML/uk/gwenview/importer.png
/usr/share/doc/HTML/uk/gwenview/index.cache.bz2
/usr/share/doc/HTML/uk/gwenview/index.docbook
/usr/share/doc/HTML/uk/gwenview/modified-bar.png
/usr/share/doc/HTML/uk/gwenview/start-page.png
/usr/share/doc/HTML/uk/gwenview/view_mode.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgwenviewlib.so.4.97.0
/usr/lib64/libgwenviewlib.so.5
/usr/lib64/qt5/plugins/kf5/kfileitemaction/slideshowfileitemaction.so
/usr/lib64/qt5/plugins/kf5/parts/gvpart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gwenview/1bd373e4851a93027ba70064bd7dbdc6827147e1
/usr/share/package-licenses/gwenview/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/gwenview/a21ac62aee75f8fcb26b1de6fc90e5eea271854c

%files locales -f gwenview.lang
%defattr(-,root,root,-)

