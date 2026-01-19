---
layout: default
title: On the Probability of First Success in Differential Evolution: Hazard Identities and Tail Bounds
---

# On the Probability of First Success in Differential Evolution: Hazard Identities and Tail Bounds
**arXiv**：[2601.11499v1](https://arxiv.org/abs/2601.11499) · [PDF](https://arxiv.org/pdf/2601.11499.pdf)  
**作者**：Dimitar Nedanovski, Svetoslav Nenov, Dimitar Pilev  

**一句话要点**：提出条件风险框架分析差分进化首次命中时间，推导生存概率恒等式与尾界

**关键词**：差分进化, 首次命中时间, 条件风险, 生存分析, L-SHADE算法, 尾界分析

## 3 点简述
- 研究差分进化中首次命中时间的概率分布，采用条件风险框架替代传统马尔可夫链或漂移分析
- 为L-SHADE算法构建可检验的见证事件，推导条件风险下界，分离理论常数与经验频率
- 在CEC2017基准上应用Kaplan-Meier生存分析，识别三种经验模式：强聚类成功、近似几何尾和难解案例

## 摘要（原文）

> We study first-hitting times in Differential Evolution (DE) through a conditional hazard frame work. Instead of analyzing convergence via Markov-chain transition kernels or drift arguments, we ex press the survival probability of a measurable target set $A$ as a product of conditional first-hit probabilities (hazards) $p_t=\Prob(E_t\mid\mathcal F_{t-1})$. This yields distribution-free identities for survival and explicit tail bounds whenever deterministic lower bounds on the hazard hold on the survival event.
>   For the L-SHADE algorithm with current-to-$p$best/1 mutation, we construct a checkable algorithmic witness event $\mathcal L_t$ under which the conditional hazard admits an explicit lower bound depending only on sampling rules, population size, and crossover statistics. This separates theoretical constants from empirical event frequencies and explains why worst-case constant-hazard bounds are typically conservative.
>   We complement the theory with a Kaplan--Meier survival analysis on the CEC2017 benchmark suite . Across functions and budgets, we identify three distinct empirical regimes: (i) strongly clustered success, where hitting times concentrate in short bursts; (ii) approximately geometric tails, where a constant-hazard model is accurate; and (iii) intractable cases with no observed hits within the evaluation horizon. The results show that while constant-hazard bounds provide valid tail envelopes, the practical behavior of L-SHADE is governed by burst-like transitions rather than homogeneous per-generati on success probabilities.

