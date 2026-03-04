---
layout: default
title: cuNRTO: GPU-Accelerated Nonlinear Robust Trajectory Optimization
---

# cuNRTO: GPU-Accelerated Nonlinear Robust Trajectory Optimization
**arXiv**：[2603.02642v1](https://arxiv.org/abs/2603.02642) · [PDF](https://arxiv.org/pdf/2603.02642.pdf)  
**作者**：Jiawei Wang, Arshiya Taj Abdul, Evangelos A. Theodorou  

**一句话要点**：提出cuNRTO框架，通过GPU加速非线性鲁棒轨迹优化以应对不确定性下的计算挑战。

**关键词**：鲁棒轨迹优化, GPU加速, 二阶锥规划, CUDA实现, 并行计算, 自主系统

## 3 点简述
- 核心问题：鲁棒轨迹优化中大规模二阶锥规划约束导致计算成本高昂。
- 方法要点：引入NRTO-DR和NRTO-FullADMM架构，利用Douglas-Rachford分裂和ADMM方法并行化求解。
- 实验或效果：在单轮车、四旋翼和Franka机械臂模型上验证，实现最高139.6倍加速。

## 摘要（原文）

> Robust trajectory optimization enables autonomous systems to operate safely under uncertainty by computing control policies that satisfy the constraints for all bounded disturbances. However, these problems often lead to large Second Order Conic Programming (SOCP) constraints, which are computationally expensive. In this work, we propose the CUDA Nonlinear Robust Trajectory Optimization (cuNRTO) framework by introducing two dynamic optimization architectures that have direct application to robust decision-making and are implemented on CUDA. The first architecture, NRTO-DR, leverages the Douglas-Rachford (DR) splitting method to solve the SOCP inner subproblems of NRTO, thereby significantly reducing the computational burden through parallel SOCP projections and sparse direct solves. The second architecture, NRTO-FullADMM, is a novel variant that further exploits the problem structure to improve scalability using the Alternating Direction Method of Multipliers (ADMM). Finally, we provide GPU implementation of the proposed methodologies using custom CUDA kernels for SOC projection steps and cuBLAS GEMM chains for feedback gain updates. We validate the performance of cuNRTO through simulated experiments on unicycle, quadcopter, and Franka manipulator models, demonstrating speedup up to 139.6$\times$.

