---
layout: default
title: Range-Edit: Semantic Mask Guided Outdoor LiDAR Scene Editing
---

# Range-Edit: Semantic Mask Guided Outdoor LiDAR Scene Editing
**arXiv**：[2511.17269v1](https://arxiv.org/abs/2511.17269) · [PDF](https://arxiv.org/pdf/2511.17269.pdf)  
**作者**：Suchetan G. Uppur, Hemant Kumar, Vaibhav Kumar  

**一句话要点**：提出基于语义掩码的LiDAR场景编辑方法，以生成多样合成点云数据。

**关键词**：LiDAR点云编辑, 语义掩码引导, 扩散模型生成, 自动驾驶数据增强, 范围图像投影

## 3 点简述
- 核心问题：真实LiDAR数据难以获取复杂边缘案例，限制自动驾驶系统泛化。
- 方法要点：使用范围图像投影和语义掩码引导扩散模型，实现几何一致编辑。
- 实验或效果：在KITTI-360数据集验证，能生成高质量动态场景和边缘案例。

## 摘要（原文）

> Training autonomous driving and navigation systems requires large and diverse point cloud datasets that capture complex edge case scenarios from various dynamic urban settings. Acquiring such diverse scenarios from real-world point cloud data, especially for critical edge cases, is challenging, which restricts system generalization and robustness. Current methods rely on simulating point cloud data within handcrafted 3D virtual environments, which is time-consuming, computationally expensive, and often fails to fully capture the complexity of real-world scenes. To address some of these issues, this research proposes a novel approach that addresses the problem discussed by editing real-world LiDAR scans using semantic mask-based guidance to generate novel synthetic LiDAR point clouds. We incorporate range image projection and semantic mask conditioning to achieve diffusion-based generation. Point clouds are transformed to 2D range view images, which are used as an intermediate representation to enable semantic editing using convex hull-based semantic masks. These masks guide the generation process by providing information on the dimensions, orientations, and locations of objects in the real environment, ensuring geometric consistency and realism. This approach demonstrates high-quality LiDAR point cloud generation, capable of producing complex edge cases and dynamic scenes, as validated on the KITTI-360 dataset. This offers a cost-effective and scalable solution for generating diverse LiDAR data, a step toward improving the robustness of autonomous driving systems.

