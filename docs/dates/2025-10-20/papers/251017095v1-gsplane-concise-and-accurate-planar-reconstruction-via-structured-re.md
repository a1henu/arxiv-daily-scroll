---
layout: default
title: GSPlane: Concise and Accurate Planar Reconstruction via Structured Representation
---

# GSPlane: Concise and Accurate Planar Reconstruction via Structured Representation
**arXiv**：[2510.17095v1](https://arxiv.org/abs/2510.17095) · [PDF](https://arxiv.org/pdf/2510.17095.pdf)  
**作者**：Ruitong Gan, Junran Peng, Yang Liu, Chuanchen Luo, Qing Li, Zhaoxiang Zhang  

**一句话要点**：提出GSPlane以解决高斯溅射在平面重建中平滑性和精度不足的问题

**关键词**：平面重建, 高斯溅射, 几何优化, 结构化表示, 网格简化

## 3 点简述
- 高斯溅射在平面区域重建中常缺乏平滑性和精度
- 利用分割和法线预测模型提取平面先验，增强几何一致性
- 实验显示在保持渲染质量下，显著提升网格几何准确性

## 摘要（原文）

> Planes are fundamental primitives of 3D sences, especially in man-made
> environments such as indoor spaces and urban streets. Representing these planes
> in a structured and parameterized format facilitates scene editing and physical
> simulations in downstream applications. Recently, Gaussian Splatting (GS) has
> demonstrated remarkable effectiveness in the Novel View Synthesis task, with
> extensions showing great potential in accurate surface reconstruction. However,
> even state-of-the-art GS representations often struggle to reconstruct planar
> regions with sufficient smoothness and precision. To address this issue, we
> propose GSPlane, which recovers accurate geometry and produces clean and
> well-structured mesh connectivity for plane regions in the reconstructed scene.
> By leveraging off-the-shelf segmentation and normal prediction models, GSPlane
> extracts robust planar priors to establish structured representations for
> planar Gaussian coordinates, which help guide the training process by enforcing
> geometric consistency. To further enhance training robustness, a Dynamic
> Gaussian Re-classifier is introduced to adaptively reclassify planar Gaussians
> with persistently high gradients as non-planar, ensuring more reliable
> optimization. Furthermore, we utilize the optimized planar priors to refine the
> mesh layouts, significantly improving topological structure while reducing the
> number of vertices and faces. We also explore applications of the structured
> planar representation, which enable decoupling and flexible manipulation of
> objects on supportive planes. Extensive experiments demonstrate that, with no
> sacrifice in rendering quality, the introduction of planar priors significantly
> improves the geometric accuracy of the extracted meshes across various
> baselines.

