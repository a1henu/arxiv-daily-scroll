---
layout: default
title: Point-Supervised Skeleton-Based Human Action Segmentation
---

# Point-Supervised Skeleton-Based Human Action Segmentation
**arXiv**：[2603.06201v1](https://arxiv.org/abs/2603.06201) · [PDF](https://arxiv.org/pdf/2603.06201.pdf)  
**作者**：Hongsong Wang, Yiqin Shen, Pengbo Yan, Jie Gui  

**一句话要点**：提出点监督框架以解决骨架动作分割中标注成本高和边界模糊问题

**关键词**：骨架动作分割, 点监督学习, 伪标签生成, 多模态特征, 动作边界检测, 标注效率

## 3 点简述
- 核心问题：骨架动作分割需帧级标注，成本高且边界模糊。
- 方法要点：使用点监督，结合原型相似性、能量函数和聚类生成伪标签。
- 实验或效果：在多个数据集上建立基准，性能竞争甚至超越全监督方法。

## 摘要（原文）

> Skeleton-based temporal action segmentation is a fundamental yet challenging task, playing a crucial role in enabling intelligent systems to perceive and respond to human activities. While fully-supervised methods achieve satisfactory performance, they require costly frame-level annotations and are sensitive to ambiguous action boundaries. To address these issues, we introduce a point-supervised framework for skeleton-based action segmentation, where only a single frame per action segment is labeled. We leverage multimodal skeleton data, including joint, bone, and motion information, encoded via a pretrained unified model to extract rich feature representations. To generate reliable pseudo-labels, we propose a novel prototype similarity method and integrate it with two existing methods: energy function and constrained K-Medoids clustering. Multimodal pseudo-label integration is proposed to enhance the reliability of the pseudo-label and guide the model training. We establish new benchmarks on PKU-MMD (X-Sub and X-View), MCFS-22, and MCFS-130, and implement baselines for point-supervised skeleton-based human action segmentation. Extensive experiments show that our method achieves competitive performance, even surpassing some fully-supervised methods while significantly reducing annotation effort.

