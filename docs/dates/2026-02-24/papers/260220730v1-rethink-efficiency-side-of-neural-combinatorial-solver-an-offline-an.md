---
layout: default
title: Rethink Efficiency Side of Neural Combinatorial Solver: An Offline and Self-Play Paradigm
---

# Rethink Efficiency Side of Neural Combinatorial Solver: An Offline and Self-Play Paradigm
**arXiv**：[2602.20730v1](https://arxiv.org/abs/2602.20730) · [PDF](https://arxiv.org/pdf/2602.20730.pdf)  
**作者**：Zhenxing Xu, Zeyuan Ma, Weidong Bao, Hui Yan, Yan Zheng, Ji Wang  

**一句话要点**：提出ECO离线自学习范式，提升神经组合优化效率

**关键词**：神经组合优化, 离线学习, 自学习, 效率优化, Mamba架构, 直接偏好优化

## 3 点简述
- 核心问题：在线范式效率低，限制神经组合优化应用
- 方法要点：采用两阶段离线范式，结合监督预热与直接偏好优化
- 实验或效果：在TSP和CVRP上竞争基线，内存与训练吞吐优势显著

## 摘要（原文）

> We propose ECO, a versatile learning paradigm that enables efficient offline self-play for Neural Combinatorial Optimization (NCO). ECO addresses key limitations in the field through: 1) Paradigm Shift: Moving beyond inefficient online paradigms, we introduce a two-phase offline paradigm consisting of supervised warm-up and iterative Direct Preference Optimization (DPO); 2) Architecture Shift: We deliberately design a Mamba-based architecture to further enhance the efficiency in the offline paradigm; and 3) Progressive Bootstrapping: To stabilize training, we employ a heuristic-based bootstrapping mechanism that ensures continuous policy improvement during training. Comparison results on TSP and CVRP highlight that ECO performs competitively with up-to-date baselines, with significant advantage on the efficiency side in terms of memory utilization and training throughput. We provide further in-depth analysis on the efficiency, throughput and memory usage of ECO. Ablation studies show rationale behind our designs.

