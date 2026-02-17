---
layout: default
title: Selective Synchronization Attention
---

# Selective Synchronization Attention
**arXiv**：[2602.14445v1](https://arxiv.org/abs/2602.14445) · [PDF](https://arxiv.org/pdf/2602.14445.pdf)  
**作者**：Hasi Hays  

**一句话要点**：提出选择性同步注意力以替代Transformer自注意力，基于耦合振荡器模型实现高效计算与自然稀疏性。

**关键词**：注意力机制, 振荡器模型, 计算复杂度, 稀疏注意力, 位置编码, Transformer替代

## 3 点简述
- 核心问题：Transformer自注意力计算复杂度高且缺乏生物神经计算基础。
- 方法要点：用Kuramoto模型稳态解推导闭式注意力权重，通过振荡器频率和相位实现同步。
- 实验或效果：OSN块作为Transformer替代，初始化时即显示非均匀耦合模式，增强架构归纳偏置。

## 摘要（原文）

> The Transformer architecture has become the foundation of modern deep learning, yet its core self-attention mechanism suffers from quadratic computational complexity and lacks grounding in biological neural computation. We propose Selective Synchronization Attention (SSA), a novel attention mechanism that replaces the standard dot-product self-attention with a closed-form operator derived from the steady-state solution of the Kuramoto model of coupled oscillators. In SSA, each token is represented as an oscillator characterized by a learnable natural frequency and phase; the synchronization strength between token pairs, determined by a frequency-dependent coupling and phase-locking condition, serves as the attention weight. This formulation provides three key advantages: (i) natural sparsity arising from the phase-locking threshold, whereby tokens with incompatible frequencies automatically receive zero attention weight without explicit masking; (ii) unified positional-semantic encoding through the natural frequency spectrum, eliminating the need for separate positional encodings; and (iii) a single-pass, closed-form computation that avoids iterative ODE integration, with all components (coupling, order parameter, synchronization) derived from the oscillatory framework. We instantiate SSA within the Oscillatory Synchronization Network (OSN), a drop-in replacement for the Transformer block. Analysis of the synchronization matrices reveals non-uniform, head-diverse coupling patterns even at initialization, demonstrating a stronger architectural inductive bias than the approximately uniform attention produced by randomly initialized Transformers.

