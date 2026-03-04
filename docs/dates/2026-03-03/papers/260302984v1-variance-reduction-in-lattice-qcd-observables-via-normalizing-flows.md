---
layout: default
title: Variance reduction in lattice QCD observables via normalizing flows
---

# Variance reduction in lattice QCD observables via normalizing flows
**arXiv**：[2603.02984v1](https://arxiv.org/abs/2603.02984) · [PDF](https://arxiv.org/pdf/2603.02984.pdf)  
**作者**：Ryan Abbott, Denis Boyda, Yang Fu, Daniel C. Hackett, Gurtej Kanwar, Fernando Romero-López, Phiala E. Shanahan, Julian M. Urban  

**一句话要点**：提出基于归一化流的方差缩减方法，用于格点QCD中胶子相关可观测量计算。

**关键词**：格点量子色动力学, 归一化流, 方差缩减, 胶子相关函数, 格点场论, 计算物理

## 3 点简述
- 核心问题：格点场论中胶子相关可观测量计算方差高，影响精度与效率。
- 方法要点：利用归一化流构造无偏、降方差估计器，适用于SU(3)杨-米尔斯理论和两味QCD。
- 实验或效果：方差缩减10-60倍，计算优势显著，且方差缩减近似与格点体积无关。

## 摘要（原文）

> Normalizing flows can be used to construct unbiased, reduced-variance estimators for lattice field theory observables that are defined by a derivative with respect to action parameters. This work implements the approach for observables involving gluonic operator insertions in the SU(3) Yang-Mills theory and two-flavor Quantum Chromodynamics (QCD) in four space-time dimensions. Variance reduction by factors of $10$-$60$ is achieved in glueball correlation functions and in gluonic matrix elements related to hadron structure, with demonstrated computational advantages. The observed variance reduction is found to be approximately independent of the lattice volume, so that volume transfer can be utilized to minimize training costs.

