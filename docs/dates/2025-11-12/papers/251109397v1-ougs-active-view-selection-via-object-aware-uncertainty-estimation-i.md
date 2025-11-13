---
layout: default
title: OUGS: Active View Selection via Object-aware Uncertainty Estimation in 3DGS
---

# OUGS: Active View Selection via Object-aware Uncertainty Estimation in 3DGS
**arXiv**：[2511.09397v1](https://arxiv.org/abs/2511.09397) · [PDF](https://arxiv.org/pdf/2511.09397.pdf)  
**作者**：Haiyi Li, Qi Chen, Denis Kalkofen, Hsiang-Ting Chen  

**一句话要点**：提出OUGS框架，通过对象感知不确定性估计优化3DGS主动视图选择

**关键词**：3D高斯泼溅, 主动视图选择, 不确定性估计, 对象感知重建, 语义分割

## 3 点简述
- 核心问题：现有主动重建方法依赖场景级不确定性，易受背景干扰，对象重建效率低。
- 方法要点：基于3D高斯原语物理参数推导不确定性，结合语义分割实现对象感知评分。
- 实验或效果：在公共数据集上验证，提升重建效率与对象质量，优于现有方法。

## 摘要（原文）

> Recent advances in 3D Gaussian Splatting (3DGS) have achieved state-of-the-art results for novel view synthesis. However, efficiently capturing high-fidelity reconstructions of specific objects within complex scenes remains a significant challenge. A key limitation of existing active reconstruction methods is their reliance on scene-level uncertainty metrics, which are often biased by irrelevant background clutter and lead to inefficient view selection for object-centric tasks. We present OUGS, a novel framework that addresses this challenge with a more principled, physically-grounded uncertainty formulation for 3DGS. Our core innovation is to derive uncertainty directly from the explicit physical parameters of the 3D Gaussian primitives (e.g., position, scale, rotation). By propagating the covariance of these parameters through the rendering Jacobian, we establish a highly interpretable uncertainty model. This foundation allows us to then seamlessly integrate semantic segmentation masks to produce a targeted, object-aware uncertainty score that effectively disentangles the object from its environment. This allows for a more effective active view selection strategy that prioritizes views critical to improving object fidelity. Experimental evaluations on public datasets demonstrate that our approach significantly improves the efficiency of the 3DGS reconstruction process and achieves higher quality for targeted objects compared to existing state-of-the-art methods, while also serving as a robust uncertainty estimator for the global scene.

