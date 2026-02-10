---
layout: default
title: Chamelion: Reliable Change Detection for Long-Term LiDAR Mapping in Transient Environments
---

# Chamelion: Reliable Change Detection for Long-Term LiDAR Mapping in Transient Environments
**arXiv**：[2602.08189v1](https://arxiv.org/abs/2602.08189) · [PDF](https://arxiv.org/pdf/2602.08189.pdf)  
**作者**：Seoyeon Jang, Alex Junho Lee, I Made Aswin Nahrendra, Hyun Myung  

**一句话要点**：提出双头网络Chamelion，用于瞬态环境中的在线变化检测与长期地图维护。

**关键词**：在线变化检测, 长期地图维护, 瞬态环境, 数据增强, 双头网络, 激光雷达映射

## 3 点简述
- 核心问题：瞬态环境如建筑工地中，遮挡和时空变化导致现有方法难以检测变化并更新地图。
- 方法要点：设计双头网络，通过数据增强合成结构变化，无需大量真实标注即可训练模型。
- 实验或效果：在真实建筑工地和室内办公室场景中验证，实现高效准确的地图更新。

## 摘要（原文）

> Online change detection is crucial for mobile robots to efficiently navigate through dynamic environments. Detecting changes in transient settings, such as active construction sites or frequently reconfigured indoor spaces, is particularly challenging due to frequent occlusions and spatiotemporal variations. Existing approaches often struggle to detect changes and fail to update the map across different observations. To address these limitations, we propose a dual-head network designed for online change detection and long-term map maintenance. A key difficulty in this task is the collection and alignment of real-world data, as manually registering structural differences over time is both labor-intensive and often impractical. To overcome this, we develop a data augmentation strategy that synthesizes structural changes by importing elements from different scenes, enabling effective model training without the need for extensive ground-truth annotations. Experiments conducted at real-world construction sites and in indoor office environments demonstrate that our approach generalizes well across diverse scenarios, achieving efficient and accurate map updates.\resubmit{Our source code and additional material are available at: https://chamelion-pages.github.io/.

