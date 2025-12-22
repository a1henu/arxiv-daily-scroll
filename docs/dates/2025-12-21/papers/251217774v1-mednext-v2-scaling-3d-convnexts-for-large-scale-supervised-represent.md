---
layout: default
title: MedNeXt-v2: Scaling 3D ConvNeXts for Large-Scale Supervised Representation Learning in Medical Image Segmentation
---

# MedNeXt-v2: Scaling 3D ConvNeXts for Large-Scale Supervised Representation Learning in Medical Image Segmentation
**arXiv**：[2512.17774v1](https://arxiv.org/abs/2512.17774) · [PDF](https://arxiv.org/pdf/2512.17774.pdf)  
**作者**：Saikat Roy, Yannick Kirchhoff, Constantin Ulrich, Maximillian Rokuss, Tassilo Wald, Fabian Isensee, Klaus Maier-Hein  

**一句话要点**：提出MedNeXt-v2以提升大规模监督预训练在3D医学图像分割中的表示学习效果

**关键词**：3D医学图像分割, 大规模监督预训练, ConvNeXt架构, 表示学习, 全局响应归一化

## 3 点简述
- 核心问题：现有大规模预训练忽视主干网络作为有效表示学习器的优化，导致性能受限
- 方法要点：基于ConvNeXt改进微架构，引入3D全局响应归一化模块，采用深度、宽度和上下文缩放
- 实验或效果：在18k CT体积上预训练，在六个CT和MR基准测试中实现最优性能，超越七个公开模型

## 摘要（原文）

> Large-scale supervised pretraining is rapidly reshaping 3D medical image segmentation. However, existing efforts focus primarily on increasing dataset size and overlook the question of whether the backbone network is an effective representation learner at scale. In this work, we address this gap by revisiting ConvNeXt-based architectures for volumetric segmentation and introducing MedNeXt-v2, a compound-scaled 3D ConvNeXt that leverages improved micro-architecture and data scaling to deliver state-of-the-art performance. First, we show that routinely used backbones in large-scale pretraining pipelines are often suboptimal. Subsequently, we use comprehensive backbone benchmarking prior to scaling and demonstrate that stronger from scratch performance reliably predicts stronger downstream performance after pretraining. Guided by these findings, we incorporate a 3D Global Response Normalization module and use depth, width, and context scaling to improve our architecture for effective representation learning. We pretrain MedNeXt-v2 on 18k CT volumes and demonstrate state-of-the-art performance when fine-tuning across six challenging CT and MR benchmarks (144 structures), showing consistent gains over seven publicly released pretrained models. Beyond improvements, our benchmarking of these models also reveals that stronger backbones yield better results on similar data, representation scaling disproportionately benefits pathological segmentation, and that modality-specific pretraining offers negligible benefit once full finetuning is applied. In conclusion, our results establish MedNeXt-v2 as a strong backbone for large-scale supervised representation learning in 3D Medical Image Segmentation. Our code and pretrained models are made available with the official nnUNet repository at: https://www.github.com/MIC-DKFZ/nnUNet

