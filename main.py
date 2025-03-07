from transformers import AutoModelForCausalLM, AutoTokenizer

# PolyLM-1.7B
# model_path = "DAMO-NLP-MT/polylm-1.7b"
# PolyLM-13B
model_path = "DAMO-NLP-MT/polylm-13b"
# PolyLM-Multialpaca-13B
# model_path = "DAMO-NLP-MT/polylm-multialpaca-13b"
# PolyLM-Chat-13B
# model_path = "DAMO-NLP-MT/polylm-chat-13b"

tokenizer = AutoTokenizer.from_pretrained(model_path, legacy=False, use_fast=False)
model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", trust_remote_code=True)
model.eval()

# PolyLM-13B/PolyLM-1.7B
input_doc = f"Beijing is the capital of China.\nTranslate this sentence from English to Chinese."
# PolyLM-Multialpaca-13B
# input_doc = f"Beijing is the capital of China.\nTranslate this sentence from English to Chinese.\n\n"
# PolyLM-Chat-13B
# input_doc = f"Beijing is the capital of China.\nTranslate this sentence from English to Chinese."
# input_doc = "<|user|>\n" + f"{input_doc}\n" + "<|assistant|>\n"

inputs = tokenizer(input_doc, return_tensors="pt")

generate_ids = model.generate(
  inputs.input_ids,
  attention_mask=inputs.attention_mask,
  do_sample=False,
  num_beams=4,
  max_length=128,
  early_stopping=True
)

decoded = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
print(f">>> {decoded}")
### results
### Beijing is the capital of China.\nTranslate this sentence from English to Chinese.\\n北京是中华人民共和国的首都。\n ...