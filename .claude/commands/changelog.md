# Update Changelog

Update the CHANGELOG.md with recent changes.

## Instructions

1. Run `git log --oneline $(git describe --tags --abbrev=0 2>/dev/null || echo "HEAD~10")..HEAD` to see commits since the last tag (or last 10 commits if no tags)

2. Also check `git diff --cached --name-only` and `git diff --name-only` for any uncommitted changes that should be documented

3. Read CHANGELOG.md to understand the current state and format

4. Update the `[Unreleased]` section with appropriate entries using these categories:
   - **Added** - new features
   - **Changed** - changes to existing functionality
   - **Deprecated** - features being removed soon
   - **Removed** - features that were removed
   - **Fixed** - bug fixes
   - **Security** - vulnerability fixes

5. Follow the project's tone: light, fun, pub-themed. Keep entries concise (one line each).

6. If the [Unreleased] section has the placeholder "Nothing yet. Buy us a pint and we might add something." - replace it with the actual changes.

7. Show the user what you added to the changelog.
