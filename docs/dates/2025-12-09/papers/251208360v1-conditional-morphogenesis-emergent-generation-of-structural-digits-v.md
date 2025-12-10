---
layout: default
title: Conditional Morphogenesis: Emergent Generation of Structural Digits via Neural Cellular Automata
---

# Conditional Morphogenesis: Emergent Generation of Structural Digits via Neural Cellular Automata
**arXiv**：[2512.08360v1](https://arxiv.org/abs/2512.08360) · [PDF](https://arxiv.org/pdf/2512.08360.pdf)  
**作者**：Ali Sakour  

**一句话要点**：提出条件神经细胞自动机以解决类别条件结构生成问题

**关键词**：条件生成, 神经细胞自动机, 结构模式形成, 自组织, 局部规则, 生物启发性

## 3 点简述
- 核心问题：现有神经细胞自动机研究多关注连续纹理合成或单目标恢复，类别条件结构生成挑战未充分探索。
- 方法要点：通过空间广播类向量引导，从通用种子生长出不同拓扑结构，如MNIST数字，保持严格局部性和平移等变性。
- 实验或效果：模型实现稳定收敛，从单像素正确形成数字拓扑，展现出类似生物系统的鲁棒性。

## 摘要（原文）

> Biological systems exhibit remarkable morphogenetic plasticity, where a single genome can encode various specialized cellular structures triggered by local chemical signals. In the domain of Deep Learning, Differentiable Neural Cellular Automata (NCA) have emerged as a paradigm to mimic this self-organization. However, existing NCA research has predominantly focused on continuous texture synthesis or single-target object recovery, leaving the challenge of class-conditional structural generation largely unexplored. In this work, we propose a novel Conditional Neural Cellular Automata (c-NCA) architecture capable of growing distinct topological structures - specifically MNIST digits - from a single generic seed, guided solely by a spatially broadcasted class vector. Unlike traditional generative models (e.g., GANs, VAEs) that rely on global reception fields, our model enforces strict locality and translation equivariance. We demonstrate that by injecting a one-hot condition into the cellular perception field, a single set of local rules can learn to break symmetry and self-assemble into ten distinct geometric attractors. Experimental results show that our c-NCA achieves stable convergence, correctly forming digit topologies from a single pixel, and exhibits robustness characteristic of biological systems. This work bridges the gap between texture-based NCAs and structural pattern formation, offering a lightweight, biologically plausible alternative for conditional generation.

