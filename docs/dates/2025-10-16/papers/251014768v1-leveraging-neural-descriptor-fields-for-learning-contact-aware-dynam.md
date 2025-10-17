---
layout: default
title: Leveraging Neural Descriptor Fields for Learning Contact-Aware Dynamic Recovery
---

# Leveraging Neural Descriptor Fields for Learning Contact-Aware Dynamic Recovery
**arXiv**：[2510.14768v1](https://arxiv.org/abs/2510.14768) · [PDF](https://arxiv.org/pdf/2510.14768.pdf)  
**作者**：Fan Yang, Zixuan Huang, Abhinav Kumar, Sergio Aguilera Marinovic, Soshi Iba, Rana Soltani Zarrin, Dmitry Berenson  

**一句话要点**：提出CADRE框架以解决灵巧操作中物体掉落恢复问题

**关键词**：强化学习, 神经描述符场, 接触感知, 动态恢复, 灵巧操作, 零样本泛化

## 3 点简述
- 核心问题：现实灵巧操作易受干扰导致物体掉落，需在抓取范围内恢复
- 方法要点：结合NDF提取隐式接触特征，提升手指-物体对应推理能力
- 实验或效果：训练效率与收敛性能改善，零样本泛化至未见物体

## 摘要（原文）

> Real-world dexterous manipulation often encounters unexpected errors and
> disturbances, which can lead to catastrophic failures, such as dropping the
> manipulated object. To address this challenge, we focus on the problem of
> catching a falling object while it remains within grasping range and,
> importantly, resetting the system to a configuration favorable for resuming the
> primary manipulation task. We propose Contact-Aware Dynamic Recovery (CADRE), a
> reinforcement learning framework that incorporates a Neural Descriptor Field
> (NDF)-inspired module to extract implicit contact features. Compared to methods
> that rely solely on object pose or point cloud input, NDFs can directly reason
> about finger-object correspondence and adapt to different object geometries.
> Our experiments show that incorporating contact features improves training
> efficiency, enhances convergence performance for RL training, and ultimately
> leads to more successful recoveries. Additionally, we demonstrate that CADRE
> can generalize zero-shot to unseen objects with different geometries.

