---
layout: default
title: SPAARS: Safer RL Policy Alignment through Abstract Exploration and Refined Exploitation of Action Space
---

# SPAARS: Safer RL Policy Alignment through Abstract Exploration and Refined Exploitation of Action Space
**arXiv**：[2603.09378v1](https://arxiv.org/abs/2603.09378) · [PDF](https://arxiv.org/pdf/2603.09378.pdf)  
**作者**：Swaminathan S K, Aritra Hazra  

**一句话要点**：提出SPAARS课程学习框架，通过抽象探索和精细利用动作空间实现更安全的离线到在线强化学习策略对齐

**关键词**：离线到在线强化学习, 课程学习, 潜在空间探索, 策略对齐, 安全强化学习, 变分自编码器

## 3 点简述
- 核心问题：离线到在线强化学习中，如何在保持离线数据行为支持的同时安全地进行在线探索
- 方法要点：先约束探索于低维潜在流形确保安全，再无缝转移到原始动作空间绕过解码器瓶颈
- 实验效果：在多个基准任务上超越基线方法，SPAARS-SUPE在kitchen-mixed-v0上获得0.825归一化回报

## 摘要（原文）

> Offline-to-online reinforcement learning (RL) offers a promising paradigm for robotics by pre-training policies on safe, offline demonstrations and fine-tuning them via online interaction. However, a fundamental challenge remains: how to safely explore online without deviating from the behavioral support of the offline data? While recent methods leverage conditional variational autoencoders (CVAEs) to bound exploration within a latent space, they inherently suffer from an exploitation gap -- a performance ceiling imposed by the decoder's reconstruction loss. We introduce SPAARS, a curriculum learning framework that initially constrains exploration to the low-dimensional latent manifold for sample-efficient, safe behavioral improvement, then seamlessly transfers control to the raw action space, bypassing the decoder bottleneck. SPAARS has two instantiations: the CVAE-based variant requires only unordered (s,a) pairs and no trajectory segmentation; SPAARS-SUPE pairs SPAARS with OPAL temporal skill pretraining for stronger exploration structure at the cost of requiring trajectory chunks. We prove an upper bound on the exploitation gap using the Performance Difference Lemma, establish that latent-space policy gradients achieve provable variance reduction over raw-space exploration, and show that concurrent behavioral cloning during the latent phase directly controls curriculum transition stability. Empirically, SPAARS-SUPE achieves 0.825 normalized return on kitchen-mixed-v0 versus 0.75 for SUPE, with 5x better sample efficiency; standalone SPAARS achieves 92.7 and 102.9 normalized return on hopper-medium-v2 and walker2d-medium-v2 respectively, surpassing IQL baselines of 66.3 and 78.3 respectively, confirming the utility of the unordered-pair CVAE instantiation.

