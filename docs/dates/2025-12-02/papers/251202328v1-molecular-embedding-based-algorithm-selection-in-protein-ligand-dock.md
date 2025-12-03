---
layout: default
title: Molecular Embedding-Based Algorithm Selection in Protein-Ligand Docking
---

# Molecular Embedding-Based Algorithm Selection in Protein-Ligand Docking
**arXiv**：[2512.02328v1](https://arxiv.org/abs/2512.02328) · [PDF](https://arxiv.org/pdf/2512.02328.pdf)  
**作者**：Jiabao Brad Wang, Siyuan Cao, Hongxuan Wu, Yiliang Yuan, Mustafa Misir  

**一句话要点**：提出MolAS系统，基于分子嵌入预测蛋白质-配体对接算法性能，提升选择准确性。

**关键词**：蛋白质-配体对接, 算法选择, 分子嵌入, 注意力机制, 残差解码器, 性能预测

## 3 点简述
- 核心问题：对接算法选择高度依赖上下文，无单一方法在所有场景下可靠。
- 方法要点：使用预训练分子嵌入，结合注意力池化和浅层残差解码器进行轻量级算法选择。
- 实验或效果：在五个基准测试中，相比最佳单一算法提升达15%，缩小虚拟最佳算法差距17-66%。

## 摘要（原文）

> Selecting an effective docking algorithm is highly context-dependent, and no single method performs reliably across structural, chemical, or protocol regimes. We introduce MolAS, a lightweight algorithm selection system that predicts per-algorithm performance from pretrained protein-ligand embeddings using attentional pooling and a shallow residual decoder. With only hundreds to a few thousand labelled complexes, MolAS achieves up to 15% absolute improvement over the single-best solver (SBS) and closes 17-66% of the Virtual Best Solver (VBS)-SBS gap across five diverse docking benchmarks. Analyses of reliability, embedding geometry, and solver-selection patterns show that MolAS succeeds when the oracle landscape exhibits low entropy and separable solver behaviour, but collapses under protocol-induced hierarchy shifts. These findings indicate that the main barrier to robust docking AS is not representational capacity but instability in solver rankings across pose-generation regimes, positioning MolAS as both a practical in-domain selector and a diagnostic tool for assessing when AS is feasible.

