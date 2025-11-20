---
layout: default
title: Transferable Dual-Domain Feature Importance Attack against AI-Generated Image Detector
---

# Transferable Dual-Domain Feature Importance Attack against AI-Generated Image Detector
**arXiv**：[2511.15571v1](https://arxiv.org/abs/2511.15571) · [PDF](https://arxiv.org/pdf/2511.15571.pdf)  
**作者**：Weiheng Zhu, Gang Cao, Jing Liu, Lifang Yu, Shaowei Weng  

**一句话要点**：提出双域特征重要性攻击以评估AI生成图像检测器的安全性

**关键词**：AI生成图像检测, 对抗攻击, 特征重要性, 双域融合, 迁移性增强

## 3 点简述
- 核心问题：AI生成图像检测器在干净条件下准确率高，但对抗攻击评估不足。
- 方法要点：通过空间插值梯度和频率感知扰动捕获特征重要性，融合双域指导对抗样本生成。
- 实验或效果：跨模型实验验证了攻击的迁移性、透明性和鲁棒性。

## 摘要（原文）

> Recent AI-generated image (AIGI) detectors achieve impressive accuracy under clean condition. In view of antiforensics, it is significant to develop advanced adversarial attacks for evaluating the security of such detectors, which remains unexplored sufficiently. This letter proposes a Dual-domain Feature Importance Attack (DuFIA) scheme to invalidate AIGI detectors to some extent. Forensically important features are captured by the spatially interpolated gradient and frequency-aware perturbation. The adversarial transferability is enhanced by jointly modeling spatial and frequency-domain feature importances, which are fused to guide the optimization-based adversarial example generation. Extensive experiments across various AIGI detectors verify the cross-model transferability, transparency and robustness of DuFIA.

