---
layout: default
title: Pruning for Generalization: A Transfer-Oriented Spatiotemporal Graph Framework
---

# Pruning for Generalization: A Transfer-Oriented Spatiotemporal Graph Framework
**arXiv**：[2602.04153v1](https://arxiv.org/abs/2602.04153) · [PDF](https://arxiv.org/pdf/2602.04153.pdf)  
**作者**：Zihao Jing, Yuxi Long, Ganlin Feng  

**一句话要点**：提出TL-GPSTGN框架，通过结构感知剪枝提升图结构多元时间序列预测的样本效率和跨域泛化能力。

**关键词**：多元时间序列预测, 图结构学习, 上下文剪枝, 跨域泛化, 时空卷积网络

## 3 点简述
- 核心问题：图结构多元时间序列预测在数据稀缺和跨域偏移下性能下降。
- 方法要点：基于信息论和相关性准则剪除非优化图上下文，构建紧凑语义表示，并集成到时空卷积架构中。
- 实验或效果：在大规模交通基准测试中，TL-GPSTGN在低数据迁移场景下持续优于基线模型。

## 摘要（原文）

> Multivariate time series forecasting in graph-structured domains is critical for real-world applications, yet existing spatiotemporal models often suffer from performance degradation under data scarcity and cross-domain shifts. We address these challenges through the lens of structure-aware context selection. We propose TL-GPSTGN, a transfer-oriented spatiotemporal framework that enhances sample efficiency and out-of-distribution generalization by selectively pruning non-optimized graph context. Specifically, our method employs information-theoretic and correlation-based criteria to extract structurally informative subgraphs and features, resulting in a compact, semantically grounded representation. This optimized context is subsequently integrated into a spatiotemporal convolutional architecture to capture complex multivariate dynamics. Evaluations on large-scale traffic benchmarks demonstrate that TL-GPSTGN consistently outperforms baselines in low-data transfer scenarios. Our findings suggest that explicit context pruning serves as a powerful inductive bias for improving the robustness of graph-based forecasting models.

