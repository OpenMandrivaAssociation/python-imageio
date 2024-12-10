%global pypi_name imageio

Name:           python-%{pypi_name}
Version:        2.36.1
Release:        1
Group:          Development/Python
Summary:        Python library for reading and writing image data
License:        BSD
URL:            https://imageio.github.io/
Source0:        https://pypi.io/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

#{?python_provide:%python_provide python-%{pypi_name}}

%description
Imageio is a Python library that provides an easy interface to read
and write a wide range of image data, including animated images,
volumetric data, and scientific formats.

%files
%doc README.md docs
%license LICENSE
%{_bindir}/%{pypi_name}_download_bin
%{_bindir}/%{pypi_name}_remove_bin
%{python_sitelib}/%{pypi_name}/
%{python_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %%{pypi_name}.egg-info

%build
%py_build

%install
%py_install

