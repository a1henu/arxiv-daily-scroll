---
layout: default
title: Transform-Invariant Generative Ray Path Sampling for Efficient Radio Propagation Modeling
---

# Transform-Invariant Generative Ray Path Sampling for Efficient Radio Propagation Modeling
**arXiv**：[2603.01655v1](https://arxiv.org/abs/2603.01655) · [PDF](https://arxiv.org/pdf/2603.01655.pdf)  
**作者**：Jérome Eertmans, Enrico M. Vitucci, Vittorio Degli-Esposti, Nicola Di Cicco, Laurent Jacques, Claude Oestges  

**一句话要点**：提出基于生成流网络的射线路径采样框架，以高效解决射线追踪计算复杂度高的问题。

**关键词**：射线追踪, 生成流网络, 无线电传播建模, 机器学习辅助框架, 路径采样

## 3 点简述
- 射线追踪在无线电传播建模中计算复杂度呈指数增长，限制大规模或实时应用。
- 采用生成流网络替代穷举搜索，结合经验回放、均匀探索策略和物理掩码确保学习鲁棒性。
- 实验显示速度显著提升，GPU快10倍，CPU快1000倍，同时保持高覆盖精度。

## 摘要（原文）

> Ray tracing has become a standard for accurate radio propagation modeling, but suffers from exponential computational complexity, as the number of candidate paths scales with the number of objects raised to the power of the interaction order. This bottleneck limits its use in large-scale or real-time applications, forcing traditional tools to rely on heuristics to reduce the number of path candidates at the cost of potentially reduced accuracy. To overcome this limitation, we propose a comprehensive machine-learning-assisted framework that replaces exhaustive path searching with intelligent sampling via Generative Flow Networks. Applying such generative models to this domain presents significant challenges, particularly sparse rewards due to the rarity of valid paths, which can lead to convergence failures and trivial solutions when evaluating high-order interactions in complex environments. To ensure robust learning and efficient exploration, our framework incorporates three key architectural components. First, we implement an \emph{experience replay buffer} to capture and retain rare valid paths. Second, we adopt a uniform exploratory policy to improve generalization and prevent the model from overfitting to simple geometries. Third, we apply a physics-based action masking strategy that filters out physically impossible paths before the model even considers them. As demonstrated in our experimental validation, the proposed model achieves substantial speedups over exhaustive search -- up to $10\times$ faster on GPU and $1000\times$ faster on CPU -- while maintaining high coverage accuracy and successfully uncovering complex propagation paths. The complete source code, tests, and tutorial are available at https://github.com/jeertmans/sampling-paths.

