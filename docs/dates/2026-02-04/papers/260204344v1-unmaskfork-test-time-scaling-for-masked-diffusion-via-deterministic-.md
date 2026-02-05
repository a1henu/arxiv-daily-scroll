---
layout: default
title: UnMaskFork: Test-Time Scaling for Masked Diffusion via Deterministic Action Branching
---

# UnMaskFork: Test-Time Scaling for Masked Diffusion via Deterministic Action Branching
**arXiv**：[2602.04344v1](https://arxiv.org/abs/2602.04344) · [PDF](https://arxiv.org/pdf/2602.04344.pdf)  
**作者**：Kou Misaki, Takuya Akiba  

**一句话要点**：提出UnMaskFork框架，通过确定性动作分支优化掩码扩散语言模型的推理生成路径。

**关键词**：掩码扩散语言模型, 测试时扩展, 蒙特卡洛树搜索, 确定性动作分支, 推理优化, 复杂任务生成

## 3 点简述
- 核心问题：掩码扩散语言模型在推理时缺乏高效搜索策略，影响复杂任务性能。
- 方法要点：将去掩码轨迹建模为搜索树，利用蒙特卡洛树搜索和多个模型进行确定性部分去掩码。
- 实验或效果：在复杂编码基准上优于现有测试时扩展基线，数学推理任务中展现强可扩展性。

## 摘要（原文）

> Test-time scaling strategies have effectively leveraged inference-time compute to enhance the reasoning abilities of Autoregressive Large Language Models. In this work, we demonstrate that Masked Diffusion Language Models (MDLMs) are inherently amenable to advanced search strategies, owing to their iterative and non-autoregressive generation process. To leverage this, we propose UnMaskFork (UMF), a framework that formulates the unmasking trajectory as a search tree and employs Monte Carlo Tree Search to optimize the generation path. In contrast to standard scaling methods relying on stochastic sampling, UMF explores the search space through deterministic partial unmasking actions performed by multiple MDLMs. Our empirical evaluation demonstrates that UMF consistently outperforms existing test-time scaling baselines on complex coding benchmarks, while also exhibiting strong scalability on mathematical reasoning tasks.

