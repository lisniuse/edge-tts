"""
Edge TTS 音频合成工具
使用微软Edge的免费TTS服务合成音频
"""

import asyncio
import argparse
import edge_tts
import os


async def list_voices():
    """列出所有可用的语音"""
    voices = await edge_tts.list_voices()

    print("\n可用的中文语音:")
    print("-" * 80)
    chinese_voices = [v for v in voices if v["Locale"].startswith("zh")]
    for voice in chinese_voices:
        print(f"名称: {voice['ShortName']}")
        print(f"  语言: {voice['Locale']}")
        print(f"  性别: {voice['Gender']}")
        print(f"  描述: {voice['FriendlyName']}")
        print()

    return voices


async def synthesize_text(text, output_file, voice="zh-CN-XiaoxiaoNeural", rate="+0%", volume="+0%"):
    """
    合成文本到音频文件

    参数:
        text: 要合成的文本
        output_file: 输出文件路径
        voice: 语音名称 (默认: zh-CN-XiaoxiaoNeural - 晓晓)
        rate: 语速调整 (例如: +50%, -20%, +0%)
        volume: 音量调整 (例如: +50%, -20%, +0%)
    """
    communicate = edge_tts.Communicate(text, voice, rate=rate, volume=volume)

    print(f"\n正在合成音频...")
    print(f"文本: {text[:50]}{'...' if len(text) > 50 else ''}")
    print(f"语音: {voice}")
    print(f"语速: {rate}")
    print(f"音量: {volume}")
    print(f"输出: {output_file}")

    await communicate.save(output_file)
    print(f"\n✓ 合成完成! 文件已保存到: {output_file}")


async def synthesize_from_file(input_file, output_file, voice="zh-CN-XiaoxiaoNeural", rate="+0%", volume="+0%"):
    """从文本文件读取内容并合成"""
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read().strip()

    await synthesize_text(text, output_file, voice, rate, volume)


def main():
    parser = argparse.ArgumentParser(
        description="Edge TTS 音频合成工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  # 列出所有可用的语音
  python edge_tts_synthesizer.py --list-voices

  # 合成简单文本
  python edge_tts_synthesizer.py -t "你好，世界！" -o output.mp3

  # 使用不同的语音
  python edge_tts_synthesizer.py -t "Hello World" -o output.mp3 -v zh-CN-YunxiNeural

  # 调整语速和音量
  python edge_tts_synthesizer.py -t "快速朗读" -o output.mp3 --rate +50% --volume +20%

  # 从文件读取文本
  python edge_tts_synthesizer.py -f input.txt -o output.mp3

常用中文语音:
  zh-CN-XiaoxiaoNeural  - 晓晓 (女声)
  zh-CN-YunxiNeural     - 云希 (男声)
  zh-CN-XiaoyiNeural    - 晓伊 (女声)
  zh-CN-YunjianNeural   - 云健 (男声)
  zh-CN-YunyangNeural   - 云扬 (男声)
        """
    )

    parser.add_argument('-l', '--list-voices', action='store_true',
                        help='列出所有可用的语音')
    parser.add_argument('-t', '--text', type=str,
                        help='要合成的文本')
    parser.add_argument('-f', '--file', type=str,
                        help='包含要合成文本的文件路径')
    parser.add_argument('-o', '--output', type=str,
                        help='输出音频文件路径 (支持 .mp3, .wav 等格式)')
    parser.add_argument('-v', '--voice', type=str, default='zh-CN-XiaoxiaoNeural',
                        help='语音名称 (默认: zh-CN-XiaoxiaoNeural)')
    parser.add_argument('--rate', type=str, default='+0%',
                        help='语速调整 (例如: +50%%, -20%%, 默认: +0%%)')
    parser.add_argument('--volume', type=str, default='+0%',
                        help='音量调整 (例如: +50%%, -20%%, 默认: +0%%)')

    args = parser.parse_args()

    # 列出语音
    if args.list_voices:
        asyncio.run(list_voices())
        return

    # 验证参数
    if not args.text and not args.file:
        parser.error("请提供 --text 或 --file 参数")

    if not args.output:
        parser.error("请提供 --output 参数指定输出文件")

    # 确保输出目录存在
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 合成音频
    try:
        if args.file:
            asyncio.run(synthesize_from_file(
                args.file, args.output, args.voice, args.rate, args.volume
            ))
        else:
            asyncio.run(synthesize_text(
                args.text, args.output, args.voice, args.rate, args.volume
            ))
    except Exception as e:
        print(f"\n✗ 错误: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
