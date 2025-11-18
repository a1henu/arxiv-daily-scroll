---
layout: default
title: Segment Anything Across Shots: A Method and Benchmark
---

# Segment Anything Across Shots: A Method and Benchmark
**arXiv**：[2511.13715v1](https://arxiv.org/abs/2511.13715) · [PDF](https://arxiv.org/pdf/2511.13715.pdf)  
**作者**：Hengrui Hu, Kaining Ying, Henghui Ding  

**一句话要点**：提出SAAS模型与TMA数据增强，解决多镜头视频对象分割中的镜头不连续问题。

**关键词**：多镜头视频对象分割, 数据增强策略, 镜头转换检测, 半监督学习, 基准数据集

## 3 点简述
- 核心问题：现有VOS方法难以处理多镜头视频中的镜头不连续，限制实际应用。
- 方法要点：引入TMA数据增强策略，利用单镜头数据模拟跨镜头泛化；开发SAAS模型，有效检测和理解镜头转换。
- 实验或效果：在YouMVOS和Cut-VOS基准上，SAAS实现最先进性能，验证跨复杂转换的分割能力。

## 摘要（原文）

> This work focuses on multi-shot semi-supervised video object segmentation (MVOS), which aims at segmenting the target object indicated by an initial mask throughout a video with multiple shots. The existing VOS methods mainly focus on single-shot videos and struggle with shot discontinuities, thereby limiting their real-world applicability. We propose a transition mimicking data augmentation strategy (TMA) which enables cross-shot generalization with single-shot data to alleviate the severe annotated multi-shot data sparsity, and the Segment Anything Across Shots (SAAS) model, which can detect and comprehend shot transitions effectively. To support evaluation and future study in MVOS, we introduce Cut-VOS, a new MVOS benchmark with dense mask annotations, diverse object categories, and high-frequency transitions. Extensive experiments on YouMVOS and Cut-VOS demonstrate that the proposed SAAS achieves state-of-the-art performance by effectively mimicking, understanding, and segmenting across complex transitions. The code and datasets are released at https://henghuiding.com/SAAS/.

