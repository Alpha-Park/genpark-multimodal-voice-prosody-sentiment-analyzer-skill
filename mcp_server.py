import sys, json
from client import MultimodalVoiceProsodyAnalyzer

def handle_mcp():
    analyzer = MultimodalVoiceProsodyAnalyzer()
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(analyzer.run_voice_prosody_benchmark(), indent=2))
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")
            
            if method == "initialize":
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {
                    "protocolVersion": "2024-11-05",
                    "serverInfo": {"name": "genpark-multimodal-voice-prosody-sentiment-analyzer-skill", "version": "1.0.0"},
                    "capabilities": {"tools": {}}
                }}
            elif method == "tools/list":
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {"tools": [
                    {"name": "analyze_speech_prosody", "description": "Analyze vocal prosody metrics and emotional state.", "inputSchema": {"type": "object", "properties": {"transcript": {"type": "string"}, "words_per_minute": {"type": "number"}}}},
                    {"name": "compute_agent_adaptation_profile", "description": "Compute agent conversational modulation.", "inputSchema": {"type": "object", "properties": {"prosody_analysis": {"type": "object"}}}},
                    {"name": "run_voice_prosody_benchmark", "description": "Run voice prosody benchmark.", "inputSchema": {"type": "object"}}
                ]}}
            elif method == "tools/call":
                tname = req.get("params", {}).get("name")
                args = req.get("params", {}).get("arguments", {})
                if tname == "analyze_speech_prosody":
                    res = analyzer.analyze_speech_prosody(args.get("transcript", ""), args.get("words_per_minute", 160.0))
                elif tname == "compute_agent_adaptation_profile":
                    res = analyzer.compute_agent_adaptation_profile(args.get("prosody_analysis", {}))
                else:
                    res = analyzer.run_voice_prosody_benchmark()
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
            else:
                resp = {"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}
            
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32000, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    handle_mcp()
