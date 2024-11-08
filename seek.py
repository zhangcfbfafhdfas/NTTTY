import pyautogui
import pytesseract
import pyperclip
import time
import os
from PIL import Image

def ocr_image(image_path):
    """识别图片中的文字，并返回识别出的文本"""
    try:
        # 打开图像
        img = Image.open(image_path)
        
        # 使用tesseract进行OCR识别
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error: {str(e)}"

def take_screenshot():
    """自动触发系统截图工具，并等待用户完成截图"""
    print("准备进行截图...")
    time.sleep(1)  # 给用户1秒准备时间

    # 模拟按下系统截图快捷键 (Windows+Shift+S)
    # MacOS 可能需要调整为 Command+Shift+4，Linux 根据系统截图工具调整
    pyautogui.hotkey('win', 'shift', 's')  # Windows系统的截图快捷键
    print("请使用系统截图工具进行截图...")
    
    # 等待用户完成截图
    time.sleep(5)  # 根据情况调整等待时间，确保用户完成截图

def get_latest_screenshot():
    """从默认的截图文件夹中获取最新的截图文件 (适用于Windows)"""
    # Windows默认的截图保存路径（适用于Windows+Shift+S截图）
    screenshot_folder = os.path.join(os.getenv('USERPROFILE'), 'Pictures', 'Screenshots')
    
    # 获取文件夹中最新的截图文件
    screenshot_files = sorted(
        [os.path.join(screenshot_folder, f) for f in os.listdir(screenshot_folder) if f.endswith('.png')],
        key=os.path.getctime,
        reverse=True
    )
    if screenshot_files:
        return screenshot_files[0]  # 返回最新的截图文件
    else:
        return None

def delete_screenshot(file_path):
    """删除指定的截图文件"""
    try:
        os.remove(file_path)
        print(f"截图文件已删除: {file_path}")
    except Exception as e:
        print(f"无法删除截图文件: {file_path}，错误: {str(e)}")

def main():
    # 启动截图工具
    take_screenshot()

    # 获取最新截图
    latest_screenshot = get_latest_screenshot()
    if not latest_screenshot:
        print("未找到截图文件，请确认截图已保存。")
        return

    # OCR识别截图中的文字
    text = ocr_image(latest_screenshot)

    # 输出识别结果
    print("识别结果：")
    print(text)

    # 将识别结果复制到剪贴板
    pyperclip.copy(text)
    print("识别结果已复制到剪贴板！")

    # 删除截图文件
    delete_screenshot(latest_screenshot)

if __name__ == "__main__":
    main()
