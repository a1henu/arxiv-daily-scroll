---
layout: default
title: Flow Matching-Based Autonomous Driving Planning with Advanced Interactive Behavior Modeling
---

# Flow Matching-Based Autonomous Driving Planning with Advanced Interactive Behavior Modeling
**arXiv**：[2510.11083v1](https://arxiv.org/abs/2510.11083) · [PDF](https://arxiv.org/pdf/2510.11083.pdf)  
**作者**：Tianyi Tan, Yinan Zheng, Ruiming Liang, Zexu Wang, Kexin Zheng, Jinliang Zheng, Jianxiong Li, Xianyuan Zhan, Jingjing Liu  

**一句话要点**：提出Flow Planner以解决复杂驾驶场景中的交互行为建模问题

**关键词**：自动驾驶规划, 交互行为建模, 流匹配, 轨迹标记化, 多模态生成, 学习型方法

## 3 点简述
- 核心问题：交互驾驶行为建模困难，数据稀缺导致传统模仿学习难以捕捉高价值行为
- 方法要点：采用细粒度轨迹标记化和流匹配，结合分类器自由引导生成多模态行为
- 实验或效果：在nuPlan和interPlan数据集上实现SOTA性能，有效建模交互行为

## 摘要（原文）

> Modeling interactive driving behaviors in complex scenarios remains a
> fundamental challenge for autonomous driving planning. Learning-based
> approaches attempt to address this challenge with advanced generative models,
> removing the dependency on over-engineered architectures for representation
> fusion. However, brute-force implementation by simply stacking transformer
> blocks lacks a dedicated mechanism for modeling interactive behaviors that are
> common in real driving scenarios. The scarcity of interactive driving data
> further exacerbates this problem, leaving conventional imitation learning
> methods ill-equipped to capture high-value interactive behaviors. We propose
> Flow Planner, which tackles these problems through coordinated innovations in
> data modeling, model architecture, and learning scheme. Specifically, we first
> introduce fine-grained trajectory tokenization, which decomposes the trajectory
> into overlapping segments to decrease the complexity of whole trajectory
> modeling. With a sophisticatedly designed architecture, we achieve efficient
> temporal and spatial fusion of planning and scene information, to better
> capture interactive behaviors. In addition, the framework incorporates flow
> matching with classifier-free guidance for multi-modal behavior generation,
> which dynamically reweights agent interactions during inference to maintain
> coherent response strategies, providing a critical boost for interactive
> scenario understanding. Experimental results on the large-scale nuPlan dataset
> and challenging interactive interPlan dataset demonstrate that Flow Planner
> achieves state-of-the-art performance among learning-based approaches while
> effectively modeling interactive behaviors in complex driving scenarios.

