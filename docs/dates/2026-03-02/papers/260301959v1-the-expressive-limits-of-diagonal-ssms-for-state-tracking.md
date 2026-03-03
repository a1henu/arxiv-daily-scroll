---
layout: default
title: The Expressive Limits of Diagonal SSMs for State-Tracking
---

# The Expressive Limits of Diagonal SSMs for State-Tracking
**arXiv**：[2603.01959v1](https://arxiv.org/abs/2603.01959) · [PDF](https://arxiv.org/pdf/2603.01959.pdf)  
**作者**：Mehran Shakerinava, Behnoush Khavari, Siamak Ravanbakhsh, Sarath Chandar  

**一句话要点**：揭示对角SSMs在状态跟踪任务中的表达力限制，基于群论分析其精确表达能力。

**关键词**：状态空间模型, 表达力分析, 群论, 状态跟踪, 序列建模, 理论限制

## 3 点简述
- 研究对角SSMs在序列状态跟踪任务中的表达力理论限制。
- 证明单层DCD SSMs无法表达非阿贝尔群的状态跟踪，多层模型表达能力与群结构相关。
- 实验显示多层模型常无法学习非阿贝尔群状态跟踪，揭示表达力与可学习性之间的差距。

## 摘要（原文）

> State-Space Models (SSMs) have recently been shown to achieve strong empirical performance on a variety of long-range sequence modeling tasks while remaining efficient and highly-parallelizable. However, the theoretical understanding of their expressive power remains limited. In this work, we study the expressivity of input-Dependent Complex-valued Diagonal (DCD) SSMs on sequential state-tracking tasks. We show that single-layer DCD SSMs cannot express state-tracking of any non-Abelian group at finite precision. More generally, we show that $k$-layer DCD SSMs can express state-tracking of a group if and only if that group has a subnormal series of length $k$, with Abelian factors. That is, we identify the precise expressivity range of $k$-layer DCD SSMs within the solvable groups. Empirically, we find that multi-layer models often fail to learn state-tracking for non-Abelian groups, highlighting a gap between expressivity and learnability.

