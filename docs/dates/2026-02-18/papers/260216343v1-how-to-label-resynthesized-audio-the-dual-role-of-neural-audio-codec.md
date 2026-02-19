---
layout: default
title: How to Label Resynthesized Audio: The Dual Role of Neural Audio Codecs in Audio Deepfake Detection
---

# How to Label Resynthesized Audio: The Dual Role of Neural Audio Codecs in Audio Deepfake Detection
**arXiv**：[2602.16343v1](https://arxiv.org/abs/2602.16343) · [PDF](https://arxiv.org/pdf/2602.16343.pdf)  
**作者**：Yixuan Xiao, Florian Lux, Alejandro Pérez-González-de-Martos, Ngoc Thang Vu  

**一句话要点**：提出ASVspoof 5扩展数据集以解决神经音频编解码器在音频深度伪造检测中的双重标签问题

**关键词**：音频深度伪造检测, 神经音频编解码器, ASVspoof数据集, 标签策略, 音频重合成

## 3 点简述
- 核心问题：神经音频编解码器重合成音频在检测中可能被标记为真实或伪造，导致标签不确定性
- 方法要点：构建挑战性数据集，研究不同标签选择对检测性能的影响
- 实验或效果：提供标签策略的见解，填补相关研究空白

## 摘要（原文）

> Since Text-to-Speech systems typically don't produce waveforms directly, recent spoof detection studies use resynthesized waveforms from vocoders and neural audio codecs to simulate an attacker. Unlike vocoders, which are specifically designed for speech synthesis, neural audio codecs were originally developed for compressing audio for storage and transmission. However, their ability to discretize speech also sparked interest in language-modeling-based speech synthesis. Owing to this dual functionality, codec resynthesized data may be labeled as either bonafide or spoof. So far, very little research has addressed this issue. In this study, we present a challenging extension of the ASVspoof 5 dataset constructed for this purpose. We examine how different labeling choices affect detection performance and provide insights into labeling strategies.

