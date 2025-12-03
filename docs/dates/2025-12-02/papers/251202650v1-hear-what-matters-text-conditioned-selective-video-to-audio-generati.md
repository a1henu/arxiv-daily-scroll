---
layout: default
title: Hear What Matters! Text-conditioned Selective Video-to-Audio Generation
---

# Hear What Matters! Text-conditioned Selective Video-to-Audio Generation
**arXiv**：[2512.02650v1](https://arxiv.org/abs/2512.02650) · [PDF](https://arxiv.org/pdf/2512.02650.pdf)  
**作者**：Junwon Lee, Juhan Nam, Jiyoung Lee  

**一句话要点**：提出SelVA模型以解决多对象视频中文本条件选择性音频生成问题

**关键词**：视频到音频生成, 文本条件生成, 选择性音频分离, 跨注意力调制, 自增强训练

## 3 点简述
- 核心问题：现有方法生成混合音频，难以从多对象视频中分离用户指定声源。
- 方法要点：使用文本提示作为目标源选择器，调制视频编码器提取相关特征，并引入补充令牌优化跨注意力。
- 实验或效果：在VGG-MONOAUDIO基准上验证，音频质量、语义对齐和时间同步表现优异。

## 摘要（原文）

> This work introduces a new task, text-conditioned selective video-to-audio (V2A) generation, which produces only the user-intended sound from a multi-object video. This capability is especially crucial in multimedia production, where audio tracks are handled individually for each sound source for precise editing, mixing, and creative control. However, current approaches generate single source-mixed sounds at once, largely because visual features are entangled, and region cues or prompts often fail to specify the source. We propose SelVA, a novel text-conditioned V2A model that treats the text prompt as an explicit selector of target source and modulates video encoder to distinctly extract prompt-relevant video features. The proposed supplementary tokens promote cross-attention by suppressing text-irrelevant activations with efficient parameter tuning, yielding robust semantic and temporal grounding. SelVA further employs a self-augmentation scheme to overcome the lack of mono audio track supervision. We evaluate SelVA on VGG-MONOAUDIO, a curated benchmark of clean single-source videos for such a task. Extensive experiments and ablations consistently verify its effectiveness across audio quality, semantic alignment, and temporal synchronization. Code and demo are available at https://jnwnlee.github.io/selva-demo/.

