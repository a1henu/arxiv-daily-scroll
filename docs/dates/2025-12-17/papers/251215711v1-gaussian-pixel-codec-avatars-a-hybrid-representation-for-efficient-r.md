---
layout: default
title: Gaussian Pixel Codec Avatars: A Hybrid Representation for Efficient Rendering
---

# Gaussian Pixel Codec Avatars: A Hybrid Representation for Efficient Rendering
**arXiv**：[2512.15711v1](https://arxiv.org/abs/2512.15711) · [PDF](https://arxiv.org/pdf/2512.15711.pdf)  
**作者**：Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Tomas Simon, Forrest Iandola, Giljoo Nam  

**一句话要点**：提出高斯像素编解码化身，结合网格与高斯实现移动端高效渲染

**关键词**：头部化身, 混合表示, 可微渲染, 3D高斯, 移动渲染, 多视图图像

## 3 点简述
- 核心问题：移动设备上高效渲染逼真头部化身，需平衡内存、渲染效率与真实感。
- 方法要点：采用三角形网格与各向异性3D高斯的混合表示，统一可微渲染管道处理网格为半透明层。
- 实验或效果：训练神经网络解码表情码，实现高斯化身的真实感与网格化身的渲染性能匹配。

## 摘要（原文）

> We present Gaussian Pixel Codec Avatars (GPiCA), photorealistic head avatars that can be generated from multi-view images and efficiently rendered on mobile devices. GPiCA utilizes a unique hybrid representation that combines a triangle mesh and anisotropic 3D Gaussians. This combination maximizes memory and rendering efficiency while maintaining a photorealistic appearance. The triangle mesh is highly efficient in representing surface areas like facial skin, while the 3D Gaussians effectively handle non-surface areas such as hair and beard. To this end, we develop a unified differentiable rendering pipeline that treats the mesh as a semi-transparent layer within the volumetric rendering paradigm of 3D Gaussian Splatting. We train neural networks to decode a facial expression code into three components: a 3D face mesh, an RGBA texture, and a set of 3D Gaussians. These components are rendered simultaneously in a unified rendering engine. The networks are trained using multi-view image supervision. Our results demonstrate that GPiCA achieves the realism of purely Gaussian-based avatars while matching the rendering performance of mesh-based avatars.

