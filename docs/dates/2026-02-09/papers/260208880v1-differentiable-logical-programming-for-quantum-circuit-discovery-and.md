---
layout: default
title: Differentiable Logical Programming for Quantum Circuit Discovery and Optimization
---

# Differentiable Logical Programming for Quantum Circuit Discovery and Optimization
**arXiv**：[2602.08880v1](https://arxiv.org/abs/2602.08880) · [PDF](https://arxiv.org/pdf/2602.08880.pdf)  
**作者**：Antonin Sulc  

**一句话要点**：提出可微分逻辑编程框架以解决量子电路设计与优化问题

**关键词**：量子电路设计, 可微分逻辑编程, 神经符号框架, 梯度优化, 硬件适应

## 3 点简述
- 量子电路设计依赖启发式或规则方法，可能次优或缺乏通用性。
- 将电路设计建模为可微分逻辑编程，使用连续开关表示门操作，通过梯度下降优化逻辑公理。
- 在4量子比特QFT发现和133量子比特硬件实验中，分别从候选门中恢复电路并提升保真度59.3个百分点。

## 摘要（原文）

> Designing high-fidelity quantum circuits remains challenging, and current paradigms often depend on heuristic, fixed-ansatz structures or rule-based compilers that can be suboptimal or lack generality. We introduce a neuro-symbolic framework that reframes quantum circuit design as a differentiable logic programming problem. Our model represents a scaffold of potential quantum gates and parameterized operations as a set of learnable, continuous ``truth values'' or ``switches,'' $s \in [0, 1]^N$. These switches are optimized via standard gradient descent to satisfy a user-defined set of differentiable, logical axioms (e.g., correctness, simplicity, robustness). We provide a theoretical formulation bridging continuous logic (via T-norms) and unitary evolution (via geodesic interpolation), while addressing the barren plateau problem through biased initialization. We illustrate the approach on tasks including discovery of a 4-qubit Quantum Fourier Transform (QFT) from a scaffold of 21 candidate gates. We also report a hardware-aware adaptation experiment on the 133-qubit IBM Torino processor, where the method improved fidelity by 59.3 percentage points in a localized routing task while adapting to hardware failures.

