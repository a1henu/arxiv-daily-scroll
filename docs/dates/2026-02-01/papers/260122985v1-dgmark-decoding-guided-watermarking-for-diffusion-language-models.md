---
layout: default
title: dgMARK: Decoding-Guided Watermarking for Diffusion Language Models
---

# dgMARK: Decoding-Guided Watermarking for Diffusion Language Models
**arXiv**：[2601.22985v1](https://arxiv.org/abs/2601.22985) · [PDF](https://arxiv.org/pdf/2601.22985.pdf)  
**作者**：Pyo Min Hong, Albert No  

**一句话要点**：提出dgMARK，一种解码引导的水印方法，用于离散扩散语言模型的水印嵌入与检测。

**关键词**：扩散语言模型, 水印嵌入, 解码引导, 奇偶约束, 鲁棒检测

## 3 点简述
- 核心问题：离散扩散语言模型生成顺序敏感，为水印嵌入提供新通道。
- 方法要点：通过解码引导，利用二进制哈希的奇偶约束，在不显式重加权概率下嵌入水印。
- 实验或效果：水印检测基于奇偶匹配统计，滑动窗口检测器增强对编辑操作的鲁棒性。

## 摘要（原文）

> We propose dgMARK, a decoding-guided watermarking method for discrete diffusion language models (dLLMs). Unlike autoregressive models, dLLMs can generate tokens in arbitrary order. While an ideal conditional predictor would be invariant to this order, practical dLLMs exhibit strong sensitivity to the unmasking order, creating a new channel for watermarking. dgMARK steers the unmasking order toward positions whose high-reward candidate tokens satisfy a simple parity constraint induced by a binary hash, without explicitly reweighting the model's learned probabilities. The method is plug-and-play with common decoding strategies (e.g., confidence, entropy, and margin-based ordering) and can be strengthened with a one-step lookahead variant. Watermarks are detected via elevated parity-matching statistics, and a sliding-window detector ensures robustness under post-editing operations including insertion, deletion, substitution, and paraphrasing.

