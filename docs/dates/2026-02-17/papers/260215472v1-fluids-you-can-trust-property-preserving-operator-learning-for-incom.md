---
layout: default
title: Fluids You Can Trust: Property-Preserving Operator Learning for Incompressible Flows
---

# Fluids You Can Trust: Property-Preserving Operator Learning for Incompressible Flows
**arXiv**：[2602.15472v1](https://arxiv.org/abs/2602.15472) · [PDF](https://arxiv.org/pdf/2602.15472.pdf)  
**作者**：Ramansh Sharma, Matthew Lowery, Houman Owhadi, Varun Shankar  

**一句话要点**：提出基于核的保性质算子学习方法，用于不可压缩流动的高效代理建模。

**关键词**：算子学习, 不可压缩流动, 核方法, 物理性质保持, 代理模型, Navier-Stokes方程

## 3 点简述
- 传统数值求解器计算成本高，现有神经算子无法精确保持不可压缩性等物理性质。
- 方法通过保性质核基映射输入函数到输出系数，确保预测速度场解析满足物理性质。
- 在2D和3D不可压缩流动问题中，相比神经算子，误差降低达六个数量级，训练快五个数量级。

## 摘要（原文）

> We present a novel property-preserving kernel-based operator learning method for incompressible flows governed by the incompressible Navier-Stokes equations. Traditional numerical solvers incur significant computational costs to respect incompressibility. Operator learning offers efficient surrogate models, but current neural operators fail to exactly enforce physical properties such as incompressibility, periodicity, and turbulence. Our method maps input functions to expansion coefficients of output functions in a property-preserving kernel basis, ensuring that predicted velocity fields analytically and simultaneously preserve the aforementioned physical properties. We evaluate the method on challenging 2D and 3D, laminar and turbulent, incompressible flow problems. Our method achieves up to six orders of magnitude lower relative $\ell_2$ errors upon generalization and trains up to five orders of magnitude faster compared to neural operators. Moreover, while our method enforces incompressibility analytically, neural operators exhibit very large deviations. Our results show that our method provides an accurate and efficient surrogate for incompressible flows.

