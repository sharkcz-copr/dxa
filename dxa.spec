Name:           dxa
Version:        0.1.5
Release:        1%{?dist}
Summary:        6502 disassembler

Group:          Development/Tools
License:        GPLv2+
URL:            https://www.floodgap.com/retrotech/xa/
Source0:        https://www.floodgap.com/retrotech/xa/dists/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
# for tests
BuildRequires:  xa


%description
dxa is the semi-official disassembler option for the xa package, a weakly
patched version of Marko Mäkelä's d65 disassembler that generates  output
similar to the de facto coding conventions used for xa. The package is
designed to intelligently(?) scan arbitrary code and (with hints) can identify
the difference between data and valid machine code, generating a sane looking,
"perfect" disassembly with data and code portions.

Perfect, in this case, means that you can take what dxa spits out and feed it
right back into xa, and get the exact same object file you started with, even
if sometimes  dxa can't identify everything correctly. With a few extra
options, you can tease and twist the output to generate something not quite
so parseable, or even more like true assembler source.


%prep
%setup -q

# fix encoding
for f in dxa.1
do
    iconv -f ISO-8859-1 -t UTF-8 < $f > $f.new
    touch -r $f $f.new
    mv $f.new $f
done


%build
%make_build CFLAGS="%{build_cflags} -DLONG_OPTIONS"


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1/

install -p -m 755 %{name} %{buildroot}%{_bindir}
install -p -m 644 %{name}.1 %{buildroot}%{_mandir}/man1


%check
make test


%files
%doc
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Sun Aug 14 2022 Dan Horák <dan[at]danny.cz> - 0.1.5-1
- updated to 0.1.5

* Sat Feb 09 2019 Dan Horák <dan[at]danny.cz> - 0.1.4-1
- updated to 0.1.4

* Mon Nov 17 2014 Dan Horák <dan[at]danny.cz> - 0.1.3-3
- add valgrind patch

* Sat Jan 29 2011 Dan Horák <dan[at]danny.cz> - 0.1.3-2
- add malloc patch

* Sat Feb 21 2009 Dan Horák <dan[at]danny.cz> - 0.1.3-1
- initial Fedora version
