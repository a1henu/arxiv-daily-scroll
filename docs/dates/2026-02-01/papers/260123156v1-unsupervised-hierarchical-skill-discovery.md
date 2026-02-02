---
layout: default
title: Unsupervised Hierarchical Skill Discovery
---

# Unsupervised Hierarchical Skill Discovery
**arXiv**：[2601.23156v1](https://arxiv.org/abs/2601.23156) · [PDF](https://arxiv.org/pdf/2601.23156.pdf)  
**作者**：Damion Harvey, Geraud Nangue Tasse, Branden Ingram, Benjamin Rosman, Steven James  

**一句话要点**：提出基于语法的无监督技能分割与层次结构发现方法，用于强化学习轨迹分析。

**关键词**：无监督技能发现, 层次强化学习, 轨迹分割, 语法方法, 像素环境

## 3 点简述
- 核心问题：无监督分割轨迹为可重用技能并发现层次结构，避免依赖动作标签或奖励。
- 方法要点：使用语法方法从无标签轨迹中分割技能并诱导层次结构，捕获低层行为到高层技能的组成。
- 实验或效果：在Craftax和Minecraft等高维像素环境中评估，技能分割、重用和层次质量优于基线，加速下游任务学习。

## 摘要（原文）

> We consider the problem of unsupervised skill segmentation and hierarchical structure discovery in reinforcement learning. While recent approaches have sought to segment trajectories into reusable skills or options, most rely on action labels, rewards, or handcrafted annotations, limiting their applicability. We propose a method that segments unlabelled trajectories into skills and induces a hierarchical structure over them using a grammar-based approach. The resulting hierarchy captures both low-level behaviours and their composition into higher-level skills. We evaluate our approach in high-dimensional, pixel-based environments, including Craftax and the full, unmodified version of Minecraft. Using metrics for skill segmentation, reuse, and hierarchy quality, we find that our method consistently produces more structured and semantically meaningful hierarchies than existing baselines. Furthermore, as a proof of concept for utility, we demonstrate that these discovered hierarchies accelerate and stabilise learning on downstream reinforcement learning tasks.

