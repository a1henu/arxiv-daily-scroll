---
layout: default
title: Comprehensive Robust Dynamic Mode Decomposition from Mode Extraction to Dimensional Reduction
---

# Comprehensive Robust Dynamic Mode Decomposition from Mode Extraction to Dimensional Reduction
**arXiv**：[2601.11116v1](https://arxiv.org/abs/2601.11116) · [PDF](https://arxiv.org/pdf/2601.11116.pdf)  
**作者**：Yuki Nakamura, Shingo Takemoto, Shunsuke Ono  

**一句话要点**：提出综合鲁棒动态模态分解，从模态提取到降维全流程抗混合噪声

**关键词**：动态模态分解, 鲁棒性优化, 凸优化, 降维技术, 噪声处理, 流体动力学

## 3 点简述
- 标准DMD依赖最小二乘估计，在噪声下性能显著下降，现有鲁棒变体不稳定且低维表示不忠实
- 引入基于凸优化的预处理方法去除混合噪声，实现准确稳定模态提取；提出新凸优化降维公式，将鲁棒提取模态与原始噪声观测显式关联
- 在流体动力学数据集上实验，CR-DMD在噪声条件下模态准确性和低维表示保真度优于现有鲁棒DMD方法

## 摘要（原文）

> We propose Comprehensive Robust Dynamic Mode Decomposition (CR-DMD), a novel framework that robustifies the entire DMD process - from mode extraction to dimensional reduction - against mixed noise. Although standard DMD widely used for uncovering spatio-temporal patterns and constructing low-dimensional models of dynamical systems, it suffers from significant performance degradation under noise due to its reliance on least-squares estimation for computing the linear time evolution operator. Existing robust variants typically modify the least-squares formulation, but they remain unstable and fail to ensure faithful low-dimensional representations. First, we introduce a convex optimization-based preprocessing method designed to effectively remove mixed noise, achieving accurate and stable mode extraction. Second, we propose a new convex formulation for dimensional reduction that explicitly links the robustly extracted modes to the original noisy observations, constructing a faithful representation of the original data via a sparse weighted sum of the modes. Both stages are efficiently solved by a preconditioned primal-dual splitting method. Experiments on fluid dynamics datasets demonstrate that CR-DMD consistently outperforms state-of-the-art robust DMD methods in terms of mode accuracy and fidelity of low-dimensional representations under noisy conditions.

