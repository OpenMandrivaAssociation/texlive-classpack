Name:		texlive-classpack
Version:	55218
Release:	1
Summary:	XML mastering for LaTeX classes and packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/classpack
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/classpack.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/classpack.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/classpack.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an experiment in using XML (specifically
DocBook 5) to mark up and maintain LaTeX classes and packages.
XSLT 2 styleheets generate the .dtx and .ins distribution files
expected by end users.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/classpack
%doc %{_texmfdistdir}/doc/support/classpack
#- source
%doc %{_texmfdistdir}/source/support/classpack

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
