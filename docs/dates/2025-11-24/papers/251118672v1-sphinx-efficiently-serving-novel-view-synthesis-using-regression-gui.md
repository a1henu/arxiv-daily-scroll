---
layout: default
title: Sphinx: Efficiently Serving Novel View Synthesis using Regression-Guided Selective Refinement
---

# Sphinx: Efficiently Serving Novel View Synthesis using Regression-Guided Selective Refinement
**arXiv**：[2511.18672v1](https://arxiv.org/abs/2511.18672) · [PDF](https://arxiv.org/pdf/2511.18672.pdf)  
**作者**：Yuchen Xia, Souvik Kundu, Mosharaf Chowdhury, Nishil Talati  

**一句话要点**：提出Sphinx框架以高效服务新视角合成，实现高质量与低延迟平衡

**关键词**：新视角合成, 扩散模型, 回归引导, 选择性细化, 自适应噪声调度, 高效推理

## 3 点简述
- 核心问题：扩散模型NVS计算成本高，回归模型质量差，需兼顾质量与效率
- 方法要点：使用回归初始化引导扩散去噪，结合选择性细化和自适应噪声调度
- 实验或效果：平均加速1.8倍，感知退化低于5%，建立新帕累托前沿

## 摘要（原文）

> Novel View Synthesis (NVS) is the task of generating new images of a scene from viewpoints that were not part of the original input. Diffusion-based NVS can generate high-quality, temporally consistent images, however, remains computationally prohibitive. Conversely, regression-based NVS offers suboptimal generation quality despite requiring significantly lower compute; leaving the design objective of a high-quality, inference-efficient NVS framework an open challenge. To close this critical gap, we present Sphinx, a training-free hybrid inference framework that achieves diffusion-level fidelity at a significantly lower compute. Sphinx proposes to use regression-based fast initialization to guide and reduce the denoising workload for the diffusion model. Additionally, it integrates selective refinement with adaptive noise scheduling, allowing more compute to uncertain regions and frames. This enables Sphinx to provide flexible navigation of the performance-quality trade-off, allowing adaptation to latency and fidelity requirements for dynamically changing inference scenarios. Our evaluation shows that Sphinx achieves an average 1.8x speedup over diffusion model inference with negligible perceptual degradation of less than 5%, establishing a new Pareto frontier between quality and latency in NVS serving.

