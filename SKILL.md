---
name: edge-tts
description: Text-to-speech synthesis using Microsoft Edge's free TTS service. Use when users request converting text to audio, generating speech from text, creating audio files, or mention TTS, text-to-speech, voice synthesis, or want to convert txt files to mp3/wav. Supports Chinese and other languages with multiple voices, adjustable speed and volume.
---

# Edge TTS - Text-to-Speech Synthesis

Convert text to natural-sounding speech using Microsoft Edge's free TTS service.

## Quick Start

Generate audio from text:

```bash
python scripts/edge_tts_synthesizer.py -t "你好，世界！" -o output.mp3
```

Generate audio from a text file:

```bash
python scripts/edge_tts_synthesizer.py -f input.txt -o output.mp3
```

## Common Usage Patterns

### Basic text synthesis

For simple text-to-speech:

```bash
python scripts/edge_tts_synthesizer.py \
  -t "Your text here" \
  -o output.mp3
```

### Using different voices

Choose from available voices (default is zh-CN-XiaoxiaoNeural - female voice):

```bash
# Male voice (Yunxi)
python scripts/edge_tts_synthesizer.py \
  -t "这是男声示例" \
  -o output.mp3 \
  -v zh-CN-YunxiNeural

# Female voice (Xiaoyi)
python scripts/edge_tts_synthesizer.py \
  -t "这是女声示例" \
  -o output.mp3 \
  -v zh-CN-XiaoyiNeural
```

**Common Chinese voices:**
- `zh-CN-XiaoxiaoNeural` - 晓晓 (female, default)
- `zh-CN-YunxiNeural` - 云希 (male)
- `zh-CN-XiaoyiNeural` - 晓伊 (female)
- `zh-CN-YunjianNeural` - 云健 (male)
- `zh-CN-YunyangNeural` - 云扬 (male)

To list all available voices:

```bash
python scripts/edge_tts_synthesizer.py --list-voices
```

### Adjusting speed and volume

Control speech rate and volume:

```bash
# Faster speech (+50%)
python scripts/edge_tts_synthesizer.py \
  -t "快速朗读" \
  -o output.mp3 \
  --rate +50%

# Slower speech (-20%)
python scripts/edge_tts_synthesizer.py \
  -t "慢速朗读" \
  -o output.mp3 \
  --rate -20%

# Louder volume (+30%)
python scripts/edge_tts_synthesizer.py \
  -t "大声朗读" \
  -o output.mp3 \
  --volume +30%

# Combined adjustments
python scripts/edge_tts_synthesizer.py \
  -t "又快又大声" \
  -o output.mp3 \
  --rate +50% \
  --volume +20%
```

### Processing text files

Read from a file instead of inline text:

```bash
python scripts/edge_tts_synthesizer.py \
  -f input.txt \
  -o output.mp3 \
  -v zh-CN-XiaoxiaoNeural
```

### Batch processing

When processing multiple texts or creating multiple voice versions:

```bash
# Create multiple voice versions
for voice in zh-CN-XiaoxiaoNeural zh-CN-YunxiNeural zh-CN-XiaoyiNeural; do
  python scripts/edge_tts_synthesizer.py \
    -t "同样的文本，不同的声音" \
    -o "output_${voice}.mp3" \
    -v "$voice"
done

# Process multiple text files
for file in *.txt; do
  python scripts/edge_tts_synthesizer.py \
    -f "$file" \
    -o "${file%.txt}.mp3"
done
```

## Output Format

The script supports multiple audio formats:
- `.mp3` (recommended for smaller file size)
- `.wav` (recommended for higher quality)
- Other formats supported by Edge TTS

Specify the format via the output filename extension.

## Error Handling

If synthesis fails:
1. Check internet connection (Edge TTS requires online access)
2. Verify the voice name is correct (use `--list-voices`)
3. Ensure output directory exists and is writable
4. Check that the text encoding is UTF-8 for non-ASCII characters

## Dependencies

This script requires the `edge-tts` Python package. Install with:

```bash
pip install edge-tts
```

The script handles this automatically via the import, but users need the package installed.
