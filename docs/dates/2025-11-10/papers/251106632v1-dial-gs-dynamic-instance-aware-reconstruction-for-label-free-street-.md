---
layout: default
title: DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting
---

# DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting
**arXiv**：[2511.06632v1](https://arxiv.org/abs/2511.06632) · [PDF](https://arxiv.org/pdf/2511.06632.pdf)  
**作者**：Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang  

**一句话要点**：提出DIAL-GS方法，以解决无标签街景中动态实例重建问题

**关键词**：街景重建, 4D高斯溅射, 动态实例感知, 自监督学习, 城市建模

## 3 点简述
- 核心问题：监督方法依赖昂贵标注，自监督方法混淆动静元素且无法区分动态实例
- 方法要点：利用外观位置不一致识别动态实例，采用实例感知4D高斯实现自适应重建
- 实验或效果：在城市场景中超越基线，提升重建质量和实例级编辑能力

## 摘要（原文）

> Urban scene reconstruction is critical for autonomous driving, enabling
> structured 3D representations for data synthesis and closed-loop testing.
> Supervised approaches rely on costly human annotations and lack scalability,
> while current self-supervised methods often confuse static and dynamic elements
> and fail to distinguish individual dynamic objects, limiting fine-grained
> editing. We propose DIAL-GS, a novel dynamic instance-aware reconstruction
> method for label-free street scenes with 4D Gaussian Splatting. We first
> accurately identify dynamic instances by exploiting appearance-position
> inconsistency between warped rendering and actual observation. Guided by
> instance-level dynamic perception, we employ instance-aware 4D Gaussians as the
> unified volumetric representation, realizing dynamic-adaptive and
> instance-aware reconstruction. Furthermore, we introduce a reciprocal mechanism
> through which identity and dynamics reinforce each other, enhancing both
> integrity and consistency. Experiments on urban driving scenarios show that
> DIAL-GS surpasses existing self-supervised baselines in reconstruction quality
> and instance-level editing, offering a concise yet powerful solution for urban
> scene modeling.

