---
layout: default
title: Vision-Language Controlled Deep Unfolding for Joint Medical Image Restoration and Segmentation
---

# Vision-Language Controlled Deep Unfolding for Joint Medical Image Restoration and Segmentation
**arXiv**：[2601.23103v1](https://arxiv.org/abs/2601.23103) · [PDF](https://arxiv.org/pdf/2601.23103.pdf)  
**作者**：Ping Chen, Zicheng Huang, Xiangming Wang, Yungeng Liu, Bingyu Liang, Haijin Zeng, Yongyong Chen  

**一句话要点**：提出VL-DUN框架，通过联合优化解决医学图像恢复与分割的协同问题。

**关键词**：医学图像处理, 联合优化, 深度展开, Mamba机制, 图像恢复, 图像分割

## 3 点简述
- 核心问题：传统方法孤立处理医学图像恢复与分割，导致次优结果，缺乏协同优化。
- 方法要点：采用联合展开机制和频率感知Mamba机制，实现恢复与分割的数学耦合与高效全局建模。
- 实验或效果：在多模态基准测试中，PSNR提升0.92 dB，Dice系数提高9.76%，代码已开源。

## 摘要（原文）

> We propose VL-DUN, a principled framework for joint All-in-One Medical Image Restoration and Segmentation (AiOMIRS) that bridges the gap between low-level signal recovery and high-level semantic understanding. While standard pipelines treat these tasks in isolation, our core insight is that they are fundamentally synergistic: restoration provides clean anatomical structures to improve segmentation, while semantic priors regularize the restoration process. VL-DUN resolves the sub-optimality of sequential processing through two primary innovations. (1) We formulate AiOMIRS as a unified optimization problem, deriving an interpretable joint unfolding mechanism where restoration and segmentation are mathematically coupled for mutual refinement. (2) We introduce a frequency-aware Mamba mechanism to capture long-range dependencies for global segmentation while preserving the high-frequency textures necessary for restoration. This allows for efficient global context modeling with linear complexity, effectively mitigating the spectral bias of standard architectures. As a pioneering work in the AiOMIRS task, VL-DUN establishes a new state-of-the-art across multi-modal benchmarks, improving PSNR by 0.92 dB and the Dice coefficient by 9.76\%. Our results demonstrate that joint collaborative learning offers a superior, more robust solution for complex clinical workflows compared to isolated task processing. The codes are provided in https://github.com/cipi666/VLDUN.

