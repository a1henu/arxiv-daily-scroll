---
layout: default
title: MoE3D: A Mixture-of-Experts Module for 3D Reconstruction
---

# MoE3D: A Mixture-of-Experts Module for 3D Reconstruction
**arXiv**：[2601.05208v1](https://arxiv.org/abs/2601.05208) · [PDF](https://arxiv.org/pdf/2601.05208.pdf)  
**作者**：Zichen Wang, Ang Cao, Liam J. Wang, Jeong Joon Park  

**一句话要点**：提出MoE3D模块以提升3D重建质量，通过混合专家机制锐化深度边界并减少飞点伪影。

**关键词**：3D重建, 混合专家, 深度估计, 伪影减少, 动态融合

## 3 点简述
- 核心问题：现有前馈3D重建模型存在深度边界模糊和飞点伪影问题。
- 方法要点：预测多个候选深度图，通过动态权重融合以优化重建结果。
- 实验或效果：集成预训练骨干如VGGT，显著提升质量且计算开销小。

## 摘要（原文）

> MoE3D is a mixture-of-experts module designed to sharpen depth boundaries and mitigate flying-point artifacts (highlighted in red) of existing feed-forward 3D reconstruction models (left side). MoE3D predicts multiple candidate depth maps and fuses them via dynamic weighting (visualized by MoE weights on the right side). When integrated with a pre-trained 3D reconstruction backbone such as VGGT, it substantially enhances reconstruction quality with minimal additional computational overhead. Best viewed digitally.

