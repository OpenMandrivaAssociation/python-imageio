%define module imageio
%define oname ImageIO

Name:		python-imageio
Version:	2.37.3
Release:	1
Group:		Development/Python
Summary:	Python library for reading and writing image data
License:	BSD
URL:		https://imageio.github.io/
Source0:	https://files.pythonhosted.org/packages/source/i/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Imageio is a Python library that provides an easy interface to read
and write a wide range of image data, including animated images,
volumetric data, and scientific formats.

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info

# Plugins are not executable scripts
for plugin in imageio/plugins/_*.py ; do
    echo "Fixing $plugin..."
    sed -i -e '1{/\/usr\/bin.*python/d}' $plugin
done

%build -p
export IMAGEIO_NO_INTERNET=1

%install -p
export IMAGEIO_NO_INTERNET=1

%files
%doc README.md docs
%license LICENSE
%{_bindir}/%{module}_download_bin
%{_bindir}/%{module}_remove_bin
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}.dist-info
