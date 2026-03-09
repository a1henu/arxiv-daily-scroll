---
layout: default
title: Reflective Flow Sampling Enhancement
---

# Reflective Flow Sampling Enhancement
**arXiv**：[2603.06165v1](https://arxiv.org/abs/2603.06165) · [PDF](https://arxiv.org/pdf/2603.06165.pdf)  
**作者**：Zikai Zhou, Muyao Wang, Shitong Shao, Lichen Bai, Haoyi Xiong, Bo Han, Zeke Xie  

**一句话要点**：提出反射流采样以增强流匹配模型的推理质量与提示对齐

**关键词**：文本到图像生成, 流匹配模型, 推理增强, 提示对齐, 无训练优化

## 3 点简述
- 针对流匹配模型（如FLUX）推理增强方法缺失的问题
- 基于理论推导，通过线性组合文本表示与流反转提升文本-图像对齐
- 实验证明在多个基准上提升生成质量和提示对齐，并展现测试时缩放能力

## 摘要（原文）

> The growing demand for text-to-image generation has led to rapid advances in generative modeling. Recently, text-to-image diffusion models trained with flow matching algorithms, such as FLUX, have achieved remarkable progress and emerged as strong alternatives to conventional diffusion models. At the same time, inference-time enhancement strategies have been shown to improve the generation quality and text-prompt alignment of text-to-image diffusion models. However, these techniques are mainly applicable to conventional diffusion models and usually fail to perform well on flow models. To bridge this gap, we propose Reflective Flow Sampling (RF-Sampling), a theoretically-grounded and training-free inference enhancement framework explicitly designed for flow models, especially for the CFG-distilled variants (i.e., models distilled from CFG guidance techniques), like FLUX. Departing from heuristic interpretations, we provide a formal derivation proving that RF-Sampling implicitly performs gradient ascent on the text-image alignment score. By leveraging a linear combination of textual representations and integrating them with flow inversion, RF-Sampling allows the model to explore noise spaces that are more consistent with the input prompt. Extensive experiments across multiple benchmarks demonstrate that RF-Sampling consistently improves both generation quality and prompt alignment. Moreover, RF-Sampling is also the first inference enhancement method that can exhibit test-time scaling ability to some extent on FLUX.

