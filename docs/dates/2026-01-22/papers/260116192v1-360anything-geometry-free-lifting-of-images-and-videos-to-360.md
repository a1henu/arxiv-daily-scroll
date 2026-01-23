---
layout: default
title: 360Anything: Geometry-Free Lifting of Images and Videos to 360°
---

# 360Anything: Geometry-Free Lifting of Images and Videos to 360°
**arXiv**：[2601.16192v1](https://arxiv.org/abs/2601.16192) · [PDF](https://arxiv.org/pdf/2601.16192.pdf)  
**作者**：Ziyi Wu, Daniel Watson, Andrea Tagliasacchi, David J. Fleet, Marcus A. Brubaker, Saurabh Saxena  

**一句话要点**：提出360Anything框架，以数据驱动方式实现无几何信息的图像和视频到360°全景的转换。

**关键词**：全景生成, 扩散变换器, 数据驱动映射, 循环潜在编码, 零样本估计

## 3 点简述
- 核心问题：现有方法依赖相机元数据，难以处理野外数据中缺失或噪声的校准信息。
- 方法要点：基于预训练扩散变换器，将透视输入和全景目标视为令牌序列，学习映射关系。
- 实验或效果：在图像和视频生成任务中达到最先进性能，并引入循环潜在编码消除边界伪影。

## 摘要（原文）

> Lifting perspective images and videos to 360° panoramas enables immersive 3D world generation. Existing approaches often rely on explicit geometric alignment between the perspective and the equirectangular projection (ERP) space. Yet, this requires known camera metadata, obscuring the application to in-the-wild data where such calibration is typically absent or noisy. We propose 360Anything, a geometry-free framework built upon pre-trained diffusion transformers. By treating the perspective input and the panorama target simply as token sequences, 360Anything learns the perspective-to-equirectangular mapping in a purely data-driven way, eliminating the need for camera information. Our approach achieves state-of-the-art performance on both image and video perspective-to-360° generation, outperforming prior works that use ground-truth camera information. We also trace the root cause of the seam artifacts at ERP boundaries to zero-padding in the VAE encoder, and introduce Circular Latent Encoding to facilitate seamless generation. Finally, we show competitive results in zero-shot camera FoV and orientation estimation benchmarks, demonstrating 360Anything's deep geometric understanding and broader utility in computer vision tasks. Additional results are available at https://360anything.github.io/.

