---
layout: default
title: Implementing the First-Order Logic of Here and There
---

# Implementing the First-Order Logic of Here and There
**arXiv**：[2601.03848v1](https://arxiv.org/abs/2601.03848) · [PDF](https://arxiv.org/pdf/2601.03848.pdf)  
**作者**：Jens Otten, Torsten Schaub  

**一句话要点**：提出基于序列演算和嵌入方法的自动定理证明器，用于一阶此处与彼处逻辑。

**关键词**：一阶此处与彼处逻辑, 自动定理证明, 序列演算, 直觉逻辑嵌入, Skolem化, 基准评估

## 3 点简述
- 核心问题：为一阶此处与彼处逻辑开发高效的自动定理证明器。
- 方法要点：结合原生序列演算和嵌入到直觉逻辑的优化策略，如自由变量和Skolem化。
- 实验或效果：在大规模一阶公式基准集上评估，为更高效证明器奠定基础。

## 摘要（原文）

> We present automated theorem provers for the first-order logic of here and there (HT). They are based on a native sequent calculus for the logic of HT and an axiomatic embedding of the logic of HT into intuitionistic logic. The analytic proof search in the sequent calculus is optimized by using free variables and skolemization. The embedding is used in combination with sequent, tableau and connection calculi for intuitionistic first-order logic. All provers are evaluated on a large benchmark set of first-order formulas, providing a foundation for the development of more efficient HT provers.

