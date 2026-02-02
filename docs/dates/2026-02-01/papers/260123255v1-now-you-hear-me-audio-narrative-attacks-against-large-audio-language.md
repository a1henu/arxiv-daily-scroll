---
layout: default
title: Now You Hear Me: Audio Narrative Attacks Against Large Audio-Language Models
---

# Now You Hear Me: Audio Narrative Attacks Against Large Audio-Language Models
**arXiv**：[2601.23255v1](https://arxiv.org/abs/2601.23255) · [PDF](https://arxiv.org/pdf/2601.23255.pdf)  
**作者**：Ye Yu, Haibo Jin, Yaoning Yu, Jun Zhuang, Haohan Wang  

**一句话要点**：提出音频叙事攻击方法，利用文本转语音模型绕过大型音频语言模型的安全机制。

**关键词**：音频语言模型, 安全漏洞, 文本转语音攻击, 叙事风格音频, 越狱攻击

## 3 点简述
- 核心问题：大型音频语言模型处理原始语音输入时存在未充分表征的安全漏洞。
- 方法要点：设计文本转音频越狱攻击，将禁止指令嵌入叙事风格音频流中。
- 实验或效果：攻击在Gemini 2.0 Flash等模型上成功率高达98.26%，远超纯文本基线。

## 摘要（原文）

> Large audio-language models increasingly operate on raw speech inputs, enabling more seamless integration across domains such as voice assistants, education, and clinical triage. This transition, however, introduces a distinct class of vulnerabilities that remain largely uncharacterized. We examine the security implications of this modality shift by designing a text-to-audio jailbreak that embeds disallowed directives within a narrative-style audio stream. The attack leverages an advanced instruction-following text-to-speech (TTS) model to exploit structural and acoustic properties, thereby circumventing safety mechanisms primarily calibrated for text. When delivered through synthetic speech, the narrative format elicits restricted outputs from state-of-the-art models, including Gemini 2.0 Flash, achieving a 98.26% success rate that substantially exceeds text-only baselines. These results highlight the need for safety frameworks that jointly reason over linguistic and paralinguistic representations, particularly as speech-based interfaces become more prevalent.

