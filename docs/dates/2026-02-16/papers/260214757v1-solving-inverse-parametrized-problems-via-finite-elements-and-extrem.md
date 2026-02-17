---
layout: default
title: Solving Inverse Parametrized Problems via Finite Elements and Extreme Learning Networks
---

# Solving Inverse Parametrized Problems via Finite Elements and Extreme Learning Networks
**arXiv**：[2602.14757v1](https://arxiv.org/abs/2602.14757) · [PDF](https://arxiv.org/pdf/2602.14757.pdf)  
**作者**：Erik Burman, Mats G. Larson, Karl Larsson, Jonatan Vallin  

**一句话要点**：提出基于有限元与极限学习网络的插值降阶建模框架，用于控制、反问题和不确定性量化中的参数化偏微分方程求解。

**关键词**：降阶建模, 有限元方法, 极限学习机, 反问题求解, 参数化偏微分方程, 误差估计

## 3 点简述
- 针对参数化偏微分方程，开发插值降阶建模框架，结合有限元空间离散与参数近似。
- 在低维参数空间使用经典插值，高维空间采用极限学习机代理，建立误差估计与稳定性分析。
- 应用于定量光声层析反问题，实现计算效率提升且保持精度，验证框架有效性。

## 摘要（原文）

> We develop an interpolation-based reduced-order modeling framework for parameter-dependent partial differential equations arising in control, inverse problems, and uncertainty quantification. The solution is discretized in the physical domain using finite element methods, while the dependence on a finite-dimensional parameter is approximated separately. We establish existence, uniqueness, and regularity of the parametric solution and derive rigorous error estimates that explicitly quantify the interplay between spatial discretization and parameter approximation.
>   In low-dimensional parameter spaces, classical interpolation schemes yield algebraic convergence rates based on Sobolev regularity in the parameter variable. In higher-dimensional parameter spaces, we replace classical interpolation by extreme learning machine (ELM) surrogates and obtain error bounds under explicit approximation and stability assumptions. The proposed framework is applied to inverse problems in quantitative photoacoustic tomography, where we derive potential and parameter reconstruction error estimates and demonstrate substantial computational savings compared to standard approaches, without sacrificing accuracy.

