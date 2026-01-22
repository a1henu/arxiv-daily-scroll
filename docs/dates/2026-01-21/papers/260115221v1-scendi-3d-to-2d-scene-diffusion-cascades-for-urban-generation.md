---
layout: default
title: ScenDi: 3D-to-2D Scene Diffusion Cascades for Urban Generation
---

# ScenDi: 3D-to-2D Scene Diffusion Cascades for Urban Generation
**arXiv**：[2601.15221v1](https://arxiv.org/abs/2601.15221) · [PDF](https://arxiv.org/pdf/2601.15221.pdf)  
**作者**：Hanlei Guo, Jiahao Shao, Xinya Chen, Xiyang Tan, Sheng Miao, Yujun Shen, Yiyi Liao  

**一句话要点**：提出ScenDi方法，通过3D与2D扩散模型级联生成可控城市场景，解决细节与相机控制平衡问题。

**关键词**：城市场景生成, 扩散模型, 3D高斯, 视频扩散, 相机控制, 条件合成

## 3 点简述
- 核心问题：现有3D扩散模型细节退化，2D扩散模型相机控制性差，城市场景生成面临挑战。
- 方法要点：先训练3D潜在扩散模型生成3D高斯，再以渲染图像为条件训练2D视频扩散模型增强细节。
- 实验或效果：在Waymo和KITTI-360数据集上验证，能基于输入条件生成场景并遵循准确相机轨迹。

## 摘要（原文）

> Recent advancements in 3D object generation using diffusion models have achieved remarkable success, but generating realistic 3D urban scenes remains challenging. Existing methods relying solely on 3D diffusion models tend to suffer a degradation in appearance details, while those utilizing only 2D diffusion models typically compromise camera controllability. To overcome this limitation, we propose ScenDi, a method for urban scene generation that integrates both 3D and 2D diffusion models. We first train a 3D latent diffusion model to generate 3D Gaussians, enabling the rendering of images at a relatively low resolution. To enable controllable synthesis, this 3DGS generation process can be optionally conditioned by specifying inputs such as 3d bounding boxes, road maps, or text prompts. Then, we train a 2D video diffusion model to enhance appearance details conditioned on rendered images from the 3D Gaussians. By leveraging the coarse 3D scene as guidance for 2D video diffusion, ScenDi generates desired scenes based on input conditions and successfully adheres to accurate camera trajectories. Experiments on two challenging real-world datasets, Waymo and KITTI-360, demonstrate the effectiveness of our approach.

