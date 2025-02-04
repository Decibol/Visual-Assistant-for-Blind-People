from llama_cpp import Llama
import time

class LocalLLMProcessor:
    def __init__(self):
        self.llm = None
        self.last_processed = 0
        self.cooldown = 10
        self.load_model()
        
    def generate_description(self, detections):
        if time.time() - self.last_processed < self.cooldown:
            return None
        # Use a quantized model for better performance
        model_path = "models/llama-2-7b-chat.Q4_K_M.gguf"
        self.llm = Llama(
            model_path=model_path,
            n_ctx=2048,  # Context window
            n_threads=4,  # CPU threads
            n_gpu_layers=0  # Change if using GPU
        )
        self.last_processed = time.time()
        return response
        
    def generate_description(self, detections):
        if not detections:
            return "No significant objects detected."
            
        objects = ', '.join([d['label'] for d in detections])
        
        prompt = f"""<s>[INST] <<SYS>>
You are a helpful assistant for blind people. Describe the environment in a concise, helpful way.
Focus on spatial relationships and important objects. Use simple language. Max 2 sentences.
<</SYS>>

Detected objects: {objects}. Describe the scene for someone who can't see. [/INST]"""
        
        try:
            response = self.llm(
                prompt=prompt,
                max_tokens=100,
                temperature=0.7,
                top_p=0.95,
                repeat_penalty=1.1,
                stop=["</s>", "\n"]
            )
            return response['choices'][0]['text'].strip()
        except Exception as e:
            print(f"LLM Error: {e}")
            return "I'm having trouble understanding the scene."