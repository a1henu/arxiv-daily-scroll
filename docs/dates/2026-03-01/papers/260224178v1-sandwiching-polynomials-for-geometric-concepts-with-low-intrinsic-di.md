---
layout: default
title: Sandwiching Polynomials for Geometric Concepts with Low Intrinsic Dimension
---

# Sandwiching Polynomials for Geometric Concepts with Low Intrinsic Dimension
**arXiv**：[2602.24178v1](https://arxiv.org/abs/2602.24178) · [PDF](https://arxiv.org/pdf/2602.24178.pdf)  
**作者**：Adam R. Klivans, Konstantinos Stavropoulos, Arsen Vasilyan  

**一句话要点**：提出低度三明治多项式构造方法，改进低维几何概念在分布学习中的近似度界

**关键词**：三明治多项式, 低维几何概念, 高斯分布, 多项式阈值函数, 分布学习, 逼近理论

## 3 点简述
- 核心问题：低度三明治多项式在分布偏移等学习场景中近似复杂函数类时度界过高
- 方法要点：利用目标函数边界光滑性直接构造Lipschitz函数，简化证明并应用高维逼近理论
- 实验或效果：对高斯分布下k个半空间函数，度界从指数级改进为多项式级，提升显著

## 摘要（原文）

> Recent work has shown the surprising power of low-degree sandwiching polynomial approximators in the context of challenging learning settings such as learning with distribution shift, testable learning, and learning with contamination. A pair of sandwiching polynomials approximate a target function in expectation while also providing pointwise upper and lower bounds on the function's values. In this paper, we give a new method for constructing low-degree sandwiching polynomials that yield greatly improved degree bounds for several fundamental function classes and marginal distributions. In particular, we obtain degree $\mathrm{poly}(k)$ sandwiching polynomials for functions of $k$ halfspaces under the Gaussian distribution, improving exponentially over the prior $2^{O(k)}$ bound. More broadly, our approach applies to function classes that are low-dimensional and have smooth boundary.
>   In contrast to prior work, our proof is relatively simple and directly uses the smoothness of the target function's boundary to construct sandwiching Lipschitz functions, which are amenable to results from high-dimensional approximation theory. For low-dimensional polynomial threshold functions (PTFs) with respect to Gaussians, we obtain doubly exponential improvements without applying the FT-mollification method of Kane used in the best previous result.

