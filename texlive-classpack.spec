# revision 33101
# category Package
# catalog-ctan /support/classpack
# catalog-date 2014-02-26 23:03:13 +0100
# catalog-license lppl1.3
# catalog-version 0.77
Name:		texlive-classpack
Version:	0.77
Release:	5
Summary:	XML mastering for LaTeX classes and packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/classpack
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/classpack.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/classpack.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/classpack.source.tar.xz
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
%{_texmfdistdir}/tex/latex/classpack/classpack.sty
%doc %{_texmfdistdir}/doc/support/classpack/MANIFEST
%doc %{_texmfdistdir}/doc/support/classpack/README
%doc %{_texmfdistdir}/doc/support/classpack/classpack.pdf
%doc %{_texmfdistdir}/doc/support/classpack/db2bibtex.xsl
%doc %{_texmfdistdir}/doc/support/classpack/db2dtx.xsl
%doc %{_texmfdistdir}/doc/support/classpack/db2plaintext.xsl
%doc %{_texmfdistdir}/doc/support/classpack/decommentbbl.awk
%doc %{_texmfdistdir}/doc/support/classpack/doctexbook.dtd
%doc %{_texmfdistdir}/doc/support/classpack/getgis.sh
%doc %{_texmfdistdir}/doc/support/classpack/lppl.xml
%doc %{_texmfdistdir}/doc/support/classpack/prepost.xml
%doc %{_texmfdistdir}/doc/support/classpack/readme.xml
%doc %{_texmfdistdir}/doc/support/classpack/test.sh
#- source
%doc %{_texmfdistdir}/source/support/classpack/classpack.dtx
%doc %{_texmfdistdir}/source/support/classpack/classpack.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
