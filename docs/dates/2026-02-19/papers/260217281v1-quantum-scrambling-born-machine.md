---
layout: default
title: Quantum Scrambling Born Machine
---

# Quantum Scrambling Born Machine
**arXiv**：[2602.17281v1](https://arxiv.org/abs/2602.17281) · [PDF](https://arxiv.org/pdf/2602.17281.pdf)  
**作者**：Marcin Płodzień  

**一句话要点**：提出量子搅动玻恩机，通过固定纠缠酉算子和单量子比特旋转优化实现量子生成建模。

**关键词**：量子生成建模, 玻恩规则, 纠缠酉算子, 单量子比特旋转, 变分哈密顿问题

## 3 点简述
- 量子生成建模利用玻恩规则通过测量参数化量子态定义概率分布，是近期量子计算的应用方向。
- 模型采用固定纠缠酉算子作为搅动库提供多量子比特纠缠，仅优化单量子比特旋转，简化训练过程。
- 实验表明，当纠缠器产生接近Haar典型纠缠时，模型能学习目标分布，性能与经典生成模型竞争。

## 摘要（原文）

> Quantum generative modeling, where the Born rule naturally defines probability distributions through measurement of parameterized quantum states, is a promising near-term application of quantum computing. We propose a Quantum Scrambling Born Machine in which a fixed entangling unitary -- acting as a scrambling reservoir -- provides multi-qubit entanglement, while only single-qubit rotations are optimized. We consider three entangling unitaries -- a Haar random unitary and two physically realizable approximations, a finite-depth brickwork random circuit and analog time evolution under nearest-neighbor spin-chain Hamiltonians -- and show that, for the benchmark distributions and system sizes considered, once the entangler produces near-Haar-typical entanglement the model learns the target distribution with weak sensitivity to the scrambler's microscopic origin. Finally, promoting the Hamiltonian couplings to trainable parameters casts the generative task as a variational Hamiltonian problem, with performance competitive with representative classical generative models at matched parameter count.

