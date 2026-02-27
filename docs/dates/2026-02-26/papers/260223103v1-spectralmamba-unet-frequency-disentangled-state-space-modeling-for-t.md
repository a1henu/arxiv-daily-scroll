---
layout: default
title: SpectralMamba-UNet: Frequency-Disentangled State Space Modeling for Texture-Structure Consistent Medical Image Segmentation
---

# SpectralMamba-UNet: Frequency-Disentangled State Space Modeling for Texture-Structure Consistent Medical Image Segmentation
**arXiv**：[2602.23103v1](https://arxiv.org/abs/2602.23103) · [PDF](https://arxiv.org/pdf/2602.23103.pdf)  
**作者**：Fuhao Zhang, Lei Liu, Jialin Zhang, Ya-Nan Zhang, Nan Mu  

**一句话要点**：提出SpectralMamba-UNet，通过频域解耦建模解决医学图像分割中全局结构与局部纹理一致性问题。

**关键词**：医学图像分割, 状态空间模型, 频域解耦, 离散余弦变换, 多尺度融合

## 3 点简述
- 核心问题：现有状态空间模型在医学图像分割中因一维序列化削弱局部空间连续性和高频细节表示。
- 方法要点：引入频域解耦框架，使用离散余弦变换分离低频和高频特征，分别通过频域Mamba建模全局上下文和保留边界细节。
- 实验或效果：在五个公开基准测试中验证了方法在不同模态和分割目标上的有效性和泛化能力。

## 摘要（原文）

> Accurate medical image segmentation requires effective modeling of both global anatomical structures and fine-grained boundary details. Recent state space models (e.g., Vision Mamba) offer efficient long-range dependency modeling. However, their one-dimensional serialization weakens local spatial continuity and high-frequency representation. To this end, we propose SpectralMamba-UNet, a novel frequency-disentangled framework to decouple the learning of structural and textural information in the spectral domain. Our Spectral Decomposition and Modeling (SDM) module applies discrete cosine transform to decompose low- and high-frequency features, where low frequency contributes to global contextual modeling via a frequency-domain Mamba and high frequency preserves boundary-sensitive details. To balance spectral contributions, we introduce a Spectral Channel Reweighting (SCR) mechanism to form channel-wise frequency-aware attention, and a Spectral-Guided Fusion (SGF) module to achieve adaptively multi-scale fusion in the decoder. Experiments on five public benchmarks demonstrate consistent improvements across diverse modalities and segmentation targets, validating the effectiveness and generalizability of our approach.

