---
layout: default
title: Closing the Generalization Gap in Parameter-efficient Federated Edge Learning
---

# Closing the Generalization Gap in Parameter-efficient Federated Edge Learning
**arXiv**：[2511.23282v1](https://arxiv.org/abs/2511.23282) · [PDF](https://arxiv.org/pdf/2511.23282.pdf)  
**作者**：Xinnong Du, Zhonghao Lyu, Xiaowen Cao, Chunyang Wen, Shuguang Cui, Jie Xu  

**一句话要点**：提出参数高效的联邦边缘学习框架，通过模型剪枝与客户端选择解决泛化与资源利用问题。

**关键词**：联邦边缘学习, 模型泛化, 参数高效, 模型剪枝, 客户端选择, 系统优化

## 3 点简述
- 核心问题：联邦边缘学习中数据有限、异构及资源受限导致模型泛化差和性能下降。
- 方法要点：结合信息论泛化分析与系统优化，联合优化剪枝率、客户端选择和资源分配。
- 实验或效果：实验显示优于现有基线，验证了泛化感知分析与系统级优化的有效性。

## 摘要（原文）

> Federated edge learning (FEEL) provides a promising foundation for edge artificial intelligence (AI) by enabling collaborative model training while preserving data privacy. However, limited and heterogeneous local datasets, as well as resource-constrained deployment, severely degrade both model generalization and resource utilization, leading to a compromised learning performance. Therefore, we propose a parameter-efficient FEEL framework that jointly leverages model pruning and client selection to tackle such challenges. First, we derive an information-theoretic generalization statement that characterizes the discrepancy between training and testing function losses and embed it into the convergence analysis. It reveals that a larger local generalization statement can undermine the global convergence. Then, we formulate a generalization-aware average squared gradient norm bound minimization problem, by jointly optimizing the pruning ratios, client selection, and communication-computation resources under energy and delay constraints. Despite its non-convexity, the resulting mixed-integer problem is efficiently solved via an alternating optimization algorithm. Extensive experiments demonstrate that the proposed design achieves superior learning performance than state-of-the-art baselines, validating the effectiveness of coupling generalization-aware analysis with system-level optimization for efficient FEEL.

