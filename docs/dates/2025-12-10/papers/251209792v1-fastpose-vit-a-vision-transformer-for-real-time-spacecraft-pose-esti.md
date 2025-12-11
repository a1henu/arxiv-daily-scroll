---
layout: default
title: FastPose-ViT: A Vision Transformer for Real-Time Spacecraft Pose Estimation
---

# FastPose-ViT: A Vision Transformer for Real-Time Spacecraft Pose Estimation
**arXiv**：[2512.09792v1](https://arxiv.org/abs/2512.09792) · [PDF](https://arxiv.org/pdf/2512.09792.pdf)  
**作者**：Pierre Ancey, Andrew Price, Saqib Javed, Mathieu Salzmann  

**一句话要点**：提出FastPose-ViT以解决航天器实时姿态估计问题，基于Vision Transformer直接回归6DoF姿态。

**关键词**：航天器姿态估计, Vision Transformer, 实时计算, 边缘部署, 6DoF回归, 投影几何

## 3 点简述
- 核心问题：航天器6DoF姿态估计对自主操作至关重要，现有PnP方法计算量大，不适合资源受限边缘设备。
- 方法要点：采用Vision Transformer架构，通过裁剪图像和新颖数学形式主义，基于投影几何和表观旋转直接回归姿态。
- 实验或效果：在SPEED数据集上性能优于非PnP方法，与PnP方法竞争，量化后在NVIDIA Jetson Orin Nano上实现约75ms延迟和33FPS吞吐量。

## 摘要（原文）

> Estimating the 6-degrees-of-freedom (6DoF) pose of a spacecraft from a single image is critical for autonomous operations like in-orbit servicing and space debris removal. Existing state-of-the-art methods often rely on iterative Perspective-n-Point (PnP)-based algorithms, which are computationally intensive and ill-suited for real-time deployment on resource-constrained edge devices. To overcome these limitations, we propose FastPose-ViT, a Vision Transformer (ViT)-based architecture that directly regresses the 6DoF pose. Our approach processes cropped images from object bounding boxes and introduces a novel mathematical formalism to map these localized predictions back to the full-image scale. This formalism is derived from the principles of projective geometry and the concept of "apparent rotation", where the model predicts an apparent rotation matrix that is then corrected to find the true orientation. We demonstrate that our method outperforms other non-PnP strategies and achieves performance competitive with state-of-the-art PnP-based techniques on the SPEED dataset. Furthermore, we validate our model's suitability for real-world space missions by quantizing it and deploying it on power-constrained edge hardware. On the NVIDIA Jetson Orin Nano, our end-to-end pipeline achieves a latency of ~75 ms per frame under sequential execution, and a non-blocking throughput of up to 33 FPS when stages are scheduled concurrently.

