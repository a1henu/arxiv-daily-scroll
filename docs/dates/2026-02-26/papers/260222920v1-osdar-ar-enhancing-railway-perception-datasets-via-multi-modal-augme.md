---
layout: default
title: OSDaR-AR: Enhancing Railway Perception Datasets via Multi-modal Augmented Reality
---

# OSDaR-AR: Enhancing Railway Perception Datasets via Multi-modal Augmented Reality
**arXiv**：[2602.22920v1](https://arxiv.org/abs/2602.22920) · [PDF](https://arxiv.org/pdf/2602.22920.pdf)  
**作者**：Federico Nesti, Gianluca D'Amico, Mauro Marinoni, Giorgio Buttazzo  

**一句话要点**：提出多模态增强现实框架以解决铁路感知数据稀缺与真实感不足问题

**关键词**：铁路感知, 增强现实, 多模态数据, sim-to-real, 障碍检测, 公开数据集

## 3 点简述
- 铁路安全关键任务如障碍检测缺乏高质量标注数据，现有仿真器存在sim-to-real差距
- 利用Unreal Engine 5集成虚拟对象到真实铁路序列，基于LiDAR和INS/GNSS确保时空一致性
- 提出分割优化策略提升真实感，并发布OSDaR-AR公开数据集支持下一代系统开发

## 摘要（原文）

> Although deep learning has significantly advanced the perception capabilities of intelligent transportation systems, railway applications continue to suffer from a scarcity of high-quality, annotated data for safety-critical tasks like obstacle detection. While photorealistic simulators offer a solution, they often struggle with the ``sim-to-real" gap; conversely, simple image-masking techniques lack the spatio-temporal coherence required to obtain augmented single- and multi-frame scenes with the correct appearance and dimensions. This paper introduces a multi-modal augmented reality framework designed to bridge this gap by integrating photorealistic virtual objects into real-world railway sequences from the OSDaR23 dataset. Utilizing Unreal Engine 5 features, our pipeline leverages LiDAR point-clouds and INS/GNSS data to ensure accurate object placement and temporal stability across RGB frames. This paper also proposes a segmentation-based refinement strategy for INS/GNSS data to significantly improve the realism of the augmented sequences, as confirmed by the comparative study presented in the paper. Carefully designed augmented sequences are collected to produce OSDaR-AR, a public dataset designed to support the development of next-generation railway perception systems. The dataset is available at the following page: https://syndra.retis.santannapisa.it/osdarar.html

