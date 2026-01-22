---
layout: default
title: Pb4U-GNet: Resolution-Adaptive Garment Simulation via Propagation-before-Update Graph Network
---

# Pb4U-GNet: Resolution-Adaptive Garment Simulation via Propagation-before-Update Graph Network
**arXiv**：[2601.15110v1](https://arxiv.org/abs/2601.15110) · [PDF](https://arxiv.org/pdf/2601.15110.pdf)  
**作者**：Aoran Liu, Kun Hu, Clinton Ansun Mo, Qiuxia Wu, Wenxiong Kang, Zhiyong Wang  

**一句话要点**：提出Pb4U-GNet以解决服装模拟中跨分辨率泛化差的问题

**关键词**：服装模拟, 图神经网络, 分辨率自适应, 传播-更新解耦, 跨分辨率泛化

## 3 点简述
- 核心问题：现有图神经网络在服装模拟中因固定传播深度和分辨率依赖位移导致跨分辨率泛化性能下降
- 方法要点：通过传播-更新解耦框架，结合动态传播深度控制和几何感知更新缩放实现分辨率自适应
- 实验或效果：仅用低分辨率网格训练，在多种分辨率上表现出强泛化能力，解决了神经服装模拟的关键挑战

## 摘要（原文）

> Garment simulation is fundamental to various applications in computer vision and graphics, from virtual try-on to digital human modelling. However, conventional physics-based methods remain computationally expensive, hindering their application in time-sensitive scenarios. While graph neural networks (GNNs) offer promising acceleration, existing approaches exhibit poor cross-resolution generalisation, demonstrating significant performance degradation on higher-resolution meshes beyond the training distribution. This stems from two key factors: (1) existing GNNs employ fixed message-passing depth that fails to adapt information aggregation to mesh density variation, and (2) vertex-wise displacement magnitudes are inherently resolution-dependent in garment simulation. To address these issues, we introduce Propagation-before-Update Graph Network (Pb4U-GNet), a resolution-adaptive framework that decouples message propagation from feature updates. Pb4U-GNet incorporates two key mechanisms: (1) dynamic propagation depth control, adjusting message-passing iterations based on mesh resolution, and (2) geometry-aware update scaling, which scales predictions according to local mesh characteristics. Extensive experiments show that even trained solely on low-resolution meshes, Pb4U-GNet exhibits strong generalisability across diverse mesh resolutions, addressing a fundamental challenge in neural garment simulation.

