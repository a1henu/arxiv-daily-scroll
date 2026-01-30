---
layout: default
title: Do Reasoning Models Enhance Embedding Models?
---

# Do Reasoning Models Enhance Embedding Models?
**arXiv**：[2601.21192v1](https://arxiv.org/abs/2601.21192) · [PDF](https://arxiv.org/pdf/2601.21192.pdf)  
**作者**：Wun Yu Chan, Shaojin Chen, Huihao Jing, Kwun Hang Lau, Elton Chun-Chai Li, Zihao Wang, Haoran Li, Yangqiu Song  

**一句话要点**：提出HRSA框架分析推理模型对嵌入模型初始化无增益的原因，揭示流形重对齐现象。

**关键词**：嵌入模型, 推理模型, 表示相似性分析, 流形几何, 对比学习, 语义表示

## 3 点简述
- 研究推理模型作为嵌入初始化是否提升语义表示性能，发现无一致优势。
- 引入HRSA框架分解表示相似性，揭示RLVR优化不改变全局流形几何。
- 实验表明对比学习驱动基线与推理初始化模型对齐，称为流形重对齐。

## 摘要（原文）

> State-of-the-art embedding models are increasingly derived from decoder-only Large Language Model (LLM) backbones adapted via contrastive learning. Given the emergence of reasoning models trained via Reinforcement Learning with Verifiable Rewards (RLVR), a natural question arises: do enhanced reasoning translate to superior semantic representations when these models serve as embedding initializations? Contrary to expectation, our evaluation on MTEB and BRIGHT reveals a **null effect**: embedding models initialized from RLVR-tuned backbones yield no consistent performance advantage over their base counterparts when subjected to identical training recipes. To unpack this paradox, we introduce **H**ierarchical **R**epresentation **S**imilarity **A**nalysis (HRSA), a framework that decomposes similarity across representation, geometry, and function levels. HRSA reveals that while RLVR induces irreversible latent manifold's local geometry reorganization and reversible coordinate basis drift, it preserves the global manifold geometry and linear readout. Consequently, subsequent contrastive learning drives strong alignment between base- and reasoning-initialized models, a phenomenon we term **Manifold Realignment**. Empirically, our findings suggest that unlike Supervised Fine-Tuning (SFT), RLVR optimizes trajectories within an existing semantic landscape rather than fundamentally restructuring the landscape itself.

