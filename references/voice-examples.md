# Voice Examples and Advanced Usage

## Common Voice Selection Patterns

### By Gender

**Female voices (recommended for general use):**
- `zh-CN-XiaoxiaoNeural` - 晓晓 (warm, friendly)
- `zh-CN-XiaoyiNeural` - 晓伊 (clear, professional)
- `zh-CN-XiaochenNeural` - 晓辰 (energetic)
- `zh-CN-XiaohanNeural` - 晓涵 (calm)
- `zh-CN-XiaomengNeural` - 晓梦 (gentle)
- `zh-CN-XiaomoNeural` - 晓墨 (mature)
- `zh-CN-XiaoqiuNeural` - 晓秋 (warm)
- `zh-CN-XiaoruiNeural` - 晓睿 (clear)
- `zh-CN-XiaoshuangNeural` - 晓双 (lively)
- `zh-CN-XiaoxuanNeural` - 晓萱 (soft)
- `zh-CN-XiaoyanNeural` - 晓颜 (sweet)
- `zh-CN-XiaoyouNeural` - 晓悠 (child voice)
- `zh-CN-XiaozhenNeural` - 晓甄 (professional)

**Male voices:**
- `zh-CN-YunxiNeural` - 云希 (warm, general use)
- `zh-CN-YunjianNeural` - 云健 (strong, newsreader)
- `zh-CN-YunyangNeural` - 云扬 (energetic, young)
- `zh-CN-YunfengNeural` - 云枫 (calm, mature)
- `zh-CN-YunhaoNeural` - 云皓 (bright)
- `zh-CN-YunxiaNeural` - 云夏 (clear)
- `zh-CN-YunyeNeural` - 云野 (storyteller)

### By Use Case

**Professional/News:**
- `zh-CN-XiaoyiNeural` (female)
- `zh-CN-YunjianNeural` (male)

**Friendly/Conversational:**
- `zh-CN-XiaoxiaoNeural` (female, default)
- `zh-CN-YunxiNeural` (male)

**Storytelling/Narration:**
- `zh-CN-XiaomengNeural` (female, gentle)
- `zh-CN-YunyeNeural` (male, storyteller)

**Children's Content:**
- `zh-CN-XiaoyouNeural` (child voice)

### Regional Varieties

**Mainland China (zh-CN):** Standard Mandarin (see above)

**Taiwan (zh-TW):**
- `zh-TW-HsiaoChenNeural` (female)
- `zh-TW-HsiaoYuNeural` (female)
- `zh-TW-YunJheNeural` (male)

**Hong Kong (zh-HK):**
- `zh-HK-HiuGaaiNeural` (female)
- `zh-HK-HiuMaanNeural` (female)
- `zh-HK-WanLungNeural` (male)

## Advanced Examples

### Creating Dialogue with Multiple Voices

```bash
# Character 1 (female)
python scripts/edge_tts_synthesizer.py \
  -t "你好，今天天气真好！" \
  -o dialogue_part1.mp3 \
  -v zh-CN-XiaoxiaoNeural

# Character 2 (male)
python scripts/edge_tts_synthesizer.py \
  -t "是啊，我们出去走走吧。" \
  -o dialogue_part2.mp3 \
  -v zh-CN-YunxiNeural
```

### Speed Variations for Different Content Types

```bash
# Slow for educational content
python scripts/edge_tts_synthesizer.py \
  -t "这是一个重要的概念，请仔细理解。" \
  -o educational.mp3 \
  --rate -10%

# Normal speed for general narration
python scripts/edge_tts_synthesizer.py \
  -t "故事发生在一个晴朗的早晨。" \
  -o narration.mp3 \
  --rate +0%

# Fast for exciting action
python scripts/edge_tts_synthesizer.py \
  -t "快跑！他们追上来了！" \
  -o action.mp3 \
  --rate +30%
```

### Emphasis with Volume

```bash
# Normal volume for main content
python scripts/edge_tts_synthesizer.py \
  -t "这是主要内容。" \
  -o main.mp3 \
  --volume +0%

# Louder for emphasis
python scripts/edge_tts_synthesizer.py \
  -t "这一点非常重要！" \
  -o emphasis.mp3 \
  --volume +30%
```

### Multi-language Support

```bash
# English
python scripts/edge_tts_synthesizer.py \
  -t "Hello, this is a test." \
  -o english.mp3 \
  -v en-US-JennyNeural

# Japanese
python scripts/edge_tts_synthesizer.py \
  -t "こんにちは、世界。" \
  -o japanese.mp3 \
  -v ja-JP-NanamiNeural

# Korean
python scripts/edge_tts_synthesizer.py \
  -t "안녕하세요, 세계입니다." \
  -o korean.mp3 \
  -v ko-KR-SunHiNeural
```

## Parameter Ranges

### Rate (Speed)
- Minimum: `-50%` (half speed)
- Maximum: `+100%` (double speed)
- Recommended range: `-20%` to `+50%`
- Default: `+0%`

### Volume
- Minimum: `-50%` (quieter)
- Maximum: `+50%` (louder)
- Recommended range: `-10%` to `+30%`
- Default: `+0%`

## Tips for Best Results

1. **Choose appropriate voice for content:**
   - Use calm, clear voices for educational content
   - Use energetic voices for marketing or entertainment
   - Use professional voices for news or formal content

2. **Adjust speed based on content complexity:**
   - Slower for complex technical content
   - Normal for storytelling
   - Faster for action or excitement

3. **Consider your audience:**
   - Children's content: use XiaoyouNeural or gentler voices
   - Professional audience: use XiaoyiNeural or YunjianNeural
   - General audience: use XiaoxiaoNeural or YunxiNeural

4. **File naming for batch processing:**
   - Use descriptive names: `chapter1_xiaoxiao.mp3`
   - Include voice name for comparison: `test_yunxi.mp3`
   - Use timestamps for versions: `script_20240101.mp3`
