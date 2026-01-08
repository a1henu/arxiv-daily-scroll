---
layout: default
title: Lightweight and perceptually-guided voice conversion for electro-laryngeal speech
---

# Lightweight and perceptually-guided voice conversion for electro-laryngeal speech
**arXiv**：[2601.03892v1](https://arxiv.org/abs/2601.03892) · [PDF](https://arxiv.org/pdf/2601.03892.pdf)  
**作者**：Benedikt Mayrhofer, Franz Pernkopf, Philipp Aichinger, Martin Hagmüller  

**一句话要点**：提出轻量级感知引导语音转换方法，用于改善电子喉语音的自然度和可懂度。

**关键词**：语音转换, 电子喉语音, 轻量级架构, 感知损失, 可懂度提升, 自监督学习

## 3 点简述
- 电子喉语音存在音高恒定、韵律有限和机械噪声问题，降低自然度和可懂度。
- 通过移除音高和能量模块，结合自监督预训练与监督微调，并引入感知和可懂度损失进行优化。
- 最佳模型显著降低字符错误率，提升自然度评分，缩小与健康语音的差距。

## 摘要（原文）

> Electro-laryngeal (EL) speech is characterized by constant pitch, limited prosody, and mechanical noise, reducing naturalness and intelligibility. We propose a lightweight adaptation of the state-of-the-art StreamVC framework to this setting by removing pitch and energy modules and combining self-supervised pretraining with supervised fine-tuning on parallel EL and healthy (HE) speech data, guided by perceptual and intelligibility losses. Objective and subjective evaluations across different loss configurations confirm their influence: the best model variant, based on WavLM features and human-feedback predictions (+WavLM+HF), drastically reduces character error rate (CER) of EL inputs, raises naturalness mean opinion score (nMOS) from 1.1 to 3.3, and consistently narrows the gap to HE ground-truth speech in all evaluated metrics. These findings demonstrate the feasibility of adapting lightweight voice conversion architectures to EL voice rehabilitation while also identifying prosody generation and intelligibility improvements as the main remaining bottlenecks.

