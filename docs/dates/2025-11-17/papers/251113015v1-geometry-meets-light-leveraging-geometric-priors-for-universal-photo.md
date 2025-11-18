---
layout: default
title: Geometry Meets Light: Leveraging Geometric Priors for Universal Photometric Stereo under Limited Multi-Illumination Cues
---

# Geometry Meets Light: Leveraging Geometric Priors for Universal Photometric Stereo under Limited Multi-Illumination Cues
**arXiv**：[2511.13015v1](https://arxiv.org/abs/2511.13015) · [PDF](https://arxiv.org/pdf/2511.13015.pdf)  
**作者**：King-Man Tam, Satoshi Ikehata, Yuta Asano, Zhaoyi An, Rei Kawakami  

**一句话要点**：提出GeoUniPS以在有限多光照线索下提升通用光度立体性能

**关键词**：通用光度立体, 几何先验, 双分支编码器, 3D重建模型, 透视投影数据集

## 3 点简述
- 通用光度立体在多光照线索不可靠时性能下降，如偏置光照或阴影区域
- 集成合成监督与来自大规模3D重建模型的几何先验，设计光-几何双分支编码器
- 在多个数据集上实现最先进性能，尤其在复杂野外场景中表现优异

## 摘要（原文）

> Universal Photometric Stereo is a promising approach for recovering surface normals without strict lighting assumptions. However, it struggles when multi-illumination cues are unreliable, such as under biased lighting or in shadows or self-occluded regions of complex in-the-wild scenes. We propose GeoUniPS, a universal photometric stereo network that integrates synthetic supervision with high-level geometric priors from large-scale 3D reconstruction models pretrained on massive in-the-wild data. Our key insight is that these 3D reconstruction models serve as visual-geometry foundation models, inherently encoding rich geometric knowledge of real scenes. To leverage this, we design a Light-Geometry Dual-Branch Encoder that extracts both multi-illumination cues and geometric priors from the frozen 3D reconstruction model. We also address the limitations of the conventional orthographic projection assumption by introducing the PS-Perp dataset with realistic perspective projection to enable learning of spatially varying view directions. Extensive experiments demonstrate that GeoUniPS delivers state-of-the-arts performance across multiple datasets, both quantitatively and qualitatively, especially in the complex in-the-wild scenes.

