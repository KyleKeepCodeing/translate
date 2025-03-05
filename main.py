#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

app = Flask(__name__)
CORS(app)  # 启用跨域支持

# 初始化翻译器
print("正在加载翻译模型...")
translator = pipeline(
    Tasks.translation,
    model='damo/nlp_csanmt_translation_zh2vi',  # 中文到越南语的模型
    device='cpu'  # 如果有GPU可以改成'gpu'
)
print("模型加载完成！")

def translate_to_vietnamese(text):
    """将中文文本翻译成越南语（离线）"""
    try:
        result = translator(text)
        return result['translation']
    except Exception as e:
        return str(e)

@app.route('/translate', methods=['POST'])
def translate():
    """翻译API端点"""
    try:
        data = request.get_json()
        
        # 检查请求数据
        if not data or 'text' not in data:
            return jsonify({
                'success': False,
                'error': '请提供要翻译的文本',
                'example': {
                    'text': '你好，世界'
                }
            }), 400
        
        chinese_text = data['text']
        
        # 进行翻译
        vietnamese_translation = translate_to_vietnamese(chinese_text)
        
        # 返回结果
        return jsonify({
            'success': True,
            'source_text': chinese_text,
            'translated_text': vietnamese_translation
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'翻译过程中出现错误：{str(e)}'
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """健康检查端点"""
    return jsonify({
        'status': 'ok',
        'service': 'chinese-vietnamese-translator-offline'
    })

if __name__ == "__main__":
    print("\n翻译API服务已启动！")
    print("健康检查接口：GET http://localhost:8010/health")
    print("翻译接口：POST http://localhost:8010/translate")
    print("示例请求：")
    print('''
    curl -X POST http://localhost:8010/translate 
         -H "Content-Type: application/json" 
         -d '{"text": "你好，世界"}'
    ''')
    app.run(host='0.0.0.0', port=8010)
