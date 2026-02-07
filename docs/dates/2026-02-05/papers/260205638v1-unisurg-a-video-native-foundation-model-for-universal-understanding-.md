---
layout: default
title: UniSurg: A Video-Native Foundation Model for Universal Understanding of Surgical Videos
---

# UniSurg: A Video-Native Foundation Model for Universal Understanding of Surgical Videos
**arXiv**：[2602.05638v1](https://arxiv.org/abs/2602.05638) · [PDF](https://arxiv.org/pdf/2602.05638.pdf)  
**作者**：Jinlin Wu, Felix Holm, Chuxi Chen, An Wang, Yaxin Hu, Xiaofan Ye, Zelin Zang, Miao Xu, Lihua Zhou, Huai Liao, Danny T. M. Chan, Ming Feng, Wai S. Poon, Hongliang Ren, Dong Yi, Nassir Navab, Gaofeng Meng, Jiebo Luo, Hongbin Liu, Zhen Lei  

**一句话要点**：提出UniSurg视频原生基础模型，通过潜在运动预测实现手术视频的通用理解。

**关键词**：手术视频分析, 基础模型, 潜在运动预测, 自蒸馏训练, 大规模数据集

## 3 点简述
- 核心问题：现有基础模型依赖像素级重建，浪费模型容量于低层次视觉细节，而非手术理解所需的语义结构。
- 方法要点：基于V-JEPA架构，引入运动引导潜在预测、时空亲和自蒸馏和特征多样性正则化，专注于语义区域和关系一致性。
- 实验或效果：在17个基准测试中显著优于现有方法，包括手术流程识别、动作三元组识别、技能评估、息肉分割和深度估计。

## 摘要（原文）

> While foundation models have advanced surgical video analysis, current approaches rely predominantly on pixel-level reconstruction objectives that waste model capacity on low-level visual details - such as smoke, specular reflections, and fluid motion - rather than semantic structures essential for surgical understanding. We present UniSurg, a video-native foundation model that shifts the learning paradigm from pixel-level reconstruction to latent motion prediction. Built on the Video Joint Embedding Predictive Architecture (V-JEPA), UniSurg introduces three key technical innovations tailored to surgical videos: 1) motion-guided latent prediction to prioritize semantically meaningful regions, 2) spatiotemporal affinity self-distillation to enforce relational consistency, and 3) feature diversity regularization to prevent representation collapse in texture-sparse surgical scenes. To enable large-scale pretraining, we curate UniSurg-15M, the largest surgical video dataset to date, comprising 3,658 hours of video from 50 sources across 13 anatomical regions. Extensive experiments across 17 benchmarks demonstrate that UniSurg significantly outperforms state-of-the-art methods on surgical workflow recognition (+14.6% F1 on EgoSurgery, +10.3% on PitVis), action triplet recognition (39.54% mAP-IVT on CholecT50), skill assessment, polyp segmentation, and depth estimation. These results establish UniSurg as a new standard for universal, motion-oriented surgical video understanding.

