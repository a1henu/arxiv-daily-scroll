---
layout: default
title: From Pixels to Predicates Structuring urban perception with scene graphs
---

# From Pixels to Predicates Structuring urban perception with scene graphs
**arXiv**：[2512.19221v1](https://arxiv.org/abs/2512.19221) · [PDF](https://arxiv.org/pdf/2512.19221.pdf)  
**作者**：Yunlong Liu, Shuyang Li, Pengyuan Liu, Yu Zhang, Rudi Stouffs  

**一句话要点**：提出基于场景图的三阶段流程，以结构化表示提升城市感知预测的准确性与可解释性。

**关键词**：城市感知预测, 场景图, 图自编码器, 街景图像分析, 结构化表示, 跨城市泛化

## 3 点简述
- 核心问题：现有城市感知研究依赖像素特征或对象共现统计，忽略显式关系对感知的影响。
- 方法要点：使用OpenPSG提取对象-谓词-对象三元组，通过GraphMAE学习场景嵌入，神经网络预测感知分数。
- 实验或效果：相比基线模型平均提升26%准确率，跨城市泛化性能强，可解释关系模式如涂鸦在墙上。

## 摘要（原文）

> Perception research is increasingly modelled using streetscapes, yet many approaches still rely on pixel features or object co-occurrence statistics, overlooking the explicit relations that shape human perception. This study proposes a three stage pipeline that transforms street view imagery (SVI) into structured representations for predicting six perceptual indicators. In the first stage, each image is parsed using an open-set Panoptic Scene Graph model (OpenPSG) to extract object predicate object triplets. In the second stage, compact scene-level embeddings are learned through a heterogeneous graph autoencoder (GraphMAE). In the third stage, a neural network predicts perception scores from these embeddings. We evaluate the proposed approach against image-only baselines in terms of accuracy, precision, and cross-city generalization. Results indicate that (i) our approach improves perception prediction accuracy by an average of 26% over baseline models, and (ii) maintains strong generalization performance in cross-city prediction tasks. Additionally, the structured representation clarifies which relational patterns contribute to lower perception scores in urban scenes, such as graffiti on wall and car parked on sidewalk. Overall, this study demonstrates that graph-based structure provides expressive, generalizable, and interpretable signals for modelling urban perception, advancing human-centric and context-aware urban analytics.

