---
layout: default
title: Remote Sensing Change Detection via Weak Temporal Supervision
---

# Remote Sensing Change Detection via Weak Temporal Supervision
**arXiv**：[2601.02126v1](https://arxiv.org/abs/2601.02126) · [PDF](https://arxiv.org/pdf/2601.02126.pdf)  
**作者**：Xavier Bou, Elliot Vincent, Gabriele Facciolo, Rafael Grompone von Gioi, Jean-Michel Morel, Thibaud Ehret  

**一句话要点**：提出弱时序监督策略以解决遥感变化检测中标注数据稀缺问题

**关键词**：遥感变化检测, 弱监督学习, 时序分析, 对象感知优化, 零样本性能, 数据扩展

## 3 点简述
- 核心问题：遥感语义变化检测依赖像素级标注，但标注成本高且数据集稀缺。
- 方法要点：利用现有单时相数据集的多时相观测，通过假设真实双时相对无变化、不同位置配对生成变化示例，结合对象感知变化图生成和迭代优化处理弱标签噪声。
- 实验或效果：在扩展的FLAIR和IAILD数据集上验证，实现强零样本和低数据性能，并在法国大区域展示可扩展性。

## 摘要（原文）

> Semantic change detection in remote sensing aims to identify land cover changes between bi-temporal image pairs. Progress in this area has been limited by the scarcity of annotated datasets, as pixel-level annotation is costly and time-consuming. To address this, recent methods leverage synthetic data or generate artificial change pairs, but out-of-domain generalization remains limited. In this work, we introduce a weak temporal supervision strategy that leverages additional temporal observations of existing single-temporal datasets, without requiring any new annotations. Specifically, we extend single-date remote sensing datasets with new observations acquired at different times and train a change detection model by assuming that real bi-temporal pairs mostly contain no change, while pairing images from different locations to generate change examples. To handle the inherent noise in these weak labels, we employ an object-aware change map generation and an iterative refinement process. We validate our approach on extended versions of the FLAIR and IAILD aerial datasets, achieving strong zero-shot and low-data regime performance across different benchmarks. Lastly, we showcase results over large areas in France, highlighting the scalability potential of our method.

