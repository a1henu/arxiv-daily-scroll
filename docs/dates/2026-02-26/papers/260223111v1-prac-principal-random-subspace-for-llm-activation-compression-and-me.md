---
layout: default
title: PRAC: Principal-Random Subspace for LLM Activation Compression and Memory-Efficient Training
---

# PRAC: Principal-Random Subspace for LLM Activation Compression and Memory-Efficient Training
**arXiv**：[2602.23111v1](https://arxiv.org/abs/2602.23111) · [PDF](https://arxiv.org/pdf/2602.23111.pdf)  
**作者**：Yanyi Li, Yimu Zhang, Cong Fang  

**一句话要点**：提出PRAC方法以解决大模型训练中激活内存瓶颈问题

**关键词**：激活压缩, 内存高效训练, 子空间分解, 梯度估计, 大语言模型

## 3 点简述
- 激活内存成为大模型训练主要瓶颈，现有压缩方法未利用谱结构
- PRAC将激活分解为主子空间和随机子空间，实现无偏低方差梯度估计
- 实验显示PRAC可减少36%内存，性能损失可忽略且计算成本低

## 摘要（原文）

> Activations have become the primary memory bottleneck in large-batch LLM training. However, existing compression methods fail to exploit the spectral structure of activations, resulting in slow convergence or limited compression. To address this, we bridge the relationship between the algorithm's fast convergence and the requirements for subspace projection, and show that an effective compression should yield an unbiased estimate of the original activation with low variance. We propose Principal-Random Subspace for LLM Activation Compression (PRAC), which novelly decomposes activations into two components: a principal subspace captured via SVD to retain dominant information, and a random subspace sampled from the orthogonal complement to approximate the tail. By introducing a precise scaling factor, we prove that PRAC yields an unbiased gradient estimator with minimum variance under certain conditions. Extensive experiments on pre-training and fine-tuning tasks demonstrate that PRAC achieves up to 36% total memory reduction with negligible performance degradation and minimal computational cost.

