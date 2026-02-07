---
layout: default
title: TimelyFreeze: Adaptive Parameter Freezing Mechanism for Pipeline Parallelism
---

# TimelyFreeze: Adaptive Parameter Freezing Mechanism for Pipeline Parallelism
**arXiv**：[2602.05754v1](https://arxiv.org/abs/2602.05754) · [PDF](https://arxiv.org/pdf/2602.05754.pdf)  
**作者**：Seonghye Cho, Jaemin Han, Hyunjin Kim, Euisoo Jung, Jae-Gil Lee  

**一句话要点**：提出TimelyFreeze自适应参数冻结机制，以优化流水线并行训练中的吞吐量问题。

**关键词**：流水线并行, 参数冻结, 训练优化, 深度学习, 模型训练, 吞吐量提升

## 3 点简述
- 核心问题：流水线并行训练中，现有参数冻结方法常过度冻结，导致不必要的精度下降。
- 方法要点：将流水线调度建模为有向无环图，通过线性规划计算最优冻结比率，在精度约束下最小化批次执行时间。
- 实验或效果：在LLaMA-8B上实现高达40%的训练吞吐量提升，同时保持可比精度，适用于多种流水线并行设置。

## 摘要（原文）

> Pipeline parallelism enables training models that exceed single-device memory, but practical throughput remains limited by pipeline bubbles. Although parameter freezing can improve training throughput by adaptively skipping backward computation, existing methods often over-freeze parameters, resulting in unnecessary accuracy degradation. To address this issue, we propose TimelyFreeze, which models the pipeline schedule as a directed acyclic graph and solves a linear program to compute optimal freeze ratios that minimize batch execution time under accuracy constraints. Experiments show that TimelyFreeze achieves up to 40% training throughput improvement on LLaMA-8B with comparable accuracy. Overall, it enables faster large-scale model training without compromising convergence and generalizes across diverse pipeline-parallel settings.

