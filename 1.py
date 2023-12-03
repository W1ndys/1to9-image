from PIL import Image
import os

def split_image_into_nine(image_path, output_folder):
    # 打开图像文件
    img = Image.open(image_path)

    # 确定单个格子的宽度和高度
    width, height = img.size
    cell_width = width // 3
    cell_height = height // 3

    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 分割图像并保存到输出文件夹中
    for i in range(3):
        for j in range(3):
            box = (j * cell_width, i * cell_height, (j + 1) * cell_width, (i + 1) * cell_height)
            cell = img.crop(box)
            cell.save(os.path.join(output_folder, f"cell_{i}_{j}.png"))

    print("图片已成功分割成九宫格并保存到输出文件夹中！")

if __name__ == "__main__":
    # 输入图片文件路径和输出文件夹路径
    input_image_path = "input_image.jpg"  # 更改为你的图片文件名
    output_folder_path = "output"  # 输出文件夹名

    split_image_into_nine(input_image_path, output_folder_path)
