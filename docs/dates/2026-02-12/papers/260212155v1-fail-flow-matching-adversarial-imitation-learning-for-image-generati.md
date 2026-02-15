---
layout: default
title: FAIL: Flow Matching Adversarial Imitation Learning for Image Generation
---

# FAIL: Flow Matching Adversarial Imitation Learning for Image Generation
**arXiv**：[2602.12155v1](https://arxiv.org/abs/2602.12155) · [PDF](https://arxiv.org/pdf/2602.12155.pdf)  
**作者**：Yeyao Ma, Chen Li, Xiaosong Zhang, Han Hu, Weidi Xie  

**一句话要点**：提出FAIL方法，通过对抗模仿学习优化流匹配模型，无需显式奖励或成对比较。

**关键词**：流匹配模型, 对抗模仿学习, 图像生成, 后训练优化, 策略漂移, 奖励黑客缓解

## 3 点简述
- 核心问题：流匹配模型后训练中，监督微调无法纠正未见状态下的策略漂移，偏好优化方法成本高。
- 方法要点：FAIL通过对抗训练最小化策略与专家分布差异，提供FAIL-PD和FAIL-PG两种算法。
- 实验或效果：使用少量演示微调FLUX模型，在提示跟随和美学基准上表现竞争性，并推广到离散图像和视频生成。

## 摘要（原文）

> Post-training of flow matching models-aligning the output distribution with a high-quality target-is mathematically equivalent to imitation learning. While Supervised Fine-Tuning mimics expert demonstrations effectively, it cannot correct policy drift in unseen states. Preference optimization methods address this but require costly preference pairs or reward modeling. We propose Flow Matching Adversarial Imitation Learning (FAIL), which minimizes policy-expert divergence through adversarial training without explicit rewards or pairwise comparisons. We derive two algorithms: FAIL-PD exploits differentiable ODE solvers for low-variance pathwise gradients, while FAIL-PG provides a black-box alternative for discrete or computationally constrained settings. Fine-tuning FLUX with only 13,000 demonstrations from Nano Banana pro, FAIL achieves competitive performance on prompt following and aesthetic benchmarks. Furthermore, the framework generalizes effectively to discrete image and video generation, and functions as a robust regularizer to mitigate reward hacking in reward-based optimization. Code and data are available at https://github.com/HansPolo113/FAIL.

