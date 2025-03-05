# 中英文翻译服务

这是一个基于ModelScope的中英文翻译服务，使用了PolyLM 13B模型。

## 功能特点

- 支持中英文双向翻译
- 使用高性能的PolyLM 13B模型
- 简单易用的接口

## 环境要求

- Python 3.9+
- CUDA支持（推荐）

## 安装步骤

1. 克隆代码库：
```bash
git clone [repository-url]
cd translate
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用Docker运行

1. 构建Docker镜像：
```bash
docker-compose build
```

2. 运行服务：
```bash
docker-compose up
```

## 直接运行

```bash
python main.py
```

## 使用示例

```python
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

# 初始化翻译pipeline
pipeline_ins = pipeline(Tasks.text_generation, 
                       model='damo/nlp_polylm_assistant_13b_text_generation')

# 翻译示例
input_text = "Beijing is the capital of China."
result = pipeline_ins(input_text)
print(result['text'])
```

## 注意事项

- 首次运行时会自动下载模型，可能需要一些时间
- 建议使用GPU进行推理以获得更好的性能
- 模型文件较大，请确保有足够的磁盘空间

## 许可证

本项目采用 MIT 许可证

curl
curl -X POST http://localhost:5000/translate -H "Content-Type: application/json" -d "{\"text\": \"你好，帮我把中文翻译成越南语\"}"