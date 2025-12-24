---
layout: default
title: SynCraft: Guiding Large Language Models to Predict Edit Sequences for Molecular Synthesizability Optimization
---

# SynCraft: Guiding Large Language Models to Predict Edit Sequences for Molecular Synthesizability Optimization
**arXiv**：[2512.20333v1](https://arxiv.org/abs/2512.20333) · [PDF](https://arxiv.org/pdf/2512.20333.pdf)  
**作者**：Junren Li, Luhua Lai  

**一句话要点**：提出SynCraft框架，利用大语言模型预测编辑序列以优化分子可合成性

**关键词**：分子可合成性优化, 大语言模型推理, 结构编辑序列, 化学空间探索, 药物设计

## 3 点简述
- 核心问题：生成式AI产生大量合成不可及的分子，现有方法损害结构新颖性或药效团。
- 方法要点：将可合成性优化重构为结构编辑问题，预测原子级编辑序列而非直接生成SMILES。
- 实验或效果：在基准测试中优于现有方法，成功编辑PLK1抑制剂并挽救RIPK1候选分子。

## 摘要（原文）

> Generative artificial intelligence has revolutionized the exploration of chemical space, yet a critical bottleneck remains that a substantial fraction of generated molecules is synthetically inaccessible. Current solutions, such as post-hoc filtering or projection-based methods, often compromise structural novelty or disrupt key pharmacophores by forcing molecules into pre-defined synthetic templates. Herein, we introduce SynCraft, a reasoning-based framework that reframes synthesizability optimization not as a sequence translation task, but as a precise structural editing problem. Leveraging the emergent reasoning capabilities of Large Language Models, SynCraft navigates the "synthesis cliff" where minimal structural modifications yield significant gains in synthetic feasibility. By predicting executable sequences of atom-level edits rather than generating SMILES strings directly, SynCraft circumvents the syntactic fragility of LLMs while harnessing their chemical intuition. Extensive benchmarks demonstrate that SynCraft outperforms state-of-the-art baselines in generating synthesizable analogs with high structural fidelity. Furthermore, through interaction-aware prompting, SynCraft successfully replicates expert medicinal chemistry intuition in editing PLK1 inhibitors and rescuing high-scoring but previously discarded RIPK1 candidates in previous molecular generation literatures.

