---
layout: default
title: Light Up Your Face: A Physically Consistent Dataset and Diffusion Model for Face Fill-Light Enhancement
---

# Light Up Your Face: A Physically Consistent Dataset and Diffusion Model for Face Fill-Light Enhancement
**arXiv**：[2602.04300v1](https://arxiv.org/abs/2602.04300) · [PDF](https://arxiv.org/pdf/2602.04300.pdf)  
**作者**：Jue Gong, Zihan Zhou, Jingkai Wang, Xiaohong Liu, Yulun Zhang, Xiaokang Yang  

**一句话要点**：提出LightYourFace-160K数据集与FiLitDiff模型，以物理一致方式增强面部补光，保持背景光照不变。

**关键词**：面部补光增强, 物理一致渲染, 扩散模型, 数据集构建, 光照控制, 前景背景一致性

## 3 点简述
- 核心问题：现有面部重光照方法常改变整体场景，导致前景背景不一致，不满足实际补光需求。
- 方法要点：构建大规模配对数据集LYF-160K，基于物理渲染器；训练FiLitDiff扩散模型，使用物理感知光照提示实现可控补光。
- 实验或效果：在保留测试集上展示高感知质量、竞争性全参考指标，并更好保持背景光照。

## 摘要（原文）

> Face fill-light enhancement (FFE) brightens underexposed faces by adding virtual fill light while keeping the original scene illumination and background unchanged. Most face relighting methods aim to reshape overall lighting, which can suppress the input illumination or modify the entire scene, leading to foreground-background inconsistency and mismatching practical FFE needs. To support scalable learning, we introduce LightYourFace-160K (LYF-160K), a large-scale paired dataset built with a physically consistent renderer that injects a disk-shaped area fill light controlled by six disentangled factors, producing 160K before-and-after pairs. We first pretrain a physics-aware lighting prompt (PALP) that embeds the 6D parameters into conditioning tokens, using an auxiliary planar-light reconstruction objective. Building on a pretrained diffusion backbone, we then train a fill-light diffusion (FiLitDiff), an efficient one-step model conditioned on physically grounded lighting codes, enabling controllable and high-fidelity fill lighting at low computational cost. Experiments on held-out paired sets demonstrate strong perceptual quality and competitive full-reference metrics, while better preserving background illumination. The dataset and model will be at https://github.com/gobunu/Light-Up-Your-Face.

