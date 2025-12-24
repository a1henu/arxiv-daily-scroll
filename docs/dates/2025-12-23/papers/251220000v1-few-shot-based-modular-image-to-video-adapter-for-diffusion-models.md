---
layout: default
title: Few-Shot-Based Modular Image-to-Video Adapter for Diffusion Models
---

# Few-Shot-Based Modular Image-to-Video Adapter for Diffusion Models
**arXiv**：[2512.20000v1](https://arxiv.org/abs/2512.20000) · [PDF](https://arxiv.org/pdf/2512.20000.pdf)  
**作者**：Zhenhao Li, Shaohan Yi, Zheng Liu, Leonartinus Gao, Minh Ngoc Le, Ambrose Ling, Zhuoran Wang, Md Amirul Islam, Zhixiang Chi, Yuanhao Yu  

**一句话要点**：提出模块化图像到视频适配器以解决扩散模型在图像动画中的运动控制难题

**关键词**：扩散模型, 图像动画, 少样本学习, 模块化适配器, 运动控制, 轻量网络

## 3 点简述
- 扩散模型在图像动画中面临数据稀缺导致运动记忆化而非提示遵从的问题
- MIVA作为轻量子网络，可捕获单一运动模式，支持少样本训练和并行扩展
- 实验显示MIVA在有限数据下实现精确运动控制，生成质量优于大规模数据集训练模型

## 摘要（原文）

> Diffusion models (DMs) have recently achieved impressive photorealism in image and video generation. However, their application to image animation remains limited, even when trained on large-scale datasets. Two primary challenges contribute to this: the high dimensionality of video signals leads to a scarcity of training data, causing DMs to favor memorization over prompt compliance when generating motion; moreover, DMs struggle to generalize to novel motion patterns not present in the training set, and fine-tuning them to learn such patterns, especially using limited training data, is still under-explored. To address these limitations, we propose Modular Image-to-Video Adapter (MIVA), a lightweight sub-network attachable to a pre-trained DM, each designed to capture a single motion pattern and scalable via parallelization. MIVAs can be efficiently trained on approximately ten samples using a single consumer-grade GPU. At inference time, users can specify motion by selecting one or multiple MIVAs, eliminating the need for prompt engineering. Extensive experiments demonstrate that MIVA enables more precise motion control while maintaining, or even surpassing, the generation quality of models trained on significantly larger datasets.

