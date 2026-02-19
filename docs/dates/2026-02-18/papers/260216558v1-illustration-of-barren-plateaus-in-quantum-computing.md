---
layout: default
title: Illustration of Barren Plateaus in Quantum Computing
---

# Illustration of Barren Plateaus in Quantum Computing
**arXiv**：[2602.16558v1](https://arxiv.org/abs/2602.16558) · [PDF](https://arxiv.org/pdf/2602.16558.pdf)  
**作者**：Gerhard Stenzel, Tobias Rohe, Michael Kölle, Leo Sünkel, Jonas Stein, Claudia Linnhoff-Popien  

**一句话要点**：揭示参数共享在量子电路中通过欺骗性梯度加剧优化困难，提出检测算法与量化框架。

**关键词**：变分量子电路, 参数共享, 欺骗性梯度, 贫瘠高原, 量子优化, 梯度检测

## 3 点简述
- 研究参数共享在变分量子电路中如何通过欺骗性梯度误导优化器，加剧贫瘠高原现象。
- 通过实验分析，展示参数共享增加梯度幅度和欺骗性比率，导致传统优化器收敛性能下降。
- 引入梯度欺骗性检测算法和量化框架，评估量子电路优化难度，为电路设计提供新见解。

## 摘要（原文）

> Variational Quantum Circuits (VQCs) have emerged as a promising paradigm for quantum machine learning in the NISQ era. While parameter sharing in VQCs can reduce the parameter space dimensionality and potentially mitigate the barren plateau phenomenon, it introduces a complex trade-off that has been largely overlooked. This paper investigates how parameter sharing, despite creating better global optima with fewer parameters, fundamentally alters the optimization landscape through deceptive gradients -- regions where gradient information exists but systematically misleads optimizers away from global optima. Through systematic experimental analysis, we demonstrate that increasing degrees of parameter sharing generate more complex solution landscapes with heightened gradient magnitudes and measurably higher deceptiveness ratios. Our findings reveal that traditional gradient-based optimizers (Adam, SGD) show progressively degraded convergence as parameter sharing increases, with performance heavily dependent on hyperparameter selection. We introduce a novel gradient deceptiveness detection algorithm and a quantitative framework for measuring optimization difficulty in quantum circuits, establishing that while parameter sharing can improve circuit expressivity by orders of magnitude, this comes at the cost of significantly increased landscape deceptiveness. These insights provide important considerations for quantum circuit design in practical applications, highlighting the fundamental mismatch between classical optimization strategies and quantum parameter landscapes shaped by parameter sharing.

