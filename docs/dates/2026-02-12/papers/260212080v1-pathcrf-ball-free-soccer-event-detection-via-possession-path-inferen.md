---
layout: default
title: PathCRF: Ball-Free Soccer Event Detection via Possession Path Inference from Player Trajectories
---

# PathCRF: Ball-Free Soccer Event Detection via Possession Path Inference from Player Trajectories
**arXiv**：[2602.12080v1](https://arxiv.org/abs/2602.12080) · [PDF](https://arxiv.org/pdf/2602.12080.pdf)  
**作者**：Hyunsung Kim, Kunhee Lee, Sangwoo Seo, Sang-Ki Ko, Jinsung Yoon, Chanyoung Park  

**一句话要点**：提出PathCRF框架，仅使用球员轨迹数据检测足球事件，以解决依赖球追踪的高成本问题。

**关键词**：足球事件检测, 球员轨迹分析, 条件随机场, 动态图建模, Viterbi解码

## 3 点简述
- 核心问题：足球事件检测依赖球追踪，成本高，限制数据驱动分析的普及。
- 方法要点：将球员轨迹建模为动态图，使用CRF选择边序列，通过Viterbi解码检测事件。
- 实验或效果：PathCRF生成准确、逻辑一致的控球路径，减少手动标注需求。

## 摘要（原文）

> Despite recent advances in AI, event data collection in soccer still relies heavily on labor-intensive manual annotation. Although prior work has explored automatic event detection using player and ball trajectories, ball tracking also remains difficult to scale due to high infrastructural and operational costs. As a result, comprehensive data collection in soccer is largely confined to top-tier competitions, limiting the broader adoption of data-driven analysis in this domain. To address this challenge, this paper proposes PathCRF, a framework for detecting on-ball soccer events using only player tracking data. We model player trajectories as a fully connected dynamic graph and formulate event detection as the problem of selecting exactly one edge corresponding to the current possession state at each time step. To ensure logical consistency of the resulting edge sequence, we employ a Conditional Random Field (CRF) that forbids impossible transitions between consecutive edges. Both emission and transition scores dynamically computed from edge embeddings produced by a Set Attention-based backbone architecture. During inference, the most probable edge sequence is obtained via Viterbi decoding, and events such as ball controls or passes are detected whenever the selected edge changes between adjacent time steps. Experiments show that PathCRF produces accurate, logically consistent possession paths, enabling reliable downstream analyses while substantially reducing the need for manual event annotation. The source code is available at https://github.com/hyunsungkim-ds/pathcrf.git.

