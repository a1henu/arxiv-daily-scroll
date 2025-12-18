---
layout: default
title: Expand and Prune: Maximizing Trajectory Diversity for Effective GRPO in Generative Models
---

# Expand and Prune: Maximizing Trajectory Diversity for Effective GRPO in Generative Models
**arXiv**：[2512.15347v1](https://arxiv.org/abs/2512.15347) · [PDF](https://arxiv.org/pdf/2512.15347.pdf)  
**作者**：Shiran Ge, Chenyi Huang, Yuang Ai, Qihang Fan, Huaibo Huang, Ran He  

**一句话要点**：提出Pro-GRPO框架以解决GRPO中轨迹多样性与计算成本的冲突

**关键词**：生成模型对齐, 轨迹多样性, 计算效率优化, 潜在特征剪枝, GRPO改进

## 3 点简述
- 核心问题：GRPO在大组规模与计算成本间存在冲突，轨迹奖励聚类导致优化价值有限
- 方法要点：设计动态框架Pro-GRPO，集成基于潜在特征的轨迹剪枝，采用扩展-剪枝策略提升多样性
- 实验或效果：在扩散和流模型中验证了Pro-GRPO的通用性和有效性，降低了计算开销

## 摘要（原文）

> Group Relative Policy Optimization (GRPO) is a powerful technique for aligning generative models, but its effectiveness is bottlenecked by the conflict between large group sizes and prohibitive computational costs. In this work, we investigate the trade-off through empirical studies, yielding two key observations. First, we discover the reward clustering phenomenon in which many trajectories collapse toward the group-mean reward, offering limited optimization value. Second, we design a heuristic strategy named Optimal Variance Filtering (OVF), and verify that a high-variance subset of trajectories, selected by OVF can outperform the larger, unfiltered group. However, this static, post-sampling OVF approach still necessitates critical computational overhead, as it performs unnecessary sampling for trajectories that are ultimately discarded. To resolve this, we propose Pro-GRPO (Proactive GRPO), a novel dynamic framework that integrates latent feature-based trajectory pruning into the sampling process. Through the early termination of reward-clustered trajectories, Pro-GRPO reduces computational overhead. Leveraging its efficiency, Pro-GRPO employs an "Expand-and-Prune" strategy. This strategy first expands the size of initial sampling group to maximize trajectory diversity, then it applies multi-step OVF to the latents, avoiding prohibitive computational costs. Extensive experiments on both diffusion-based and flow-based models demonstrate the generality and effectiveness of our Pro-GRPO framework.

