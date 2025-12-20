---
layout: default
title: Cartesian-nj: Extending e3nn to Irreducible Cartesian Tensor Product and Contracion
---

# Cartesian-nj: Extending e3nn to Irreducible Cartesian Tensor Product and Contracion
**arXiv**：[2512.16882v1](https://arxiv.org/abs/2512.16882) · [PDF](https://arxiv.org/pdf/2512.16882.pdf)  
**作者**：Zemin Xu, Chenyu Wu, Wenbo Xie, Daiqian Xie, P. Hu  

**一句话要点**：提出Cartesian-nj符号以扩展e3nn支持不可约笛卡尔张量积与收缩，并发布cartnn包进行系统比较。

**关键词**：等变机器学习, 不可约笛卡尔张量, 张量积, 原子模拟, e3nn扩展, 模型比较

## 3 点简述
- 核心问题：不可约笛卡尔张量在等变原子机器学习中是否优于球形张量，设计原理是否完备。
- 方法要点：定义Cartesian-3j和Cartesian-nj符号，作为张量耦合系数，支持不可约笛卡尔张量组合。
- 实验或效果：实现Cartesian版MACE、NequIP和Allegro，首次系统比较笛卡尔与球形模型，评估优势条件。

## 摘要（原文）

> Equivariant atomistic machine learning models have brought substantial gains in both extrapolation capability and predictive accuracy. Depending on the basis of the space, two distinct types of irreducible representations are utilized. From architectures built upon spherical tensors (STs) to more recent formulations employing irreducible Cartesian tensors (ICTs), STs have remained dominant owing to their compactness, elegance, and theoretical completeness. Nevertheless, questions have persisted regarding whether ST constructions are the only viable design principle, motivating continued development of Cartesian networks. In this work, we introduce the Cartesian-3j and Cartesian-nj symbol, which serve as direct analogues of the Wigner-3j and Wigner-nj symbol defined for tensor coupling. These coefficients enable the combination of any two ICTs into a new ICT. Building on this foundation, we extend e3nn to support irreducible Cartesian tensor product, and we release the resulting Python package as cartnn. Within this framework, we implement Cartesian counterparts of MACE, NequIP, and Allegro, allowing the first systematic comparison of Cartesian and spherical models to assess whether Cartesian formulations may offer advantages under specific conditions. Using TACE as a representative example, we further examine whether architectures constructed from irreducible Cartesian tensor product and contraction(ICTP and ICTC) are conceptually well-founded in Cartesian space and whether opportunities remain for improving their design.

