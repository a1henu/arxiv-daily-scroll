---
layout: default
title: A Unified Framework for Multimodal Image Reconstruction and Synthesis using Denoising Diffusion Models
---

# A Unified Framework for Multimodal Image Reconstruction and Synthesis using Denoising Diffusion Models
**arXiv**：[2602.08249v1](https://arxiv.org/abs/2602.08249) · [PDF](https://arxiv.org/pdf/2602.08249.pdf)  
**作者**：Weijie Gan, Xucheng Wang, Tongyao Wang, Wenshang Wang, Chunwei Ying, Yuyang Hu, Yasheng Chen, Hongyu An, Ulugbek S. Kamilov  

**一句话要点**：提出Any2all统一框架，利用去噪扩散模型解决多模态图像重建与合成的虚拟修复问题。

**关键词**：多模态图像重建, 图像合成, 去噪扩散模型, 虚拟修复, 统一框架

## 3 点简述
- 核心问题：现有方法需多个任务特定模型，处理不完整多模态成像数据时训练部署复杂。
- 方法要点：训练单一无条件扩散模型，通过虚拟修复从任意输入组合生成所有目标模态。
- 实验或效果：在PET/MR/CT脑数据集验证，性能优于专用方法，失真度竞争且感知质量更优。

## 摘要（原文）

> Image reconstruction and image synthesis are important for handling incomplete multimodal imaging data, but existing methods require various task-specific models, complicating training and deployment workflows. We introduce Any2all, a unified framework that addresses this limitation by formulating these disparate tasks as a single virtual inpainting problem. We train a single, unconditional diffusion model on the complete multimodal data stack. This model is then adapted at inference time to ``inpaint'' all target modalities from any combination of inputs of available clean images or noisy measurements. We validated Any2all on a PET/MR/CT brain dataset. Our results show that Any2all can achieve excellent performance on both multimodal reconstruction and synthesis tasks, consistently yielding images with competitive distortion-based performance and superior perceptual quality over specialized methods.

