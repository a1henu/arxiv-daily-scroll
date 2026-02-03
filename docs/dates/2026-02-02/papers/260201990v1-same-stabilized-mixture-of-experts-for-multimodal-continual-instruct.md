---
layout: default
title: SAME: Stabilized Mixture-of-Experts for Multimodal Continual Instruction Tuning
---

# SAME: Stabilized Mixture-of-Experts for Multimodal Continual Instruction Tuning
**arXiv**：[2602.01990v1](https://arxiv.org/abs/2602.01990) · [PDF](https://arxiv.org/pdf/2602.01990.pdf)  
**作者**：Zhen-Hao Xie, Jun-Tao Tang, Yu-Cheng Shi, Han-Jia Ye, De-Chuan Zhan, Da-Wei Zhou  

**一句话要点**：提出SAME方法以解决多模态持续指令调优中的专家路由漂移问题

**关键词**：多模态持续指令调优, 专家路由漂移, 正交子空间分解, 历史输入协方差, 自适应专家激活

## 3 点简述
- 核心问题：多模态持续指令调优中专家路由漂移和专家漂移导致性能下降
- 方法要点：通过正交子空间分解稳定路由，基于历史输入协方差调节专家更新
- 实验或效果：在广泛实验中展示SOTA性能，无需排练

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) achieve strong performance through instruction tuning, but real-world deployment requires them to continually expand their capabilities, making Multimodal Continual Instruction Tuning (MCIT) essential. Recent methods leverage sparse expert routing to promote task specialization, but we find that the expert routing process suffers from drift as the data distribution evolves. For example, a grounding query that previously activated localization experts may instead be routed to irrelevant experts after learning OCR tasks. Meanwhile, the grounding-related experts can be overwritten by new tasks and lose their original functionality. Such failure reflects two problems: router drift, where expert selection becomes inconsistent over time, and expert drift, where shared experts are overwritten across tasks. Therefore, we propose StAbilized Mixture-of-Experts (SAME) for MCIT. To address router drift, SAME stabilizes expert selection by decomposing routing dynamics into orthogonal subspaces and updating only task-relevant directions. To mitigate expert drift, we regulate expert updates via curvature-aware scaling using historical input covariance in a rehearsal-free manner. SAME also introduces adaptive expert activation to freeze selected experts during training, reducing redundant computation and cross-task interference. Extensive experiments demonstrate its SOTA performance.

