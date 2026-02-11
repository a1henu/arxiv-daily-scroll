---
layout: default
title: Empirical Stability Analysis of Kolmogorov-Arnold Networks in Hard-Constrained Recurrent Physics-Informed Discovery
---

# Empirical Stability Analysis of Kolmogorov-Arnold Networks in Hard-Constrained Recurrent Physics-Informed Discovery
**arXiv**：[2602.09988v1](https://arxiv.org/abs/2602.09988) · [PDF](https://arxiv.org/pdf/2602.09988.pdf)  
**作者**：Enzo Nicolas Spotorno, Josafat Leal Filho, Antonio Augusto Medeiros Frohlich  

**一句话要点**：评估KAN在硬约束循环物理信息架构中的稳定性，发现其在振荡系统中存在局限

**关键词**：Kolmogorov-Arnold网络, 硬约束循环物理信息架构, 振荡系统, 稳定性分析, 归纳偏置, 残差流形

## 3 点简述
- 研究Kolmogorov-Arnold网络在硬约束循环物理信息架构中的集成，以评估振荡系统中学习残差流形的保真度
- 通过敏感性分析发现，KAN在小规模单变量多项式残差上表现竞争性，但在深层配置中不稳定且对乘法项失败
- 实验结果表明KAN的加性归纳偏置在状态耦合中受限，为未来混合建模提供初步经验证据

## 摘要（原文）

> We investigate the integration of Kolmogorov-Arnold Networks (KANs) into hard-constrained recurrent physics-informed architectures (HRPINN) to evaluate the fidelity of learned residual manifolds in oscillatory systems. Motivated by the Kolmogorov-Arnold representation theorem and preliminary gray-box results, we hypothesized that KANs would enable efficient recovery of unknown terms compared to MLPs. Through initial sensitivity analysis on configuration sensitivity, parameter scale, and training paradigm, we found that while small KANs are competitive on univariate polynomial residuals (Duffing), they exhibit severe hyperparameter fragility, instability in deeper configurations, and consistent failure on multiplicative terms (Van der Pol), generally outperformed by standard MLPs. These empirical challenges highlight limitations of the additive inductive bias in the original KAN formulation for state coupling and provide preliminary empirical evidence of inductive bias limitations for future hybrid modeling.

