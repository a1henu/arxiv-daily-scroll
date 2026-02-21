---
layout: default
title: Quantum Scrambling Born Machine
---

# Quantum Scrambling Born Machine
**arXiv**：[2602.17281v1](https://arxiv.org/abs/2602.17281) · [PDF](https://arxiv.org/pdf/2602.17281.pdf)  
**作者**：Marcin Płodzień  

**一句话要点**：提出量子搅动玻恩机，通过固定纠缠酉算子和单量子比特旋转优化实现量子生成建模。

**关键词**：量子生成建模, 玻恩机, 量子纠缠, 变分哈密顿量, 量子计算应用, 近量子计算

## 3 点简述
- 核心问题：量子生成建模中如何高效利用纠缠资源生成概率分布。
- 方法要点：使用固定纠缠酉算子作为搅动库，仅优化单量子比特旋转参数。
- 实验或效果：在基准分布上，一旦纠缠接近Haar典型，模型学习目标分布，性能与经典模型竞争。

## 摘要（原文）

> Quantum generative modeling, where the Born rule naturally defines probability distributions through measurement of parameterized quantum states, is a promising near-term application of quantum computing. We propose a Quantum Scrambling Born Machine in which a fixed entangling unitary -- acting as a scrambling reservoir -- provides multi-qubit entanglement, while only single-qubit rotations are optimized. We consider three entangling unitaries -- a Haar random unitary and two physically realizable approximations, a finite-depth brickwork random circuit and analog time evolution under nearest-neighbor spin-chain Hamiltonians -- and show that, for the benchmark distributions and system sizes considered, once the entangler produces near-Haar-typical entanglement the model learns the target distribution with weak sensitivity to the scrambler's microscopic origin. Finally, promoting the Hamiltonian couplings to trainable parameters casts the generative task as a variational Hamiltonian problem, with performance competitive with representative classical generative models at matched parameter count.

