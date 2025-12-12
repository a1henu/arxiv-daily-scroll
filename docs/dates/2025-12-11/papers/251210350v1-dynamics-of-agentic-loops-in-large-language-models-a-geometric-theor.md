---
layout: default
title: Dynamics of Agentic Loops in Large Language Models: A Geometric Theory of Trajectories
---

# Dynamics of Agentic Loops in Large Language Models: A Geometric Theory of Trajectories
**arXiv**：[2512.10350v1](https://arxiv.org/abs/2512.10350) · [PDF](https://arxiv.org/pdf/2512.10350.pdf)  
**作者**：Nicolas Tacheny  

**一句话要点**：提出几何框架分析大语言模型代理循环轨迹，以控制收敛与发散动态。

**关键词**：大语言模型, 代理循环, 几何分析, 动态系统, 语义嵌入, 轨迹测量

## 3 点简述
- 核心问题：代理循环在语义嵌入空间中的几何行为（如收敛或发散）未知。
- 方法要点：引入几何框架，区分人工空间与嵌入空间，并应用等距校准消除余弦相似度偏差。
- 实验或效果：通过受控实验识别收缩重写循环和探索性总结否定循环两种基本动态机制。

## 摘要（原文）

> Agentic systems built on large language models operate through recursive feedback loops, where each output becomes the next input. Yet the geometric behavior of these agentic loops (whether they converge, diverge, or exhibit more complex dynamics) remains poorly understood. This paper introduces a geometric framework for analyzing agentic trajectories in semantic embedding space, treating iterative transformations as discrete dynamical systems. We distinguish the artifact space, where linguistic transformations occur, from the embedding space, where geometric measurements are performed. Because cosine similarity is biased by embedding anisotropy, we introduce an isotonic calibration that eliminates systematic bias and aligns similarities with human semantic judgments while preserving high local stability. This enables rigorous measurement of trajectories, clusters and attractors. Through controlled experiments on singular agentic loops, we identify two fundamental regimes. A contractive rewriting loop converges toward a stable attractor with decreasing dispersion, while an exploratory summarize and negate loop produces unbounded divergence with no cluster formation. These regimes display qualitatively distinct geometric signatures of contraction and expansion. Our results show that prompt design directly governs the dynamical regime of an agentic loop, enabling systematic control of convergence, divergence and trajectory structure in iterative LLM transformations.

