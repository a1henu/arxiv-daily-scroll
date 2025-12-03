---
layout: default
title: Learning Multimodal Embeddings for Traffic Accident Prediction and Causal Estimation
---

# Learning Multimodal Embeddings for Traffic Accident Prediction and Causal Estimation
**arXiv**：[2512.02920v1](https://arxiv.org/abs/2512.02920) · [PDF](https://arxiv.org/pdf/2512.02920.pdf)  
**作者**：Ziniu Zhang, Minxuan Duan, Haris N. Koutsopoulos, Hongyang R. Zhang  

**一句话要点**：提出多模态嵌入方法，结合路网与卫星图像预测交通事故并进行因果分析

**关键词**：交通事故预测, 多模态学习, 图神经网络, 卫星图像分析, 因果估计

## 3 点简述
- 核心问题：现有交通事故预测主要依赖路网结构特征，忽略道路表面及环境的物理信息。
- 方法要点：构建包含路网数据、卫星图像、天气统计和交通量的大型多模态数据集，集成视觉与网络嵌入。
- 实验或效果：多模态方法提升预测准确率，AUROC达90.1%，并基于匹配估计器进行因果分析，识别关键影响因素。

## 摘要（原文）

> We consider analyzing traffic accident patterns using both road network data and satellite images aligned to road graph nodes. Previous work for predicting accident occurrences relies primarily on road network structural features while overlooking physical and environmental information from the road surface and its surroundings. In this work, we construct a large multimodal dataset across six U.S. states, containing nine million traffic accident records from official sources, and one million high-resolution satellite images for each node of the road network. Additionally, every node is annotated with features such as the region's weather statistics and road type (e.g., residential vs. motorway), and each edge is annotated with traffic volume information (i.e., Average Annual Daily Traffic). Utilizing this dataset, we conduct a comprehensive evaluation of multimodal learning methods that integrate both visual and network embeddings. Our findings show that integrating both data modalities improves prediction accuracy, achieving an average AUROC of $90.1\%$, which is a $3.7\%$ gain over graph neural network models that only utilize graph structures. With the improved embeddings, we conduct a causal analysis based on a matching estimator to estimate the key contributing factors influencing traffic accidents. We find that accident rates rise by $24\%$ under higher precipitation, by $22\%$ on higher-speed roads such as motorways, and by $29\%$ due to seasonal patterns, after adjusting for other confounding factors. Ablation studies confirm that satellite imagery features are essential for achieving accurate prediction.

