---
layout: default
title: Modality Dominance-Aware Optimization for Embodied RGB-Infrared Perception
---

# Modality Dominance-Aware Optimization for Embodied RGB-Infrared Perception
**arXiv**：[2601.00598v1](https://arxiv.org/abs/2601.00598) · [PDF](https://arxiv.org/pdf/2601.00598.pdf)  
**作者**：Xianhui Liu, Siqi Jiang, Yi Xie, Yuqing Lin, Siao Liu  

**一句话要点**：提出模态主导感知优化框架以解决RGB-红外感知中的优化偏差问题

**关键词**：RGB-红外感知, 跨模态融合, 模态主导指数, 优化偏差, 特征对齐, 对抗均衡正则化

## 3 点简述
- 核心问题：RGB-红外模态信息密度和特征质量差异导致训练偏向主导模态，阻碍有效融合
- 方法要点：引入模态主导指数量化偏差，并开发模态主导感知跨模态学习框架进行优化调控
- 实验或效果：在三个RGB-红外基准测试中验证框架有效缓解优化偏差，实现先进性能

## 摘要（原文）

> RGB-Infrared (RGB-IR) multimodal perception is fundamental to embodied multimedia systems operating in complex physical environments. Although recent cross-modal fusion methods have advanced RGB-IR detection, the optimization dynamics caused by asymmetric modality characteristics remain underexplored. In practice, disparities in information density and feature quality introduce persistent optimization bias, leading training to overemphasize a dominant modality and hindering effective fusion. To quantify this phenomenon, we propose the Modality Dominance Index (MDI), which measures modality dominance by jointly modeling feature entropy and gradient contribution. Based on MDI, we develop a Modality Dominance-Aware Cross-modal Learning (MDACL) framework that regulates cross-modal optimization. MDACL incorporates Hierarchical Cross-modal Guidance (HCG) to enhance feature alignment and Adversarial Equilibrium Regularization (AER) to balance optimization dynamics during fusion. Extensive experiments on three RGB-IR benchmarks demonstrate that MDACL effectively mitigates optimization bias and achieves SOTA performance.

