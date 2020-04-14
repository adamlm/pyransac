"""Packages classes.

This module contains helpful classes.
"""

from dataclasses import dataclass


@dataclass
class RansacParams:
    """Random sample consensus (RANSAC) function parameters.

    """
    samples: int
    """The number of random samples to take per iteration."""

    iterations: int
    """Maximum number iterations to complete."""

    confidence: float
    """The RANSAC confidence value (0 <= confidence <= 1)."""

    threshold: float
    """The error threshold to consider a point an inlier"""
