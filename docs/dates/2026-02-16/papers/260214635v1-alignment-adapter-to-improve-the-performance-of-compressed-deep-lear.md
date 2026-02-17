---
layout: default
title: Alignment Adapter to Improve the Performance of Compressed Deep Learning Models
---

# Alignment Adapter to Improve the Performance of Compressed Deep Learning Models
**arXiv**：[2602.14635v1](https://arxiv.org/abs/2602.14635) · [PDF](https://arxiv.org/pdf/2602.14635.pdf)  
**作者**：Rohit Raj Rai, Abhishek Dhaka, Amit Awekar  

**一句话要点**：提出对齐适配器以提升压缩深度学习模型在资源受限环境中的性能

**关键词**：模型压缩, 对齐适配器, 轻量模块, NLP任务, 嵌入对齐

## 3 点简述
- 压缩模型性能常落后于大型模型，需轻量解决方案
- AlAd通过滑动窗口对齐嵌入，保持局部语义，兼容不同压缩方法
- 实验显示AlAd在NLP任务中显著提升性能，开销微小

## 摘要（原文）

> Compressed Deep Learning (DL) models are essential for deployment in resource-constrained environments. But their performance often lags behind their large-scale counterparts. To bridge this gap, we propose Alignment Adapter (AlAd): a lightweight, sliding-window-based adapter. It aligns the token-level embeddings of a compressed model with those of the original large model. AlAd preserves local contextual semantics, enables flexible alignment across differing dimensionalities or architectures, and is entirely agnostic to the underlying compression method. AlAd can be deployed in two ways: as a plug-and-play module over a frozen compressed model, or by jointly fine-tuning AlAd with the compressed model for further performance gains. Through experiments on BERT-family models across three token-level NLP tasks, we demonstrate that AlAd significantly boosts the performance of compressed models with only marginal overhead in size and latency.

