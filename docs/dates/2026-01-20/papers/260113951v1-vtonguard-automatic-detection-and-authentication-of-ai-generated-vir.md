---
layout: default
title: VTONGuard: Automatic Detection and Authentication of AI-Generated Virtual Try-On Content
---

# VTONGuard: Automatic Detection and Authentication of AI-Generated Virtual Try-On Content
**arXiv**：[2601.13951v1](https://arxiv.org/abs/2601.13951) · [PDF](https://arxiv.org/pdf/2601.13951.pdf)  
**作者**：Shengyi Wu, Yan Hong, Shengyao Chen, Zheng Wang, Xianbing Sun, Jiahui Zhan, Jun Lan, Jianfu Zhang  

**一句话要点**：提出VTONGuard基准数据集与多任务框架，以检测和认证AI生成的虚拟试穿内容，促进负责任部署。

**关键词**：虚拟试穿检测, AI生成内容认证, 基准数据集, 多任务学习, 边界感知特征学习

## 3 点简述
- 核心问题：AI生成虚拟试穿内容真实性引发担忧，需可靠检测方法。
- 方法要点：构建大规模基准数据集，包含真实与合成图像，并设计集成辅助分割的多任务框架。
- 实验或效果：系统评估多种检测范式，新框架在基准上表现最佳，但跨范式泛化仍具挑战。

## 摘要（原文）

> With the rapid advancement of generative AI, virtual try-on (VTON) systems are becoming increasingly common in e-commerce and digital entertainment. However, the growing realism of AI-generated try-on content raises pressing concerns about authenticity and responsible use. To address this, we present VTONGuard, a large-scale benchmark dataset containing over 775,000 real and synthetic try-on images. The dataset covers diverse real-world conditions, including variations in pose, background, and garment styles, and provides both authentic and manipulated examples. Based on this benchmark, we conduct a systematic evaluation of multiple detection paradigms under unified training and testing protocols. Our results reveal each method's strengths and weaknesses and highlight the persistent challenge of cross-paradigm generalization. To further advance detection, we design a multi-task framework that integrates auxiliary segmentation to enhance boundary-aware feature learning, achieving the best overall performance on VTONGuard. We expect this benchmark to enable fair comparisons, facilitate the development of more robust detection models, and promote the safe and responsible deployment of VTON technologies in practice.

