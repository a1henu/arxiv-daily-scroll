---
layout: default
title: UltraStar: Semantic-Aware Star Graph Modeling for Echocardiography Navigation
---

# UltraStar: Semantic-Aware Star Graph Modeling for Echocardiography Navigation
**arXiv**：[2603.01461v1](https://arxiv.org/abs/2603.01461) · [PDF](https://arxiv.org/pdf/2603.01461.pdf)  
**作者**：Teng Wang, Haojun Jiang, Chenxi Li, Diwen Wang, Yihang Tang, Zhenguo Sun, Yujiao Deng, Shiji Song, Gao Huang  

**一句话要点**：提出UltraStar，通过星图建模和语义感知采样，解决超声心动图导航中历史轨迹噪声问题。

**关键词**：超声心动图导航, 星图建模, 语义感知采样, 全局定位, 历史轨迹噪声, 长序列性能

## 3 点简述
- 核心问题：超声心动图导航中，历史扫描轨迹噪声导致现有序列模型在长序列上性能下降。
- 方法要点：将导航重构为基于锚点的全局定位，建立星图连接关键帧，并引入语义感知采样选择代表性地标。
- 实验或效果：在131万样本数据集上，UltraStar优于基线，且在长输入序列上扩展性更好。

## 摘要（原文）

> Echocardiography is critical for diagnosing cardiovascular diseases, yet the shortage of skilled sonographers hinders timely patient care, due to high operational difficulties. Consequently, research on automated probe navigation has significant clinical potential. To achieve robust navigation, it is essential to leverage historical scanning information, mimicking how experts rely on past feedback to adjust subsequent maneuvers. Practical scanning data collected from sonographers typically consists of noisy trajectories inherently generated through trial-and-error exploration. However, existing methods typically model this history as a sequential chain, forcing models to overfit these noisy paths, leading to performance degradation on long sequences. In this paper, we propose UltraStar, which reformulates probe navigation from path regression to anchor-based global localization. By establishing a Star Graph, UltraStar treats historical keyframes as spatial anchors connected directly to the current view, explicitly modeling geometric constraints for precise positioning. We further enhance the Star Graph with a semantic-aware sampling strategy that actively selects the representative landmarks from massive history logs, reducing redundancy for accurate anchoring. Extensive experiments on a dataset with over 1.31 million samples demonstrate that UltraStar outperforms baselines and scales better with longer input lengths, revealing a more effective topology for history modeling under noisy exploration.

