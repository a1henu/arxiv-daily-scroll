---
layout: default
title: Revis: Sparse Latent Steering to Mitigate Object Hallucination in Large Vision-Language Models
---

# Revis: Sparse Latent Steering to Mitigate Object Hallucination in Large Vision-Language Models
**arXiv**：[2602.11824v1](https://arxiv.org/abs/2602.11824) · [PDF](https://arxiv.org/pdf/2602.11824.pdf)  
**作者**：Jialin Wu, Wei Shi, Han Shen, Peigui Qi, Kunsheng Tang, Zhicong Huang, Binghao Wang, Zhou Yang  

**一句话要点**：提出REVIS框架以缓解大型视觉语言模型中的物体幻觉问题

**关键词**：物体幻觉缓解, 稀疏潜在干预, 正交投影, 训练免费框架, 视觉语言模型

## 3 点简述
- 核心问题：LVLMs中视觉特征与文本表示在深层网络交织，导致物体幻觉。
- 方法要点：通过正交投影提取纯视觉向量，在抑制发生的精确深度进行稀疏干预。
- 实验或效果：在标准基准上，REVIS将物体幻觉率降低约19%，同时保持一般推理能力。

## 摘要（原文）

> Despite the advanced capabilities of Large Vision-Language Models (LVLMs), they frequently suffer from object hallucination. One reason is that visual features and pretrained textual representations often become intertwined in the deeper network layers. To address this, we propose REVIS, a training-free framework designed to explicitly re-activate this suppressed visual information. Rooted in latent space geometry, REVIS extracts the pure visual information vector via orthogonal projection and employs a calibrated strategy to perform sparse intervention only at the precise depth where suppression occurs. This surgical approach effectively restores visual information with minimal computational cost. Empirical evaluations on standard benchmarks demonstrate that REVIS reduces object hallucination rates by approximately 19% compared to state-of-the-art baselines, while preserving general reasoning capabilities.

