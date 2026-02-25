---
layout: default
title: LESA: Learnable Stage-Aware Predictors for Diffusion Model Acceleration
---

# LESA: Learnable Stage-Aware Predictors for Diffusion Model Acceleration
**arXiv**：[2602.20497v1](https://arxiv.org/abs/2602.20497) · [PDF](https://arxiv.org/pdf/2602.20497.pdf)  
**作者**：Peiliang Cai, Jiacheng Liu, Haowen Xu, Xinyu Wang, Chang Zou, Linfeng Zhang  

**一句话要点**：提出LESA框架，通过可学习的阶段感知预测器加速扩散模型推理。

**关键词**：扩散模型加速, 特征预测, 阶段感知学习, KAN网络, 多专家架构, 推理优化

## 3 点简述
- 核心问题：扩散模型推理计算成本高，现有特征缓存方法难以适应复杂阶段动态，导致质量下降。
- 方法要点：基于两阶段训练，使用KAN学习时间特征映射，并采用多阶段多专家架构分配专用预测器。
- 实验或效果：在FLUX.1-dev、Qwen-Image和HunyuanVideo上实现5-6倍加速，质量保持或提升，验证泛化能力。

## 摘要（原文）

> Diffusion models have achieved remarkable success in image and video generation tasks. However, the high computational demands of Diffusion Transformers (DiTs) pose a significant challenge to their practical deployment. While feature caching is a promising acceleration strategy, existing methods based on simple reusing or training-free forecasting struggle to adapt to the complex, stage-dependent dynamics of the diffusion process, often resulting in quality degradation and failing to maintain consistency with the standard denoising process. To address this, we propose a LEarnable Stage-Aware (LESA) predictor framework based on two-stage training. Our approach leverages a Kolmogorov-Arnold Network (KAN) to accurately learn temporal feature mappings from data. We further introduce a multi-stage, multi-expert architecture that assigns specialized predictors to different noise-level stages, enabling more precise and robust feature forecasting. Extensive experiments show our method achieves significant acceleration while maintaining high-fidelity generation. Experiments demonstrate 5.00x acceleration on FLUX.1-dev with minimal quality degradation (1.0% drop), 6.25x speedup on Qwen-Image with a 20.2% quality improvement over the previous SOTA (TaylorSeer), and 5.00x acceleration on HunyuanVideo with a 24.7% PSNR improvement over TaylorSeer. State-of-the-art performance on both text-to-image and text-to-video synthesis validates the effectiveness and generalization capability of our training-based framework across different models. Our code is included in the supplementary materials and will be released on GitHub.

