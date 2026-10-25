# Disclaimer

**Independent project.** bracketPML is not affiliated with, endorsed by or supported by AVEVA. AVEVA, E3D and Everything3D are trademarks of their respective owners and are used here only to say what the material is about.

**Where the facts come from.** Every status in the register comes from a run: a command typed or pasted into AVEVA E3D 2.1 on a working installation, with the answer E3D printed recorded at the time. Test runs use an anonymised training project (zone `/PMLC`, database `12345678`); no customer or employer data is published.

**What is not here.** No AVEVA documentation is copied: where a manual is quoted, it is a short quotation with its source. The attribute reference names each attribute and its owners and members as the data model has them (with the manual page); what each attribute means is written in our own words. No vendor PML library (PMLLIB) code is included.

**Your installation may differ.** E3D versions, licences and project setups differ. A command verified on 2.1 may behave differently on another version or with different project defaults. Run the module's probe on a test project before relying on anything — and if your E3D answers differently, send a [run report](CONTRIBUTING.md).

**No warranty.** The code is provided as is (see [LICENSE](LICENSE)). Anything that writes to a model can damage it: use a rollback mark ([guard](modules/guard/README.md)), check before `SAVEWORK`, and try new code on a test project first.
