---
layout: default
title: A novel network for classification of cuneiform tablet metadata
---

# A novel network for classification of cuneiform tablet metadata
**arXiv**：[2603.03892v1](https://arxiv.org/abs/2603.03892) · [PDF](https://arxiv.org/pdf/2603.03892.pdf)  
**作者**：Frederik Hagelskjær  

**一句话要点**：提出卷积启发的网络结构，用于楔形文字泥板元数据分类，以解决标注数据有限和高分辨率点云表示的挑战。

**关键词**：楔形文字泥板分类, 点云处理, 卷积网络, 元数据分类, 高分辨率点云

## 3 点简述
- 核心问题：楔形文字泥板元数据分类面临标注数据集有限和高分辨率点云表示的困难。
- 方法要点：设计卷积启发的架构，逐步下采样点云并整合局部邻居信息，最后在特征空间计算邻居以包含全局信息。
- 实验或效果：与基于Transformer的Point-BERT相比，该方法始终获得最佳性能，源代码和数据集将在发表时发布。

## 摘要（原文）

> In this paper, we present a network structure for classifying metadata of cuneiform tablets. The problem is of practical importance, as the size of the existing corpus far exceeds the number of experts available to analyze it. But the task is made difficult by the combination of limited annotated datasets and the high-resolution point-cloud representation of each tablet. To address this, we develop a convolution-inspired architecture that gradually down-scales the point cloud while integrating local neighbor information. The final down-scaled point cloud is then processed by computing neighbors in the feature space to include global information. Our method is compared with the state-of-the-art transformer-based network Point-BERT, and consistently obtains the best performance. Source code and datasets will be released at publication.

