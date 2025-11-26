---
layout: default
title: UltraViCo: Breaking Extrapolation Limits in Video Diffusion Transformers
---

# UltraViCo: Breaking Extrapolation Limits in Video Diffusion Transformers
**arXiv**：[2511.20123v1](https://arxiv.org/abs/2511.20123) · [PDF](https://arxiv.org/pdf/2511.20123.pdf)  
**作者**：Min Zhao, Hongzhou Zhu, Yingze Wang, Bokai Yan, Jintao Zhang, Guande He, Ling Yang, Chongxuan Li, Jun Zhu  

**一句话要点**：提出UltraViCo方法以解决视频扩散变换器长度外推中的注意力分散问题

**关键词**：视频扩散变换器, 长度外推, 注意力机制, 训练免费方法, 可控视频合成

## 3 点简述
- 核心问题：视频长度外推时出现注意力分散，导致质量下降和周期性内容重复
- 方法要点：通过恒定衰减因子抑制训练窗口外令牌的注意力，无需训练即可应用
- 实验或效果：在4倍外推下，动态度和成像质量分别提升233%和40.5%

## 摘要（原文）

> Despite advances, video diffusion transformers still struggle to generalize beyond their training length, a challenge we term video length extrapolation. We identify two failure modes: model-specific periodic content repetition and a universal quality degradation. Prior works attempt to solve repetition via positional encodings, overlooking quality degradation and achieving only limited extrapolation. In this paper, we revisit this challenge from a more fundamental view: attention maps, which directly govern how context influences outputs. We identify that both failure modes arise from a unified cause: attention dispersion, where tokens beyond the training window dilute learned attention patterns. This leads to quality degradation and repetition emerges as a special case when this dispersion becomes structured into periodic attention patterns, induced by harmonic properties of positional encodings. Building on this insight, we propose UltraViCo, a training-free, plug-and-play method that suppresses attention for tokens beyond the training window via a constant decay factor. By jointly addressing both failure modes, we outperform a broad set of baselines largely across models and extrapolation ratios, pushing the extrapolation limit from 2x to 4x. Remarkably, it improves Dynamic Degree and Imaging Quality by 233% and 40.5% over the previous best method at 4x extrapolation. Furthermore, our method generalizes seamlessly to downstream tasks such as controllable video synthesis and editing.

