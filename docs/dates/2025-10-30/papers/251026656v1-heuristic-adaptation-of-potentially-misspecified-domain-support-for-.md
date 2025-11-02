---
layout: default
title: Heuristic Adaptation of Potentially Misspecified Domain Support for Likelihood-Free Inference in Stochastic Dynamical Systems
---

# Heuristic Adaptation of Potentially Misspecified Domain Support for Likelihood-Free Inference in Stochastic Dynamical Systems
**arXiv**：[2510.26656v1](https://arxiv.org/abs/2510.26656) · [PDF](https://arxiv.org/pdf/2510.26656.pdf)  
**作者**：Georgios Kamaras, Craig Innes, Subramanian Ramamoorthy  

**一句话要点**：提出三种启发式LFI变体以解决随机动力系统中领域支持误设问题

**关键词**：无似然推断, 随机动力系统, 领域适应, 后验推断, 启发式方法, 机器人学习

## 3 点简述
- 核心问题：LFI中固定支持可能导致后验次优且虚假确定
- 方法要点：EDGE、MODE和CENTRE变体根据后验模式偏移自适应调整支持
- 实验效果：在DLO操作任务中提升参数推断和策略学习的鲁棒性

## 摘要（原文）

> In robotics, likelihood-free inference (LFI) can provide the domain
> distribution that adapts a learnt agent in a parametric set of deployment
> conditions. LFI assumes an arbitrary support for sampling, which remains
> constant as the initial generic prior is iteratively refined to more
> descriptive posteriors. However, a potentially misspecified support can lead to
> suboptimal, yet falsely certain, posteriors. To address this issue, we propose
> three heuristic LFI variants: EDGE, MODE, and CENTRE. Each interprets the
> posterior mode shift over inference steps in its own way and, when integrated
> into an LFI step, adapts the support alongside posterior inference. We first
> expose the support misspecification issue and evaluate our heuristics using
> stochastic dynamical benchmarks. We then evaluate the impact of heuristic
> support adaptation on parameter inference and policy learning for a dynamic
> deformable linear object (DLO) manipulation task. Inference results in a finer
> length and stiffness classification for a parametric set of DLOs. When the
> resulting posteriors are used as domain distributions for sim-based policy
> learning, they lead to more robust object-centric agent performance.

