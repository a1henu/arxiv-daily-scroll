---
layout: default
title: Robust Out-of-Order Retrieval for Grid-Based Storage at Maximum Capacity
---

# Robust Out-of-Order Retrieval for Grid-Based Storage at Maximum Capacity
**arXiv**：[2601.19144v1](https://arxiv.org/abs/2601.19144) · [PDF](https://arxiv.org/pdf/2601.19144.pdf)  
**作者**：Tzvika Geft, William Zhang, Jingjin Yu, Kostas Bekris  

**一句话要点**：提出基于k-有界扰动的网格存储框架，以在最大容量下实现无序检索的零重定位。

**关键词**：网格存储系统, 无序检索, 负载重定位, k-有界扰动, 自动化物流, 优化算法

## 3 点简述
- 研究网格存储系统中，检索序列不确定时的负载重定位最小化问题。
- 证明网格宽度Θ(k)是消除重定位的必要充分条件，并提供高效求解器。
- 实验显示，在k不超过网格宽度一半时，基本消除重定位；k达全宽时重定位减少50%以上。

## 摘要（原文）

> This paper proposes a framework for improving the operational efficiency of automated storage systems under uncertainty. It considers a 2D grid-based storage for uniform-sized loads (e.g., containers, pallets, or totes), which are moved by a robot (or other manipulator) along a collision-free path in the grid. The loads are labeled (i.e., unique) and must be stored in a given sequence, and later be retrieved in a different sequence -- an operational pattern that arises in logistics applications, such as last-mile distribution centers and shipyards. The objective is to minimize the load relocations to ensure efficient retrieval. A previous result guarantees a zero-relocation solution for known storage and retrieval sequences, even for storage at full capacity, provided that the side of the grid through which loads are stored/retrieved is at least 3 cells wide. However, in practice, the retrieval sequence can change after the storage phase. To address such uncertainty, this work investigates \emph{$k$-bounded perturbations} during retrieval, under which any two loads may depart out of order if they are originally at most $k$ positions apart. We prove that a $Θ(k)$ grid width is necessary and sufficient for eliminating relocations at maximum capacity. We also provide an efficient solver for computing a storage arrangement that is robust to such perturbations. To address the higher-uncertainty case where perturbations exceed $k$, a strategy is introduced to effectively minimize relocations. Extensive experiments show that, for $k$ up to half the grid width, the proposed storage-retrieval framework essentially eliminates relocations. For $k$ values up to the full grid width, relocations are reduced by $50\%+$.

