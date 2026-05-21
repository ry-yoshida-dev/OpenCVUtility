import cv2
from enum import Enum

class OpenCVInterpolationFlag(Enum):
    """
    Interpolation flags for OpenCV.
    
    Attributes:
    ----------
    NEAREST: Nearest neighbor interpolation.
    LINEAR: Linear interpolation.
    LINEAR_EXACT: Linear interpolation with exact calculation.
    CUBIC: Cubic interpolation.
    LANCZOS4: Lanczos4 interpolation.
    AREA: Area-based interpolation.
    """
    NEAREST = "nearest"
    LINEAR = "linear"
    LINEAR_EXACT = "linear_exact"
    CUBIC = "cubic"
    LANCZOS4 = "lanczos4"
    AREA = "area"

    @property
    def cv2_flag(self) -> int:
        """
        Get the OpenCV interpolation flag.
        
        Returns:
        -------
        int: The OpenCV interpolation flag.
        """
        match self:
            case self.NEAREST:
                return cv2.INTER_NEAREST
            case self.LINEAR:
                return cv2.INTER_LINEAR
            case self.LINEAR_EXACT:
                return cv2.INTER_LINEAR_EXACT
            case self.CUBIC:
                return cv2.INTER_CUBIC
            case self.LANCZOS4:
                return cv2.INTER_LANCZOS4
            case self.AREA:
                return cv2.INTER_AREA
