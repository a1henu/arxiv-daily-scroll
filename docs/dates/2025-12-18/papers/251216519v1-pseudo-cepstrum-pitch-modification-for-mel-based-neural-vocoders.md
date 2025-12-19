---
layout: default
title: Pseudo-Cepstrum: Pitch Modification for Mel-Based Neural Vocoders
---

# Pseudo-Cepstrum: Pitch Modification for Mel-Based Neural Vocoders
**arXiv**：[2512.16519v1](https://arxiv.org/abs/2512.16519) · [PDF](https://arxiv.org/pdf/2512.16519.pdf)  
**作者**：Nikolaos Ellinas, Alexandra Vioni, Panos Kakoulidis, Georgios Vamvoukakis, Myrsini Christidou, Konstantinos Markopoulos, Junkwang Oh, Gunu Jho, Inchul Hwang, Aimilios Chalamandaris, Pirros Tsiakoulis  

**一句话要点**：提出基于伪倒谱的基频修改方法，适用于任何基于梅尔谱的神经声码器。

**关键词**：基频修改, 伪倒谱, 神经声码器, 梅尔谱, 倒谱分析, 语音合成

## 3 点简述
- 核心问题：传统基频修改方法需特定训练或模型调整，兼容性受限。
- 方法要点：通过伪逆梅尔变换和DCT/IDCT在倒谱域直接平移谐波结构，无需估计峰值位置。
- 实验或效果：经主客观指标验证，优于传统方法，兼容多种先进声码器。

## 摘要（原文）

> This paper introduces a cepstrum-based pitch modification method that can be applied to any mel-spectrogram representation. As a result, this method is compatible with any mel-based vocoder without requiring any additional training or changes to the model. This is achieved by directly modifying the cepstrum feature space in order to shift the harmonic structure to the desired target. The spectrogram magnitude is computed via the pseudo-inverse mel transform, then converted to the cepstrum by applying DCT. In this domain, the cepstral peak is shifted without having to estimate its position and the modified mel is recomputed by applying IDCT and mel-filterbank. These pitch-shifted mel-spectrogram features can be converted to speech with any compatible vocoder. The proposed method is validated experimentally with objective and subjective metrics on various state-of-the-art neural vocoders as well as in comparison with traditional pitch modification methods.

