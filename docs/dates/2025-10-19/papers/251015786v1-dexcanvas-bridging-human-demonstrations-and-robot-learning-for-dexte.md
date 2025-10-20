---
layout: default
title: DexCanvas: Bridging Human Demonstrations and Robot Learning for Dexterous Manipulation
---

# DexCanvas: Bridging Human Demonstrations and Robot Learning for Dexterous Manipulation
**arXiv**：[2510.15786v1](https://arxiv.org/abs/2510.15786) · [PDF](https://arxiv.org/pdf/2510.15786.pdf)  
**作者**：Xinyue Xu, Jieqiang Sun, Jing, Dai, Siyuan Chen, Lanjie Ma, Ke Sun, Bin Zhao, Jianbo Yuan, Yiwen Lu  

**一句话要点**：提出DexCanvas数据集，桥接人类演示与机器人学习，用于灵巧操作任务。

**关键词**：灵巧操作数据集, 人类演示学习, 强化学习控制, 多模态数据, 接触力推断

## 3 点简述
- 核心问题：机器人灵巧操作缺乏大规模、系统化的人类演示数据。
- 方法要点：构建混合真实-合成数据集，结合多模态数据和强化学习训练。
- 实验或效果：数据集支持策略训练，重现人类动作并推断接触力。

## 摘要（原文）

> We present DexCanvas, a large-scale hybrid real-synthetic human manipulation
> dataset containing 7,000 hours of dexterous hand-object interactions seeded
> from 70 hours of real human demonstrations, organized across 21 fundamental
> manipulation types based on the Cutkosky taxonomy. Each entry combines
> synchronized multi-view RGB-D, high-precision mocap with MANO hand parameters,
> and per-frame contact points with physically consistent force profiles. Our
> real-to-sim pipeline uses reinforcement learning to train policies that control
> an actuated MANO hand in physics simulation, reproducing human demonstrations
> while discovering the underlying contact forces that generate the observed
> object motion. DexCanvas is the first manipulation dataset to combine
> large-scale real demonstrations, systematic skill coverage based on established
> taxonomies, and physics-validated contact annotations. The dataset can
> facilitate research in robotic manipulation learning, contact-rich control, and
> skill transfer across different hand morphologies.

