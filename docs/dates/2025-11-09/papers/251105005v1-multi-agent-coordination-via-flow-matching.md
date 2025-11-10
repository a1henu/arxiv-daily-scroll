---
layout: default
title: Multi-agent Coordination via Flow Matching
---

# Multi-agent Coordination via Flow Matching
**arXiv**：[2511.05005v1](https://arxiv.org/abs/2511.05005) · [PDF](https://arxiv.org/pdf/2511.05005.pdf)  
**作者**：Dongsu Lee, Daehee Lee, Amy Zhang  

**一句话要点**：提出MAC-Flow框架以解决多智能体协调中性能与计算速度的权衡问题

**关键词**：多智能体协调, 流匹配, 离线强化学习, 策略蒸馏, 推理加速

## 3 点简述
- 核心问题：现有方法在离线多智能体协调中难以兼顾复杂行为建模与实时高效执行
- 方法要点：先学习基于流的联合行为表示，再蒸馏为去中心化单步策略
- 实验或效果：在多个基准测试中，推理速度比扩散方法快约14.5倍，性能保持良好

## 摘要（原文）

> This work presents MAC-Flow, a simple yet expressive framework for
> multi-agent coordination. We argue that requirements of effective coordination
> are twofold: (i) a rich representation of the diverse joint behaviors present
> in offline data and (ii) the ability to act efficiently in real time. However,
> prior approaches often sacrifice one for the other, i.e., denoising
> diffusion-based solutions capture complex coordination but are computationally
> slow, while Gaussian policy-based solutions are fast but brittle in handling
> multi-agent interaction. MAC-Flow addresses this trade-off by first learning a
> flow-based representation of joint behaviors, and then distilling it into
> decentralized one-step policies that preserve coordination while enabling fast
> execution. Across four different benchmarks, including $12$ environments and
> $34$ datasets, MAC-Flow alleviates the trade-off between performance and
> computational cost, specifically achieving about $\boldsymbol{\times14.5}$
> faster inference compared to diffusion-based MARL methods, while maintaining
> good performance. At the same time, its inference speed is similar to that of
> prior Gaussian policy-based offline multi-agent reinforcement learning (MARL)
> methods.

