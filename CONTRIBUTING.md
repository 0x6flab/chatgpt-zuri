# Contributing to 0x6flab/chatgpt-zuri

The following is a set of guidelines to contribute to chatgptzuri, which are hosted on the [0x6flab Organization](https://github.com/0x6flab) on GitHub.

This project adheres to the [Contributor Covenant 1.2](http://contributor-covenant.org/version/1/2/0). By participating, you are expected to uphold this code. Please report unacceptable behavior to [abuse@rodneyosodo.com](mailto:abuse@rodneyosodo.com).

## Reporting issues

Reporting issues are a great way to contribute to the project. We are perpetually grateful about a well-written, thorough bug report.

Before raising a new issue, check [our issue list](https://github.com/0x6flab/chatgpt-zuri/issues) to determine if it already contains the problem that you are facing.

A good bug report shouldn't leave others needing to chase you for more information. Please be as detailed as possible. The following questions might serve as a template for writing a detailed report:

- What were you trying to achieve?
- What are the expected results?
- What are the received results?
- What are the steps to reproduce the issue?
- In what environment did you encounter the issue?

## Pull requests

Good pull requests (e.g. patches, improvements, new features) are a fantastic help. They should remain focused in scope and avoid unrelated commits.

**Please ask first** before embarking on any significant pull request (e.g. implementing new features, refactoring code etc.), otherwise you risk spending a lot of time working on something that the maintainers might not want to merge into the project.

To contribute to the project, [fork](https://help.github.com/articles/fork-a-repo/) it, clone your fork repository, and configure the remotes:

```bash
git clone https://github.com/<your-username>/chatgpt-zuri.git
cd chatgpt-zuri
git remote add upstream https://github.com/0x6flab/chatgpt-zuri.git
```

If your cloned repository is behind the upstream commits, then get the latest changes from upstream:

```bash
git checkout main
git pull --rebase upstream main
```

Create a new topic branch from `main` using the naming convention `CZ-[issue-number]` to help us keep track of your contribution scope:

```bash
git checkout -b CZ-[issue-number]
```

Note that every commit you make must be signed. By signing off your work you indicate that you are accepting the [Developer Certificate of Origin](https://developercertificate.org/).

Use your real name (sorry, no pseudonyms or anonymous contributions). If you set your `user.name` and `user.email` git configs, you can sign your commit automatically with `git commit -s`.

Locally merge (or rebase) the upstream development branch into your topic branch:

```bash
git pull --rebase upstream main
```

Push your topic branch up to your fork:

```bash
git push origin CZ-[issue-number]
```

[Open a Pull Request](https://help.github.com/articles/using-pull-requests/) with a clear title and detailed description.
