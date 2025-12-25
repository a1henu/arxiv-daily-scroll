---
layout: default
title: FluencyVE: Marrying Temporal-Aware Mamba with Bypass Attention for Video Editing
---

# FluencyVE: Marrying Temporal-Aware Mamba with Bypass Attention for Video Editing
**arXiv**：[2512.21015v1](https://arxiv.org/abs/2512.21015) · [PDF](https://arxiv.org/pdf/2512.21015.pdf)  
**作者**：Mingshu Cai, Yixuan Li, Osamu Yoshie, Yuya Ieiri  

**一句话要点**：提出FluencyVE，结合Mamba与旁路注意力以解决视频编辑中的时序不一致与高计算成本问题。

**关键词**：视频编辑, 时序建模, Mamba模型, 低秩近似, 计算效率, Stable Diffusion

## 3 点简述
- 核心问题：现有视频编辑方法存在时序不一致和高计算开销，难以扩展文本到图像模型的成功。
- 方法要点：集成Mamba模块替代时序注意力，采用低秩近似和加权平均技术以保持生成能力并降低计算负担。
- 实验或效果：在真实视频中编辑属性、主体和位置方面展示出有前景的结果，验证了方法的有效性。

## 摘要（原文）

> Large-scale text-to-image diffusion models have achieved unprecedented success in image generation and editing. However, extending this success to video editing remains challenging. Recent video editing efforts have adapted pretrained text-to-image models by adding temporal attention mechanisms to handle video tasks. Unfortunately, these methods continue to suffer from temporal inconsistency issues and high computational overheads. In this study, we propose FluencyVE, which is a simple yet effective one-shot video editing approach. FluencyVE integrates the linear time-series module, Mamba, into a video editing model based on pretrained Stable Diffusion models, replacing the temporal attention layer. This enables global frame-level attention while reducing the computational costs. In addition, we employ low-rank approximation matrices to replace the query and key weight matrices in the causal attention, and use a weighted averaging technique during training to update the attention scores. This approach significantly preserves the generative power of the text-to-image model while effectively reducing the computational burden. Experiments and analyses demonstrate promising results in editing various attributes, subjects, and locations in real-world videos.

