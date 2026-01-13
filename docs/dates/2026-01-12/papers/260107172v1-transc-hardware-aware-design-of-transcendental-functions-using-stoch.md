---
layout: default
title: TranSC: Hardware-Aware Design of Transcendental Functions Using Stochastic Logic
---

# TranSC: Hardware-Aware Design of Transcendental Functions Using Stochastic Logic
**arXiv**：[2601.07172v1](https://arxiv.org/abs/2601.07172) · [PDF](https://arxiv.org/pdf/2601.07172.pdf)  
**作者**：Mehran Moghadam, Sercan Aygun, M. Hassan Najafi  

**一句话要点**：提出TranSC方法，利用随机计算和低差异序列实现硬件友好的超越函数设计。

**关键词**：超越函数实现, 随机计算, 硬件优化, 低差异序列, 设计自动化

## 3 点简述
- 核心问题：超越函数在硬件实现中复杂度高，传统方法难以平衡精度与效率。
- 方法要点：采用随机计算，引入Van der Corput低差异序列替代伪随机源，提升计算精度和效率。
- 实验或效果：在多种函数上验证，MSE降低达98%，硬件面积、功耗和能耗分别减少33%、72%和64%。

## 摘要（原文）

> The hardware-friendly implementation of transcendental functions remains a longstanding challenge in design automation. These functions, which cannot be expressed as finite combinations of algebraic operations, pose significant complexity in digital circuit design. This study introduces a novel approach, TranSC, that utilizes stochastic computing (SC) for lightweight yet accurate implementation of transcendental functions. Building on established SC techniques, our method explores alternative random sources-specifically, quasi-random Van der Corput low-discrepancy (LD) sequences-instead of conventional pseudo-randomness. This shift enhances both the accuracy and efficiency of SC-based computations. We validate our approach through extensive experiments on various function types, including trigonometric, hyperbolic, and activation functions. The proposed design approach significantly reduces MSE by up to 98% compared to the state-of-the-art solutions while reducing hardware area, power consumption, and energy usage by 33%, 72%, and 64%, respectively.

