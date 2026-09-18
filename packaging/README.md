# Distribution packages

The recipes package the checked-in Hunspell dictionary release without
regenerating historical lexical sources. The main dictionary is installed in
/usr/share/hunspell; the supplementary pair is example data under
/usr/share/doc/hunspell-sv/examples.

## Debian / Ubuntu

Install build-essential, debhelper, dictionaries-common-dev, hunspell and
python3. Run `dpkg-buildpackage -b -us -uc` from the repository root for an
unsigned binary package. A full source build also needs the upstream orig
tarball matching the version in debian/changelog.

The package is Architecture: all, Multi-Arch: foreign, and uses the official
installdeb-hunspell helper for dictionaries-common registration and lifecycle
scripts. Epoch 1 preserves upgrade ordering from the existing distribution
package. The package deliberately provides sv_SE only, not a separate
Finland-Swedish dictionary.

## Fedora RPM

Install rpm-build, python3 and hunspell. Place the release archive in SOURCES
as hunspell-sv-2026.09.17.tar.gz with top-level hunspell-sv-2026.09.17/.
Copy packaging/rpm/COPYING and COPYING.LESSER into SOURCES, then run:

    rpmbuild -ba packaging/rpm/hunspell-sv.spec

The binary package is noarch and requires hunspell-filesystem. Both source
and binary RPMs can be built from the supplied SRPM on another Fedora host.

## Validation and scope

Packages were tested in Ubuntu 24.04 and Fedora 44 environments, including
upgrade from stock dictionaries, spelling checks, removal and reinstallation.
The Debian package is unsigned. The RPM is unsigned and uses Fedora 44's
macros and dependency conventions; it is not advertised as universal across
all RPM distributions.

The upstream project's declared license is recorded in debian/copyright
and the RPM License tag. Upstream does not provide a complete rights inventory
for every lexical source. Package format validation is not legal clearance
or acceptance into an official distribution archive.
