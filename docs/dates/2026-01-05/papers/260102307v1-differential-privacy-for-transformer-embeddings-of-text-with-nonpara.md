---
layout: default
title: Differential Privacy for Transformer Embeddings of Text with Nonparametric Variational Information Bottleneck
---

# Differential Privacy for Transformer Embeddings of Text with Nonparametric Variational Information Bottleneck
**arXiv**：[2601.02307v1](https://arxiv.org/abs/2601.02307) · [PDF](https://arxiv.org/pdf/2601.02307.pdf)  
**作者**：Dina El Zein, James Henderson  

**一句话要点**：提出非参数变分差分隐私方法，通过噪声注入保护Transformer嵌入的文本数据共享。

**关键词**：差分隐私, Transformer嵌入, 非参数变分信息瓶颈, 文本数据共享, 隐私保护

## 3 点简述
- Transformer嵌入易泄露敏感信息，需隐私保护方法。
- 集成非参数变分信息瓶颈层，注入噪声并校准噪声水平。
- 在GLUE基准测试中，噪声水平可调节隐私与准确性的权衡。

## 摘要（原文）

> We propose a privacy-preserving method for sharing text data by sharing noisy versions of their transformer embeddings. It has been shown that hidden representations learned by deep models can encode sensitive information from the input, making it possible for adversaries to recover the input data with considerable accuracy. This problem is exacerbated in transformer embeddings because they consist of multiple vectors, one per token. To mitigate this risk, we propose Nonparametric Variational Differential Privacy (NVDP), which ensures both useful data sharing and strong privacy protection. We take a differential privacy approach, integrating a Nonparametric Variational Information Bottleneck (NVIB) layer into the transformer architecture to inject noise into its multi-vector embeddings and thereby hide information, and measuring privacy protection with Rényi divergence and its corresponding Bayesian Differential Privacy (BDP) guarantee. Training the NVIB layer calibrates the noise level according to utility. We test NVDP on the GLUE benchmark and show that varying the noise level gives us a useful tradeoff between privacy and accuracy. With lower noise levels, our model maintains high accuracy while offering strong privacy guarantees, effectively balancing privacy and utility.

