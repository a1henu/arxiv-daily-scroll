---
layout: default
title: Automatic Generation of Polynomial Symmetry Breaking Constraints
---

# Automatic Generation of Polynomial Symmetry Breaking Constraints
**arXiv**：[2602.08297v1](https://arxiv.org/abs/2602.08297) · [PDF](https://arxiv.org/pdf/2602.08297.pdf)  
**作者**：Madalina Erascu, Johannes Middeke  

**一句话要点**：提出基于代数方法的随机多项式不等式生成，以打破整数规划中的对称性。

**关键词**：整数规划, 对称性打破, 多项式不等式, 代数方法, 符号计算, 0-1装箱问题

## 3 点简述
- 整数规划中的对称性导致冗余搜索，需通过对称性打破约束消除等价解。
- 方法输入任意基多项式和特定置换群，在符号计算软件中生成随机多项式不等式作为打破器。
- 案例研究显示，简单二次打破器能有效减少求解时间，尤其在变量和置换组合较少时。

## 摘要（原文）

> Symmetry in integer programming causes redundant search and is often handled with symmetry breaking constraints that remove as many equivalent solutions as possible. We propose an algebraic method which allows to generate a random family of polynomial inequalities which can be used as symmetry breakers. The method requires as input an arbitrary base polynomial and a group of permutations which is specific to the integer program. The computations can be easily carried out in any major symbolic computation software. In order to test our approach, we describe a case study on near half-capacity 0-1 bin packing instances which exhibit substantial symmetries. We statically generate random quadratic breakers and add them to a baseline integer programming problem which we then solve with Gurobi. It turns out that simple symmetry breakers, especially combining few variables and permutations, most consistently reduce work time.

