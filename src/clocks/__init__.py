"""Shared helpers for the Aging Clocks course.

Notebooks keep the scientific logic; this package keeps the plumbing
(downloading, caching, parsing) so that it is not repeated in every chapter.
"""

from clocks.paths import DATA_DIR, REPO_ROOT

__all__ = ["DATA_DIR", "REPO_ROOT"]
