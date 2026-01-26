---
layout: default
title: Theory of Minimal Weight Perturbations in Deep Networks and its Applications for Low-Rank Activated Backdoor Attacks
---

# Theory of Minimal Weight Perturbations in Deep Networks and its Applications for Low-Rank Activated Backdoor Attacks
**arXiv**：[2601.16880v1](https://arxiv.org/abs/2601.16880) · [PDF](https://arxiv.org/pdf/2601.16880.pdf)  
**作者**：Bethan Evans, Jared Tanner  

**一句话要点**：提出深度网络最小权重扰动理论，应用于低秩激活后门攻击的压缩阈值分析。

**关键词**：深度网络扰动理论, 后门攻击, 低秩压缩, 权重扰动, 压缩阈值, 输出敏感性

## 3 点简述
- 推导单层深度网络实现指定输出变化所需的最小范数权重扰动公式。
- 应用该理论于精度修改激活的后门攻击，建立可证明的压缩阈值。
- 实验显示低秩压缩能可靠激活潜在后门，同时保持全精度准确率。

## 摘要（原文）

> The minimal norm weight perturbations of DNNs required to achieve a specified change in output are derived and the factors determining its size are discussed. These single-layer exact formulae are contrasted with more generic multi-layer Lipschitz constant based robustness guarantees; both are observed to be of the same order which indicates similar efficacy in their guarantees. These results are applied to precision-modification-activated backdoor attacks, establishing provable compression thresholds below which such attacks cannot succeed, and show empirically that low-rank compression can reliably activate latent backdoors while preserving full-precision accuracy. These expressions reveal how back-propagated margins govern layer-wise sensitivity and provide certifiable guarantees on the smallest parameter updates consistent with a desired output shift.

