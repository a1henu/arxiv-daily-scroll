---
layout: default
title: Dynamics Reveals Structure: Challenging the Linear Propagation Assumption
---

# Dynamics Reveals Structure: Challenging the Linear Propagation Assumption
**arXiv**：[2601.21601v1](https://arxiv.org/abs/2601.21601) · [PDF](https://arxiv.org/pdf/2601.21601.pdf)  
**作者**：Hoyeon Chang, Bálint Mucsányi, Seong Joon Oh  

**一句话要点**：挑战线性传播假设，揭示神经网络知识编辑与推理的结构性限制

**关键词**：线性传播假设, 关系代数, 知识编辑, 多跳推理, 张量分解, 神经网络结构

## 3 点简述
- 研究线性传播假设在关系代数操作中的几何限制，聚焦否定、逆和组合操作
- 证明否定和逆操作需张量分解，组合操作因双线性与否定不兼容导致特征图坍缩
- 指出知识编辑失败、逆转诅咒和多跳推理问题可能源于线性传播假设的内在结构限制

## 摘要（原文）

> Neural networks adapt through first-order parameter updates, yet it remains unclear whether such updates preserve logical coherence. We investigate the geometric limits of the Linear Propagation Assumption (LPA), the premise that local updates coherently propagate to logical consequences. To formalize this, we adopt relation algebra and study three core operations on relations: negation flips truth values, converse swaps argument order, and composition chains relations. For negation and converse, we prove that guaranteeing direction-agnostic first-order propagation necessitates a tensor factorization separating entity-pair context from relation content. However, for composition, we identify a fundamental obstruction. We show that composition reduces to conjunction, and prove that any conjunction well-defined on linear features must be bilinear. Since bilinearity is incompatible with negation, this forces the feature map to collapse. These results suggest that failures in knowledge editing, the reversal curse, and multi-hop reasoning may stem from common structural limitations inherent to the LPA.

