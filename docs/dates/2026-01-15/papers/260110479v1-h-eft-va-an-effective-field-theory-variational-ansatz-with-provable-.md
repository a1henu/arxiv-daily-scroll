---
layout: default
title: H-EFT-VA: An Effective-Field-Theory Variational Ansatz with Provable Barren Plateau Avoidance
---

# H-EFT-VA: An Effective-Field-Theory Variational Ansatz with Provable Barren Plateau Avoidance
**arXiv**：[2601.10479v1](https://arxiv.org/abs/2601.10479) · [PDF](https://arxiv.org/pdf/2601.10479.pdf)  
**作者**：Eyad I. B Hamid  

**一句话要点**：提出H-EFT-VA变分量子算法架构，通过层次化初始化避免贫瘠高原，保持高纠缠和表达能力。

**关键词**：变分量子算法, 贫瘠高原, 有效场论, 梯度方差, 量子纠缠, 基态保真度

## 3 点简述
- 变分量子算法面临贫瘠高原现象，导致梯度消失和训练困难。
- H-EFT-VA基于有效场论，通过UV截断初始化限制状态探索，理论证明梯度方差有逆多项式下界。
- 实验显示在横向场伊辛和Heisenberg XXZ模型中，能量收敛和基态保真度显著优于标准硬件高效架构。

## 摘要（原文）

> Variational Quantum Algorithms (VQAs) are critically threatened by the Barren Plateau (BP) phenomenon. In this work, we introduce the H-EFT Variational Ansatz (H-EFT-VA), an architecture inspired by Effective Field Theory (EFT). By enforcing a hierarchical "UV-cutoff" on initialization, we theoretically restrict the circuit's state exploration, preventing the formation of approximate unitary 2-designs. We provide a rigorous proof that this localization guarantees an inverse-polynomial lower bound on the gradient variance: $Var[\partial θ] \in Ω(1/poly(N))$. Crucially, unlike approaches that avoid BPs by limiting entanglement, we demonstrate that H-EFT-VA maintains volume-law entanglement and near-Haar purity, ensuring sufficient expressibility for complex quantum states. Extensive benchmarking across 16 experiments -- including Transverse Field Ising and Heisenberg XXZ models -- confirms a 109x improvement in energy convergence and a 10.7x increase in ground-state fidelity over standard Hardware-Efficient Ansatze (HEA), with a statistical significance of $p < 10^{-88}$.

