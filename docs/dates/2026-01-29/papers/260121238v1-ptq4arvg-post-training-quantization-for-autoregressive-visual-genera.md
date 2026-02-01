---
layout: default
title: PTQ4ARVG: Post-Training Quantization for AutoRegressive Visual Generation Models
---

# PTQ4ARVG: Post-Training Quantization for AutoRegressive Visual Generation Models
**arXiv**：[2601.21238v1](https://arxiv.org/abs/2601.21238) · [PDF](https://arxiv.org/pdf/2601.21238.pdf)  
**作者**：Xuewen Liu, Zhikai Li, Jing Zhang, Mengjuan Chen, Qingyi Gu  

**一句话要点**：提出PTQ4ARVG框架以解决自回归视觉生成模型的后训练量化挑战

**关键词**：自回归视觉生成, 后训练量化, 模型压缩, 异常值处理, 分布校准, 低比特量化

## 3 点简述
- 核心问题：量化ARVG模型面临通道级异常值、令牌级动态激活和样本级分布不匹配三大挑战。
- 方法要点：采用增益投影缩放、静态令牌级量化和分布引导校准三种训练免费技术。
- 实验或效果：在8位和6位量化下保持ARVG模型性能，代码已开源。

## 摘要（原文）

> AutoRegressive Visual Generation (ARVG) models retain an architecture compatible with language models, while achieving performance comparable to diffusion-based models. Quantization is commonly employed in neural networks to reduce model size and computational latency. However, applying quantization to ARVG remains largely underexplored, and existing quantization methods fail to generalize effectively to ARVG models. In this paper, we explore this issue and identify three key challenges: (1) severe outliers at channel-wise level, (2) highly dynamic activations at token-wise level, and (3) mismatched distribution information at sample-wise level. To these ends, we propose PTQ4ARVG, a training-free post-training quantization (PTQ) framework consisting of: (1) Gain-Projected Scaling (GPS) mitigates the channel-wise outliers, which expands the quantization loss via a Taylor series to quantify the gain of scaling for activation-weight quantization, and derives the optimal scaling factor through differentiation.(2) Static Token-Wise Quantization (STWQ) leverages the inherent properties of ARVG, fixed token length and position-invariant distribution across samples, to address token-wise variance without incurring dynamic calibration overhead.(3) Distribution-Guided Calibration (DGC) selects samples that contribute most to distributional entropy, eliminating the sample-wise distribution mismatch. Extensive experiments show that PTQ4ARVG can effectively quantize the ARVG family models to 8-bit and 6-bit while maintaining competitive performance. Code is available at http://github.com/BienLuky/PTQ4ARVG .

