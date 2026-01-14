---
layout: default
title: Sampling via Stochastic Interpolants by Langevin-based Velocity and Initialization Estimation in Flow ODEs
---

# Sampling via Stochastic Interpolants by Langevin-based Velocity and Initialization Estimation in Flow ODEs
**arXiv**：[2601.08527v1](https://arxiv.org/abs/2601.08527) · [PDF](https://arxiv.org/pdf/2601.08527.pdf)  
**作者**：Chenguang Duan, Yuling Jiao, Gabriele Steidl, Christian Wald, Jerry Zhijian Yang, Ruizhe Zhang  

**一句话要点**：提出基于朗之万采样的随机插值流ODE方法，用于从非归一化玻尔兹曼密度高效采样。

**关键词**：概率流ODE, 朗之万采样, 随机插值, 玻尔兹曼密度采样, 贝叶斯推断

## 3 点简述
- 核心问题：从非归一化玻尔兹曼密度采样，传统方法在高维多模态分布中效率低。
- 方法要点：利用朗之万采样器生成中间时间样本并估计流ODE的速度场，确保收敛性。
- 实验或效果：数值实验验证了方法在高维多模态分布和贝叶斯推断任务中的高效性。

## 摘要（原文）

> We propose a novel method for sampling from unnormalized Boltzmann densities based on a probability-flow ordinary differential equation (ODE) derived from linear stochastic interpolants. The key innovation of our approach is the use of a sequence of Langevin samplers to enable efficient simulation of the flow. Specifically, these Langevin samplers are employed (i) to generate samples from the interpolant distribution at intermediate times and (ii) to construct, starting from these intermediate times, a robust estimator of the velocity field governing the flow ODE. For both applications of the Langevin diffusions, we establish convergence guarantees. Extensive numerical experiments demonstrate the efficiency of the proposed method on challenging multimodal distributions across a range of dimensions, as well as its effectiveness in Bayesian inference tasks.

