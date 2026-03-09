---
layout: default
title: FlowMotion: Training-Free Flow Guidance for Video Motion Transfer
---

# FlowMotion: Training-Free Flow Guidance for Video Motion Transfer
**arXiv**：[2603.06289v1](https://arxiv.org/abs/2603.06289) · [PDF](https://arxiv.org/pdf/2603.06289.pdf)  
**作者**：Zhen Wang, Youcan Xu, Jun Xiao, Long Chen  

**一句话要点**：提出FlowMotion框架，通过流引导实现高效灵活的视频运动迁移

**关键词**：视频运动迁移, 免训练框架, 流引导, 潜在预测, 速度正则化

## 3 点简述
- 核心问题：现有免训练方法依赖中间输出，计算开销大且灵活性有限。
- 方法要点：基于流模型的潜在预测提取运动表示，对齐源与生成视频的运动模式。
- 实验或效果：实现时间和资源效率优势，性能与先进方法相当。

## 摘要（原文）

> Video motion transfer aims to generate a target video that inherits motion patterns from a source video while rendering new scenes. Existing training-free approaches focus on constructing motion guidance based on the intermediate outputs of pre-trained T2V models, which results in heavy computational overhead and limited flexibility. In this paper, we present FlowMotion, a novel training-free framework that enables efficient and flexible motion transfer by directly leveraging the predicted outputs of flow-based T2V models. Our key insight is that early latent predictions inherently encode rich temporal information. Motivated by this, we propose flow guidance, which extracts motion representations based on latent predictions to align motion patterns between source and generated videos. We further introduce a velocity regularization strategy to stabilize optimization and ensure smooth motion evolution. By operating purely on model predictions, FlowMotion achieves superior time and resource efficiency as well as competitive performance compared with state-of-the-art methods.

