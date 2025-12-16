---
layout: default
title: USTM: Unified Spatial and Temporal Modeling for Continuous Sign Language Recognition
---

# USTM: Unified Spatial and Temporal Modeling for Continuous Sign Language Recognition
**arXiv**：[2512.13415v1](https://arxiv.org/abs/2512.13415) · [PDF](https://arxiv.org/pdf/2512.13415.pdf)  
**作者**：Ahmed Abul Hasanaath, Hamzah Luqman  

**一句话要点**：提出USTM框架，通过统一时空建模解决连续手语识别中细粒度特征和长程依赖问题。

**关键词**：连续手语识别, 时空建模, Swin Transformer, 轻量级适配器, RGB视频处理

## 3 点简述
- 核心问题：现有方法难以捕捉手语视频中的细粒度手部和面部线索及长程时间依赖。
- 方法要点：结合Swin Transformer骨干与轻量级时间适配器TAPE，实现高效时空特征提取。
- 实验或效果：在PHOENIX14等数据集上达到SOTA性能，仅用RGB视频超越多模态方法。

## 摘要（原文）

> Continuous sign language recognition (CSLR) requires precise spatio-temporal modeling to accurately recognize sequences of gestures in videos. Existing frameworks often rely on CNN-based spatial backbones combined with temporal convolution or recurrent modules. These techniques fail in capturing fine-grained hand and facial cues and modeling long-range temporal dependencies. To address these limitations, we propose the Unified Spatio-Temporal Modeling (USTM) framework, a spatio-temporal encoder that effectively models complex patterns using a combination of a Swin Transformer backbone enhanced with lightweight temporal adapter with positional embeddings (TAPE). Our framework captures fine-grained spatial features alongside short and long-term temporal context, enabling robust sign language recognition from RGB videos without relying on multi-stream inputs or auxiliary modalities. Extensive experiments on benchmarked datasets including PHOENIX14, PHOENIX14T, and CSL-Daily demonstrate that USTM achieves state-of-the-art performance against RGB-based as well as multi-modal CSLR approaches, while maintaining competitive performance against multi-stream approaches. These results highlight the strength and efficacy of the USTM framework for CSLR. The code is available at https://github.com/gufranSabri/USTM

