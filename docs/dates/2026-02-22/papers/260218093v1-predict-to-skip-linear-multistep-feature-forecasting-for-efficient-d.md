---
layout: default
title: Predict to Skip: Linear Multistep Feature Forecasting for Efficient Diffusion Transformers
---

# Predict to Skip: Linear Multistep Feature Forecasting for Efficient Diffusion Transformers
**arXiv**：[2602.18093v1](https://arxiv.org/abs/2602.18093) · [PDF](https://arxiv.org/pdf/2602.18093.pdf)  
**作者**：Hanshuai Cui, Zhiqing Tang, Qianli Ma, Zhi Yao, Weijia Jia  

**一句话要点**：提出PrediT框架，通过线性多步特征预测加速扩散变换器，减少计算成本并保持生成质量。

**关键词**：扩散变换器, 免训练加速, 特征预测, 线性多步方法, 图像生成, 视频生成

## 3 点简述
- 扩散变换器迭代去噪过程计算成本高，现有免训练加速方法依赖特征缓存重用，可能导致潜在漂移和视觉退化。
- 基于模型输出沿扩散轨迹平滑演变的观察，将特征预测建模为线性多步问题，使用经典方法预测未来输出，结合校正器防止误差累积。
- 实验验证PrediT在多种基于DiT的图像和视频生成模型中实现高达5.54倍延迟降低，质量退化可忽略。

## 摘要（原文）

> Diffusion Transformers (DiT) have emerged as a widely adopted backbone for high-fidelity image and video generation, yet their iterative denoising process incurs high computational costs. Existing training-free acceleration methods rely on feature caching and reuse under the assumption of temporal stability. However, reusing features for multiple steps may lead to latent drift and visual degradation. We observe that model outputs evolve smoothly along much of the diffusion trajectory, enabling principled predictions rather than naive reuse. Based on this insight, we propose \textbf{PrediT}, a training-free acceleration framework that formulates feature prediction as a linear multistep problem. We employ classical linear multistep methods to forecast future model outputs from historical information, combined with a corrector that activates in high-dynamics regions to prevent error accumulation. A dynamic step modulation mechanism adaptively adjusts the prediction horizon by monitoring the feature change rate. Together, these components enable substantial acceleration while preserving generation fidelity. Extensive experiments validate that our method achieves up to $5.54\times$ latency reduction across various DiT-based image and video generation models, while incurring negligible quality degradation.

