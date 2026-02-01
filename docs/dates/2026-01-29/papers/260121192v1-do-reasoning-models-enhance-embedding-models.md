---
layout: default
title: Do Reasoning Models Enhance Embedding Models?
---

# Do Reasoning Models Enhance Embedding Models?
**arXiv**：[2601.21192v1](https://arxiv.org/abs/2601.21192) · [PDF](https://arxiv.org/pdf/2601.21192.pdf)  
**作者**：Wun Yu Chan, Shaojin Chen, Huihao Jing, Kwun Hang Lau, Elton Chun-Chai Li, Zihao Wang, Haoran Li, Yangqiu Song  

**一句话要点**：提出HRSA框架分析推理模型初始化嵌入模型无性能提升的原因，揭示流形重对齐现象。

**关键词**：嵌入模型, 推理模型, HRSA框架, 流形重对齐, 对比学习, 语义表示

## 3 点简述
- 核心问题：推理模型初始化是否提升嵌入模型性能，实验显示无一致优势。
- 方法要点：引入HRSA框架，分解表示、几何和功能层面的相似性。
- 实验或效果：RLVR优化语义景观内轨迹，而非重构景观，导致流形重对齐。

## 摘要（原文）

> State-of-the-art embedding models are increasingly derived from decoder-only Large Language Model (LLM) backbones adapted via contrastive learning. Given the emergence of reasoning models trained via Reinforcement Learning with Verifiable Rewards (RLVR), a natural question arises: do enhanced reasoning translate to superior semantic representations when these models serve as embedding initializations? Contrary to expectation, our evaluation on MTEB and BRIGHT reveals a **null effect**: embedding models initialized from RLVR-tuned backbones yield no consistent performance advantage over their base counterparts when subjected to identical training recipes. To unpack this paradox, we introduce **H**ierarchical **R**epresentation **S**imilarity **A**nalysis (HRSA), a framework that decomposes similarity across representation, geometry, and function levels. HRSA reveals that while RLVR induces irreversible latent manifold's local geometry reorganization and reversible coordinate basis drift, it preserves the global manifold geometry and linear readout. Consequently, subsequent contrastive learning drives strong alignment between base- and reasoning-initialized models, a phenomenon we term **Manifold Realignment**. Empirically, our findings suggest that unlike Supervised Fine-Tuning (SFT), RLVR optimizes trajectories within an existing semantic landscape rather than fundamentally restructuring the landscape itself.

