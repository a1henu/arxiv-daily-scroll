---
layout: default
title: Generalizable Equivariant Diffusion Models for Non-Abelian Lattice Gauge Theory
---

# Generalizable Equivariant Diffusion Models for Non-Abelian Lattice Gauge Theory
**arXiv**：[2601.19552v1](https://arxiv.org/abs/2601.19552) · [PDF](https://arxiv.org/pdf/2601.19552.pdf)  
**作者**：Gert Aarts, Diaa E. Habibi, Andreas Ipp, David I. Müller, Thomas R. Ranner, Lingxiao Wang, Wei Wang, Qianteng Zhu  

**一句话要点**：提出规范等变扩散模型，用于非阿贝尔晶格规范理论的物理建模

**关键词**：规范等变扩散模型, 非阿贝尔晶格规范理论, 晶格规范等变卷积神经网络, Metropolis-adjusted annealed Langevin算法, 物理建模泛化

## 3 点简述
- 核心问题：如何准确建模非阿贝尔晶格规范理论的物理，如二维U(2)和SU(2)规范理论。
- 方法要点：基于晶格规范等变卷积神经网络（L-CNNs），结合Metropolis-adjusted annealed Langevin算法（MAALA），确保局部和全局对称性。
- 实验或效果：在单一蒙特卡洛生成集上训练，模型能泛化到更大反耦合和晶格尺寸，精度损失可忽略，接受率保持较高。

## 摘要（原文）

> We demonstrate that gauge equivariant diffusion models can accurately model the physics of non-Abelian lattice gauge theory using the Metropolis-adjusted annealed Langevin algorithm (MAALA), as exemplified by computations in two-dimensional U(2) and SU(2) gauge theories. Our network architecture is based on lattice gauge equivariant convolutional neural networks (L-CNNs), which respect local and global symmetries on the lattice. Models are trained on a single ensemble generated using a traditional Monte Carlo method. By studying Wilson loops of various size as well as the topological susceptibility, we find that the diffusion approach generalizes remarkably well to larger inverse couplings and lattice sizes with negligible loss of accuracy while retaining moderately high acceptance rates.

