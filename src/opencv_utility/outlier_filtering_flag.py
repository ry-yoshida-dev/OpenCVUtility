from __future__ import annotations
import cv2
from enum import Enum

class OpenCVOutlierFilteringFlag(Enum):
    """
    Enhanced outlier filtering flags for OpenCV, including modern USAC variants.
    """
    NONE = "none"
    RANSAC = "ransac"
    LMEDS = "lmeds"
    RHO = "rho"
    MAGSAC = "magsac"
    SEVEN_POINT = "seven_point"
    EIGHT_POINT = "eight_point"
    
    # Modern USAC flags (OpenCV 4.5.0+)
    USAC_DEFAULT = "usac_default"
    USAC_PARALLEL = "usac_parallel"
    USAC_FAST = "usac_fast"
    USAC_ACCURATE = "usac_accurate"
    USAC_PROSAC = "usac_prosac"

    @property
    def cv2_flag(self) -> int:
        """
        Get the flag for general functions like cv2.findHomography or cv2.solvePnPRansac.
        """
        match self:
            case self.NONE:
                return 0
            case self.RANSAC:
                return cv2.RANSAC
            case self.LMEDS:
                return cv2.LMEDS
            case self.RHO:
                return cv2.RHO
            case self.MAGSAC:
                return cv2.MAGSAC
            case self.USAC_DEFAULT:
                return cv2.USAC_DEFAULT
            case self.USAC_PARALLEL:
                return cv2.USAC_PARALLEL
            case self.USAC_FAST:
                return cv2.USAC_FAST
            case self.USAC_ACCURATE:
                return cv2.USAC_ACCURATE
            case self.USAC_PROSAC:
                return cv2.USAC_PROSAC
            case _:
                raise ValueError(
                    f"Flag '{self.name}' is not supported for general estimation.\n"
                    + "Did you mean to use fundamental_matrix_flag?"
                )

    @property
    def fundamental_matrix_flag(self) -> int:
        """
        Get the flag specifically for cv2.findFundamentalMat.
        """
        match self:
            case self.NONE:
                return 0
            case self.RANSAC:
                return cv2.FM_RANSAC
            case self.LMEDS:
                return cv2.FM_LMEDS
            case self.MAGSAC:
                return cv2.USAC_MAGSAC
            case self.SEVEN_POINT:
                return cv2.FM_7POINT
            case self.EIGHT_POINT:
                return cv2.FM_8POINT
            case self.USAC_DEFAULT:
                return cv2.USAC_DEFAULT
            case self.USAC_PARALLEL:
                return cv2.USAC_PARALLEL
            case self.USAC_FAST:
                return cv2.USAC_FAST
            case self.USAC_ACCURATE:
                return cv2.USAC_ACCURATE
            case self.USAC_PROSAC:
                return cv2.USAC_PROSAC
            case self.RHO:
                raise ValueError("RHO is not supported for Fundamental Matrix estimation.")

    @classmethod
    def from_string(cls, string: str) -> OpenCVOutlierFilteringFlag:
        """
        Get the CV2OutlierFilteringFlag from a string.
        """
        return cls(string.lower())