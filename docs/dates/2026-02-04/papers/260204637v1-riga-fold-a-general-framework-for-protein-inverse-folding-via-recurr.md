---
layout: default
title: RIGA-Fold: A General Framework for Protein Inverse Folding via Recurrent Interaction and Geometric Awareness
---

# RIGA-Fold: A General Framework for Protein Inverse Folding via Recurrent Interaction and Geometric Awareness
**arXiv**：[2602.04637v1](https://arxiv.org/abs/2602.04637) · [PDF](https://arxiv.org/pdf/2602.04637.pdf)  
**作者**：Sisi Yuan, Jiehuang Chen, Junchuang Cai, Dong Xu, Xueliang Li, Zexuan Zhu, Junkai Ji  

**一句话要点**：提出RIGA-Fold框架，通过循环交互与几何感知解决蛋白质逆折叠中的长程依赖与误差累积问题。

**关键词**：蛋白质逆折叠, 几何感知, 循环交互, 全局上下文桥接, 序列恢复, 结构一致性

## 3 点简述
- 核心问题：现有GNN方法因受限感受野和单次推理范式，导致长程依赖缺失和误差累积。
- 方法要点：结合几何注意力更新模块和全局上下文桥接，实现SE(3)不变编码与动态全局信息注入。
- 实验或效果：在CATH 4.2等基准测试中，RIGA-Fold*在序列恢复和结构一致性上显著优于现有方法。

## 摘要（原文）

> Protein inverse folding, the task of predicting amino acid sequences for desired structures, is pivotal for de novo protein design. However, existing GNN-based methods typically suffer from restricted receptive fields that miss long-range dependencies and a "single-pass" inference paradigm that leads to error accumulation. To address these bottlenecks, we propose RIGA-Fold, a framework that synergizes Recurrent Interaction with Geometric Awareness. At the micro-level, we introduce a Geometric Attention Update (GAU) module where edge features explicitly serve as attention keys, ensuring strictly SE(3)-invariant local encoding. At the macro-level, we design an attention-based Global Context Bridge that acts as a soft gating mechanism to dynamically inject global topological information. Furthermore, to bridge the gap between structural and sequence modalities, we introduce an enhanced variant, RIGA-Fold*, which integrates trainable geometric features with frozen evolutionary priors from ESM-2 and ESM-IF via a dual-stream architecture. Finally, a biologically inspired ``predict-recycle-refine'' strategy is implemented to iteratively denoise sequence distributions. Extensive experiments on CATH 4.2, TS50, and TS500 benchmarks demonstrate that our geometric framework is highly competitive, while RIGA-Fold* significantly outperforms state-of-the-art baselines in both sequence recovery and structural consistency.

