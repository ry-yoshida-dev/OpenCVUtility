# OpenCV Utility

`opencv-utility` is a small Python package that wraps common **OpenCV flags** as typed enums, so callers can pass string-friendly values and resolve the correct `cv2` constant at runtime (including modern **USAC** variants).

## Documentation

| Topic | Link |
|--------|------|
| Package overview and module index | [src/opencv_utility/README.md](src/opencv_utility/README.md) |
| Interpolation and robust-estimation flags | [src/opencv_utility/flag/README.md](src/opencv_utility/flag/README.md) |

## Installation

From the project root:

```bash
pip install -e .
```

Or install dependencies only (use when developing without installing the package):

```bash
pip install -r requirements.txt
```

Requires **OpenCV 4.5+** for USAC-related outlier-filtering members (`opencv-contrib-python` is listed in `pyproject.toml`).

## Usage

```python
import cv2
from opencv_utility import OpenCVInterpolationFlag, OpenCVOutlierFilteringFlag

# Map enum → cv2 constant
interp = OpenCVInterpolationFlag.LANCZOS4.cv2_flag  # cv2.INTER_LANCZOS4
method = OpenCVOutlierFilteringFlag.USAC_ACCURATE.cv2_flag

# General robust estimation (e.g. findHomography, solvePnPRansac)
H, mask = cv2.findHomography(src, dst, method=method)

# Fundamental matrix (some members use a different cv2 constant)
fm_method = OpenCVOutlierFilteringFlag.RANSAC.fundamental_matrix_flag
F, mask = cv2.findFundamentalMat(pts1, pts2, fm_method)

# Parse from config strings
flag = OpenCVOutlierFilteringFlag.from_string("magsac")
```

See [src/opencv_utility/flag/README.md](src/opencv_utility/flag/README.md) for method comparison tables and API compatibility notes.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
