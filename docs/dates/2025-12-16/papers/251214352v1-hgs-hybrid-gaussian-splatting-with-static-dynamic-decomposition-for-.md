---
layout: default
title: HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis
---

# HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis
**arXiv**：[2512.14352v1](https://arxiv.org/abs/2512.14352) · [PDF](https://arxiv.org/pdf/2512.14352.pdf)  
**作者**：Kaizhe Zhang, Yijie Zhou, Weizhan Zhang, Caixia Yan, Haipeng Du, yugui xie, Yu-Hui Wen, Yong-Jin Liu  

**一句话要点**：提出混合高斯溅射框架，通过静态-动态分解实现紧凑动态视图合成

**关键词**：动态视图合成, 高斯溅射, 静态-动态分解, 径向基函数, 实时渲染, 模型压缩

## 3 点简述
- 核心问题：现有动态视图合成方法模型复杂、参数冗余，导致模型大、渲染慢，不适用于实时应用。
- 方法要点：采用静态-动态分解策略，动态区域用时变径向基函数建模，静态区域共享时不变参数以减少冗余。
- 实验或效果：模型大小减少高达98%，在RTX 3090上4K分辨率达125 FPS，渲染质量与先进方法相当，细节和突变场景保真度高。

## 摘要（原文）

> Dynamic novel view synthesis (NVS) is essential for creating immersive experiences. Existing approaches have advanced dynamic NVS by introducing 3D Gaussian Splatting (3DGS) with implicit deformation fields or indiscriminately assigned time-varying parameters, surpassing NeRF-based methods. However, due to excessive model complexity and parameter redundancy, they incur large model sizes and slow rendering speeds, making them inefficient for real-time applications, particularly on resource-constrained devices. To obtain a more efficient model with fewer redundant parameters, in this paper, we propose Hybrid Gaussian Splatting (HGS), a compact and efficient framework explicitly designed to disentangle static and dynamic regions of a scene within a unified representation. The core innovation of HGS lies in our Static-Dynamic Decomposition (SDD) strategy, which leverages Radial Basis Function (RBF) modeling for Gaussian primitives. Specifically, for dynamic regions, we employ time-dependent RBFs to effectively capture temporal variations and handle abrupt scene changes, while for static regions, we reduce redundancy by sharing temporally invariant parameters. Additionally, we introduce a two-stage training strategy tailored for explicit models to enhance temporal coherence at static-dynamic boundaries. Experimental results demonstrate that our method reduces model size by up to 98% and achieves real-time rendering at up to 125 FPS at 4K resolution on a single RTX 3090 GPU. It further sustains 160 FPS at 1352 * 1014 on an RTX 3050 and has been integrated into the VR system. Moreover, HGS achieves comparable rendering quality to state-of-the-art methods while providing significantly improved visual fidelity for high-frequency details and abrupt scene changes.

