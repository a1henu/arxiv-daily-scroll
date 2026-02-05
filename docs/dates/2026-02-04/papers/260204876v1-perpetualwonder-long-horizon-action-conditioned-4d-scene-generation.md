---
layout: default
title: PerpetualWonder: Long-Horizon Action-Conditioned 4D Scene Generation
---

# PerpetualWonder: Long-Horizon Action-Conditioned 4D Scene Generation
**arXiv**：[2602.04876v1](https://arxiv.org/abs/2602.04876) · [PDF](https://arxiv.org/pdf/2602.04876.pdf)  
**作者**：Jiahao Zhan, Zizhang Li, Hong-Xing Yu, Jiajun Wu  

**一句话要点**：提出PerpetualWonder，通过闭环系统实现单图像驱动的长时程动作条件4D场景生成。

**关键词**：4D场景生成, 动作条件生成, 闭环系统, 统一表示, 长时程模拟, 单图像驱动

## 3 点简述
- 核心问题：现有方法物理状态与视觉表示解耦，导致生成更新无法修正后续交互的底层物理。
- 方法要点：引入统一表示双向链接物理状态与视觉基元，支持生成式修正动态与外观；采用多视角监督机制解决优化模糊性。
- 实验或效果：从单图像成功模拟复杂多步交互，保持物理合理性与视觉一致性。

## 摘要（原文）

> We introduce PerpetualWonder, a hybrid generative simulator that enables long-horizon, action-conditioned 4D scene generation from a single image. Current works fail at this task because their physical state is decoupled from their visual representation, which prevents generative refinements to update the underlying physics for subsequent interactions. PerpetualWonder solves this by introducing the first true closed-loop system. It features a novel unified representation that creates a bidirectional link between the physical state and visual primitives, allowing generative refinements to correct both the dynamics and appearance. It also introduces a robust update mechanism that gathers supervision from multiple viewpoints to resolve optimization ambiguity. Experiments demonstrate that from a single image, PerpetualWonder can successfully simulate complex, multi-step interactions from long-horizon actions, maintaining physical plausibility and visual consistency.

