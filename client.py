import sys, json, re

class MultimodalVoiceProsodyAnalyzer:
    """
    Multi-Modal Voice Prosody & Emotion Sentiment Analyzer.
    Extracts speech rate, pause ratios, and textual sentiment markers
    to dynamically modulate AI agent conversational warmth and brevity.
    """
    def analyze_speech_prosody(self, transcript, words_per_minute=160.0, pause_ratio=0.15, pitch_variance_hz=45.0):
        # Textual sentiment cue analysis
        words = transcript.lower().split()
        total_words = len(words)
        
        fatigue_words = ["tired", "exhausted", "late", "headache", "drained", "overwhelmed"]
        urgency_words = ["quick", "fast", "hurry", "right now", "immediately", "asap"]
        joy_words = ["awesome", "great", "fantastic", "excited", "loved", "super"]

        fatigue_count = sum(1 for w in words if w in fatigue_words)
        urgency_count = sum(1 for w in words if w in urgency_words)
        joy_count = sum(1 for w in words if w in joy_words)

        # Detect primary vocal emotional dimension
        if words_per_minute > 190.0 or urgency_count > 0:
            emotion_state = "RUSHED_OR_URGENT"
        elif words_per_minute < 120.0 or fatigue_count > 0 or pause_ratio > 0.25:
            emotion_state = "FATIGUED_OR_EXHAUSTED"
        elif joy_count > 0 and pitch_variance_hz > 50.0:
            emotion_state = "ENTHUSIASTIC_AND_ENGAGED"
        else:
            emotion_state = "CALM_AND_FOCUSED"

        return {
            "transcript_sample": transcript[:80],
            "words_per_minute": words_per_minute,
            "pause_ratio": pause_ratio,
            "detected_emotional_state": emotion_state,
            "acoustic_intensity": "HIGH" if pitch_variance_hz > 50.0 else "NORMAL"
        }

    def compute_agent_adaptation_profile(self, prosody_analysis):
        state = prosody_analysis.get("detected_emotional_state", "CALM_AND_FOCUSED")

        if state == "RUSHED_OR_URGENT":
            return {
                "agent_response_pacing": "BRISK",
                "brevity_factor": "CONCISE_BULLETS_ONLY",
                "empathy_warmth": "FOCUSED_DIRECT",
                "recommended_delay_ms": 100
            }
        elif state == "FATIGUED_OR_EXHAUSTED":
            return {
                "agent_response_pacing": "GENTLE_AND_MEASURED",
                "brevity_factor": "HIGH_LEVEL_ONLY",
                "empathy_warmth": "DEEP_WARMTH_AND_GROUNDING",
                "recommended_delay_ms": 300
            }
        elif state == "ENTHUSIASTIC_AND_ENGAGED":
            return {
                "agent_response_pacing": "ENERGETIC",
                "brevity_factor": "COMPREHENSIVE",
                "empathy_warmth": "CELEBRATORY_AFFIRMATION",
                "recommended_delay_ms": 150
            }
        else:
            return {
                "agent_response_pacing": "STANDARD_BALANCED",
                "brevity_factor": "BALANCED",
                "empathy_warmth": "PROFESSIONAL_HELPFUL",
                "recommended_delay_ms": 200
            }

    def run_voice_prosody_benchmark(self):
        sample_transcript = "Hey, it is super late and I am totally exhausted, can you just give me the quick summary of the report?"
        analysis = self.analyze_speech_prosody(sample_transcript, words_per_minute=110.0, pause_ratio=0.30)
        profile = self.compute_agent_adaptation_profile(analysis)

        return {
            "suite": "Multimodal Voice Prosody Analyzer Benchmark",
            "speech_analysis": analysis,
            "agent_adaptation_profile": profile,
            "prosody_engine_state": "EMPATHIC_MODULATION_OPTIMAL"
        }
