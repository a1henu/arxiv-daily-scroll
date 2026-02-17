---
layout: default
title: Constrained and Composite Sampling via Proximal Sampler
---

# Constrained and Composite Sampling via Proximal Sampler
**arXiv**：[2602.14478v1](https://arxiv.org/abs/2602.14478) · [PDF](https://arxiv.org/pdf/2602.14478.pdf)  
**作者**：Thanh Dang, Jiaming Liang  

**一句话要点**：提出基于近端采样器的约束与复合采样方法，利用提升变换减少对约束集几何的依赖。

**关键词**：对数凹采样, 约束采样, 复合采样, 近端采样器, 提升变换, 混合时间分析

## 3 点简述
- 研究对数凹分布采样问题：约束采样（目标分布定义在凸集上）和复合采样（目标分布为两个凸函数之和）。
- 通过提升变换将约束采样转化为高维均匀分布采样，使用近端采样器实现，仅需分离和次梯度预言机，避免投影或障碍函数。
- 将复合采样通过双重提升变换转化为约束采样，利用不同预言机组合构建分离预言机，并建立混合时间界限于Rényi和χ²散度。

## 摘要（原文）

> We study two log-concave sampling problems: constrained sampling and composite sampling. First, we consider sampling from a target distribution with density proportional to $\exp(-f(x))$ supported on a convex set $K \subset \mathbb{R}^d$, where $f$ is convex. The main challenge is enforcing feasibility without degrading mixing. Using an epigraph transformation, we reduce this task to sampling from a nearly uniform distribution over a lifted convex set in $\mathbb{R}^{d+1}$. We then solve the lifted problem using a proximal sampler. Assuming only a separation oracle for $K$ and a subgradient oracle for $f$, we develop an implementation of the proximal sampler based on the cutting-plane method and rejection sampling. Unlike existing constrained samplers that rely on projection, reflection, barrier functions, or mirror maps, our approach enforces feasibility using only minimal oracle access, resulting in a practical and unbiased sampler without knowing the geometry of the constraint set.
>   Second, we study composite sampling, where the target is proportional to $\exp(-f(x)-h(x))$ with closed and convex $f$ and $h$. This composite structure is standard in Bayesian inference with $f$ modeling data fidelity and $h$ encoding prior information. We reduce composite sampling via an epigraph lifting of $h$ to constrained sampling in $\mathbb{R}^{d+1}$, which allows direct application of the constrained sampling algorithm developed in the first part. This reduction results in a double epigraph lifting formulation in $\mathbb{R}^{d+2}$, on which we apply a proximal sampler. By keeping $f$ and $h$ separate, we further demonstrate how different combinations of oracle access (such as subgradient and proximal) can be leveraged to construct separation oracles for the lifted problem. For both sampling problems, we establish mixing time bounds measured in Rényi and $χ^2$ divergences.

