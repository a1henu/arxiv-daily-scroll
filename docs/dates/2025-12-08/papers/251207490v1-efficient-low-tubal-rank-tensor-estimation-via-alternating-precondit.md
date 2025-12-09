---
layout: default
title: Efficient Low-Tubal-Rank Tensor Estimation via Alternating Preconditioned Gradient Descent
---

# Efficient Low-Tubal-Rank Tensor Estimation via Alternating Preconditioned Gradient Descent
**arXiv**：[2512.07490v1](https://arxiv.org/abs/2512.07490) · [PDF](https://arxiv.org/pdf/2512.07490.pdf)  
**作者**：Zhiyu Liu, Zhi Han, Yandong Tang, Jun Fan, Yao Wang  

**一句话要点**：提出交替预条件梯度下降算法以解决低管秩张量估计中的过参数化收敛问题

**关键词**：低管秩张量估计, 交替预条件梯度下降, 过参数化收敛, 张量分解, 张量恢复, 线性收敛保证

## 3 点简述
- 核心问题：低管秩张量估计中，传统方法计算成本高，梯度下降在秩过估计时收敛慢或发散
- 方法要点：通过添加预条件项和交替更新因子，加速过参数化设置下的收敛，并建立线性收敛保证
- 实验或效果：理论分析显示算法在线性收敛且收敛率独立于张量条件数，合成数据模拟验证了理论断言

## 摘要（原文）

> The problem of low-tubal-rank tensor estimation is a fundamental task with wide applications across high-dimensional signal processing, machine learning, and image science. Traditional approaches tackle such a problem by performing tensor singular value decomposition, which is computationally expensive and becomes infeasible for large-scale tensors. Recent approaches address this issue by factorizing the tensor into two smaller factor tensors and solving the resulting problem using gradient descent. However, this kind of approach requires an accurate estimate of the tensor rank, and when the rank is overestimated, the convergence of gradient descent and its variants slows down significantly or even diverges. To address this problem, we propose an Alternating Preconditioned Gradient Descent (APGD) algorithm, which accelerates convergence in the over-parameterized setting by adding a preconditioning term to the original gradient and updating these two factors alternately. Based on certain geometric assumptions on the objective function, we establish linear convergence guarantees for more general low-tubal-rank tensor estimation problems. Then we further analyze the specific cases of low-tubal-rank tensor factorization and low-tubal-rank tensor recovery. Our theoretical results show that APGD achieves linear convergence even under over-parameterization, and the convergence rate is independent of the tensor condition number. Extensive simulations on synthetic data are carried out to validate our theoretical assertions.

