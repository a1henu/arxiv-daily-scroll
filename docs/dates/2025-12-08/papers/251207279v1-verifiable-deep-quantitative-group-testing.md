---
layout: default
title: Verifiable Deep Quantitative Group Testing
---

# Verifiable Deep Quantitative Group Testing
**arXiv**：[2512.07279v1](https://arxiv.org/abs/2512.07279) · [PDF](https://arxiv.org/pdf/2512.07279.pdf)  
**作者**：Shreyas Jayant Grampurohit, Satish Mulleti, Ajit Rajwade  

**一句话要点**：提出基于神经网络的定量群组测试框架，实现高精度解码与结构可验证性。

**关键词**：定量群组测试, 神经网络解码, 结构可验证性, 雅可比矩阵分析, 组合恢复问题

## 3 点简述
- 核心问题：定量群组测试中，从少量池化测试中识别缺陷物品子集。
- 方法要点：使用多层感知机映射噪声测量向量至二进制缺陷指示器，并可从雅可比矩阵恢复池化结构。
- 实验或效果：模型在稀疏有界扰动下实现准确鲁棒恢复，并内部化组合关系而非记忆模式。

## 摘要（原文）

> We present a neural network-based framework for solving the quantitative group testing (QGT) problem that achieves both high decoding accuracy and structural verifiability. In QGT, the objective is to identify a small subset of defective items among $N$ candidates using only $M \ll N$ pooled tests, each reporting the number of defectives in the tested subset. We train a multi-layer perceptron to map noisy measurement vectors to binary defect indicators, achieving accurate and robust recovery even under sparse, bounded perturbations. Beyond accuracy, we show that the trained network implicitly learns the underlying pooling structure that links items to tests, allowing this structure to be recovered directly from the network's Jacobian. This indicates that the model does not merely memorize training patterns but internalizes the true combinatorial relationships governing QGT. Our findings reveal that standard feedforward architectures can learn verifiable inverse mappings in structured combinatorial recovery problems.

