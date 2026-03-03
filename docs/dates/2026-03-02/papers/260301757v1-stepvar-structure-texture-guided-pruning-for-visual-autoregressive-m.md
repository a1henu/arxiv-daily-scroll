---
layout: default
title: StepVAR: Structure-Texture Guided Pruning for Visual Autoregressive Models
---

# StepVAR: Structure-Texture Guided Pruning for Visual Autoregressive Models
**arXiv**：[2603.01757v1](https://arxiv.org/abs/2603.01757) · [PDF](https://arxiv.org/pdf/2603.01757.pdf)  
**作者**：Keli Liu, Zhendong Wang, Wengang Zhou, Houqiang Li  

**一句话要点**：提出StepVAR以加速视觉自回归模型推理，通过结构-纹理引导的剪枝保持生成质量。

**关键词**：视觉自回归模型, 令牌剪枝, 结构-纹理引导, 推理加速, 训练无关方法

## 3 点简述
- 视觉自回归模型在高分辨率下推理成本二次增长，后期尺度存在空间冗余。
- StepVAR结合高通滤波和PCA，联合评估结构-纹理重要性进行训练无关的令牌剪枝。
- 实验表明StepVAR在文本到图像和视频模型中加速推理，同时维持生成质量。

## 摘要（原文）

> Visual AutoRegressive (VAR) models based on next-scale prediction enable efficient hierarchical generation, yet the inference cost grows quadratically at high resolutions. We observe that the computationally intensive later scales predominantly refine high-frequency textures and exhibit substantial spatial redundancy, in contrast to earlier scales that determine the global structural layout. Existing pruning methods primarily focus on high-frequency detection for token selection, often overlooking structural coherence and consequently degrading global semantics. To address this limitation, we propose StepVAR, a training-free token pruning framework that accelerates VAR inference by jointly considering structural and textural importance. Specifically, we employ a lightweight high-pass filter to capture local texture details, while leveraging Principal Component Analysis (PCA) to preserve global structural information. This dual-criterion design enables the model to retain tokens critical for both fine-grained fidelity and overall composition. To maintain valid next-scale prediction under sparse tokens, we further introduce a nearest neighbor feature propagation strategy to reconstruct dense feature maps from pruned representations. Extensive experiments on state-of-the-art text-to-image and text-to-video VAR models demonstrate that StepVAR achieves substantial inference speedups while maintaining generation quality. Quantitative and qualitative evaluations consistently show that our method outperforms existing acceleration approaches, validating its effectiveness and general applicability across diverse VAR architectures.

