---
layout: default
title: KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver
---

# KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver
**arXiv**：[2601.11097v1](https://arxiv.org/abs/2601.11097) · [PDF](https://arxiv.org/pdf/2601.11097.pdf)  
**作者**：Rushikesh Handal, Masanori Hirano  

**一句话要点**：提出KANHedge以改进高维期权对冲性能，基于KAN的BSDE求解器

**关键词**：高维期权定价, BSDE求解器, Kolmogorov-Arnold网络, 期权对冲, 风险控制, 金融衍生品

## 3 点简述
- 高维期权定价与对冲面临维度诅咒挑战，传统PDE方法效率低
- 引入KANHedge，利用KAN的可学习B样条激活函数增强导数近似能力
- 实验显示KANHedge在定价精度相当下，显著降低对冲成本并提升风险控制

## 摘要（原文）

> High-dimensional option pricing and hedging present significant challenges in quantitative finance, where traditional PDE-based methods struggle with the curse of dimensionality. The BSDE framework offers a computationally efficient alternative to PDE-based methods, and recently proposed deep BSDE solvers, generally utilizing conventional Multi-Layer Perceptrons (MLPs), build upon this framework to provide a scalable alternative to numerical BSDE solvers. In this research, we show that although such MLP-based deep BSDEs demonstrate promising results in option pricing, there remains room for improvement regarding hedging performance. To address this issue, we introduce KANHedge, a novel BSDE-based hedger that leverages Kolmogorov-Arnold Networks (KANs) within the BSDE framework. Unlike conventional MLP approaches that use fixed activation functions, KANs employ learnable B-spline activation functions that provide enhanced function approximation capabilities for continuous derivatives. We comprehensively evaluate KANHedge on both European and American basket options across multiple dimensions and market conditions. Our experimental results demonstrate that while KANHedge and MLP achieve comparable pricing accuracy, KANHedge provides improved hedging performance. Specifically, KANHedge achieves considerable reductions in hedging cost metrics, demonstrating enhanced risk control capabilities.

