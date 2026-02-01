---
layout: default
title: Information Filtering via Variational Regularization for Robot Manipulation
---

# Information Filtering via Variational Regularization for Robot Manipulation
**arXiv**：[2601.21926v1](https://arxiv.org/abs/2601.21926) · [PDF](https://arxiv.org/pdf/2601.21926.pdf)  
**作者**：Jinhao Zhang, Wenlong Xia, Yaojia Wang, Zhexuan Zhou, Huizhe Li, Yichen Lai, Haoming Song, Youmin Gong, Jie Me  

**一句话要点**：提出变分正则化以过滤机器人操作中扩散策略的中间特征噪声

**关键词**：机器人操作, 扩散策略, 变分正则化, 信息瓶颈, 视觉运动策略, 特征去噪

## 3 点简述
- 问题：扩散策略的中间特征存在冗余和任务无关噪声，影响性能。
- 方法：引入变分正则化模块，通过时间步条件高斯和KL散度正则化形成自适应信息瓶颈。
- 效果：在三个仿真基准上提升成功率，真实世界实验表现良好。

## 摘要（原文）

> Diffusion-based visuomotor policies built on 3D visual representations have achieved strong performance in learning complex robotic skills. However, most existing methods employ an oversized denoising decoder. While increasing model capacity can improve denoising, empirical evidence suggests that it also introduces redundancy and noise in intermediate feature blocks. Crucially, we find that randomly masking backbone features at inference time (without changing training) can improve performance, confirming the presence of task-irrelevant noise in intermediate features. To this end, we propose Variational Regularization (VR), a lightweight module that imposes a timestep-conditioned Gaussian over backbone features and applies a KL-divergence regularizer, forming an adaptive information bottleneck. Extensive experiments on three simulation benchmarks (RoboTwin2.0, Adroit, and MetaWorld) show that, compared to the baseline DP3, our approach improves the success rate by 6.1% on RoboTwin2.0 and by 4.1% on Adroit and MetaWorld, achieving new state-of-the-art results. Real-world experiments further demonstrate that our method performs well in practical deployments. Code will released.

