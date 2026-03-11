---
layout: default
title: Mousse: Rectifying the Geometry of Muon with Curvature-Aware Preconditioning
---

# Mousse: Rectifying the Geometry of Muon with Curvature-Aware Preconditioning
**arXiv**：[2603.09697v1](https://arxiv.org/abs/2603.09697) · [PDF](https://arxiv.org/pdf/2603.09697.pdf)  
**作者**：Yechen Zhang, Shuhao Xing, Junhao Huang, Kai Lv, Yunhua Zhou, Xipeng Qiu, Qipeng Guo, Kai Chen  

**一句话要点**：提出Mousse优化器，通过曲率感知预条件解决Muon在深度神经网络中的几何约束问题。

**关键词**：优化算法, 谱方法, 预条件, 深度神经网络, 语言模型训练

## 3 点简述
- Muon优化器假设各向同性优化景观，在深度神经网络中可能导致高曲率方向不稳定和平坦方向进展受限。
- Mousse结合谱方法的结构稳定性和二阶预条件的几何适应性，在由Shampoo统计诱导的白化坐标系中操作。
- 在160M至800M参数的语言模型上，Mousse比Muon减少约12%训练步数，计算开销可忽略。

## 摘要（原文）

> Recent advances in spectral optimization, notably Muon, have demonstrated that constraining update steps to the Stiefel manifold can significantly accelerate training and improve generalization. However, Muon implicitly assumes an isotropic optimization landscape, enforcing a uniform spectral update norm across all eigen-directions. We argue that this "egalitarian" constraint is suboptimal for Deep Neural Networks, where the curvature spectrum is known to be highly heavy-tailed and ill-conditioned. In such landscapes, Muon risks amplifying instabilities in high-curvature directions while limiting necessary progress in flat directions. In this work, we propose \textbf{Mousse} (\textbf{M}uon \textbf{O}ptimization \textbf{U}tilizing \textbf{S}hampoo's \textbf{S}tructural \textbf{E}stimation), a novel optimizer that reconciles the structural stability of spectral methods with the geometric adaptivity of second-order preconditioning. Instead of applying Newton-Schulz orthogonalization directly to the momentum matrix, Mousse operates in a whitened coordinate system induced by Kronecker-factored statistics (derived from Shampoo). Mathematically, we formulate Mousse as the solution to a spectral steepest descent problem constrained by an anisotropic trust region, where the optimal update is derived via the polar decomposition of the whitened gradient. Empirical results across language models ranging from 160M to 800M parameters demonstrate that Mousse consistently outperforms Muon, achieving around $\sim$12\% reduction in training steps with negligible computational overhead.

