import os
import sys
from PIL import Image


def split_image(image_path, horizontal_splits, vertical_splits):
    print(
        f"Starting image split with parameters: {image_path}, {horizontal_splits}, {vertical_splits}"
    )
    # 打开图片
    image = Image.open(image_path)
    img_width, img_height = image.size
    print(f"Image loaded: {image_path} (Width: {img_width}, Height: {img_height})")

    # 计算每个子图片的宽度和高度
    split_width = img_width // horizontal_splits
    split_height = img_height // vertical_splits
    print(
        f"Splitting image into {horizontal_splits}x{vertical_splits} (Each piece: {split_width}x{split_height})"
    )

    # 获取图片的文件名和扩展名
    image_name, image_ext = os.path.splitext(os.path.basename(image_path))

    # 创建一个新的文件夹用于保存切分后的图片
    output_dir = os.path.join(
        os.getcwd(), image_name
    )  # 使用 os.getcwd() 获取当前工作目录
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output directory created: {output_dir}")

    # 开始切分图片并保存
    for i in range(horizontal_splits):
        for j in range(vertical_splits):
            left = i * split_width
            upper = j * split_height
            right = (i + 1) * split_width if i < horizontal_splits - 1 else img_width
            lower = (j + 1) * split_height if j < vertical_splits - 1 else img_height

            # 切分图片
            cropped_image = image.crop((left, upper, right, lower))
            print(f"Image cropped: ({left}, {upper}, {right}, {lower})")

            # 生成新的图片文件名
            cropped_image_name = f"{image_name}_{i}_{j}{image_ext}"
            cropped_image_path = os.path.join(output_dir, cropped_image_name)

            # 保存切分后的图片
            cropped_image.save(cropped_image_path)
            print(f"Saved: {cropped_image_path}")

    print("Image splitting complete.")
    sys.exit(1)


if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) != 4:
        print(
            "Usage: python split_image.py <image_path> <horizontal_splits> <vertical_splits>"
        )
        sys.exit(1)

    # 获取命令行参数
    image_path = sys.argv[1]
    horizontal_splits = int(sys.argv[2])
    vertical_splits = int(sys.argv[3])

    # 调用切分函数
    split_image(image_path, horizontal_splits, vertical_splits)
