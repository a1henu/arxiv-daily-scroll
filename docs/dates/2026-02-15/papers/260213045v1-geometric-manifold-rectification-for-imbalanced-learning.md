---
layout: default
title: Geometric Manifold Rectification for Imbalanced Learning
---

# Geometric Manifold Rectification for Imbalanced Learning
**arXiv**：[2602.13045v1](https://arxiv.org/abs/2602.13045) · [PDF](https://arxiv.org/pdf/2602.13045.pdf)  
**作者**：Xubin Wang, Qing Li, Weijia Jia  

**一句话要点**：提出几何流形矫正框架以处理不平衡表格数据中的噪声和类重叠问题

**关键词**：不平衡分类, 几何流形, 欠采样, 局部几何先验, 非对称清理, 表格数据

## 3 点简述
- 核心问题：多数类拓扑侵入少数类流形，模糊决策边界，传统欠采样方法易移除信息性少数样本
- 方法要点：基于局部几何先验，使用逆距离加权kNN投票进行几何置信度估计，并实施非对称清理保护少数样本
- 实验或效果：在多个基准数据集上验证，与强采样基线竞争，展示稳健处理能力

## 摘要（原文）

> Imbalanced classification presents a formidable challenge in machine learning, particularly when tabular datasets are plagued by noise and overlapping class boundaries. From a geometric perspective, the core difficulty lies in the topological intrusion of the majority class into the minority manifold, which obscures the true decision boundary. Traditional undersampling techniques, such as Edited Nearest Neighbours (ENN), typically employ symmetric cleaning rules and uniform voting, failing to capture the local manifold structure and often inadvertently removing informative minority samples. In this paper, we propose GMR (Geometric Manifold Rectification), a novel framework designed to robustly handle imbalanced structured data by exploiting local geometric priors. GMR makes two contributions: (1) Geometric confidence estimation that uses inverse-distance weighted kNN voting with an adaptive distance metric to capture local reliability; and (2) asymmetric cleaning that is strict on majority samples while conservatively protecting minority samples via a safe-guarding cap on minority removal. Extensive experiments on multiple benchmark datasets show that GMR is competitive with strong sampling baselines.

