---
layout: default
title: Co-Initialization of Control Filter and Secondary Path via Meta-Learning for Active Noise Control
---

# Co-Initialization of Control Filter and Secondary Path via Meta-Learning for Active Noise Control
**arXiv**：[2601.13849v1](https://arxiv.org/abs/2601.13849) · [PDF](https://arxiv.org/pdf/2601.13849.pdf)  
**作者**：Ziyi Yang, Li Rao, Zhengding Luo, Dongyuan Shi, Qirui Huang, Woon-Seng Gan  

**一句话要点**：提出基于元学习的控制滤波器与次级路径协同初始化方法，以提升主动噪声控制的环境适应速度。

**关键词**：主动噪声控制, 元学习, 控制滤波器初始化, 次级路径建模, FxLMS算法, 环境适应

## 3 点简述
- 核心问题：主动噪声控制（ANC）在环境变化时需快速适应，但早期性能受初始化影响大。
- 方法要点：使用模型无关元学习（MAML）联合初始化控制滤波器和次级路径模型，保持运行时算法不变。
- 实验或效果：在在线次级路径建模FxLMS测试中，相比基线，降低了早期误差、缩短达到目标时间、减少辅助噪声能量并加速路径变化后的恢复。

## 摘要（原文）

> Active noise control (ANC) must adapt quickly when the acoustic environment changes, yet early performance is largely dictated by initialization. We address this with a Model-Agnostic Meta-Learning (MAML) co-initialization that jointly sets the control filter and the secondary-path model for FxLMS-based ANC while keeping the runtime algorithm unchanged. The initializer is pre-trained on a small set of measured paths using short two-phase inner loops that mimic identification followed by residual-noise reduction, and is applied by simply setting the learned initial coefficients. In an online secondary path modeling FxLMS testbed, it yields lower early-stage error, shorter time-to-target, reduced auxiliary-noise energy, and faster recovery after path changes than a baseline without re-initialization. The method provides a simple fast start for feedforward ANC under environment changes, requiring a small set of paths to pre-train.

