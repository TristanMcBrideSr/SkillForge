
---

# SkillForge

**The Official Skill Repository for AVA**

---

## What is SkillForge?

SkillForge is the central hub for new AVA skills. Anyone can contribute—every skill in this repo becomes instantly 
available to all AVA users who enable the skills sync option, after it's approved.

---

## How SkillForge Works

* **All skills live inside the [`SkillForge/Forge/`](./SkillForge/Forge) folder** (each skill is a Python file).
* When AVA starts, it *automatically downloads and syncs* the latest skills from this repo, if the user has enabled the sync option.
* You never need to download skills by hand unless you want to.

---

## How to Add a Skill

1. **Fork this repo** (use the “Fork” button at the top right).
2. **Create your skill** following the [SKILL_TEMPLATE.md](./SKILL_TEMPLATE.md).
3. **Add your skill** (`yourSkillName.py`) inside the [`SkillForge/Forge/`](./SkillForge/Forge) directory of your fork.
4. **Commit and push** your changes to your fork.
5. **Open a Pull Request** back to this repo with a description of your skill.

---

## How Skills Get Approved

* **All skill submissions are reviewed by the repo owners.**
* Only approved, safe, and useful skills are merged into SkillForge.
* You’ll get comments or feedback if your skill needs fixes.
* Once merged, *all AVA users* will get your skill automatically (if they have the sync option enabled).

---

## Skill Guidelines

* Each skill must be a self-contained file and well-named.
* Include a short docstring at the top of your skill file explaining what it does.
* No malicious code, no hardcoded secrets or credentials.
* Keep it clean, efficient, and fun!

---

## Example: Submitting a New Skill

1. Fork this repo.
2. Add `myCoolSkill.py` inside `SkillForge/Forge/`.
3. Push and open a Pull Request.
4. Wait for approval!

---

## FAQ

**Q: Can anyone submit a skill?**
A: Yes! Anyone with a GitHub account can propose skills.

**Q: Can I use SkillForge for my own AVA?**
A: Yes! AVA will always sync the latest skills here if you enable the sync option.

**Q: Who decides what gets merged?**
A: Only the repo owners can approve/merge skills.

---

## Questions?

Open an [Issue](https://github.com/TristanMcBrideSr/SkillForge/issues) or [Pull Request](https://github.com/TristanMcBrideSr/SkillForge/pulls) any time!

---

> “**Forging skills, empowering AVA.**”

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

Project by:

- Tristan McBride Sr.
- Sybil
