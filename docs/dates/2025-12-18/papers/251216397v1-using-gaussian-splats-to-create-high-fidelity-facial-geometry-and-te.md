---
layout: default
title: Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture
---

# Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture
**arXiv**：[2512.16397v1](https://arxiv.org/abs/2512.16397) · [PDF](https://arxiv.org/pdf/2512.16397.pdf)  
**作者**：Haodi He, Jihun Yu, Ronald Fedkiw  

**一句话要点**：提出基于高斯溅射的统一人脸重建方法，从少量图像生成高保真几何与纹理

**关键词**：高斯溅射, 人脸重建, 神经纹理, 语义分割, 三角网格约束, 文本驱动资产创建

## 3 点简述
- 核心问题：从少量未校准图像重建统一、一致的人脸几何与纹理，避免依赖长视频
- 方法要点：利用高斯溅射结合语义分割和三角网格约束，实现结构化重建和纹理空间转换
- 实验或效果：仅需11张图像生成中性姿态，支持标准图形管线应用和文本驱动资产创建

## 摘要（原文）

> We leverage increasingly popular three-dimensional neural representations in order to construct a unified and consistent explanation of a collection of uncalibrated images of the human face. Our approach utilizes Gaussian Splatting, since it is more explicit and thus more amenable to constraints than NeRFs. We leverage segmentation annotations to align the semantic regions of the face, facilitating the reconstruction of a neutral pose from only 11 images (as opposed to requiring a long video). We soft constrain the Gaussians to an underlying triangulated surface in order to provide a more structured Gaussian Splat reconstruction, which in turn informs subsequent perturbations to increase the accuracy of the underlying triangulated surface. The resulting triangulated surface can then be used in a standard graphics pipeline. In addition, and perhaps most impactful, we show how accurate geometry enables the Gaussian Splats to be transformed into texture space where they can be treated as a view-dependent neural texture. This allows one to use high visual fidelity Gaussian Splatting on any asset in a scene without the need to modify any other asset or any other aspect (geometry, lighting, renderer, etc.) of the graphics pipeline. We utilize a relightable Gaussian model to disentangle texture from lighting in order to obtain a delit high-resolution albedo texture that is also readily usable in a standard graphics pipeline. The flexibility of our system allows for training with disparate images, even with incompatible lighting, facilitating robust regularization. Finally, we demonstrate the efficacy of our approach by illustrating its use in a text-driven asset creation pipeline.

