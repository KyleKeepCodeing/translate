from transformers import MarianMTModel, MarianTokenizer
from flask import Flask, request, jsonify

app = Flask(__name__)

# 根据需求选择相应模型（此处以中文→越南语为例）
model_name = "Helsinki-NLP/opus-mt-zh-vi"

# 下载并加载分词器和模型
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate(text):
    # 编码输入文本
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    # 模型生成翻译结果
    outputs = model.generate(**inputs)
    # 解码输出
    translation = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return translation[0]

@app.route('/translate', methods=['GET'])
def translate_text():
    text = request.args.get('text', '')
    if not text:
        response = jsonify({'error': '请提供要翻译的文本'})
        response.headers['Content-Type'] = 'application/json'
        return response, 400
    
    try:
        translated_text = translate(text)
        response = jsonify({
            'original_text': text,
            'translated_text': translated_text
        })
        response.headers['Content-Type'] = 'application/json'
        return response
    except Exception as e:
        response = jsonify({'error': str(e)})
        response.headers['Content-Type'] = 'application/json'
        return response, 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8010)