# flag

## Overview

`OpenCVInterpolationFlag` and `OpenCVOutlierFilteringFlag` map human-readable enum members to OpenCV integer constants. Use `.cv2_flag` for general APIs (`resize`, `warpAffine`, `findHomography`, `solvePnPRansac`, etc.). For `cv2.findFundamentalMat`, use `.fundamental_matrix_flag` (see the ✓/— columns in the outlier-filtering table).

## Interpolation (`OpenCVInterpolationFlag`)

Used with `cv2.resize`, `cv2.remap`, `cv2.warpAffine`, `cv2.warpPerspective`, and similar functions.

| Member | OpenCV constant | Notes |
|--------|-----------------|-------|
| `NEAREST` | `INTER_NEAREST` | Label maps, masks; preserves discrete values (no new gray levels) |
| `LINEAR` | `INTER_LINEAR` | Bilinear (2×2); general resize / warp |
| `LINEAR_EXACT` | `INTER_LINEAR_EXACT` | Same formula as `LINEAR`, without SIMD shortcuts that can differ slightly |
| `CUBIC` | `INTER_CUBIC` | Bicubic (4×4) |
| `LANCZOS4` | `INTER_LANCZOS4` | Lanczos window (8×8) |
| `AREA` | `INTER_AREA` | Pixel-area resampling; intended for **downscaling** (not upscaling) |

```python
from opencv_utility import OpenCVInterpolationFlag

flag = OpenCVInterpolationFlag.AREA.cv2_flag
# cv2.resize(img, dsize, interpolation=flag)
```

## Robust outlier filtering (`OpenCVOutlierFilteringFlag`)

Used with robust model fitting (`findHomography`, `findFundamentalMat`, `solvePnPRansac`, `estimateAffine2D`, etc.). Choice affects **inlier mask**, runtime, and tolerance to outliers / noise.

Use **`.cv2_flag`** for general APIs (`findHomography`, `solvePnPRansac`, `estimateAffine2D`, …). Use **`.fundamental_matrix_flag`** for `findFundamentalMat` only.

| Member | `.cv2_flag` | `.fundamental_matrix_flag` | OpenCV constant(s) | Notes |
|--------|:---:|:---:|-----------------|-------|
| `RANSAC` | ✓ | ✓ | `RANSAC` / `FM_RANSAC` | Random sample consensus |
| `LMEDS` | ✓ | ✓ | `LMEDS` / `FM_LMEDS` | Least median of squares; no explicit inlier threshold |
| `RHO` | ✓ | — | `RHO` | M-estimator; not supported for `findFundamentalMat` |
| `MAGSAC` | ✓ | ✓ | `MAGSAC` / `USAC_MAGSAC` | MAGSAC; marginalizes over noise scale (OpenCV 4+) |
| `SEVEN_POINT` | — | ✓ | `FM_7POINT` | Algebraic; exactly 7 point pairs; up to 3 solutions; FM only |
| `EIGHT_POINT` | — | ✓ | `FM_8POINT` | Linear; ≥ 8 point pairs; FM only |
| `USAC_DEFAULT` | ✓ | ✓ | `USAC_DEFAULT` | Unified RANSAC framework (OpenCV 4.5+) |
| `USAC_PARALLEL` | ✓ | ✓ | `USAC_PARALLEL` | Parallel USAC |
| `USAC_FAST` | ✓ | ✓ | `USAC_FAST` | USAC tuned for fewer iterations |
| `USAC_ACCURATE` | ✓ | ✓ | `USAC_ACCURATE` | USAC tuned for precision |
| `USAC_PROSAC` | ✓ | ✓ | `USAC_PROSAC` | PROSAC; assumes correspondences sorted by quality |

✓ = supported via the property; — = raises `ValueError` (use the other property instead).

```python
from opencv_utility import OpenCVOutlierFilteringFlag

# General robust APIs
method = OpenCVOutlierFilteringFlag.MAGSAC.cv2_flag

# Fundamental matrix only
fm = OpenCVOutlierFilteringFlag.USAC_ACCURATE.fundamental_matrix_flag

# Config / CLI strings
OpenCVOutlierFilteringFlag.from_string("usac_fast")
```

## Choosing a method (quick guide)

| Goal | Interpolation | Outlier filtering |
|------|---------------|-------------------|
| Fast preview / masks | `NEAREST` | `RANSAC` or `USAC_FAST` |
| Balanced image warp | `LINEAR` | `RANSAC` or `USAC_DEFAULT` |
| Downscale camera images | `AREA` | — |
| High-quality resize | `LANCZOS4` or `CUBIC` | — |
| Offline calibration / SfM | — | `USAC_ACCURATE` or `MAGSAC` |
| Many outliers in matches | — | `LMEDS` or `MAGSAC` |
| Exactly 7/8 point F (noiseless) | — | `SEVEN_POINT` / `EIGHT_POINT` |
