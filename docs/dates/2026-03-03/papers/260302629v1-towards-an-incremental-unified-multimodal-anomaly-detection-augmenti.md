---
layout: default
title: Towards an Incremental Unified Multimodal Anomaly Detection: Augmenting Multimodal Denoising From an Information Bottleneck Perspective
---

# Towards an Incremental Unified Multimodal Anomaly Detection: Augmenting Multimodal Denoising From an Information Bottleneck Perspective
**arXiv**：[2603.02629v1](https://arxiv.org/abs/2603.02629) · [PDF](https://arxiv.org/pdf/2603.02629.pdf)  
**作者**：Kaifang Long, Lianbo Ma, Jiaqi Liu, Liming Liu, Guoyang Xie  

**一句话要点**：提出IB-IUMAD框架，通过信息瓶颈融合与Mamba解码器解决增量统一多模态异常检测中的灾难性遗忘问题。

**关键词**：增量学习, 多模态异常检测, 信息瓶颈, 灾难性遗忘, 特征解耦

## 3 点简述
- 核心问题：增量统一多模态异常检测中，虚假和冗余特征加剧灾难性遗忘，影响模型学习新类别时保留旧知识。
- 方法要点：结合Mamba解码器解耦对象间特征耦合，以及信息瓶颈融合模块过滤冗余特征，以增强特征判别性。
- 实验或效果：在MVTec 3D-AD和Eyecandies数据集上验证了IB-IUMAD的有效性和竞争性能。

## 摘要（原文）

> The quest for incremental unified multimodal anomaly detection seeks to empower a single model with the ability to systematically detect anomalies across all categories and support incremental learning to accommodate emerging objects/categories. Central to this pursuit is resolving the catastrophic forgetting dilemma, which involves acquiring new knowledge while preserving prior learned knowledge. Despite some efforts to address this dilemma, a key oversight persists: ignoring the potential impact of spurious and redundant features on catastrophic forgetting. In this paper, we delve into the negative effect of spurious and redundant features on this dilemma in incremental unified frameworks, and reveal that under similar conditions, the multimodal framework developed by naive aggregation of unimodal architectures is more prone to forgetting. To address this issue, we introduce a novel denoising framework called IB-IUMAD, which exploits the complementary benefits of the Mamba decoder and information bottleneck fusion module: the former dedicated to disentangle inter-object feature coupling, preventing spurious feature interference between objects; the latter serves to filter out redundant features from the fused features, thus explicitly preserving discriminative information. A series of theoretical analyses and experiments on MVTec 3D-AD and Eyecandies datasets demonstrates the effectiveness and competitive performance of IB-IUMAD.

