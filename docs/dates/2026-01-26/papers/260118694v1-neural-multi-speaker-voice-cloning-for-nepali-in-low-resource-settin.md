---
layout: default
title: Neural Multi-Speaker Voice Cloning for Nepali in Low-Resource Settings
---

# Neural Multi-Speaker Voice Cloning for Nepali in Low-Resource Settings
**arXiv**：[2601.18694v1](https://arxiv.org/abs/2601.18694) · [PDF](https://arxiv.org/pdf/2601.18694.pdf)  
**作者**：Aayush M. Shrestha, Aditya Bajracharya, Projan Shakya, Dinesh B. Kshatri  

**一句话要点**：提出低资源尼泊尔语多说话人语音克隆系统，基于少量数据实现个性化语音合成。

**关键词**：语音克隆, 低资源语言, 说话人编码器, Tacotron2, WaveRNN, 尼泊尔语

## 3 点简述
- 核心问题：尼泊尔语作为低资源语言，语音克隆研究匮乏，需从有限数据中提取说话人特征。
- 方法要点：构建独立数据集，训练说话人编码器与Tacotron2合成器，通过嵌入融合生成梅尔频谱图。
- 实验或效果：系统能有效克隆未见说话人声音，验证了低资源场景下少样本语音克隆的可行性。

## 摘要（原文）

> This research presents a few-shot voice cloning system for Nepali speakers, designed to synthesize speech in a specific speaker's voice from Devanagari text using minimal data. Voice cloning in Nepali remains largely unexplored due to its low-resource nature. To address this, we constructed separate datasets: untranscribed audio for training a speaker encoder and paired text-audio data for training a Tacotron2-based synthesizer. The speaker encoder, optimized with Generative End2End loss, generates embeddings that capture the speaker's vocal identity, validated through Uniform Manifold Approximation and Projection (UMAP) for dimension reduction visualizations. These embeddings are fused with Tacotron2's text embeddings to produce mel-spectrograms, which are then converted into audio using a WaveRNN vocoder. Audio data were collected from various sources, including self-recordings, and underwent thorough preprocessing for quality and alignment. Training was performed using mel and gate loss functions under multiple hyperparameter settings. The system effectively clones speaker characteristics even for unseen voices, demonstrating the feasibility of few-shot voice cloning for the Nepali language and establishing a foundation for personalized speech synthesis in low-resource scenarios.

