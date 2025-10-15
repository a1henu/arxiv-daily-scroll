---
layout: default
title: T(R,O) Grasp: Efficient Graph Diffusion of Robot-Object Spatial Transformation for Cross-Embodiment Dexterous Grasping
---

# T(R,O) Grasp: Efficient Graph Diffusion of Robot-Object Spatial Transformation for Cross-Embodiment Dexterous Grasping
**arXiv**：[2510.12724v1](https://arxiv.org/abs/2510.12724) · [PDF](https://arxiv.org/pdf/2510.12724.pdf)  
**作者**：Xin Fei, Zhixuan Xu, Huaicong Fang, Tianrui Zhang, Lin Shao  

**一句话要点**：提出T(R,O) Grasp框架，通过图扩散模型高效生成跨具身灵巧抓取。

**关键词**：灵巧抓取, 图扩散模型, 机器人具身, 逆运动学, 跨具身泛化

## 3 点简述
- 灵巧抓取面临高维状态和动作空间的复杂性挑战。
- 使用T(R,O)图统一表示手-物空间变换，结合图扩散模型和逆运动学求解器。
- 实验显示平均成功率94.83%，推理速度0.21秒，优于现有基线。

## 摘要（原文）

> Dexterous grasping remains a central challenge in robotics due to the
> complexity of its high-dimensional state and action space. We introduce T(R,O)
> Grasp, a diffusion-based framework that efficiently generates accurate and
> diverse grasps across multiple robotic hands. At its core is the T(R,O) Graph,
> a unified representation that models spatial transformations between robotic
> hands and objects while encoding their geometric properties. A graph diffusion
> model, coupled with an efficient inverse kinematics solver, supports both
> unconditioned and conditioned grasp synthesis. Extensive experiments on a
> diverse set of dexterous hands show that T(R,O) Grasp achieves average success
> rate of 94.83%, inference speed of 0.21s, and throughput of 41 grasps per
> second on an NVIDIA A100 40GB GPU, substantially outperforming existing
> baselines. In addition, our approach is robust and generalizable across
> embodiments while significantly reducing memory consumption. More importantly,
> the high inference speed enables closed-loop dexterous manipulation,
> underscoring the potential of T(R,O) Grasp to scale into a foundation model for
> dexterous grasping.

