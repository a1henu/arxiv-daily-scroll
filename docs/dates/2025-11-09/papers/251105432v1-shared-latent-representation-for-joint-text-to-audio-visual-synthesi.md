---
layout: default
title: Shared Latent Representation for Joint Text-to-Audio-Visual Synthesis
---

# Shared Latent Representation for Joint Text-to-Audio-Visual Synthesis
**arXiv**：[2511.05432v1](https://arxiv.org/abs/2511.05432) · [PDF](https://arxiv.org/pdf/2511.05432.pdf)  
**作者**：Dogucan Yaman, Seymanur Akti, Fevziye Irem Eyiokur, Alexander Waibel  

**一句话要点**：提出基于共享潜在表示的文本到音视频合成框架，实现无真实音频的同步语音与面部生成。

**关键词**：文本到音视频合成, 潜在表示学习, 音频-视觉对齐, 两阶段训练, 唇同步生成

## 3 点简述
- 核心问题：文本到音视频合成中，如何实现紧密的音频-视觉对齐并保持说话者身份。
- 方法要点：使用Text-to-Vec模块生成Wav2Vec2嵌入，通过两阶段训练处理特征分布偏移。
- 实验效果：在TTS预测潜在特征上条件化，优于级联方法，提升唇同步和视觉真实感。

## 摘要（原文）

> We propose a text-to-talking-face synthesis framework leveraging latent
> speech representations from HierSpeech++. A Text-to-Vec module generates
> Wav2Vec2 embeddings from text, which jointly condition speech and face
> generation. To handle distribution shifts between clean and TTS-predicted
> features, we adopt a two-stage training: pretraining on Wav2Vec2 embeddings and
> finetuning on TTS outputs. This enables tight audio-visual alignment, preserves
> speaker identity, and produces natural, expressive speech and synchronized
> facial motion without ground-truth audio at inference. Experiments show that
> conditioning on TTS-predicted latent features outperforms cascaded pipelines,
> improving both lip-sync and visual realism.

