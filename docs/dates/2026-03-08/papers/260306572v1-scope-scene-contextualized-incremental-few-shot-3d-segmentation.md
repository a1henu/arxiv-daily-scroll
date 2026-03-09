---
layout: default
title: SCOPE: Scene-Contextualized Incremental Few-Shot 3D Segmentation
---

# SCOPE: Scene-Contextualized Incremental Few-Shot 3D Segmentation
**arXiv**：[2603.06572v1](https://arxiv.org/abs/2603.06572) · [PDF](https://arxiv.org/pdf/2603.06572.pdf)  
**作者**：Vishal Thengane, Zhaochong An, Tianjin Huang, Son Lam Phung, Abdesselam Bouzerdoum, Lu Yin, Na Zhao, Xiatian Zhu  

**一句话要点**：提出SCOPE框架，通过背景引导的原型增强解决3D点云增量少样本分割中的灾难性遗忘和原型学习不足问题。

**关键词**：3D点云分割, 增量少样本学习, 原型增强, 背景引导, 灾难性遗忘, 即插即用框架

## 3 点简述
- 核心问题：3D点云增量少样本分割存在灾难性遗忘、稀疏监督下原型学习差，且忽略新类别常作为未标注背景出现。
- 方法要点：SCOPE为即插即用框架，利用类无关分割模型从背景提取伪实例构建原型池，融合少样本原型以增强表示。
- 实验或效果：在ScanNet和S3DIS上实现SOTA，新类别IoU提升最高6.98%和3.61%，平均IoU提升2.25%和1.70%，遗忘低。

## 摘要（原文）

> Incremental Few-Shot (IFS) segmentation aims to learn new categories over time from only a few annotations. Although widely studied in 2D, it remains underexplored for 3D point clouds. Existing methods suffer from catastrophic forgetting or fail to learn discriminative prototypes under sparse supervision, and often overlook a key cue: novel categories frequently appear as unlabelled background in base-training scenes. We introduce SCOPE (Scene-COntextualised Prototype Enrichment), a plug-and-play background-guided prototype enrichment framework that integrates with any prototype-based 3D segmentation method. After base training, a class-agnostic segmentation model extracts high-confidence pseudo-instances from background regions to build a prototype pool. When novel classes arrive with few labelled samples, relevant background prototypes are retrieved and fused with few-shot prototypes to form enriched representations without retraining the backbone or adding parameters. Experiments on ScanNet and S3DIS show that SCOPE achieves SOTA performance, improving novel-class IoU by up to 6.98% and 3.61%, and mean IoU by 2.25% and 1.70%, respectively, while maintaining low forgetting. Code is available https://github.com/Surrey-UP-Lab/SCOPE.

