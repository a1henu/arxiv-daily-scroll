---
layout: default
title: mHC: Manifold-Constrained Hyper-Connections
---

# mHC: Manifold-Constrained Hyper-Connections
**arXiv**：[2512.24880v1](https://arxiv.org/abs/2512.24880) · [PDF](https://arxiv.org/pdf/2512.24880.pdf)  
**作者**：Zhenda Xie, Yixuan Wei, Huanqi Cao, Chenggang Zhao, Chengqi Deng, Jiashi Li, Damai Dai, Huazuo Gao, Jiang Chang, Liang Zhao, Shangyan Zhou, Zhean Xu, Zhengyan Zhang, Wangding Zeng, Shengding Hu, Yuqing Wang, Jingyang Yuan, Lean Wang, Wenfeng Liang  

**一句话要点**：提出流形约束超连接以解决超连接训练不稳定和可扩展性问题

**关键词**：残差连接, 超连接, 流形约束, 训练稳定性, 可扩展性, 拓扑架构设计

## 3 点简述
- 超连接扩展残差连接但破坏恒等映射，导致训练不稳定和内存开销
- mHC将超连接空间投影到特定流形以恢复恒等映射，并优化基础设施
- 实验表明mHC在规模化训练中有效，提升性能并增强可扩展性

## 摘要（原文）

> Recently, studies exemplified by Hyper-Connections (HC) have extended the ubiquitous residual connection paradigm established over the past decade by expanding the residual stream width and diversifying connectivity patterns. While yielding substantial performance gains, this diversification fundamentally compromises the identity mapping property intrinsic to the residual connection, which causes severe training instability and restricted scalability, and additionally incurs notable memory access overhead. To address these challenges, we propose Manifold-Constrained Hyper-Connections (mHC), a general framework that projects the residual connection space of HC onto a specific manifold to restore the identity mapping property, while incorporating rigorous infrastructure optimization to ensure efficiency. Empirical experiments demonstrate that mHC is effective for training at scale, offering tangible performance improvements and superior scalability. We anticipate that mHC, as a flexible and practical extension of HC, will contribute to a deeper understanding of topological architecture design and suggest promising directions for the evolution of foundational models.

