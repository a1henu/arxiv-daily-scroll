---
layout: default
title: Total Variation Rates for Riemannian Flow Matching
---

# Total Variation Rates for Riemannian Flow Matching
**arXiv**：[2602.05174v1](https://arxiv.org/abs/2602.05174) · [PDF](https://arxiv.org/pdf/2602.05174.pdf)  
**作者**：Yunrui Guan, Krishnakumar Balasubramanian, Shiqian Ma  

**一句话要点**：提出黎曼流匹配的总变差收敛分析，分离离散化与学习误差

**关键词**：黎曼流匹配, 总变差收敛, 流形生成模型, 欧拉离散化, 平行传输, 曲率分析

## 3 点简述
- 核心问题：黎曼流匹配采样器在流形上的总变差收敛性分析
- 方法要点：基于微分不等式控制向量场失配和参考流得分，考虑平行传输和曲率
- 实验或效果：在超球面和SPD流形上获得显式多项式迭代复杂度

## 摘要（原文）

> Riemannian flow matching (RFM) extends flow-based generative modeling to data supported on manifolds by learning a time-dependent tangent vector field whose flow-ODE transports a simple base distribution to the data law. We develop a nonasymptotic Total Variation (TV) convergence analysis for RFM samplers that use a learned vector field together with Euler discretization on manifolds. Our key technical ingredient is a differential inequality governing the evolution of TV between two manifold ODE flows, which expresses the time-derivative of TV through the divergence of the vector-field mismatch and the score of the reference flow; controlling these terms requires establishing new bounds that explicitly account for parallel transport and curvature. Under smoothness assumptions on the population flow-matching field and either uniform (compact manifolds) or mean-square (Hadamard manifolds) approximation guarantees for the learned field, we obtain explicit bounds of the form $\mathrm{TV}\le C_{\mathrm{Lip}}\,h + C_{\varepsilon}\,\varepsilon$ (with an additional higher-order $\varepsilon^2$ term on compact manifolds), cleanly separating numerical discretization and learning errors. Here, $h$ is the step-size and $\varepsilon$ is the target accuracy. Instantiations yield \emph{explicit} polynomial iteration complexities on the hypersphere $S^d$, and on the SPD$(n)$ manifolds under mild moment conditions.

