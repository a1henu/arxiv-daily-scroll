---
layout: default
title: Meta-Learning Guided Pruning for Few-Shot Plant Pathology on Edge Devices
---

# Meta-Learning Guided Pruning for Few-Shot Plant Pathology on Edge Devices
**arXiv**：[2601.02353v1](https://arxiv.org/abs/2601.02353) · [PDF](https://arxiv.org/pdf/2601.02353.pdf)  
**作者**：Shahnawaz Alam, Mohammed Mudassir Uddin, Mohammed Kaif Pasha  

**一句话要点**：提出DACIS与PMP管道，通过剪枝与元学习压缩模型，实现边缘设备上的少样本植物病理诊断。

**关键词**：少样本学习, 神经网络剪枝, 边缘计算, 植物病害识别, 元学习

## 3 点简述
- 核心问题：远程农民缺乏高性能计算资源，难以部署大模型进行实时植物病害识别。
- 方法要点：结合DACIS评分与PMP三阶段管道，先剪枝后元学习再剪枝，优化模型效率。
- 实验或效果：在PlantVillage和PlantDoc数据集上，模型大小减少78%，精度保持92.3%，Raspberry Pi 4上达7 FPS。

## 摘要（原文）

> Farmers in remote areas need quick and reliable methods for identifying plant diseases, yet they often lack access to laboratories or high-performance computing resources. Deep learning models can detect diseases from leaf images with high accuracy, but these models are typically too large and computationally expensive to run on low-cost edge devices such as Raspberry Pi. Furthermore, collecting thousands of labeled disease images for training is both expensive and time-consuming. This paper addresses both challenges by combining neural network pruning -- removing unnecessary parts of the model -- with few-shot learning, which enables the model to learn from limited examples. This paper proposes Disease-Aware Channel Importance Scoring (DACIS), a method that identifies which parts of the neural network are most important for distinguishing between different plant diseases, integrated into a three-stage Prune-then-Meta-Learn-then-Prune (PMP) pipeline. Experiments on PlantVillage and PlantDoc datasets demonstrate that the proposed approach reduces model size by 78\% while maintaining 92.3\% of the original accuracy, with the compressed model running at 7 frames per second on a Raspberry Pi 4, making real-time field diagnosis practical for smallholder farmers.

