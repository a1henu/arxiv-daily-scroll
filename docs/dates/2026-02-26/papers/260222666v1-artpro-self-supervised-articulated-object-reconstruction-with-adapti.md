---
layout: default
title: ArtPro: Self-Supervised Articulated Object Reconstruction with Adaptive Integration of Mobility Proposals
---

# ArtPro: Self-Supervised Articulated Object Reconstruction with Adaptive Integration of Mobility Proposals
**arXiv**：[2602.22666v1](https://arxiv.org/abs/2602.22666) · [PDF](https://arxiv.org/pdf/2602.22666.pdf)  
**作者**：Xuelu Li, Zhaonan Wang, Xiaogang Wang, Lei Wu, Manyi Li, Changhe Tu  

**一句话要点**：提出ArtPro框架，通过自适应整合运动提议，解决自监督铰接物体重建中初始分割敏感问题。

**关键词**：铰接物体重建, 自监督学习, 运动提议整合, 3D高斯溅射, 碰撞感知优化, 数字孪生

## 3 点简述
- 核心问题：现有自监督方法对初始分割敏感，易陷入局部最优，影响复杂多部件物体重建。
- 方法要点：基于几何特征和运动先验过分割初始化，动态合并运动一致提议，并采用碰撞感知运动剪枝。
- 实验或效果：在合成和真实物体上验证，ArtPro在准确性和稳定性上显著优于现有方法。

## 摘要（原文）

> Reconstructing articulated objects into high-fidelity digital twins is crucial for applications such as robotic manipulation and interactive simulation. Recent self-supervised methods using differentiable rendering frameworks like 3D Gaussian Splatting remain highly sensitive to the initial part segmentation. Their reliance on heuristic clustering or pre-trained models often causes optimization to converge to local minima, especially for complex multi-part objects. To address these limitations, we propose ArtPro, a novel self-supervised framework that introduces adaptive integration of mobility proposals. Our approach begins with an over-segmentation initialization guided by geometry features and motion priors, generating part proposals with plausible motion hypotheses. During optimization, we dynamically merge these proposals by analyzing motion consistency among spatial neighbors, while a collision-aware motion pruning mechanism prevents erroneous kinematic estimation. Extensive experiments on both synthetic and real-world objects demonstrate that ArtPro achieves robust reconstruction of complex multi-part objects, significantly outperforming existing methods in accuracy and stability.

