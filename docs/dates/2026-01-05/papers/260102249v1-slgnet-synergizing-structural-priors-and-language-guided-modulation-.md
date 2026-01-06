---
layout: default
title: SLGNet: Synergizing Structural Priors and Language-Guided Modulation for Multimodal Object Detection
---

# SLGNet: Synergizing Structural Priors and Language-Guided Modulation for Multimodal Object Detection
**arXiv**：[2601.02249v1](https://arxiv.org/abs/2601.02249) · [PDF](https://arxiv.org/pdf/2601.02249.pdf)  
**作者**：Xiantai Xiang, Guangyao Zhou, Zixiao Wen, Wenshuai Li, Ben Niu, Feng Wang, Lijia Huang, Qiantong Wang, Yuhan Liu, Zongxu Pan, Yuxin Hu  

**一句话要点**：提出SLGNet，结合结构先验与语言引导调制，提升多模态目标检测在复杂场景下的性能。

**关键词**：多模态目标检测, 结构先验, 语言引导调制, 参数高效框架, 视觉Transformer

## 3 点简述
- 核心问题：现有方法在跨模态结构一致性和环境感知方面不足，导致复杂场景下检测性能受限。
- 方法要点：设计结构感知适配器提取层次结构表示，并引入语言引导调制模块动态校准视觉特征。
- 实验或效果：在多个数据集上实现SOTA，如LLVIP上mAP达66.1，参数减少约87%。

## 摘要（原文）

> Multimodal object detection leveraging RGB and Infrared (IR) images is pivotal for robust perception in all-weather scenarios. While recent adapter-based approaches efficiently transfer RGB-pretrained foundation models to this task, they often prioritize model efficiency at the expense of cross-modal structural consistency. Consequently, critical structural cues are frequently lost when significant domain gaps arise, such as in high-contrast or nighttime environments. Moreover, conventional static multimodal fusion mechanisms typically lack environmental awareness, resulting in suboptimal adaptation and constrained detection performance under complex, dynamic scene variations. To address these limitations, we propose SLGNet, a parameter-efficient framework that synergizes hierarchical structural priors and language-guided modulation within a frozen Vision Transformer (ViT)-based foundation model. Specifically, we design a Structure-Aware Adapter to extract hierarchical structural representations from both modalities and dynamically inject them into the ViT to compensate for structural degradation inherent in ViT-based backbones. Furthermore, we propose a Language-Guided Modulation module that exploits VLM-driven structured captions to dynamically recalibrate visual features, thereby endowing the model with robust environmental awareness. Extensive experiments on the LLVIP, FLIR, KAIST, and DroneVehicle datasets demonstrate that SLGNet establishes new state-of-the-art performance. Notably, on the LLVIP benchmark, our method achieves an mAP of 66.1, while reducing trainable parameters by approximately 87% compared to traditional full fine-tuning. This confirms SLGNet as a robust and efficient solution for multimodal perception.

