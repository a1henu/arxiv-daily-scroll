---
layout: default
title: CETCAM: Camera-Controllable Video Generation via Consistent and Extensible Tokenization
---

# CETCAM: Camera-Controllable Video Generation via Consistent and Extensible Tokenization
**arXiv**：[2512.19020v1](https://arxiv.org/abs/2512.19020) · [PDF](https://arxiv.org/pdf/2512.19020.pdf)  
**作者**：Zelin Zhao, Xinyu Gong, Bangya Liu, Ziyang Song, Jun Zhang, Suhui Wu, Yongxin Chen, Hao Zhang  

**一句话要点**：提出CETCAM框架，通过一致可扩展的标记化实现无相机标注的视频生成控制

**关键词**：相机可控视频生成, 几何感知标记化, 视频扩散模型, 深度估计, 无标注训练, 多模态控制

## 3 点简述
- 核心问题：现有方法依赖相机位姿标注，难以扩展且与深度估计不一致，导致训练测试差异
- 方法要点：利用几何基础模型估计深度和相机参数，转换为统一几何感知标记，通过轻量上下文块集成到预训练视频扩散模型
- 实验或效果：在多个基准测试中展示领先的几何一致性、时间稳定性和视觉真实感，并适应额外控制模态如修复和布局控制

## 摘要（原文）

> Achieving precise camera control in video generation remains challenging, as existing methods often rely on camera pose annotations that are difficult to scale to large and dynamic datasets and are frequently inconsistent with depth estimation, leading to train-test discrepancies. We introduce CETCAM, a camera-controllable video generation framework that eliminates the need for camera annotations through a consistent and extensible tokenization scheme. CETCAM leverages recent advances in geometry foundation models, such as VGGT, to estimate depth and camera parameters and converts them into unified, geometry-aware tokens. These tokens are seamlessly integrated into a pretrained video diffusion backbone via lightweight context blocks. Trained in two progressive stages, CETCAM first learns robust camera controllability from diverse raw video data and then refines fine-grained visual quality using curated high-fidelity datasets. Extensive experiments across multiple benchmarks demonstrate state-of-the-art geometric consistency, temporal stability, and visual realism. Moreover, CETCAM exhibits strong adaptability to additional control modalities, including inpainting and layout control, highlighting its flexibility beyond camera control. The project page is available at https://sjtuytc.github.io/CETCam_project_page.github.io/.

