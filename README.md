# Edge TTS Skill for Claude

这是一个为 Claude 设计的 Skill (能力扩展包)，集成了 Microsoft Edge 的免费 TTS (Text-to-Speech) 服务。它允许 Claude 直接将文本转换为自然流畅的语音文件。

## 什么是 Claude Skill?

Claude Skill (Agent Skill) 是一种标准化的方式，用于扩展 Claude 的能力。通过 Skill，我们可以教 Claude 如何执行特定的任务、遵循特定的规范或使用特定的工具。

本项目遵循 [Agent Skills](https://agentskills.io) 标准，可以被 Claude Code、Claude.ai 以及其他支持该标准的 AI 代理加载和使用。

## ✨ 功能特性

- **免费且高质量**：使用 Microsoft Edge 在线 TTS 引擎，语音自然逼真。
- **多语言支持**：支持中文、英文等多种语言。
- **丰富的语音库**：
  - `zh-CN-XiaoxiaoNeural` (晓晓 - 女声)
  - `zh-CN-YunxiNeural` (云希 - 男声)
  - 以及更多...
- **精细控制**：支持调整语速 (Rate) 和音量 (Volume)。
- **多种输入**：支持直接输入文本或从文件读取文本。

## 📂 目录结构

```text
edge-tts/
├── SKILL.md                       # Skill 核心定义文件 (指令与元数据)
├── README.md                      # 项目说明文档
├── scripts/
│   ├── edge_tts_synthesizer.py    # 核心 Python 脚本
│   ├── requirements.txt           # Python 依赖
│   └── install_dependencies.sh    # 依赖安装脚本
└── references/                    # 参考文档
```

## 🚀 如何使用

### 1. 作为 Claude Skill 使用

要让 Claude 获得此能力，请确保本目录位于 Claude 的技能搜索路径中：

- **项目级**：将本仓库克隆到你的项目根目录下的 `.claude/skills/edge-tts/`。
- **用户级**：将本仓库克隆到 `~/.claude/skills/edge-tts/`。

加载成功后，你可以直接对 Claude 说：
> "帮我把这段话转成语音：你好，世界！"
> "将 `script.txt` 的内容合成音频，使用云希的声音，语速快一点。"

### 2. 作为独立工具使用

你也可以直接运行 Python 脚本来使用此功能。

**安装依赖：**

```bash
pip install -r scripts/requirements.txt
```

**命令行使用：**

```bash
# 简单合成
python scripts/edge_tts_synthesizer.py -t "你好，世界" -o output.mp3

# 指定语音和参数
python scripts/edge_tts_synthesizer.py \
  -t "这是一个测试" \
  -o test.mp3 \
  -v zh-CN-YunxiNeural \
  --rate +20%
```

查看完整帮助：
```bash
python scripts/edge_tts_synthesizer.py --help
```

## 🛠️ 开发与贡献

如果你想扩展这个 Skill：
1. 修改 `scripts/edge_tts_synthesizer.py` 增加新功能。
2. 更新 `SKILL.md` 中的指令，告诉 Claude 如何使用新参数。
3. 提交 PR！

## 📄 License

MIT
