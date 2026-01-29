---
layout: default
title: Leveraging Second-Order Curvature for Efficient Learned Image Compression: Theory and Empirical Evidence
---

# Leveraging Second-Order Curvature for Efficient Learned Image Compression: Theory and Empirical Evidence
**arXiv**：[2601.20769v1](https://arxiv.org/abs/2601.20769) · [PDF](https://arxiv.org/pdf/2601.20769.pdf)  
**作者**：Yichi Zhang, Fengqing Zhu  

**一句话要点**：提出SOAP二阶优化器以提升学习图像压缩的训练效率和性能

**关键词**：学习图像压缩, 二阶优化, 率失真优化, 训练效率, 量化鲁棒性

## 3 点简述
- 标准一阶优化器在率失真目标中面临梯度冲突，导致收敛慢和性能差
- SOAP利用牛顿预条件解决更新冲突，实现更快更稳定的训练收敛
- 二阶训练减少激活和潜在异常值，增强后训练量化的鲁棒性

## 摘要（原文）

> Training learned image compression (LIC) models entails navigating a challenging optimization landscape defined by the fundamental trade-off between rate and distortion. Standard first-order optimizers, such as SGD and Adam, struggle with \emph{gradient conflicts} arising from competing objectives, leading to slow convergence and suboptimal rate-distortion performance. In this work, we demonstrate that a simple utilization of a second-order quasi-Newton optimizer, \textbf{SOAP}, dramatically improves both training efficiency and final performance across diverse LICs. Our theoretical and empirical analyses reveal that Newton preconditioning inherently resolves the intra-step and inter-step update conflicts intrinsic to the R-D objective, facilitating faster, more stable convergence. Beyond acceleration, we uncover a critical deployability benefit: second-order trained models exhibit significantly fewer activation and latent outliers. This substantially enhances robustness to post-training quantization. Together, these results establish second-order optimization, achievable as a seamless drop-in replacement of the imported optimizer, as a powerful, practical tool for advancing the efficiency and real-world readiness of LICs.

