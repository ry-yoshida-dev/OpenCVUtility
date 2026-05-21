# opencv_utility

## Overview

Typed enums for OpenCV **interpolation** and **robust outlier filtering** flags. Each member exposes a `.cv2_flag` property (and, for fundamental-matrix estimation, `.fundamental_matrix_flag` where applicable) so application code can stay readable while still passing the correct integer to `cv2`.

## Components

| Component | Description |
|-----------|-------------|
| [flag/](./flag/README.md) | `OpenCVInterpolationFlag` and `OpenCVOutlierFilteringFlag` — comparison tables, API notes, and usage examples |

## Usage

```python
from opencv_utility import OpenCVInterpolationFlag, OpenCVOutlierFilteringFlag

OpenCVInterpolationFlag.CUBIC.cv2_flag
OpenCVOutlierFilteringFlag.USAC_FAST.cv2_flag
OpenCVOutlierFilteringFlag.EIGHT_POINT.fundamental_matrix_flag
```
