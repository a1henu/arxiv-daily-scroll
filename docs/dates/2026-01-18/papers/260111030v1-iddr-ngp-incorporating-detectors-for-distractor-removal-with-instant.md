---
layout: default
title: IDDR-NGP: Incorporating Detectors for Distractor Removal with Instant Neural Radiance Field
---

# IDDR-NGP: Incorporating Detectors for Distractor Removal with Instant Neural Radiance Field
**arXiv**：[2601.11030v1](https://arxiv.org/abs/2601.11030) · [PDF](https://arxiv.org/pdf/2601.11030.pdf)  
**作者**：Xianliang Huang, Jiajie Gou, Shuhang Chen, Zhizhou Zhong, Jihong Guan, Shuigeng Zhou  

**一句话要点**：提出IDDR-NGP，结合检测器与Instant-NGP实现统一3D场景干扰物去除

**关键词**：干扰物去除, 神经辐射场, 多视图优化, 3D场景重建, 端到端训练

## 3 点简述
- 核心问题：现有方法通常针对特定类型干扰物，缺乏统一去除多种3D场景干扰物的能力
- 方法要点：通过结合隐式3D表示与2D检测器，设计LPIPS损失和多视图补偿损失进行端到端优化
- 实验或效果：在合成和真实数据集上验证有效性，能去除雪花、彩纸等多种干扰物，性能可比现有SOTA

## 摘要（原文）

> This paper presents the first unified distractor removal method, named IDDR-NGP, which directly operates on Instant-NPG. The method is able to remove a wide range of distractors in 3D scenes, such as snowflakes, confetti, defoliation and petals, whereas existing methods usually focus on a specific type of distractors. By incorporating implicit 3D representations with 2D detectors, we demonstrate that it is possible to efficiently restore 3D scenes from multiple corrupted images. We design the learned perceptual image patch similarity~( LPIPS) loss and the multi-view compensation loss (MVCL) to jointly optimize the rendering results of IDDR-NGP, which could aggregate information from multi-view corrupted images. All of them can be trained in an end-to-end manner to synthesize high-quality 3D scenes. To support the research on distractors removal in implicit 3D representations, we build a new benchmark dataset that consists of both synthetic and real-world distractors. To validate the effectiveness and robustness of IDDR-NGP, we provide a wide range of distractors with corresponding annotated labels added to both realistic and synthetic scenes. Extensive experimental results demonstrate the effectiveness and robustness of IDDR-NGP in removing multiple types of distractors. In addition, our approach achieves results comparable with the existing SOTA desnow methods and is capable of accurately removing both realistic and synthetic distractors.

