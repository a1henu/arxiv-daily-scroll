---
layout: default
title: The Inlet Rank Collapse in Implicit Neural Representations: Diagnosis and Unified Remedy
---

# The Inlet Rank Collapse in Implicit Neural Representations: Diagnosis and Unified Remedy
**arXiv**：[2602.01526v1](https://arxiv.org/abs/2602.01526) · [PDF](https://arxiv.org/pdf/2602.01526.pdf)  
**作者**：Jianqiao Zheng, Hemanth Saratchandran, Simon Lucey  

**一句话要点**：提出入口秩塌陷诊断框架与秩扩展初始化，以提升隐式神经表示在有限训练预算下的细节恢复能力。

**关键词**：隐式神经表示, 秩塌陷诊断, NTK分解, 秩扩展初始化, 信号建模, 表达瓶颈

## 3 点简述
- 核心问题：隐式神经表示中低维输入坐标无法跨越高维嵌入空间，导致第一层秩不足，形成表达瓶颈。
- 方法要点：通过层间NTK分解诊断入口秩塌陷，统一解释位置编码、正弦激活和批归一化为秩恢复形式。
- 实验或效果：秩扩展初始化使标准MLP实现高保真重建，无需架构修改或计算开销。

## 摘要（原文）

> Implicit Neural Representations (INRs) have revolutionized continuous signal modeling, yet they struggle to recover fine-grained details within finite training budgets. While empirical techniques, such as positional encoding (PE), sinusoidal activations (SIREN), and batch normalization (BN), effectively mitigate this, their theoretical justifications are predominantly post hoc, focusing on the global NTK spectrum only after modifications are applied. In this work, we reverse this paradigm by introducing a structural diagnostic framework. By performing a layer-wise decomposition of the NTK, we mathematically identify the ``Inlet Rank Collapse'': a phenomenon where the low-dimensional input coordinates fail to span the high-dimensional embedding space, creating a fundamental rank deficiency at the first layer that acts as an expressive bottleneck for the entire network. This framework provides a unified perspective to re-interpret PE, SIREN, and BN as different forms of rank restoration. Guided by this diagnosis, we derive a Rank-Expanding Initialization, a minimalist remedy that ensures the representation rank scales with the layer width without architectural modifications or computational overhead. Our results demonstrate that this principled remedy enables standard MLPs to achieve high-fidelity reconstructions, proving that the key to empowering INRs lies in the structural optimization of the initial rank propagation to effectively populate the latent space.

