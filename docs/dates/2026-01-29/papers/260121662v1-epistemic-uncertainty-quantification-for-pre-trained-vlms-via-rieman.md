---
layout: default
title: Epistemic Uncertainty Quantification for Pre-trained VLMs via Riemannian Flow Matching
---

# Epistemic Uncertainty Quantification for Pre-trained VLMs via Riemannian Flow Matching
**arXiv**：[2601.21662v1](https://arxiv.org/abs/2601.21662) · [PDF](https://arxiv.org/pdf/2601.21662.pdf)  
**作者**：Li Ju, Mayank Nautiyal, Andreas Hellander, Ekta Vats, Prashant Singh  

**一句话要点**：提出REPVLM方法，通过黎曼流匹配量化预训练视觉语言模型的认知不确定性。

**关键词**：认知不确定性量化, 视觉语言模型, 黎曼流匹配, 超球流形, 分布外检测, 数据自动筛选

## 3 点简述
- 核心问题：视觉语言模型缺乏内在机制量化认知不确定性，即模型对自身表示的无知程度。
- 方法要点：利用嵌入的负对数密度作为认知不确定性代理，在超球流形上使用黎曼流匹配计算概率密度。
- 实验或效果：REPVLM在不确定性与预测误差间实现近乎完美的相关性，显著优于基线，并扩展至分布外检测和数据自动筛选。

## 摘要（原文）

> Vision-Language Models (VLMs) are typically deterministic in nature and lack intrinsic mechanisms to quantify epistemic uncertainty, which reflects the model's lack of knowledge or ignorance of its own representations. We theoretically motivate negative log-density of an embedding as a proxy for the epistemic uncertainty, where low-density regions signify model ignorance. The proposed method REPVLM computes the probability density on the hyperspherical manifold of the VLM embeddings using Riemannian Flow Matching. We empirically demonstrate that REPVLM achieves near-perfect correlation between uncertainty and prediction error, significantly outperforming existing baselines. Beyond classification, we also demonstrate that the model also provides a scalable metric for out-of-distribution detection and automated data curation.

