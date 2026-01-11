---
layout: default
title: TSSR: Two-Stage Swap-Reward-Driven Reinforcement Learning for Character-Level SMILES Generation
---

# TSSR: Two-Stage Swap-Reward-Driven Reinforcement Learning for Character-Level SMILES Generation
**arXiv**：[2601.04521v1](https://arxiv.org/abs/2601.04521) · [PDF](https://arxiv.org/pdf/2601.04521.pdf)  
**作者**：Jacob Ede Levine, Yun Lyan Luo, Sai Chandra Kosaraju  

**一句话要点**：提出TSSR两阶段强化学习框架，通过交换奖励驱动字符级SMILES生成，提升分子语法和化学有效性。

**关键词**：SMILES生成, 强化学习, 分子设计, 化学有效性, 语法修复, 奖励分解

## 3 点简述
- 核心问题：当前SMILES生成模型易产生语法错误和化学不合理分子，限制化学空间探索。
- 方法要点：采用两阶段强化学习，第一阶段奖励语法修复的字符交换，第二阶段基于RDKit奖励化学问题减少。
- 实验或效果：在MOSES基准测试中，TSSR显著提高语法和化学有效性，同时保持多样性和药物相似性。

## 摘要（原文）

> The design of reliable, valid, and diverse molecules is fundamental to modern drug discovery, as improved molecular generation supports efficient exploration of the chemical space for potential drug candidates and reduces the cost of early design efforts. Despite these needs, current chemical language models that generate molecules as SMILES strings are vulnerable to compounding token errors: many samples are unparseable or chemically implausible, and hard constraints meant to prevent failure can restrict exploration. To address this gap, we introduce TSSR, a Two-Stage, Swap-Reward-driven reinforcement learning (RL) framework for character-level SMILES generation. Stage one rewards local token swaps that repair syntax, promoting transitions from invalid to parseable strings. Stage two provides chemistry-aware feedback from RDKit diagnostics, rewarding reductions in valence, aromaticity, and connectivity issues. The reward decomposes into interpretable terms (swap efficiency, error reduction, distance to validity), is model agnostic, and requires no task-specific labels or hand-crafted grammars. We evaluated TSSR on the MOSES benchmark using a GRU policy trained with PPO in both pure RL (P-RL) from random initialization and fine-tuning RL (F-RL) starting from a pretrained chemical language model, assessing 10,000 generated SMILES per run. In P-RL, TSSR significantly improves syntactic validity, chemical validity, and novelty. In F-RL, TSSR preserves drug-likeness and synthesizability while increasing validity and novelty. Token-level analysis shows that syntax edits and chemistry fixes act jointly to reduce RDKit detected errors. TSSR converts a sparse terminal objective into a denser and more interpretable reward, improving both syntactic and chemical quality without reducing diversity. TSSR is dataset-agnostic and can be adapted to various reinforcement learning approaches.

