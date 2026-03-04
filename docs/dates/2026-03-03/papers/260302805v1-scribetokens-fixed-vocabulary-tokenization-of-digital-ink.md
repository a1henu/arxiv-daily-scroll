---
layout: default
title: ScribeTokens: Fixed-Vocabulary Tokenization of Digital Ink
---

# ScribeTokens: Fixed-Vocabulary Tokenization of Digital Ink
**arXiv**：[2603.02805v1](https://arxiv.org/abs/2603.02805) · [PDF](https://arxiv.org/pdf/2603.02805.pdf)  
**作者**：Douglass Wang  

**一句话要点**：提出ScribeTokens固定词汇表分词方法，将数字墨水分解为像素步长，提升手写文本生成与识别性能。

**关键词**：数字墨水处理, 固定词汇表分词, 手写文本生成, 自监督预训练, 笔迹识别

## 3 点简述
- 数字墨水缺乏统一表示，现有方法存在序列长、训练不稳定或词汇表大、泛化差等问题。
- ScribeTokens将笔迹分解为像素步长和笔状态，固定10个基础词汇表，支持BPE压缩，实现高效表示。
- 实验显示，在生成任务上CER显著降低，识别任务中无需预训练即优于向量表示，预训练后性能最佳。

## 摘要（原文）

> Digital ink -- the coordinate stream captured from stylus or touch input -- lacks a unified representation. Continuous vector representations produce long sequences and suffer from training instability, while existing token representations require large vocabularies, face out-of-vocabulary issues, and underperform vectors on recognition. We propose ScribeTokens, a tokenization that decomposes pen movement into unit pixel steps. Together with two pen-state tokens, this fixed 10-token base vocabulary suffices to represent any digital ink and enables aggressive BPE compression. On handwritten text generation, ScribeTokens dramatically outperforms vectors (17.33% vs. 70.29% CER), showing tokens are far more effective for generation. On recognition, ScribeTokens is the only token representation to outperform vectors without pretraining. We further introduce next-ink-token prediction as a self-supervised pretraining strategy, which consistently improves recognition across all token-based models and accelerates convergence by up to 83x. With pretraining, ScribeTokens achieves the best recognition results across all representations on both datasets (8.27% CER on IAM, 9.83% on DeepWriting).

