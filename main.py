from flask import Flask, request, jsonify
from flask_cors import CORS
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from modelscope import snapshot_download

app = Flask(__name__)
CORS(app)

# 初始化模型
polylm_13b_model_id = 'damo/nlp_polylm_assistant_13b_text_generation'
revision = 'v1.0.0'

print("正在下载模型...")
model_dir = snapshot_download(polylm_13b_model_id, revision)

print("正在加载模型...")
kwargs = {"do_sample": False, "num_beams": 4, "max_new_tokens": 128, "early_stopping": True, "eos_token_id": 2}
pipeline_ins = pipeline(Tasks.text_generation, model=model_dir, external_engine_for_llm=False)

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': '请提供要翻译的文本'}), 400

        input_text = data['text']
        input_text = "<|user|>\n" + f"{input_text}\n" + "<|assistant|>\n"
        
        result = pipeline_ins(input_text, **kwargs)
        return jsonify({'translation': result['text']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    print("服务启动在 http://localhost:8010")
    app.run(host='0.0.0.0', port=8010)
