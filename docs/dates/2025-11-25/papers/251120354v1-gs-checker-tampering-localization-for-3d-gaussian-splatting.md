---
layout: default
title: GS-Checker: Tampering Localization for 3D Gaussian Splatting
---

# GS-Checker: Tampering Localization for 3D Gaussian Splatting
**arXiv**：[2511.20354v1](https://arxiv.org/abs/2511.20354) · [PDF](https://arxiv.org/pdf/2511.20354.pdf)  
**作者**：Haoliang Han, Ziyuan Luo, Jun Qi, Anderson Rocha, Renjie Wan  

**一句话要点**：提出GS-Checker方法以定位3D高斯泼溅模型中的篡改区域

**关键词**：3D高斯泼溅, 篡改定位, 3D对比机制, 循环优化, 无监督学习

## 3 点简述
- 核心问题：3D高斯泼溅编辑技术易被恶意篡改，需定位篡改区域以防范风险
- 方法要点：集成3D篡改属性至高斯参数，通过3D对比机制和循环优化精确定位
- 实验或效果：无需昂贵3D标签监督，实验证明能有效定位篡改区域

## 摘要（原文）

> Recent advances in editing technologies for 3D Gaussian Splatting (3DGS) have made it simple to manipulate 3D scenes. However, these technologies raise concerns about potential malicious manipulation of 3D content. To avoid such malicious applications, localizing tampered regions becomes crucial. In this paper, we propose GS-Checker, a novel method for locating tampered areas in 3DGS models. Our approach integrates a 3D tampering attribute into the 3D Gaussian parameters to indicate whether the Gaussian has been tampered. Additionally, we design a 3D contrastive mechanism by comparing the similarity of key attributes between 3D Gaussians to seek tampering cues at 3D level. Furthermore, we introduce a cyclic optimization strategy to refine the 3D tampering attribute, enabling more accurate tampering localization. Notably, our approach does not require expensive 3D labels for supervision. Extensive experimental results demonstrate the effectiveness of our proposed method to locate the tampered 3DGS area.

