---
layout: default
title: MAD: Motion Appearance Decoupling for efficient Driving World Models
---

# MAD: Motion Appearance Decoupling for efficient Driving World Models
**arXiv**：[2601.09452v1](https://arxiv.org/abs/2601.09452) · [PDF](https://arxiv.org/pdf/2601.09452.pdf)  
**作者**：Ahmad Rahimi, Valentin Gerard, Eloi Zablocki, Matthieu Cord, Alexandre Alahi  

**一句话要点**：提出运动外观解耦框架，将通用视频扩散模型高效适配为可控自动驾驶世界模型

**关键词**：自动驾驶世界模型, 视频扩散模型, 运动外观解耦, 高效适配, 可控视频生成, 骨架化表示

## 3 点简述
- 问题：通用视频扩散模型在自动驾驶中缺乏结构化运动和物理一致性，适配需大量数据和计算
- 方法：分两阶段解耦运动与外观学习，先预测骨架化运动序列，再合成RGB视频
- 效果：适配SVD时计算量减少94%以上，MAD-LTX模型超越开源竞品，支持多模态控制

## 摘要（原文）

> Recent video diffusion models generate photorealistic, temporally coherent videos, yet they fall short as reliable world models for autonomous driving, where structured motion and physically consistent interactions are essential. Adapting these generalist video models to driving domains has shown promise but typically requires massive domain-specific data and costly fine-tuning. We propose an efficient adaptation framework that converts generalist video diffusion models into controllable driving world models with minimal supervision. The key idea is to decouple motion learning from appearance synthesis. First, the model is adapted to predict structured motion in a simplified form: videos of skeletonized agents and scene elements, focusing learning on physical and social plausibility. Then, the same backbone is reused to synthesize realistic RGB videos conditioned on these motion sequences, effectively "dressing" the motion with texture and lighting. This two-stage process mirrors a reasoning-rendering paradigm: first infer dynamics, then render appearance. Our experiments show this decoupled approach is exceptionally efficient: adapting SVD, we match prior SOTA models with less than 6% of their compute. Scaling to LTX, our MAD-LTX model outperforms all open-source competitors, and supports a comprehensive suite of text, ego, and object controls. Project page: https://vita-epfl.github.io/MAD-World-Model/

