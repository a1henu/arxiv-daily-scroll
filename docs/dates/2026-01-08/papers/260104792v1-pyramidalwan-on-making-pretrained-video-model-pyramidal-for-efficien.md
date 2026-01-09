---
layout: default
title: PyramidalWan: On Making Pretrained Video Model Pyramidal for Efficient Inference
---

# PyramidalWan: On Making Pretrained Video Model Pyramidal for Efficient Inference
**arXiv**：[2601.04792v1](https://arxiv.org/abs/2601.04792) · [PDF](https://arxiv.org/pdf/2601.04792.pdf)  
**作者**：Denis Korzhenkov, Adil Karjauv, Animesh Karnewar, Mohsen Ghafoorian, Amirhossein Habibian  

**一句话要点**：提出PyramidalWan，通过低成本微调将预训练视频扩散模型转换为金字塔模型以提升推理效率。

**关键词**：视频扩散模型, 金字塔模型, 推理效率, 微调转换, 步蒸馏

## 3 点简述
- 现有金字塔视频模型从头训练，视觉质量低于先进系统。
- 提出管道将预训练扩散模型转换为金字塔模型，保持输出质量。
- 研究并比较金字塔模型中的步蒸馏策略，进一步提高推理效率。

## 摘要（原文）

> Recently proposed pyramidal models decompose the conventional forward and backward diffusion processes into multiple stages operating at varying resolutions. These models handle inputs with higher noise levels at lower resolutions, while less noisy inputs are processed at higher resolutions. This hierarchical approach significantly reduces the computational cost of inference in multi-step denoising models. However, existing open-source pyramidal video models have been trained from scratch and tend to underperform compared to state-of-the-art systems in terms of visual plausibility. In this work, we present a pipeline that converts a pretrained diffusion model into a pyramidal one through low-cost finetuning, achieving this transformation without degradation in quality of output videos. Furthermore, we investigate and compare various strategies for step distillation within pyramidal models, aiming to further enhance the inference efficiency. Our results are available at https://qualcomm-ai-research.github.io/PyramidalWan.

