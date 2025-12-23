---
layout: default
title: Mamba-Based Modality Disentanglement Network for Multi-Contrast MRI Reconstruction
---

# Mamba-Based Modality Disentanglement Network for Multi-Contrast MRI Reconstruction
**arXiv**：[2512.19095v1](https://arxiv.org/abs/2512.19095) · [PDF](https://arxiv.org/pdf/2512.19095.pdf)  
**作者**：Weiyi Lyu, Xinming Fang, Jun Wang, Jun Shi, Guixu Zhang, Juncheng Li  

**一句话要点**：提出MambaMDN以解决多对比度MRI重建中的K空间先验利用不足和模态信息污染问题

**关键词**：多对比度MRI重建, 模态解缠, Mamba网络, K空间先验, 迭代细化

## 3 点简述
- 核心问题：加速MRI重建中K空间先验利用不足导致伪影，多对比度融合时无关信息污染目标重建质量
- 方法要点：采用双域框架，先利用参考K空间数据补全目标数据，再通过Mamba网络分离模态特征
- 实验或效果：实验表明MambaMDN显著优于现有多对比度重建方法，通过迭代细化提升重建精度

## 摘要（原文）

> Magnetic resonance imaging (MRI) is a cornerstone of modern clinical diagnosis, offering unparalleled soft-tissue contrast without ionizing radiation. However, prolonged scan times remain a major barrier to patient throughput and comfort. Existing accelerated MRI techniques often struggle with two key challenges: (1) failure to effectively utilize inherent K-space prior information, leading to persistent aliasing artifacts from zero-filled inputs; and (2) contamination of target reconstruction quality by irrelevant information when employing multi-contrast fusion strategies. To overcome these challenges, we present MambaMDN, a dual-domain framework for multi-contrast MRI reconstruction. Our approach first employs fully-sampled reference K-space data to complete the undersampled target data, generating structurally aligned but modality-mixed inputs. Subsequently, we develop a Mamba-based modality disentanglement network to extract and remove reference-specific features from the mixed representation. Furthermore, we introduce an iterative refinement mechanism to progressively enhance reconstruction accuracy through repeated feature purification. Extensive experiments demonstrate that MambaMDN can significantly outperform existing multi-contrast reconstruction methods.

