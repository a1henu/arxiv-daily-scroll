---
layout: default
title: IndustryShapes: An RGB-D Benchmark dataset for 6D object pose estimation of industrial assembly components and tools
---

# IndustryShapes: An RGB-D Benchmark dataset for 6D object pose estimation of industrial assembly components and tools
**arXiv**：[2602.05555v1](https://arxiv.org/abs/2602.05555) · [PDF](https://arxiv.org/pdf/2602.05555.pdf)  
**作者**：Panagiotis Sapoutzoglou, Orestis Vaggelis, Athina Zacharia, Evangelos Sartinas, Maria Pateraki  

**一句话要点**：提出IndustryShapes数据集以解决工业场景中6D物体姿态估计的基准测试需求

**关键词**：6D物体姿态估计, 工业机器人, RGB-D数据集, 基准测试, 实例级姿态估计, 新物体姿态估计

## 3 点简述
- 核心问题：现有数据集多关注家庭或合成场景，缺乏工业组装环境的真实数据
- 方法要点：提供RGB-D基准数据集，包含经典集和扩展集，支持实例级和新物体姿态估计
- 实验或效果：评估现有方法显示该领域仍有改进空间，数据集包含静态上架序列

## 摘要（原文）

> We introduce IndustryShapes, a new RGB-D benchmark dataset of industrial tools and components, designed for both instance-level and novel object 6D pose estimation approaches. The dataset provides a realistic and application-relevant testbed for benchmarking these methods in the context of industrial robotics bridging the gap between lab-based research and deployment in real-world manufacturing scenarios. Unlike many previous datasets that focus on household or consumer products or use synthetic, clean tabletop datasets, or objects captured solely in controlled lab environments, IndustryShapes introduces five new object types with challenging properties, also captured in realistic industrial assembly settings. The dataset has diverse complexity, from simple to more challenging scenes, with single and multiple objects, including scenes with multiple instances of the same object and it is organized in two parts: the classic set and the extended set. The classic set includes a total of 4,6k images and 6k annotated poses. The extended set introduces additional data modalities to support the evaluation of model-free and sequence-based approaches. To the best of our knowledge, IndustryShapes is the first dataset to offer RGB-D static onboarding sequences. We further evaluate the dataset on a representative set of state-of-the art methods for instance-based and novel object 6D pose estimation, including also object detection, segmentation, showing that there is room for improvement in this domain. The dataset page can be found in https://pose-lab.github.io/IndustryShapes.

