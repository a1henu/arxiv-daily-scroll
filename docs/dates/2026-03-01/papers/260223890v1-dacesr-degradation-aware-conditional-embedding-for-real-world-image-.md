---
layout: default
title: DACESR: Degradation-Aware Conditional Embedding for Real-World Image Super-Resolution
---

# DACESR: Degradation-Aware Conditional Embedding for Real-World Image Super-Resolution
**arXiv**：[2602.23890v1](https://arxiv.org/abs/2602.23890) · [PDF](https://arxiv.org/pdf/2602.23890.pdf)  
**作者**：Xiaoyan Lei, Wenlong Zhang, Biao Luo, Hui Liang, Weifeng Cao, Qiuting Lin  

**一句话要点**：提出DACESR方法，通过退化感知条件嵌入解决真实世界图像超分辨率问题。

**关键词**：图像超分辨率, 退化感知, 条件嵌入, Mamba网络, 真实世界应用

## 3 点简述
- 核心问题：多模态大模型在退化图像超分辨率中能力有限，难以平衡保真度和感知质量。
- 方法要点：使用退化选择策略训练真实嵌入提取器，结合条件特征调制器增强Mamba网络恢复纹理。
- 实验或效果：实验显示该方法有效提升退化图像识别性能，产生视觉愉悦结果，突显Mamba潜力。

## 摘要（原文）

> Multimodal large models have shown excellent ability in addressing image super-resolution in real-world scenarios by leveraging language class as condition information, yet their abilities in degraded images remain limited. In this paper, we first revisit the capabilities of the Recognize Anything Model (RAM) for degraded images by calculating text similarity. We find that directly using contrastive learning to fine-tune RAM in the degraded space is difficult to achieve acceptable results. To address this issue, we employ a degradation selection strategy to propose a Real Embedding Extractor (REE), which achieves significant recognition performance gain on degraded image content through contrastive learning. Furthermore, we use a Conditional Feature Modulator (CFM) to incorporate the high-level information of REE for a powerful Mamba-based network, which can leverage effective pixel information to restore image textures and produce visually pleasing results. Extensive experiments demonstrate that the REE can effectively help image super-resolution networks balance fidelity and perceptual quality, highlighting the great potential of Mamba in real-world applications. The source code of this work will be made publicly available at: https://github.com/nathan66666/DACESR.git

