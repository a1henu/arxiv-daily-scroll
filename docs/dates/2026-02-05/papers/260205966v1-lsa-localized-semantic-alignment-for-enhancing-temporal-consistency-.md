---
layout: default
title: LSA: Localized Semantic Alignment for Enhancing Temporal Consistency in Traffic Video Generation
---

# LSA: Localized Semantic Alignment for Enhancing Temporal Consistency in Traffic Video Generation
**arXiv**：[2602.05966v1](https://arxiv.org/abs/2602.05966) · [PDF](https://arxiv.org/pdf/2602.05966.pdf)  
**作者**：Mirlan Karimov, Teodora Spasojevic, Markus Braun, Julian Wiederer, Vasileios Belagiannis, Marc Pollefeys  

**一句话要点**：提出局部语义对齐（LSA）以增强交通视频生成中的时间一致性

**关键词**：视频生成, 时间一致性, 语义对齐, 交通场景, 微调框架

## 3 点简述
- 核心问题：现有可控视频生成方法依赖推理时控制信号，限制其作为可扩展数据引擎的实用性。
- 方法要点：通过对齐真实与生成视频中动态对象周围的语义特征，结合扩散损失微调预训练模型。
- 实验或效果：在nuScenes和KITTI数据集上，单轮微调即提升评估指标，无需推理时外部控制信号。

## 摘要（原文）

> Controllable video generation has emerged as a versatile tool for autonomous driving, enabling realistic synthesis of traffic scenarios. However, existing methods depend on control signals at inference time to guide the generative model towards temporally consistent generation of dynamic objects, limiting their utility as scalable and generalizable data engines. In this work, we propose Localized Semantic Alignment (LSA), a simple yet effective framework for fine-tuning pre-trained video generation models. LSA enhances temporal consistency by aligning semantic features between ground-truth and generated video clips. Specifically, we compare the output of an off-the-shelf feature extraction model between the ground-truth and generated video clips localized around dynamic objects inducing a semantic feature consistency loss. We fine-tune the base model by combining this loss with the standard diffusion loss. The model fine-tuned for a single epoch with our novel loss outperforms the baselines in common video generation evaluation metrics. To further test the temporal consistency in generated videos we adapt two additional metrics from object detection task, namely mAP and mIoU. Extensive experiments on nuScenes and KITTI datasets show the effectiveness of our approach in enhancing temporal consistency in video generation without the need for external control signals during inference and any computational overheads.

