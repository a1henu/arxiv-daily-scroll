---
layout: default
title: Orthogonal Uplift Learning with Permutation-Invariant Representations for Combinatorial Treatments
---

# Orthogonal Uplift Learning with Permutation-Invariant Representations for Combinatorial Treatments
**arXiv**：[2602.19851v1](https://arxiv.org/abs/2602.19851) · [PDF](https://arxiv.org/pdf/2602.19851.pdf)  
**作者**：Xinyan Su, Jiacan Gao, Mingyuan Ma, Xiao Xu, Xinrui Wan, Tianqi Gu, Enyun Yu, Jiecheng Guo, Zhiheng Zhang  

**一句话要点**：提出正交提升学习框架，用于组合治疗的因果效应估计

**关键词**：提升估计, 组合治疗, 因果推断, 正交鲁棒性, 排列不变表示, 低秩模型

## 3 点简述
- 研究组合治疗的提升估计问题，处理策略作为上下文相关动作分布而非单一标签
- 采用排列不变聚合表示策略，并集成到正交化低秩提升模型中，增强鲁棒性和泛化能力
- 在大规模随机平台数据上实验，显示在长尾策略场景下提升准确性和稳定性

## 摘要（原文）

> We study uplift estimation for combinatorial treatments. Uplift measures the pure incremental causal effect of an intervention (e.g., sending a coupon or a marketing message) on user behavior, modeled as a conditional individual treatment effect. Many real-world interventions are combinatorial: a treatment is a policy that specifies context-dependent action distributions rather than a single atomic label. Although recent work considers structured treatments, most methods rely on categorical or opaque encodings, limiting robustness and generalization to rare or newly deployed policies. We propose an uplift estimation framework that aligns treatment representation with causal semantics. Each policy is represented by the mixture it induces over contextaction components and embedded via a permutation-invariant aggregation. This representation is integrated into an orthogonalized low-rank uplift model, extending Robinson-style decompositions to learned, vector-valued treatments. We show that the resulting estimator is expressive for policy-induced causal effects, orthogonally robust to nuisance estimation errors, and stable under small policy perturbations. Experiments on large-scale randomized platform data demonstrate improved uplift accuracy and stability in long-tailed policy regimes

