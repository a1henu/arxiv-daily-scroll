---
layout: default
title: CrispEdit: Low-Curvature Projections for Scalable Non-Destructive LLM Editing
---

# CrispEdit: Low-Curvature Projections for Scalable Non-Destructive LLM Editing
**arXiv**：[2602.15823v1](https://arxiv.org/abs/2602.15823) · [PDF](https://arxiv.org/pdf/2602.15823.pdf)  
**作者**：Zarif Ikram, Arad Firouzkouhi, Stephen Tu, Mahdi Soltanolkotabi, Paria Rashidinejad  

**一句话要点**：提出CrispEdit算法，通过低曲率投影实现可扩展的非破坏性大语言模型编辑

**关键词**：大语言模型编辑, 能力保持, 约束优化, 低曲率投影, Bregman散度, K-FAC近似

## 3 点简述
- 核心问题：大语言模型编辑中，改变目标行为可能损害模型通用能力，导致代理黑客问题。
- 方法要点：将编辑视为约束优化，利用Bregman散度表达能力约束，通过低曲率子空间投影更新编辑。
- 实验或效果：在标准基准测试中，编辑成功率高，能力退化平均低于1%，优于先前方法。

## 摘要（原文）

> A central challenge in large language model (LLM) editing is capability preservation: methods that successfully change targeted behavior can quietly game the editing proxy and corrupt general capabilities, producing degenerate behaviors reminiscent of proxy/reward hacking. We present CrispEdit, a scalable and principled second-order editing algorithm that treats capability preservation as an explicit constraint, unifying and generalizing several existing editing approaches. CrispEdit formulates editing as constrained optimization and enforces the constraint by projecting edit updates onto the low-curvature subspace of the capability-loss landscape. At the crux of CrispEdit is expressing capability constraint via Bregman divergence, whose quadratic form yields the Gauss-Newton Hessian exactly and even when the base model is not trained to convergence. We make this second-order procedure efficient at the LLM scale using Kronecker-factored approximate curvature (K-FAC) and a novel matrix-free projector that exploits Kronecker structure to avoid constructing massive projection matrices. Across standard model-editing benchmarks, CrispEdit achieves high edit success while keeping capability degradation below 1% on average across datasets, significantly improving over prior editors.

