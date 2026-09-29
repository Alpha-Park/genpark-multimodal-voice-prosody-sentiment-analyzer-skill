from client import MultimodalVoiceProsodyAnalyzer
import json

analyzer = MultimodalVoiceProsodyAnalyzer()
print("=== MULTIMODAL VOICE PROSODY ANALYZER BENCHMARK ===")
res = analyzer.run_voice_prosody_benchmark()
print(json.dumps(res, indent=2))
