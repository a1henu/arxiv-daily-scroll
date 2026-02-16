---
layout: default
title: DynaGuide: A Generalizable Dynamic Guidance Framework for Unsupervised Semantic Segmentation
---

# DynaGuide: A Generalizable Dynamic Guidance Framework for Unsupervised Semantic Segmentation
**arXiv**：[2602.13020v1](https://arxiv.org/abs/2602.13020) · [PDF](https://arxiv.org/pdf/2602.13020.pdf)  
**作者**：Boujemaa Guermazi, Riadh Ksantini, Naimul Khan  

**一句话要点**：提出DynaGuide框架，通过动态双引导策略解决无监督语义分割中全局语义与局部边界协调问题。

**关键词**：无监督语义分割, 动态引导框架, 伪标签优化, 边界细化, 零射模型集成, 多组件损失

## 3 点简述
- 核心问题：现有方法难以平衡全局语义结构与细粒度边界精度，在无标注数据下性能受限。
- 方法要点：结合零射模型的全局伪标签与轻量CNN的局部边界优化，采用动态多组件损失函数进行训练。
- 实验效果：在BSD500、PASCAL VOC2012和COCO数据集上实现SOTA，mIoU提升显著，支持即插即用引导源。

## 摘要（原文）

> Unsupervised image segmentation is a critical task in computer vision. It enables dense scene understanding without human annotations, which is especially valuable in domains where labelled data is scarce. However, existing methods often struggle to reconcile global semantic structure with fine-grained boundary accuracy. This paper introduces DynaGuide, an adaptive segmentation framework that addresses these challenges through a novel dual-guidance strategy and dynamic loss optimization. Building on our previous work, DynaSeg, DynaGuide combines global pseudo-labels from zero-shot models such as DiffSeg or SegFormer with local boundary refinement using a lightweight CNN trained from scratch. This synergy allows the model to correct coarse or noisy global predictions and produce high-precision segmentations. At the heart of DynaGuide is a multi-component loss that dynamically balances feature similarity, Huber-smoothed spatial continuity, including diagonal relationships, and semantic alignment with the global pseudo-labels. Unlike prior approaches, DynaGuide trains entirely without ground-truth labels in the target domain and supports plug-and-play integration of diverse guidance sources. Extensive experiments on BSD500, PASCAL VOC2012, and COCO demonstrate that DynaGuide achieves state-of-the-art performance, improving mIoU by 17.5% on BSD500, 3.1% on PASCAL VOC2012, and 11.66% on COCO. With its modular design, strong generalization, and minimal computational footprint, DynaGuide offers a scalable and practical solution for unsupervised segmentation in real-world settings. Code available at: https://github.com/RyersonMultimediaLab/DynaGuide

