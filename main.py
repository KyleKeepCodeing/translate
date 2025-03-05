from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from modelscope import snapshot_download

polylm_13b_model_id = 'damo/nlp_polylm_assistant_13b_text_generation'
revision = 'v1.0.0'

model_dir = snapshot_download(polylm_13b_model_id, revision)

input_text = f"Beijing is the capital of China.\nTranslate this sentence from English to Chinese."
input_text = "<|user|>\n" + f"{input_text}\n" + "<|assistant|>\n"

kwargs = {"do_sample": False, "num_beams": 4, "max_new_tokens": 128, "early_stopping": True, "eos_token_id": 2}
pipeline_ins = pipeline(Tasks.text_generation, model=model_dir, external_engine_for_llm=False)

result = pipeline_ins(input_text, **kwargs)
print(result['text'])
