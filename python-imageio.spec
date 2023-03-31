%global pypi_name imageio

Name:           python-%{pypi_name}
Version:        2.6.1
Release:        4
Group:          Development/Python
Summary:        Python library for reading and writing image data
License:        BSD
URL:            http://imageio.github.io/
Source0:        http://pypi.io/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python-%{pypi_name}}

%description
Imageio is a Python library that provides an easy interface to read
and write a wide range of image data, including animated images,
volumetric data, and scientific formats.

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
#rm -rf %%{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files
%doc README.md docs
%license LICENSE
%{_bindir}/%{pypi_name}_download_bin
%{_bindir}/%{pypi_name}_remove_bin
%{python_sitelib}/%{pypi_name}/
%{python_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
