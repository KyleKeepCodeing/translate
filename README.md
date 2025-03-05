# 中文到越南语翻译器

这是一个简单的中文到越南语的翻译程序，使用了 Helsinki-NLP/opus-mt-zh-vi 模型。

## 安装依赖

在使用之前，请先安装必要的依赖：

```bash
pip install -r requirements.txt

#或者
pip3 install -r requirements.txt

```

## 使用方法

运行以下命令启动翻译程序：

```bash
python main.py
```

程序启动后：
1. 等待模型加载完成
2. 在提示符处输入要翻译的中文文本
3. 程序会显示对应的越南语翻译
4. 输入 'q' 可以退出程序

## 注意事项

- 首次运行时，程序会自动下载翻译模型，这可能需要一些时间
- 请确保您的计算机连接到互联网
- 建议输入的文本长度适中，过长的文本可能会影响翻译质量


curl
curl -X POST http://localhost:5000/translate -H "Content-Type: application/json" -d "{\"text\": \"你好，帮我把中文翻译成越南语\"}"