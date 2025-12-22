---
layout: default
title: Any-Optical-Model: A Universal Foundation Model for Optical Remote Sensing
---

# Any-Optical-Model: A Universal Foundation Model for Optical Remote Sensing
**arXiv**：[2512.17224v1](https://arxiv.org/abs/2512.17224) · [PDF](https://arxiv.org/pdf/2512.17224.pdf)  
**作者**：Xuyang Li, Chenyu Li, Danfeng Hong  

**一句话要点**：提出Any-Optical-Model以解决光学遥感基础模型在任意波段、传感器和分辨率下的泛化挑战

**关键词**：光学遥感基础模型, 频谱无关分词器, 多尺度自适应嵌入, 跨传感器融合, 波段缺失处理, 自监督预训练

## 3 点简述
- 核心问题：现有遥感基础模型因固定波段配置和分辨率，难以处理波段缺失、跨传感器融合和未知空间尺度等实际场景。
- 方法要点：引入频谱无关分词器、多尺度自适应补丁嵌入机制和多尺度语义对齐，以编码光谱身份并捕获跨分辨率纹理。
- 实验或效果：在超过10个公共数据集上验证，在波段缺失、跨传感器和跨分辨率设置下达到先进性能。

## 摘要（原文）

> Optical satellites, with their diverse band layouts and ground sampling distances, supply indispensable evidence for tasks ranging from ecosystem surveillance to emergency response. However, significant discrepancies in band composition and spatial resolution across different optical sensors present major challenges for existing Remote Sensing Foundation Models (RSFMs). These models are typically pretrained on fixed band configurations and resolutions, making them vulnerable to real world scenarios involving missing bands, cross sensor fusion, and unseen spatial scales, thereby limiting their generalization and practical deployment. To address these limitations, we propose Any Optical Model (AOM), a universal RSFM explicitly designed to accommodate arbitrary band compositions, sensor types, and resolution scales. To preserve distinctive spectral characteristics even when bands are missing or newly introduced, AOM introduces a spectrum-independent tokenizer that assigns each channel a dedicated band embedding, enabling explicit encoding of spectral identity. To effectively capture texture and contextual patterns from sub-meter to hundred-meter imagery, we design a multi-scale adaptive patch embedding mechanism that dynamically modulates the receptive field. Furthermore, to maintain global semantic consistency across varying resolutions, AOM incorporates a multi-scale semantic alignment mechanism alongside a channel-wise self-supervised masking and reconstruction pretraining strategy that jointly models spectral-spatial relationships. Extensive experiments on over 10 public datasets, including those from Sentinel-2, Landsat, and HLS, demonstrate that AOM consistently achieves state-of-the-art (SOTA) performance under challenging conditions such as band missing, cross sensor, and cross resolution settings.

