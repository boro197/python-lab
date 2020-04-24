from .production_line import ProductionLine
from .production_line_step import ProductionLineStep
from cv2 import imread, imshow, IMREAD_UNCHANGED, rotate, ROTATE_90_CLOCKWISE, blur, bitwise_not, imwrite, waitKey


class ImageModifier(ProductionLine):
    def __init__(self, image_path, output_path):
        self.__image_path = image_path
        self.__output_path = output_path
        self.__initialize_parent()
        self.__add_steps()

    def __initialize_parent(self):
        super().__init__(ReadImage(), self.__image_path)

    def __add_steps(self):
        super().add_step(Rotate())
        super().add_step(Blur())
        super().add_step(ReverseColors())
        super().add_step(ShowResult())
        super().add_step(SaveResult(self.__output_path))


class ReadImage(ProductionLineStep):
    def __call__(self, file_path):
        image = imread(file_path, IMREAD_UNCHANGED)

        return image


class Rotate(ProductionLineStep):
    def __call__(self, previous_step_result):
        image = previous_step_result
        image = rotate(image, ROTATE_90_CLOCKWISE)
        return image


class Blur(ProductionLineStep):
    def __call__(self, previous_step_result):
        image = previous_step_result
        image = blur(image, (5, 5))
        return image


class ReverseColors(ProductionLineStep):
    def __call__(self, previous_step_result):
        image = previous_step_result
        image = bitwise_not(image)
        return image


class ShowResult(ProductionLineStep):
    def __call__(self, previous_step_result):
        imshow('Result of transformations', previous_step_result)
        print('Close preview window to continue...')
        waitKey(0)
        return previous_step_result


class SaveResult(ProductionLineStep):
    def __init__(self, output_path):
        self.__output_path = output_path

    def __call__(self, previous_step_result):
        imwrite(self.__output_path, previous_step_result)
        return previous_step_result
