from transformers import MarianMTModel, MarianTokenizer
from flask import Flask, request, jsonify

app = Flask(__name__)

# 根据需求选择相应模型（此处以中文→越南语为例）
model_name = "Helsinki-NLP/opus-mt-zh-vi"

# 下载并加载分词器和模型
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate(texts):
    if isinstance(texts, str):
        texts = [texts]
    
    translations = []
    for text in texts:
        # 编码输入文本
        inputs = tokenizer(text, return_tensors="pt", padding=True)
        # 模型生成翻译结果
        outputs = model.generate(**inputs)
        # 解码输出
        translation = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
        translations.append(translation)
    return translations

@app.route('/translate', methods=['GET'])
def translate_text():
    text = request.args.get('text', '')
    text_list = request.args.getlist('list')
    
    if not text and not text_list:
        response = jsonify({'error': '请提供要翻译的文本或文本列表'})
        response.headers['Content-Type'] = 'application/json'
        return response, 400
    
    try:
        if text_list:
            translated_texts = translate(text_list)
            response = jsonify({
                'original_text': text_list,
                'translated_text': translated_texts
            })
        else:
            translated_text = translate(text)[0]
            response = jsonify({
                'original_text': [text],
                'translated_text': [translated_text]
            })
        response.headers['Content-Type'] = 'application/json'
        return response
    except Exception as e:
        response = jsonify({'error': str(e)})
        response.headers['Content-Type'] = 'application/json'
        return response, 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8010)