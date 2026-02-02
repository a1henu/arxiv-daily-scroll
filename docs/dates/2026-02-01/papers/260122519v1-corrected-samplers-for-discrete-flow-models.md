---
layout: default
title: Corrected Samplers for Discrete Flow Models
---

# Corrected Samplers for Discrete Flow Models
**arXiv**：[2601.22519v1](https://arxiv.org/abs/2601.22519) · [PDF](https://arxiv.org/pdf/2601.22519.pdf)  
**作者**：Zhengyan Wan, Yidong Ouyang, Liyan Xie, Fang Fang, Hongyuan Zha, Guang Cheng  

**一句话要点**：提出修正采样器以降低离散流模型中的离散化误差，提升生成效率与质量。

**关键词**：离散流模型, 采样器优化, 离散化误差, 生成模型, 文本到图像生成

## 3 点简述
- 针对离散流模型中现有采样器（如tau-leaping和Euler求解器）因固定转移率导致高迭代次数和误差的问题。
- 通过分析Euler采样器的一步下界，提出时间修正和位置修正两种采样器，几乎不增加计算成本。
- 在模拟和文本到图像生成任务中验证了方法能提高生成质量并减少推理时间。

## 摘要（原文）

> Discrete flow models (DFMs) have been proposed to learn the data distribution on a finite state space, offering a flexible framework as an alternative to discrete diffusion models. A line of recent work has studied samplers for discrete diffusion models, such as tau-leaping and Euler solver. However, these samplers require a large number of iterations to control discretization error, since the transition rates are frozen in time and evaluated at the initial state within each time interval. Moreover, theoretical results for these samplers often require boundedness conditions of the transition rate or they focus on a specific type of source distributions. To address those limitations, we establish non-asymptotic discretization error bounds for those samplers without any restriction on transition rates and source distributions, under the framework of discrete flow models. Furthermore, by analyzing a one-step lower bound of the Euler sampler, we propose two corrected samplers: \textit{time-corrected sampler} and \textit{location-corrected sampler}, which can reduce the discretization error of tau-leaping and Euler solver with almost no additional computational cost. We rigorously show that the location-corrected sampler has a lower iteration complexity than existing parallel samplers. We validate the effectiveness of the proposed method by demonstrating improved generation quality and reduced inference time on both simulation and text-to-image generation tasks. Code can be found in https://github.com/WanZhengyan/Corrected-Samplers-for-Discrete-Flow-Models.

