"""Flood Fill 733"""
from typing import List


def floodFill(image:  List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if 0 <= sr < len(image) and 0 <= sc < len(image[0]):
        if image[sr][sc] == color:
            return image
        else:
            current_color = image[sr][sc]
            image[sr][sc] = color
            if sr - 1 >= 0:
                if image[sr - 1][sc] == current_color:
                    image = floodFill(image, sr - 1, sc, color)
            if sr + 1 < len(image):
                if image[sr + 1][sc] == current_color:
                    image = floodFill(image, sr + 1, sc, color)
            if sc - 1 >= 0:
                if image[sr][sc - 1] == current_color:
                    image = floodFill(image, sr, sc - 1, color)
            if sc + 1 < len(image[0]):
                if image[sr][sc + 1] == current_color:
                    image = floodFill(image, sr, sc + 1, color)
    else:
        return image
    return image


if __name__ == '__main__':
    print(floodFill([[1,1,1,1],[1,1,0,1],[1,0,1,1]], 1, 1, 2))
