---
layout: default
title: Audio Deepfake Detection in the Age of Advanced Text-to-Speech models
---

# Audio Deepfake Detection in the Age of Advanced Text-to-Speech models
**arXiv**：[2601.20510v1](https://arxiv.org/abs/2601.20510) · [PDF](https://arxiv.org/pdf/2601.20510.pdf)  
**作者**：Robin Singh, Aditya Yogesh Nair, Fabio Palumbo, Florian Barbaro, Anna Dyka, Lohith Rachakonda  

**一句话要点**：评估先进TTS模型的音频深度伪造检测，提出多视图方法提升鲁棒性

**关键词**：音频深度伪造检测, 文本到语音模型, 多视图检测, 合成语音评估, 检测框架比较

## 3 点简述
- 核心问题：先进TTS模型提升合成语音真实感，对音频深度伪造检测构成新挑战。
- 方法要点：比较三种先进TTS模型，评估四种检测框架，包括语义、结构和信号级方法。
- 实验或效果：多视图检测方法结合互补分析层级，在所有评估模型中表现鲁棒。

## 摘要（原文）

> Recent advances in Text-to-Speech (TTS) systems have substantially increased the realism of synthetic speech, raising new challenges for audio deepfake detection. This work presents a comparative evaluation of three state-of-the-art TTS models--Dia2, Maya1, and MeloTTS--representing streaming, LLM-based, and non-autoregressive architectures. A corpus of 12,000 synthetic audio samples was generated using the Daily-Dialog dataset and evaluated against four detection frameworks, including semantic, structural, and signal-level approaches. The results reveal significant variability in detector performance across generative mechanisms: models effective against one TTS architecture may fail against others, particularly LLM-based synthesis. In contrast, a multi-view detection approach combining complementary analysis levels demonstrates robust performance across all evaluated models. These findings highlight the limitations of single-paradigm detectors and emphasize the necessity of integrated detection strategies to address the evolving landscape of audio deepfake threats.

