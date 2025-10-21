---
layout: default
title: Learned Inertial Odometry for Cycling Based on Mixture of Experts Algorithm
---

# Learned Inertial Odometry for Cycling Based on Mixture of Experts Algorithm
**arXiv**：[2510.17604v1](https://arxiv.org/abs/2510.17604) · [PDF](https://arxiv.org/pdf/2510.17604.pdf)  
**作者**：Hao Qiao, Yan Wang, Shuo Yang, Xiaoyao Yu, Jian kuang, Xiaoji Niu  

**一句话要点**：提出基于专家混合算法的学习惯性里程计，用于自行车定位并降低计算成本

**关键词**：学习惯性里程计, 自行车定位, 专家混合算法, 计算优化, 惯性导航

## 3 点简述
- 自行车定位受GNSS多路径和惯性导航建模限制影响，准确性不足
- 扩展TLIO方法，引入改进MoE模型，减少训练和推理计算开销
- 实验显示，相比LLIO，精度相当，参数和计算成本分别降低64.7%和81.8%

## 摘要（原文）

> With the rapid growth of bike sharing and the increasing diversity of cycling
> applications, accurate bicycle localization has become essential. traditional
> GNSS-based methods suffer from multipath effects, while existing inertial
> navigation approaches rely on precise modeling and show limited robustness.
> Tight Learned Inertial Odometry (TLIO) achieves low position drift by combining
> raw IMU data with predicted displacements by neural networks, but its high
> computational cost restricts deployment on mobile devices. To overcome this, we
> extend TLIO to bicycle localization and introduce an improved Mixture-of
> Experts (MoE) model that reduces both training and inference costs. Experiments
> show that, compared to the state-of-the-art LLIO framework, our method achieves
> comparable accuracy while reducing parameters by 64.7% and computational cost
> by 81.8%.

