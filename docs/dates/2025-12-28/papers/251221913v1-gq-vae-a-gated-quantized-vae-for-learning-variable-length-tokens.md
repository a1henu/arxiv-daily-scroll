---
layout: default
title: GQ-VAE: A gated quantized VAE for learning variable length tokens
---

# GQ-VAE: A gated quantized VAE for learning variable length tokens
**arXiv**：[2512.21913v1](https://arxiv.org/abs/2512.21913) · [PDF](https://arxiv.org/pdf/2512.21913.pdf)  
**作者**：Theo Datta, Kayla Huang, Sham Kakade, David Brandfonbrener  

**一句话要点**：提出GQ-VAE作为可独立预训练的神经分词器，以替代现有分词方法并支持变长离散标记学习。

**关键词**：神经分词器, 变分自编码器, 变长标记学习, 语言模型压缩, 门控量化

## 3 点简述
- 核心问题：现有神经分词器增加模型复杂度且需架构大改，难以大规模应用。
- 方法要点：GQ-VAE通过门控量化变分自编码器学习变长离散标记，可作为现有分词器的即插即用替代。
- 实验或效果：GQ-VAE在压缩和语言建模性能上优于标准VQ-VAE，接近BPE，并在压缩率相同时提升下游语言模型学习。

## 摘要（原文）

> While most frontier models still use deterministic frequency-based tokenization algorithms such as byte-pair encoding (BPE), there has been significant recent work to design learned neural tokenizers. However, these schemes generally add to underlying language model complexity and force large changes to architecture, making them hard to implement at large scales. To overcome these challenges, we propose the gated quantized variational autoencoder (GQ-VAE), a novel architecture that can be independently pre-trained to serve as a drop-in replacement for existing tokenizers. The key innovation of the architecture is to learn to encode variable-length discrete tokens. GQ-VAE improves compression and language modeling performance over a standard VQ-VAE tokenizer, and approaches the compression rate and language modeling performance of BPE. Interestingly, if we use BPE with a smaller vocabulary, such that the compression is equivalent between GQ-VAE and BPE, we find that GQ-VAE improves downstream language model learning. We conclude with a discussion of several exciting avenues for future work. Code can be found at https://github.com/Theo-Datta-115/gq-vae.

