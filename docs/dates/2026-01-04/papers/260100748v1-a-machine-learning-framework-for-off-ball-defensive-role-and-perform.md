---
layout: default
title: A Machine Learning Framework for Off Ball Defensive Role and Performance Evaluation in Football
---

# A Machine Learning Framework for Off Ball Defensive Role and Performance Evaluation in Football
**arXiv**：[2601.00748v1](https://arxiv.org/abs/2601.00748) · [PDF](https://arxiv.org/pdf/2601.00748.pdf)  
**作者**：Sean Groom, Shuo Wang, Francisco Belo, Axl Rice, Liam Anderson  

**一句话要点**：提出基于协变量依赖隐马尔可夫模型的角球防守角色推断与性能评估框架

**关键词**：足球分析, 防守角色推断, 隐马尔可夫模型, 反事实分析, 球员追踪数据

## 3 点简述
- 核心问题：传统指标难以评估足球中无球防守的协调移动，现有反事实方法缺乏战术上下文。
- 方法要点：使用CDHMM从球员追踪数据推断角球中的人盯人和区域防守角色，无需标注。
- 实验或效果：提出防守信用分配框架和角色条件幽灵方法，提供可解释的防守贡献评估。

## 摘要（原文）

> Evaluating off-ball defensive performance in football is challenging, as traditional metrics do not capture the nuanced coordinated movements that limit opponent action selection and success probabilities. Although widely used possession value models excel at appraising on-ball actions, their application to defense remains limited. Existing counterfactual methods, such as ghosting models, help extend these analyses but often rely on simulating "average" behavior that lacks tactical context. To address this, we introduce a covariate-dependent Hidden Markov Model (CDHMM) tailored to corner kicks, a highly structured aspect of football games. Our label-free model infers time-resolved man-marking and zonal assignments directly from player tracking data. We leverage these assignments to propose a novel framework for defensive credit attribution and a role-conditioned ghosting method for counterfactual analysis of off-ball defensive performance. We show how these contributions provide a interpretable evaluation of defensive contributions against context-aware baselines.

