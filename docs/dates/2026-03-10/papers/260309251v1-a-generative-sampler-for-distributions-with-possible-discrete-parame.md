---
layout: default
title: A Generative Sampler for distributions with possible discrete parameter based on Reversibility
---

# A Generative Sampler for distributions with possible discrete parameter based on Reversibility
**arXiv**：[2603.09251v1](https://arxiv.org/abs/2603.09251) · [PDF](https://arxiv.org/pdf/2603.09251.pdf)  
**作者**：Lei Li, Zhen Wang, Lishuo Zhang  

**一句话要点**：提出基于可逆性的生成采样框架，以解决离散或混合变量系统的采样难题。

**关键词**：生成采样, 可逆性约束, 最大均值差异, 离散参数系统, 混合变量采样, 物理过渡核

## 3 点简述
- 核心问题：连续域采样方法难以扩展至离散或混合变量系统，因梯度未定义或估计器高方差。
- 方法要点：利用详细平衡的时间可逆性，通过最小化前向与后向马尔可夫轨迹的MMD，仅依赖能量评估进行训练。
- 实验或效果：在连续高斯混合、离散伊辛模型和混合系统上准确再现热力学可观测量和模态切换行为。

## 摘要（原文）

> Learning to sample from complex unnormalized distributions is a fundamental challenge in computational physics and machine learning. While score-based and variational methods have achieved success in continuous domains, extending them to discrete or mixed-variable systems remains difficult due to ill-defined gradients or high variance in estimators. We propose a unified, target-gradient-free generative sampling framework applicable across diverse state spaces. Building on the fact that detailed balance implies the time-reversibility of the equilibrium stochastic process, we enforce this symmetry as a statistical constraint. Specifically, using a prescribed physical transition kernel (such as Metropolis-Hastings), we minimize the Maximum Mean Discrepancy (MMD) between the joint distributions of forward and backward Markov trajectories. Crucially, this training procedure relies solely on energy evaluations via acceptance ratios, circumventing the need for target score functions or continuous relaxations. We demonstrate the versatility of our method on three distinct benchmarks: (1) a continuous multi-modal Gaussian mixture, (2) the discrete high-dimensional Ising model, and (3) a challenging hybrid system coupling discrete indices with continuous dynamics. Experiments show that our framework accurately reproduces thermodynamic observables and captures mode-switching behavior across all regimes, offering a physically grounded and universally applicable alternative for equilibrium sampling.

