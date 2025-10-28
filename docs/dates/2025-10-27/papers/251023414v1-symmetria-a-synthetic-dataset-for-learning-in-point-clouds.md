---
layout: default
title: Symmetria: A Synthetic Dataset for Learning in Point Clouds
---

# Symmetria: A Synthetic Dataset for Learning in Point Clouds
**arXiv**：[2510.23414v1](https://arxiv.org/abs/2510.23414) · [PDF](https://arxiv.org/pdf/2510.23414.pdf)  
**作者**：Ivan Sipiran, Gustavo Santelices, Lucas Oyarzún, Andrea Ranieri, Chiara Romanengo, Silvia Biasotti, Bianca Falcidieno  

**一句话要点**：提出Symmetria合成数据集以解决点云学习数据稀缺问题

**关键词**：点云学习, 合成数据集, 对称性生成, 自监督预训练, 下游任务评估

## 3 点简述
- 点云学习因缺乏大规模数据集而受限
- 基于对称性生成可变形状，提供精确标注和可扩展性
- 实验显示在自监督预训练和下游任务中表现优异

## 摘要（原文）

> Unlike image or text domains that benefit from an abundance of large-scale
> datasets, point cloud learning techniques frequently encounter limitations due
> to the scarcity of extensive datasets. To overcome this limitation, we present
> Symmetria, a formula-driven dataset that can be generated at any arbitrary
> scale. By construction, it ensures the absolute availability of precise ground
> truth, promotes data-efficient experimentation by requiring fewer samples,
> enables broad generalization across diverse geometric settings, and offers easy
> extensibility to new tasks and modalities. Using the concept of symmetry, we
> create shapes with known structure and high variability, enabling neural
> networks to learn point cloud features effectively. Our results demonstrate
> that this dataset is highly effective for point cloud self-supervised
> pre-training, yielding models with strong performance in downstream tasks such
> as classification and segmentation, which also show good few-shot learning
> capabilities. Additionally, our dataset can support fine-tuning models to
> classify real-world objects, highlighting our approach's practical utility and
> application. We also introduce a challenging task for symmetry detection and
> provide a benchmark for baseline comparisons. A significant advantage of our
> approach is the public availability of the dataset, the accompanying code, and
> the ability to generate very large collections, promoting further research and
> innovation in point cloud learning.

