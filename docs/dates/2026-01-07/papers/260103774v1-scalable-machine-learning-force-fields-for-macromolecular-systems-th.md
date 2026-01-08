---
layout: default
title: Scalable Machine Learning Force Fields for Macromolecular Systems Through Long-Range Aware Message Passing
---

# Scalable Machine Learning Force Fields for Macromolecular Systems Through Long-Range Aware Message Passing
**arXiv**：[2601.03774v1](https://arxiv.org/abs/2601.03774) · [PDF](https://arxiv.org/pdf/2601.03774.pdf)  
**作者**：Chu Wang, Lin Huang, Xinran Wei, Tao Qin, Arthur Jiang, Lixue Cheng, Jia Zhang  

**一句话要点**：提出E2Former-LSR以解决大分子系统中长程相互作用导致的力场预测误差问题

**关键词**：机器学习力场, 长程相互作用, 等变变换器, 大分子系统, 分子动力学模拟

## 3 点简述
- 核心问题：传统机器学习力场依赖固定截断架构，在大分子系统中因长程相互作用导致误差随系统规模单调增加
- 方法要点：引入E2Former-LSR，一种等变变换器，通过长程注意力块显式整合长程相互作用
- 实验或效果：在MolLR25基准上验证，E2Former-LSR实现稳定误差缩放、捕获非共价衰减的优越保真度，并比纯局部模型提速达30%

## 摘要（原文）

> Machine learning force fields (MLFFs) have revolutionized molecular simulations by providing quantum mechanical accuracy at the speed of molecular mechanical computations. However, a fundamental reliance of these models on fixed-cutoff architectures limits their applicability to macromolecular systems where long-range interactions dominate. We demonstrate that this locality constraint causes force prediction errors to scale monotonically with system size, revealing a critical architectural bottleneck. To overcome this, we establish the systematically designed MolLR25 ({Mol}ecules with {L}ong-{R}ange effect) benchmark up to 1200 atoms, generated using high-fidelity DFT, and introduce E2Former-LSR, an equivariant transformer that explicitly integrates long-range attention blocks. E2Former-LSR exhibits stable error scaling, achieves superior fidelity in capturing non-covalent decay, and maintains precision on complex protein conformations. Crucially, its efficient design provides up to 30% speedup compared to purely local models. This work validates the necessity of non-local architectures for generalizable MLFFs, enabling high-fidelity molecular dynamics for large-scale chemical and biological systems.

