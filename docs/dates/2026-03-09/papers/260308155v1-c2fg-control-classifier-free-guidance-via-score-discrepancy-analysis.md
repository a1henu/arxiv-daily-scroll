---
layout: default
title: C$^2$FG: Control Classifier-Free Guidance via Score Discrepancy Analysis
---

# C$^2$FG: Control Classifier-Free Guidance via Score Discrepancy Analysis
**arXiv**：[2603.08155v1](https://arxiv.org/abs/2603.08155) · [PDF](https://arxiv.org/pdf/2603.08155.pdf)  
**作者**：Jiayang Gao, Tianyi Zheng, Jiayang Zou, Fengxiang Yang, Shice Liu, Luyao Fan, Zheyu Zhang, Hao Zhang, Jinwei Chen, Peng-Tao Jiang, Bo Li, Jia Wang  

**一句话要点**：提出C²FG方法，通过分数差异分析动态控制无分类器引导权重以优化扩散模型生成。

**关键词**：扩散模型, 无分类器引导, 分数差异分析, 动态控制, 生成任务, 训练免费方法

## 3 点简述
- 核心问题：无分类器引导依赖固定或启发式权重，忽略扩散过程动态性，导致生成效果受限。
- 方法要点：基于扩散过程理论分析分数差异，设计指数衰减控制函数，实现训练免费、即插即用的动态引导。
- 实验或效果：在多种生成任务中验证有效性，与现有策略正交，提升生成质量和适用性。

## 摘要（原文）

> Classifier-Free Guidance (CFG) is a cornerstone of modern conditional diffusion models, yet its reliance on the fixed or heuristic dynamic guidance weight is predominantly empirical and overlooks the inherent dynamics of the diffusion process. In this paper, we provide a rigorous theoretical analysis of the Classifier-Free Guidance. Specifically, we establish strict upper bounds on the score discrepancy between conditional and unconditional distributions at different timesteps based on the diffusion process. This finding explains the limitations of fixed-weight strategies and establishes a principled foundation for time-dependent guidance. Motivated by this insight, we introduce \textbf{Control Classifier-Free Guidance (C$^2$FG)}, a novel, training-free, and plug-in method that aligns the guidance strength with the diffusion dynamics via an exponential decay control function. Extensive experiments demonstrate that C$^2$FG is effective and broadly applicable across diverse generative tasks, while also exhibiting orthogonality to existing strategies.

