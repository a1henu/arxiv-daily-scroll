---
layout: default
title: Neural Texture Splatting: Expressive 3D Gaussian Splatting for View Synthesis, Geometry, and Dynamic Reconstruction
---

# Neural Texture Splatting: Expressive 3D Gaussian Splatting for View Synthesis, Geometry, and Dynamic Reconstruction
**arXiv**：[2511.18873v1](https://arxiv.org/abs/2511.18873) · [PDF](https://arxiv.org/pdf/2511.18873.pdf)  
**作者**：Yiming Wang, Shaofei Wang, Marko Mihajlovic, Siyu Tang  

**一句话要点**：提出神经纹理溅射以增强3D高斯溅射在视图合成、几何和动态重建中的表达力

**关键词**：3D高斯溅射, 神经纹理溅射, 视图合成, 几何重建, 动态重建, 全局神经场

## 3 点简述
- 3D高斯溅射表示能力受限，难以处理一般重建任务
- 引入全局神经场预测局部外观和几何，减少模型大小并促进信息交换
- 实验显示在稀疏和密集输入下，多基准测试中达到最先进性能

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a leading approach for high-quality novel view synthesis, with numerous variants extending its applicability to a broad spectrum of 3D and 4D scene reconstruction tasks. Despite its success, the representational capacity of 3DGS remains limited by the use of 3D Gaussian kernels to model local variations. Recent works have proposed to augment 3DGS with additional per-primitive capacity, such as per-splat textures, to enhance its expressiveness. However, these per-splat texture approaches primarily target dense novel view synthesis with a reduced number of Gaussian primitives, and their effectiveness tends to diminish when applied to more general reconstruction scenarios. In this paper, we aim to achieve concrete performance improvement over state-of-the-art 3DGS variants across a wide range of reconstruction tasks, including novel view synthesis, geometry and dynamic reconstruction, under both sparse and dense input settings. To this end, we introduce Neural Texture Splatting (NTS). At the core of our approach is a global neural field (represented as a hybrid of a tri-plane and a neural decoder) that predicts local appearance and geometric fields for each primitive. By leveraging this shared global representation that models local texture fields across primitives, we significantly reduce model size and facilitate efficient global information exchange, demonstrating strong generalization across tasks. Furthermore, our neural modeling of local texture fields introduces expressive view- and time-dependent effects, a critical aspect that existing methods fail to account for. Extensive experiments show that Neural Texture Splatting consistently improves models and achieves state-of-the-art results across multiple benchmarks.

