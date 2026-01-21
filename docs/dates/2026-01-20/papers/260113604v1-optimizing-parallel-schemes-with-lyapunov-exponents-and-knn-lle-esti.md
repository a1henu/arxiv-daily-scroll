---
layout: default
title: Optimizing Parallel Schemes with Lyapunov Exponents and kNN-LLE Estimation
---

# Optimizing Parallel Schemes with Lyapunov Exponents and kNN-LLE Estimation
**arXiv**：[2601.13604v1](https://arxiv.org/abs/2601.13604) · [PDF](https://arxiv.org/pdf/2601.13604.pdf)  
**作者**：Mudassir Shams, Andrei Velichko, Bruno Carpentieri  

**一句话要点**：提出基于Lyapunov指数与kNN-LLE估计的统一方法，以优化单参数逆并行求解器的稳定性

**关键词**：逆并行求解器, Lyapunov指数, kNN-LLE估计, 稳定性分析, 非线性系统求根, 自适应参数选择

## 3 点简述
- 核心问题：逆并行求解器在非线性系统求根中可能表现出振荡或混沌等不稳定动态行为
- 方法要点：结合理论分析与kNN驱动的局部最大Lyapunov指数估计，提供实时诊断与参数选择策略
- 实验或效果：实验验证理论稳定性图与经验Lyapunov剖面一致，自适应机制显著提升鲁棒性

## 摘要（原文）

> Inverse parallel schemes remain indispensable tools for computing the roots of nonlinear systems, yet their dynamical behavior can be unexpectedly rich, ranging from strong contraction to oscillatory or chaotic transients depending on the choice of algorithmic parameters and initial states. A unified analytical-data-driven methodology for identifying, measuring, and reducing such instabilities in a family of uni-parametric inverse parallel solvers is presented in this study. On the theoretical side, we derive stability and bifurcation characterizations of the underlying iterative maps, identifying parameter regions associated with periodic or chaotic behavior. On the computational side, we introduce a micro-series pipeline based on kNN-driven estimation of the local largest Lyapunov exponent (LLE), applied to scalar time series derived from solver trajectories. The resulting sliding-window Lyapunov profiles provide fine-grained, real-time diagnostics of contractive or unstable phases and reveal transient behaviors not captured by coarse linearized analysis. Leveraging this correspondence, we introduce a Lyapunov-informed parameter selection strategy that identifies solver settings associated with stable behavior, particularly when the estimated LLE indicates persistent instability. Comprehensive experiments on ensembles of perturbed initial guesses demonstrate close agreement between the theoretical stability diagrams and empirical Lyapunov profiles, and show that the proposed adaptive mechanism significantly improves robustness. The study establishes micro-series Lyapunov analysis as a practical, interpretable tool for constructing self-stabilizing root-finding schemes and opens avenues for extending such diagnostics to higher-dimensional or noise-contaminated problems.

