---
layout: default
title: Omni-Judge: Can Omni-LLMs Serve as Human-Aligned Judges for Text-Conditioned Audio-Video Generation?
---

# Omni-Judge: Can Omni-LLMs Serve as Human-Aligned Judges for Text-Conditioned Audio-Video Generation?
**arXiv**：[2602.01623v1](https://arxiv.org/abs/2602.01623) · [PDF](https://arxiv.org/pdf/2602.01623.pdf)  
**作者**：Susan Liang, Chao Huang, Filippos Bellos, Yolo Yunlong Tang, Qianxiang Shen, Jing Bi, Luchuan Song, Zeliang Zhang, Jason Corso, Chenliang Xu  

**一句话要点**：提出Omni-Judge研究，评估全模态大语言模型能否作为文本条件音频-视频生成的人类对齐评判器。

**关键词**：全模态大语言模型, 音频-视频生成评估, 多模态对齐, 可解释性评估, 文本条件生成

## 3 点简述
- 核心问题：文本到音频-视频生成模型的评估缺乏可靠、可扩展的自动方法。
- 方法要点：利用全模态大语言模型处理音频、视频和文本，提供可解释的推理反馈。
- 实验或效果：在语义对齐任务上表现优异，但在高帧率感知指标上受限，提供可解释性反馈。

## 摘要（原文）

> State-of-the-art text-to-video generation models such as Sora 2 and Veo 3 can now produce high-fidelity videos with synchronized audio directly from a textual prompt, marking a new milestone in multi-modal generation. However, evaluating such tri-modal outputs remains an unsolved challenge. Human evaluation is reliable but costly and difficult to scale, while traditional automatic metrics, such as FVD, CLAP, and ViCLIP, focus on isolated modality pairs, struggle with complex prompts, and provide limited interpretability. Omni-modal large language models (omni-LLMs) present a promising alternative: they naturally process audio, video, and text, support rich reasoning, and offer interpretable chain-of-thought feedback. Driven by this, we introduce Omni-Judge, a study assessing whether omni-LLMs can serve as human-aligned judges for text-conditioned audio-video generation. Across nine perceptual and alignment metrics, Omni-Judge achieves correlation comparable to traditional metrics and excels on semantically demanding tasks such as audio-text alignment, video-text alignment, and audio-video-text coherence. It underperforms on high-FPS perceptual metrics, including video quality and audio-video synchronization, due to limited temporal resolution. Omni-Judge provides interpretable explanations that expose semantic or physical inconsistencies, enabling practical downstream uses such as feedback-based refinement. Our findings highlight both the potential and current limitations of omni-LLMs as unified evaluators for multi-modal generation.

