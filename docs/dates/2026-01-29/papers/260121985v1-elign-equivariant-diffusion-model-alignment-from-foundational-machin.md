---
layout: default
title: Elign: Equivariant Diffusion Model Alignment from Foundational Machine Learning Force Fields
---

# Elign: Equivariant Diffusion Model Alignment from Foundational Machine Learning Force Fields
**arXiv**：[2601.21985v1](https://arxiv.org/abs/2601.21985) · [PDF](https://arxiv.org/pdf/2601.21985.pdf)  
**作者**：Yunyang Li, Lin Huang, Luojia Xia, Wenhe Zhang, Mark Gerstein  

**一句话要点**：提出Elign框架以解决E(3)-等变扩散模型在分子构象生成中的物理偏差问题

**关键词**：分子构象生成, 等变扩散模型, 机器学习力场, 强化学习优化, 物理引导对齐

## 3 点简述
- 核心问题：E(3)-等变扩散模型易复制半经验训练数据偏差，而非捕获高保真哈密顿量的平衡分布。
- 方法要点：使用预训练机器学习力场提供物理信号，并通过FED-GRPO强化学习在训练阶段优化去噪策略。
- 实验或效果：生成构象具有更低DFT能量和力，提升稳定性，推理速度与无引导采样相同。

## 摘要（原文）

> Generative models for 3D molecular conformations must respect Euclidean symmetries and concentrate probability mass on thermodynamically favorable, mechanically stable structures. However, E(3)-equivariant diffusion models often reproduce biases from semi-empirical training data rather than capturing the equilibrium distribution of a high-fidelity Hamiltonian. While physics-based guidance can correct this, it faces two computational bottlenecks: expensive quantum-chemical evaluations (e.g., DFT) and the need to repeat such queries at every sampling step. We present Elign, a post-training framework that amortizes both costs. First, we replace expensive DFT evaluations with a faster, pretrained foundational machine-learning force field (MLFF) to provide physical signals. Second, we eliminate repeated run-time queries by shifting physical steering to the training phase. To achieve the second amortization, we formulate reverse diffusion as a reinforcement learning problem and introduce Force--Energy Disentangled Group Relative Policy Optimization (FED-GRPO) to fine-tune the denoising policy. FED-GRPO includes a potential-based energy reward and a force-based stability reward, which are optimized and group-normalized independently. Experiments show that Elign generates conformations with lower gold-standard DFT energies and forces, while improving stability. Crucially, inference remains as fast as unguided sampling, since no energy evaluations are required during generation.

