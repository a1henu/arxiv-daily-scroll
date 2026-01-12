---
layout: default
title: Bidirectional Channel-selective Semantic Interaction for Semi-Supervised Medical Segmentation
---

# Bidirectional Channel-selective Semantic Interaction for Semi-Supervised Medical Segmentation
**arXiv**：[2601.05855v1](https://arxiv.org/abs/2601.05855) · [PDF](https://arxiv.org/pdf/2601.05855.pdf)  
**作者**：Kaiwen Huang, Yizhe Zhang, Yi Zhou, Tianyang Xu, Tao Zhou  

**一句话要点**：提出双向通道选择性语义交互框架以解决半监督医学分割中数据交互噪声和模型稳定性问题。

**关键词**：半监督医学分割, 语义空间扰动, 通道选择性交互, 3D医学图像, 伪标签学习, 模型鲁棒性

## 3 点简述
- 现有方法存在误差累积和结构复杂问题，且忽略标注与未标注数据流间的交互。
- 引入语义空间扰动机制和通道选择性路由器，通过强增强扰动和动态通道选择减少噪声干扰。
- 在多个3D医学数据集上实验，性能优于现有半监督方法，提升模型鲁棒性和分割准确性。

## 摘要（原文）

> Semi-supervised medical image segmentation is an effective method for addressing scenarios with limited labeled data. Existing methods mainly rely on frameworks such as mean teacher and dual-stream consistency learning. These approaches often face issues like error accumulation and model structural complexity, while also neglecting the interaction between labeled and unlabeled data streams. To overcome these challenges, we propose a Bidirectional Channel-selective Semantic Interaction~(BCSI) framework for semi-supervised medical image segmentation. First, we propose a Semantic-Spatial Perturbation~(SSP) mechanism, which disturbs the data using two strong augmentation operations and leverages unsupervised learning with pseudo-labels from weak augmentations. Additionally, we employ consistency on the predictions from the two strong augmentations to further improve model stability and robustness. Second, to reduce noise during the interaction between labeled and unlabeled data, we propose a Channel-selective Router~(CR) component, which dynamically selects the most relevant channels for information exchange. This mechanism ensures that only highly relevant features are activated, minimizing unnecessary interference. Finally, the Bidirectional Channel-wise Interaction~(BCI) strategy is employed to supplement additional semantic information and enhance the representation of important channels. Experimental results on multiple benchmarking 3D medical datasets demonstrate that the proposed method outperforms existing semi-supervised approaches.

