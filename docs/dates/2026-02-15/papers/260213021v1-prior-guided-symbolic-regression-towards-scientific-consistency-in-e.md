---
layout: default
title: Prior-Guided Symbolic Regression: Towards Scientific Consistency in Equation Discovery
---

# Prior-Guided Symbolic Regression: Towards Scientific Consistency in Equation Discovery
**arXiv**：[2602.13021v1](https://arxiv.org/abs/2602.13021) · [PDF](https://arxiv.org/pdf/2602.13021.pdf)  
**作者**：Jing Xiao, Xinhai Chen, Jiaming Peng, Qinglin Wang, Menghan Jia, Zhiquan Lai, Guangping Yu, Dongsheng Li, Tiejun Li, Jie Liu  

**一句话要点**：提出PG-SR框架以解决符号回归中的伪方程陷阱，确保科学一致性

**关键词**：符号回归, 科学一致性, 先验约束, 伪方程陷阱, 泛化保证

## 3 点简述
- 核心问题：现有符号回归方法易陷入伪方程陷阱，拟合数据但违反科学原理
- 方法要点：基于三阶段流程，引入先验约束检查器和PACE机制，逐步引导发现
- 实验或效果：PG-SR在多个领域超越基线，对先验质量、噪声和数据稀缺保持鲁棒

## 摘要（原文）

> Symbolic Regression (SR) aims to discover interpretable equations from observational data, with the potential to reveal underlying principles behind natural phenomena. However, existing approaches often fall into the Pseudo-Equation Trap: producing equations that fit observations well but remain inconsistent with fundamental scientific principles. A key reason is that these approaches are dominated by empirical risk minimization, lacking explicit constraints to ensure scientific consistency. To bridge this gap, we propose PG-SR, a prior-guided SR framework built upon a three-stage pipeline consisting of warm-up, evolution, and refinement. Throughout the pipeline, PG-SR introduces a prior constraint checker that explicitly encodes domain priors as executable constraint programs, and employs a Prior Annealing Constrained Evaluation (PACE) mechanism during the evolution stage to progressively steer discovery toward scientifically consistent regions. Theoretically, we prove that PG-SR reduces the Rademacher complexity of the hypothesis space, yielding tighter generalization bounds and establishing a guarantee against pseudo-equations. Experimentally, PG-SR outperforms state-of-the-art baselines across diverse domains, maintaining robustness to varying prior quality, noisy data, and data scarcity.

