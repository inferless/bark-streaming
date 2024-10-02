from bark import SAMPLE_RATE, generate_audio, preload_models
from bark import generate_text_semantic, semantic_to_waveform
import time
import numpy as np
import io
import base64
import soundfile as SF
import nltk

class InferlessPythonModel:
    
    def initialize(self):
        preload_models()
        nltk.download('punkt')
        
    def infer(self, inputs):
        prompt = inputs["prompt"]
        audio_array = generate_audio(prompt)
        buffer = io.BytesIO()
        
        sf.write(buffer, audio_array,SAMPLE_RATE, format='WAV')
        buffer.seek(0)
        base64_audio = base64.b64encode(buffer.read()).decode('utf-8')
        
        return {"generated_audio_base64": base64_audio}

    def finalize(self,args):
        self.pipe = None
