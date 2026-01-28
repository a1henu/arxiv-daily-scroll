---
layout: default
title: Beyond Shadows: A Large-Scale Benchmark and Multi-Stage Framework for High-Fidelity Facial Shadow Removal
---

# Beyond Shadows: A Large-Scale Benchmark and Multi-Stage Framework for High-Fidelity Facial Shadow Removal
**arXiv**：[2601.19309v1](https://arxiv.org/abs/2601.19309) · [PDF](https://arxiv.org/pdf/2601.19309.pdf)  
**作者**：Tailong Luo, Jiesong Bai, Jinyang Huang, Junyu Xia, Wangyu Wu, Xuhang Chen  

**一句话要点**：提出ASFW数据集和FSE方法以解决真实世界面部阴影去除问题

**关键词**：面部阴影去除, 真实世界数据集, 图像增强, 计算机视觉基准, 深度学习模型

## 3 点简述
- 核心问题：现有方法在复杂光照下难以去除阴影并保留纹理，且缺乏真实配对数据集
- 方法要点：构建ASFW大规模真实配对数据集，并设计Face Shadow Eraser方法展示其有效性
- 实验或效果：ASFW提升模型在真实条件下的阴影去除性能，设定新标准

## 摘要（原文）

> Facial shadows often degrade image quality and the performance of vision algorithms. Existing methods struggle to remove shadows while preserving texture, especially under complex lighting conditions, and they lack real-world paired datasets for training. We present the Augmented Shadow Face in the Wild (ASFW) dataset, the first large-scale real-world dataset for facial shadow removal, containing 1,081 paired shadow and shadow-free images created via a professional Photoshop workflow. ASFW offers photorealistic shadow variations and accurate ground truths, bridging the gap between synthetic and real domains. Deep models trained on ASFW demonstrate improved shadow removal in real-world conditions. We also introduce the Face Shadow Eraser (FSE) method to showcase the effectiveness of the dataset. Experiments demonstrate that ASFW enhances the performance of facial shadow removal models, setting new standards for this task.

