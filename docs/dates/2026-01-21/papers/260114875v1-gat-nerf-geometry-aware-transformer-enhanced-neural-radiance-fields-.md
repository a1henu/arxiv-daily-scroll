---
layout: default
title: GAT-NeRF: Geometry-Aware-Transformer Enhanced Neural Radiance Fields for High-Fidelity 4D Facial Avatars
---

# GAT-NeRF: Geometry-Aware-Transformer Enhanced Neural Radiance Fields for High-Fidelity 4D Facial Avatars
**arXiv**：[2601.14875v1](https://arxiv.org/abs/2601.14875) · [PDF](https://arxiv.org/pdf/2601.14875.pdf)  
**作者**：Zhe Chang, Haodong Jin, Ying Sun, Yan Song, Hui Yu  

**一句话要点**：提出GAT-NeRF以增强单目视频中4D面部化身的高频细节重建

**关键词**：神经辐射场, 4D面部重建, Transformer增强, 几何先验, 单目视频, 动态细节建模

## 3 点简述
- 核心问题：单目视频信息受限，NeRF难以捕捉动态皱纹等高频面部细节。
- 方法要点：结合坐标对齐MLP与轻量Transformer，融合几何先验多模态输入增强特征表示。
- 实验或效果：实验显示在视觉保真度和高频细节恢复方面达到先进水平。

## 摘要（原文）

> High-fidelity 4D dynamic facial avatar reconstruction from monocular video is a critical yet challenging task, driven by increasing demands for immersive virtual human applications. While Neural Radiance Fields (NeRF) have advanced scene representation, their capacity to capture high-frequency facial details, such as dynamic wrinkles and subtle textures from information-constrained monocular streams, requires significant enhancement. To tackle this challenge, we propose a novel hybrid neural radiance field framework, called Geometry-Aware-Transformer Enhanced NeRF (GAT-NeRF) for high-fidelity and controllable 4D facial avatar reconstruction, which integrates the Transformer mechanism into the NeRF pipeline. GAT-NeRF synergistically combines a coordinate-aligned Multilayer Perceptron (MLP) with a lightweight Transformer module, termed as Geometry-Aware-Transformer (GAT) due to its processing of multi-modal inputs containing explicit geometric priors. The GAT module is enabled by fusing multi-modal input features, including 3D spatial coordinates, 3D Morphable Model (3DMM) expression parameters, and learnable latent codes to effectively learn and enhance feature representations pertinent to fine-grained geometry. The Transformer's effective feature learning capabilities are leveraged to significantly augment the modeling of complex local facial patterns like dynamic wrinkles and acne scars. Comprehensive experiments unequivocally demonstrate GAT-NeRF's state-of-the-art performance in visual fidelity and high-frequency detail recovery, forging new pathways for creating realistic dynamic digital humans for multimedia applications.

