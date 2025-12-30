---
layout: default
title: SpatialMosaic: A Multiview VLM Dataset for Partial Visibility
---

# SpatialMosaic: A Multiview VLM Dataset for Partial Visibility
**arXiv**：[2512.23365v1](https://arxiv.org/abs/2512.23365) · [PDF](https://arxiv.org/pdf/2512.23365.pdf)  
**作者**：Kanghee Lee, Injae Lee, Minseok Kwak, Kwonyoung Ryu, Jungi Hong, Jaesik Park  

**一句话要点**：提出SpatialMosaic数据集与混合框架，以解决多视图视觉语言模型在部分可见性等现实挑战下的空间推理问题。

**关键词**：多视图视觉语言模型, 空间推理, 部分可见性, 数据集生成, 3D场景理解, 混合框架

## 3 点简述
- 核心问题：现有方法依赖预构建3D表示，难以处理部分可见性、遮挡等现实场景中的空间推理挑战。
- 方法要点：开发可扩展的多视图数据生成与标注流程，构建包含2M QA对的数据集，并引入混合框架集成3D重建模型作为几何编码器。
- 实验或效果：通过广泛实验验证数据集和任务能有效提升多视图条件下的空间推理能力，代码和数据集将公开。

## 摘要（原文）

> The rapid progress of Multimodal Large Language Models (MLLMs) has unlocked the potential for enhanced 3D scene understanding and spatial reasoning. However, existing approaches often rely on pre-constructed 3D representations or off-the-shelf reconstruction pipelines, which constrain scalability and real-world applicability. A recent line of work explores learning spatial reasoning directly from multi-view images, enabling Vision-Language Models (VLMs) to understand 3D scenes without explicit 3D reconstructions. Nevertheless, key challenges that frequently arise in real-world environments, such as partial visibility, occlusion, and low-overlap conditions that require spatial reasoning from fragmented visual cues, remain under-explored. To address these limitations, we propose a scalable multi-view data generation and annotation pipeline that constructs realistic spatial reasoning QAs, resulting in SpatialMosaic, a comprehensive instruction-tuning dataset featuring 2M QA pairs. We further introduce SpatialMosaic-Bench, a challenging benchmark for evaluating multi-view spatial reasoning under realistic and challenging scenarios, consisting of 1M QA pairs across 6 tasks. In addition, we present SpatialMosaicVLM, a hybrid framework that integrates 3D reconstruction models as geometry encoders within VLMs for robust spatial reasoning. Extensive experiments demonstrate that our proposed dataset and VQA tasks effectively enhance spatial reasoning under challenging multi-view conditions, validating the effectiveness of our data generation pipeline in constructing realistic and diverse QA pairs. Code and dataset will be available soon.

