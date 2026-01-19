---
layout: default
title: Constant Metric Scaling in Riemannian Computation
---

# Constant Metric Scaling in Riemannian Computation
**arXiv**：[2601.10992v1](https://arxiv.org/abs/2601.10992) · [PDF](https://arxiv.org/pdf/2601.10992.pdf)  
**作者**：Kisung You  

**一句话要点**：澄清黎曼计算中常数度量缩放的影响，区分变化与不变几何量。

**关键词**：黎曼几何, 度量缩放, 黎曼优化, 几何不变性, 计算数学

## 3 点简述
- 核心问题：常数度量缩放常被误解为改变曲率或流形结构，需明确其实际影响。
- 方法要点：分析缩放后变化的量（如距离、梯度大小）和不变的几何对象（如测地线、平行移动）。
- 实验或效果：在黎曼优化中，缩放可解释为步长调整，而不改变底层几何，提升计算清晰度。

## 摘要（原文）

> Constant rescaling of a Riemannian metric appears in many computational settings, often through a global scale parameter that is introduced either explicitly or implicitly. Although this operation is elementary, its consequences are not always made clear in practice and may be confused with changes in curvature, manifold structure, or coordinate representation. In this note we provide a short, self-contained account of constant metric scaling on arbitrary Riemannian manifolds. We distinguish between quantities that change under such a scaling, including norms, distances, volume elements, and gradient magnitudes, and geometric objects that remain invariant, such as the Levi--Civita connection, geodesics, exponential and logarithmic maps, and parallel transport. We also discuss implications for Riemannian optimization, where constant metric scaling can often be interpreted as a global rescaling of step sizes rather than a modification of the underlying geometry. The goal of this note is purely expository and is intended to clarify how a global metric scale parameter can be introduced in Riemannian computation without altering the geometric structures on which these methods rely.

