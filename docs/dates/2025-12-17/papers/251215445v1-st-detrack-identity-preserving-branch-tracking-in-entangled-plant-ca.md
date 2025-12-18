---
layout: default
title: ST-DETrack: Identity-Preserving Branch Tracking in Entangled Plant Canopies via Dual Spatiotemporal Evidence
---

# ST-DETrack: Identity-Preserving Branch Tracking in Entangled Plant Canopies via Dual Spatiotemporal Evidence
**arXiv**：[2512.15445v1](https://arxiv.org/abs/2512.15445) · [PDF](https://arxiv.org/pdf/2512.15445.pdf)  
**作者**：Yueqianji Chen, Kevin Williams, John H. Doonan, Paolo Remagnino, Jo Hepworth  

**一句话要点**：提出ST-DETrack以解决纠缠植物冠层中分支身份保持的跟踪问题

**关键词**：植物表型分析, 时空融合跟踪, 身份保持, 自适应门控, 生物约束

## 3 点简述
- 核心问题：自动化提取时间序列图像中的植物分支，面临非刚性生长和身份碎片化的挑战
- 方法要点：集成空间和时间解码器，通过自适应门控机制动态融合几何先验和运动一致性
- 实验或效果：在Brassica napus数据集上，分支匹配准确率达93.6%，显著优于基线方法

## 摘要（原文）

> Automated extraction of individual plant branches from time-series imagery is essential for high-throughput phenotyping, yet it remains computationally challenging due to non-rigid growth dynamics and severe identity fragmentation within entangled canopies. To overcome these stage-dependent ambiguities, we propose ST-DETrack, a spatiotemporal-fusion dual-decoder network designed to preserve branch identity from budding to flowering. Our architecture integrates a spatial decoder, which leverages geometric priors such as position and angle for early-stage tracking, with a temporal decoder that exploits motion consistency to resolve late-stage occlusions. Crucially, an adaptive gating mechanism dynamically shifts reliance between these spatial and temporal cues, while a biological constraint based on negative gravitropism mitigates vertical growth ambiguities. Validated on a Brassica napus dataset, ST-DETrack achieves a Branch Matching Accuracy (BMA) of 93.6%, significantly outperforming spatial and temporal baselines by 28.9 and 3.3 percentage points, respectively. These results demonstrate the method's robustness in maintaining long-term identity consistency amidst complex, dynamic plant architectures.

