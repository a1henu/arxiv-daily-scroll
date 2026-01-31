---
layout: default
title: Smooth Dynamic Cutoffs for Machine Learning Interatomic Potentials
---

# Smooth Dynamic Cutoffs for Machine Learning Interatomic Potentials
**arXiv**：[2601.21147v1](https://arxiv.org/abs/2601.21147) · [PDF](https://arxiv.org/pdf/2601.21147.pdf)  
**作者**：Kevin Han, Haolin Cong, Bowen Deng, Amir Barati Farimani  

**一句话要点**：提出动态截断半径以解决机器学习原子间势能模型的推理时间和内存瓶颈

**关键词**：机器学习原子间势能模型, 动态截断半径, 分子动力学模拟, 图稀疏化, 推理加速, 内存优化

## 3 点简述
- 机器学习原子间势能模型面临推理时间和内存消耗的瓶颈，阻碍大规模模拟应用
- 首次引入动态截断半径，通过控制每个原子的邻居数诱导原子图稀疏化，减少内存和加速推理
- 在四种先进模型上验证，内存消耗减少2.26倍，推理速度提升2.04倍，精度损失最小

## 摘要（原文）

> Machine learning interatomic potentials (MLIPs) have proven to be wildly useful for molecular dynamics simulations, powering countless drug and materials discovery applications. However, MLIPs face two primary bottlenecks preventing them from reaching realistic simulation scales: inference time and memory consumption. In this work, we address both issues by challenging the long-held belief that the cutoff radius for the MLIP must be held to a fixed, constant value. For the first time, we introduce a dynamic cutoff formulation that still leads to stable, long timescale molecular dynamics simulation. In introducing the dynamic cutoff, we are able to induce sparsity onto the underlying atom graph by targeting a specific number of neighbors per atom, significantly reducing both memory consumption and inference time. We show the effectiveness of a dynamic cutoff by implementing it onto 4 state of the art MLIPs: MACE, Nequip, Orbv3, and TensorNet, leading to 2.26x less memory consumption and 2.04x faster inference time, depending on the model and atomic system. We also perform an extensive error analysis and find that the dynamic cutoff models exhibit minimal accuracy dropoff compared to their fixed cutoff counterparts on both materials and molecular datasets. All model implementations and training code will be fully open sourced.

