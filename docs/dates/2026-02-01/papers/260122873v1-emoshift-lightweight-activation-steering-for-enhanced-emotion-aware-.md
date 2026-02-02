---
layout: default
title: EmoShift: Lightweight Activation Steering for Enhanced Emotion-Aware Speech Synthesis
---

# EmoShift: Lightweight Activation Steering for Enhanced Emotion-Aware Speech Synthesis
**arXiv**：[2601.22873v1](https://arxiv.org/abs/2601.22873) · [PDF](https://arxiv.org/pdf/2601.22873.pdf)  
**作者**：Li Zhou, Hao Jiang, Junjie Li, Tianrui Wang, Haizhou Li  

**一句话要点**：提出EmoShift轻量激活引导框架以增强语音合成中的情感表达可控性

**关键词**：语音合成, 情感表达, 激活引导, 轻量微调, 可控性

## 3 点简述
- 核心问题：现有情感感知TTS系统依赖固定嵌入或外部引导，难以建模情感特定潜在特征。
- 方法要点：引入EmoSteer层学习情感引导向量，在输出嵌入空间捕获潜在偏移，保持稳定表达。
- 实验或效果：仅10M可训练参数，优于零样本和全微调基线，提升情感表现力同时保持自然度和说话人相似性。

## 摘要（原文）

> Achieving precise and controllable emotional expression is crucial for producing natural and context-appropriate speech in text-to-speech (TTS) synthesis. However, many emotion-aware TTS systems, including large language model (LLM)-based designs, rely on scaling fixed emotion embeddings or external guidance, limiting their ability to model emotion-specific latent characteristics. To address this gap, we present EmoShift, a lightweight activation-steering framework incorporating a EmoSteer layer, which learns a steering vector for each target emotion in the output embedding space to capture its latent offset and maintain stable, appropriate expression across utterances and categories. With only 10M trainable parameters,less than 1/30 of full fine-tuning, EmoShift outperforms zero-shot and fully fine-tuned baselines in objective and subjective evaluations, enhancing emotional expressiveness while preserving naturalness and speaker similarity. Further analysis confirms the proposed EmoSteer layer's effectiveness and reveals its potential for controllable emotional intensity in speech synthesis.

