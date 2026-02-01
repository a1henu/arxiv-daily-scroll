---
layout: default
title: MetricAnything: Scaling Metric Depth Pretraining with Noisy Heterogeneous Sources
---

# MetricAnything: Scaling Metric Depth Pretraining with Noisy Heterogeneous Sources
**arXiv**：[2601.22054v1](https://arxiv.org/abs/2601.22054) · [PDF](https://arxiv.org/pdf/2601.22054.pdf)  
**作者**：Baorui Ma, Jiahui Yang, Donglin Di, Xuancheng Zhang, Jianxun Cui, Hao Li, Yan Xie, Wei Chen  

**一句话要点**：提出Metric Anything框架，通过稀疏度量提示从异构噪声数据中学习度量深度，实现可扩展预训练。

**关键词**：度量深度估计, 稀疏度量提示, 异构数据预训练, 视觉基础模型, 深度补全, 蒸馏学习

## 3 点简述
- 核心问题：度量深度估计面临传感器噪声、相机偏差和度量模糊性，阻碍了基础模型的扩展。
- 方法要点：使用稀疏度量提示作为通用接口，从约2000万图像-深度对中学习，无需手动提示或相机特定建模。
- 实验或效果：预训练模型在深度补全等任务中表现优异，蒸馏学生模型在单目深度估计等任务中达到先进水平。

## 摘要（原文）

> Scaling has powered recent advances in vision foundation models, yet extending this paradigm to metric depth estimation remains challenging due to heterogeneous sensor noise, camera-dependent biases, and metric ambiguity in noisy cross-source 3D data. We introduce Metric Anything, a simple and scalable pretraining framework that learns metric depth from noisy, diverse 3D sources without manually engineered prompts, camera-specific modeling, or task-specific architectures. Central to our approach is the Sparse Metric Prompt, created by randomly masking depth maps, which serves as a universal interface that decouples spatial reasoning from sensor and camera biases. Using about 20M image-depth pairs spanning reconstructed, captured, and rendered 3D data across 10000 camera models, we demonstrate-for the first time-a clear scaling trend in the metric depth track. The pretrained model excels at prompt-driven tasks such as depth completion, super-resolution and Radar-camera fusion, while its distilled prompt-free student achieves state-of-the-art results on monocular depth estimation, camera intrinsics recovery, single/multi-view metric 3D reconstruction, and VLA planning. We also show that using pretrained ViT of Metric Anything as a visual encoder significantly boosts Multimodal Large Language Model capabilities in spatial intelligence. These results show that metric depth estimation can benefit from the same scaling laws that drive modern foundation models, establishing a new path toward scalable and efficient real-world metric perception. We open-source MetricAnything at http://metric-anything.github.io/metric-anything-io/ to support community research.

