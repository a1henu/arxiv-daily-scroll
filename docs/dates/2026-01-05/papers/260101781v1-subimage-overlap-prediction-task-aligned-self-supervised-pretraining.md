---
layout: default
title: Subimage Overlap Prediction: Task-Aligned Self-Supervised Pretraining For Semantic Segmentation In Remote Sensing Imagery
---

# Subimage Overlap Prediction: Task-Aligned Self-Supervised Pretraining For Semantic Segmentation In Remote Sensing Imagery
**arXiv**：[2601.01781v1](https://arxiv.org/abs/2601.01781) · [PDF](https://arxiv.org/pdf/2601.01781.pdf)  
**作者**：Lakshay Sharma, Alex Marin  

**一句话要点**：提出子图像重叠预测任务，以少量预训练数据提升遥感图像语义分割性能。

**关键词**：自监督学习, 遥感图像分割, 子图像重叠预测, 预训练任务, 语义分割, 数据效率

## 3 点简述
- 核心问题：自监督学习通常依赖大量预训练数据，遥感图像标注成本高。
- 方法要点：从图像中提取子图像，训练模型预测其在原图中的位置语义掩码。
- 实验或效果：预训练后下游分割收敛更快，mIoU相等或更好，数据少时优势更明显。

## 摘要（原文）

> Self-supervised learning (SSL) methods have become a dominant paradigm for creating general purpose models whose capabilities can be transferred to downstream supervised learning tasks. However, most such methods rely on vast amounts of pretraining data. This work introduces Subimage Overlap Prediction, a novel self-supervised pretraining task to aid semantic segmentation in remote sensing imagery that uses significantly lesser pretraining imagery. Given an image, a sub-image is extracted and the model is trained to produce a semantic mask of the location of the extracted sub-image within the original image. We demonstrate that pretraining with this task results in significantly faster convergence, and equal or better performance (measured via mIoU) on downstream segmentation. This gap in convergence and performance widens when labeled training data is reduced. We show this across multiple architecture types, and with multiple downstream datasets. We also show that our method matches or exceeds performance while requiring significantly lesser pretraining data relative to other SSL methods. Code and model weights are provided at \href{https://github.com/sharmalakshay93/subimage-overlap-prediction}{github.com/sharmalakshay93/subimage-overlap-prediction}.

