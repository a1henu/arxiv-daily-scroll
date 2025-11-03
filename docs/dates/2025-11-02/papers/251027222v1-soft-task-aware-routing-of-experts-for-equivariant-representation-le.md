---
layout: default
title: Soft Task-Aware Routing of Experts for Equivariant Representation Learning
---

# Soft Task-Aware Routing of Experts for Equivariant Representation Learning
**arXiv**：[2510.27222v1](https://arxiv.org/abs/2510.27222) · [PDF](https://arxiv.org/pdf/2510.27222.pdf)  
**作者**：Jaebyeong Jeon, Hyeonseo Jang, Jy-yong Sohn, Kibok Lee  

**一句话要点**：提出软任务感知路由以解决等变表示学习中冗余特征学习问题

**关键词**：等变表示学习, 软任务感知路由, 投影头专家, 冗余特征减少, 迁移学习

## 3 点简述
- 核心问题：现有方法在联合学习不变和等变表示时忽略共享信息，导致冗余特征和模型容量浪费
- 方法要点：引入软任务感知路由，将投影头建模为专家，使其专注于共享或任务特定信息
- 实验或效果：在多种迁移学习任务中表现一致提升，并观察到不变和等变嵌入间典型相关性降低

## 摘要（原文）

> Equivariant representation learning aims to capture variations induced by
> input transformations in the representation space, whereas invariant
> representation learning encodes semantic information by disregarding such
> transformations. Recent studies have shown that jointly learning both types of
> representations is often beneficial for downstream tasks, typically by
> employing separate projection heads. However, this design overlooks information
> shared between invariant and equivariant learning, which leads to redundant
> feature learning and inefficient use of model capacity. To address this, we
> introduce Soft Task-Aware Routing (STAR), a routing strategy for projection
> heads that models them as experts. STAR induces the experts to specialize in
> capturing either shared or task-specific information, thereby reducing
> redundant feature learning. We validate this effect by observing lower
> canonical correlations between invariant and equivariant embeddings.
> Experimental results show consistent improvements across diverse transfer
> learning tasks. The code is available at https://github.com/YonseiML/star.

