---
layout: default
title: Shallow-circuit Supervised Learning on a Quantum Processor
---

# Shallow-circuit Supervised Learning on a Quantum Processor
**arXiv**：[2601.03235v1](https://arxiv.org/abs/2601.03235) · [PDF](https://arxiv.org/pdf/2601.03235.pdf)  
**作者**：Luca Candelori, Swarnadeep Majumder, Antonio Mezzacapo, Javier Robledo Moreno, Kharen Musaelian, Santhanam Nagarajan, Sunil Pinnamaneni, Kunal Sharma, Dario Villani  

**一句话要点**：提出基于线性哈密顿量的浅层电路监督学习方法，以解决量子机器学习中的数据加载和训练难题。

**关键词**：量子机器学习, 哈密顿量学习, 浅层量子电路, 数据表示, 近端量子硬件, 监督学习

## 3 点简述
- 核心问题：量子机器学习面临经典数据加载成本高和近端硬件算法训练性差等障碍。
- 方法要点：使用k-局部哈密顿量的基态问题紧凑表示数据，通过样本基Krylov量子对角化计算低能态。
- 实验或效果：在IBM Heron量子处理器上使用多达50量子位验证了方法的有效性和可扩展性。

## 摘要（原文）

> Quantum computing has long promised transformative advances in data analysis, yet practical quantum machine learning has remained elusive due to fundamental obstacles such as a steep quantum cost for the loading of classical data and poor trainability of many quantum machine learning algorithms designed for near-term quantum hardware. In this work, we show that one can overcome these obstacles by using a linear Hamiltonian-based machine learning method which provides a compact quantum representation of classical data via ground state problems for k-local Hamiltonians. We use the recent sample-based Krylov quantum diagonalization method to compute low-energy states of the data Hamiltonians, whose parameters are trained to express classical datasets through local gradients. We demonstrate the efficacy and scalability of the methods by performing experiments on benchmark datasets using up to 50 qubits of an IBM Heron quantum processor.

