---
layout: default
title: Optimal Anytime-Valid Tests for Composite Nulls
---

# Optimal Anytime-Valid Tests for Composite Nulls
**arXiv**：[2512.20039v1](https://arxiv.org/abs/2512.20039) · [PDF](https://arxiv.org/pdf/2512.20039.pdf)  
**作者**：Shubhanshu Shekhar  

**一句话要点**：提出基于e过程的任意时间有效检验，以匹配复合零假设的最优下界。

**关键词**：复合假设检验, 任意时间有效测试, e过程, KL散度下界, Donsker-Varadhan表示, 渐近最优性

## 3 点简述
- 研究复合零假设下最优水平α幂一检验的设计问题，关注任意时间有效测试。
- 在有限字母表情况下，基于通用e过程的检验被证明是渐近最优的，利用Donsker-Varadhan鞍点表示。
- 扩展至任意字母表，提出基于经验鞍点解的检验方法，验证了紧凑凸零假设和Hölder平滑密度模型下的最优性。

## 摘要（原文）

> We consider the problem of designing optimal level-$α$ power-one tests for composite nulls. Given a parameter $α\in (0,1)$ and a stream of $\mathcal{X}$-valued observations $\{X_n: n \geq 1\} \overset{i.i.d.}{\sim} P$, the goal is to design a level-$α$ power-one test $τ_α$ for the null $H_0: P \in \mathcal{P}_0 \subset \mathcal{P}(\mathcal{X})$. Prior works have shown that any such $τ_α$ must satisfy $\mathbb{E}_P[τ_α] \geq \tfrac{\log(1/α)}{γ^*(P, \mathcal{P}_0)}$, where $γ^*(P, \mathcal{P}_0)$ is the so-called $\mathrm{KL}_{\inf}$ or minimum divergence of $P$ to the null class. In this paper, our objective is to develop and analyze constructive schemes that match this lower bound as $α\downarrow 0$.
>   We first consider the finite-alphabet case~($\|\mathcal{X}\| = m < \infty$), and show that a test based on \emph{universal} $e$-process~(formed by the ratio of a universal predictor and the running null MLE) is optimal in the above sense. The proof relies on a Donsker-Varadhan~(DV) based saddle-point representation of $\mathrm{KL}_{\inf}$, and an application of Sion's minimax theorem. This characterization motivates a general method for arbitrary $\mathcal{X}$: construct an $e$-process based on the empirical solutions to the saddle-point representation over a sufficiently rich class of test functions. We give sufficient conditions for the optimality of this test for compact convex nulls, and verify them for Hölder smooth density models. We end the paper with a discussion on the computational aspects of implementing our proposed tests in some practical settings.

