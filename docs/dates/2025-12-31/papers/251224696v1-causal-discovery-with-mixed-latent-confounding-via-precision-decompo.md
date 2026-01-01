---
layout: default
title: Causal Discovery with Mixed Latent Confounding via Precision Decomposition
---

# Causal Discovery with Mixed Latent Confounding via Precision Decomposition
**arXiv**：[2512.24696v1](https://arxiv.org/abs/2512.24696) · [PDF](https://arxiv.org/pdf/2512.24696.pdf)  
**作者**：Amir Asiaee, Samhita Pal, James O'quinn, James P. Long  

**一句话要点**：提出DCL-DECOR方法以解决混合潜在混杂下的因果发现

**关键词**：因果发现, 混合潜在混杂, 精度矩阵分解, DAG学习, 线性高斯系统, 可识别性分析

## 3 点简述
- 研究线性高斯系统中混合潜在混杂的因果发现问题，其中全局和局部混杂并存
- 方法通过精度矩阵分解分离全局混杂效应，再应用相关噪声DAG学习恢复有向边
- 合成实验显示在全局混杂强度变化下，相比直接应用相关噪声DAG学习有改进

## 摘要（原文）

> We study causal discovery from observational data in linear Gaussian systems affected by \emph{mixed latent confounding}, where some unobserved factors act broadly across many variables while others influence only small subsets. This setting is common in practice and poses a challenge for existing methods: differentiable and score-based DAG learners can misinterpret global latent effects as causal edges, while latent-variable graphical models recover only undirected structure.
>   We propose \textsc{DCL-DECOR}, a modular, precision-led pipeline that separates these roles. The method first isolates pervasive latent effects by decomposing the observed precision matrix into a structured component and a low-rank component. The structured component corresponds to the conditional distribution after accounting for pervasive confounders and retains only local dependence induced by the causal graph and localized confounding. A correlated-noise DAG learner is then applied to this deconfounded representation to recover directed edges while modeling remaining structured error correlations, followed by a simple reconciliation step to enforce bow-freeness.
>   We provide identifiability results that characterize the recoverable causal target under mixed confounding and show how the overall problem reduces to well-studied subproblems with modular guarantees. Synthetic experiments that vary the strength and dimensionality of pervasive confounding demonstrate consistent improvements in directed edge recovery over applying correlated-noise DAG learning directly to the confounded data.

