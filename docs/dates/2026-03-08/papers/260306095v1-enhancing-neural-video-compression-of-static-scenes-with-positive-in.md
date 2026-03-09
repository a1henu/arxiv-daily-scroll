---
layout: default
title: Enhancing Neural Video Compression of Static Scenes with Positive-Incentive Noise
---

# Enhancing Neural Video Compression of Static Scenes with Positive-Incentive Noise
**arXiv**：[2603.06095v1](https://arxiv.org/abs/2603.06095) · [PDF](https://arxiv.org/pdf/2603.06095.pdf)  
**作者**：Cheng Yuan, Zhenyu Jia, Jiawei Shao, Xuelong Li  

**一句话要点**：提出正激励噪声方法以增强静态场景视频的神经压缩效率

**关键词**：神经视频压缩, 静态场景视频, 正激励噪声, 时间冗余利用, 模型微调, 带宽节省

## 3 点简述
- 核心问题：静态场景视频压缩中，传统和神经方法分别存在时间冗余利用不足和训练-测试分布差距问题。
- 方法要点：将短期时间变化重新解释为正激励噪声，通过解耦瞬态变化与持久背景，内部化结构化先验信息。
- 实验或效果：初步实验显示，相比通用神经视频压缩模型，实现73%的BD率节省，保持像素级保真度。

## 摘要（原文）

> Static scene videos, such as surveillance feeds and videotelephony streams, constitute a dominant share of storage consumption and network traffic. However, both traditional standardized codecs and neural video compression (NVC) methods struggle to encode these videos efficiently due to inadequate usage of temporal redundancy and severe distribution gaps between training and test data, respectively. While recent generative compression methods improve perceptual quality, they introduce hallucinated details that are unacceptable in authenticity-critical applications. To overcome these limitations, we propose to incorporate positive-incentive noise into NVC for static scene videos, where short-term temporal changes are reinterpreted as positive-incentive noise to facilitate model finetuning. By disentangling transient variations from the persistent background, structured prior information is internalized in the compression model. During inference, the invariant component requires minimal signaling, thus reducing data transmission while maintaining pixel-level fidelity. Preliminary experiments demonstrate a 73% Bjøntegaard delta (BD) rate saving compared to general NVC models. Our method provides an effective solution to trade computation for bandwidth, enabling robust video transmission under adverse network conditions and economic long-term retention of surveillance footage.

