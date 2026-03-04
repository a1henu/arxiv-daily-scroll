---
layout: default
title: EIMC: Efficient Instance-aware Multi-modal Collaborative Perception
---

# EIMC: Efficient Instance-aware Multi-modal Collaborative Perception
**arXiv**：[2603.02532v1](https://arxiv.org/abs/2603.02532) · [PDF](https://arxiv.org/pdf/2603.02532.pdf)  
**作者**：Kang Yang, Peng Wang, Lantao Li, Tianci Bu, Chen Sun, Deying Li, Yongcai Wang  

**一句话要点**：提出EIMC以解决多模态协同感知中的带宽浪费问题，通过早期协同和实例中心消息传递提升自动驾驶安全性。

**关键词**：多模态协同感知, 自动驾驶安全, 带宽优化, 实例中心消息传递, 早期协同范式, 热图驱动共识

## 3 点简述
- 核心问题：当前多模态协同感知采用“本地融合后通信”序列，导致高带宽需求，影响效率。
- 方法要点：引入早期协同范式，注入轻量协同体素，结合热图驱动共识协议，仅查询低置信区域实例进行融合。
- 实验或效果：在OPV2V和DAIR-V2X数据集上达到73.01% AP@0.5，带宽使用减少87.98%。

## 摘要（原文）

> Multi-modal collaborative perception calls for great attention to enhancing the safety of autonomous driving. However, current multi-modal approaches remain a ``local fusion to communication'' sequence, which fuses multi-modal data locally and needs high bandwidth to transmit an individual's feature data before collaborative fusion. EIMC innovatively proposes an early collaborative paradigm. It injects lightweight collaborative voxels, transmitted by neighbor agents, into the ego's local modality-fusion step, yielding compact yet informative 3D collaborative priors that tighten cross-modal alignment. Next, a heatmap-driven consensus protocol identifies exactly where cooperation is needed by computing per-pixel confidence heatmaps. Only the Top-K instance vectors located in these low-confidence, high-discrepancy regions are queried from peers, then fused via cross-attention for completion. Afterwards, we apply a refinement fusion that involves collecting the top-K most confident instances from each agent and enhancing their features using self-attention. The above instance-centric messaging reduces redundancy while guaranteeing that critical occluded objects are recovered. Evaluated on OPV2V and DAIR-V2X, EIMC attains 73.01\% AP@0.5 while reducing byte bandwidth usage by 87.98\% compared with the best published multi-modal collaborative detector. Code publicly released at https://github.com/sidiangongyuan/EIMC.

