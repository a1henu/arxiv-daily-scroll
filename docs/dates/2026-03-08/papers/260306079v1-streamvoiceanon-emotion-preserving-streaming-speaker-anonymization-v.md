---
layout: default
title: StreamVoiceAnon+: Emotion-Preserving Streaming Speaker Anonymization via Frame-Level Acoustic Distillation
---

# StreamVoiceAnon+: Emotion-Preserving Streaming Speaker Anonymization via Frame-Level Acoustic Distillation
**arXiv**：[2603.06079v1](https://arxiv.org/abs/2603.06079) · [PDF](https://arxiv.org/pdf/2603.06079.pdf)  
**作者**：Nikita Kuzmin, Kong Aik Lee, Eng Siong Chng  

**一句话要点**：提出StreamVoiceAnon+，通过帧级声学蒸馏在流式说话人匿名化中保留情感内容

**关键词**：流式说话人匿名化, 情感保留, 声学蒸馏, 神经音频编解码, 监督微调, 帧级处理

## 3 点简述
- 核心问题：流式说话人匿名化中，神经音频编解码语言模型易导致情感信息丢失，影响匿名语音的自然度。
- 方法要点：采用同一说话人的中性情感话语对进行监督微调，结合声学令牌隐藏状态的帧级情感蒸馏，优化模型以保留副语言属性。
- 实验或效果：在VoicePrivacy 2024协议上，情感保留UAR达49.2%，相对基线提升24%，推理延迟无增加，流式延迟保持180ms。

## 摘要（原文）

> We address the challenge of preserving emotional content in streaming speaker anonymization (SA). Neural audio codec language models trained for audio continuation tend to degrade source emotion: content tokens discard emotional information, and the model defaults to dominant acoustic patterns rather than preserving paralinguistic attributes. We propose supervised finetuning with neutral-emotion utterance pairs from the same speaker, combined with frame-level emotion distillation on acoustic token hidden states. All modifications are confined to finetuning, which takes less than 2 hours on 4 GPUs and adds zero inference latency overhead, while maintaining a competitive 180ms streaming latency. On the VoicePrivacy 2024 protocol, our approach achieves a 49.2% UAR (emotion preservation) with 5.77% WER (intelligibility), a +24% relative UAR improvement over the baseline (39.7%->49.2%) and +10% over the emotion-prompt variant (44.6% UAR), while maintaining strong privacy (EER 49.0%). Demo and code are available: https://anonymous3842031239.github.io/

