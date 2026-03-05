---
layout: default
title: Dual-Solver: A Generalized ODE Solver for Diffusion Models with Dual Prediction
---

# Dual-Solver: A Generalized ODE Solver for Diffusion Models with Dual Prediction
**arXiv**：[2603.03973v1](https://arxiv.org/abs/2603.03973) · [PDF](https://arxiv.org/pdf/2603.03973.pdf)  
**作者**：Soochul Park, Yeon Ju Lee  

**一句话要点**：提出Dual-Solver以解决扩散模型采样时函数评估次数多的问题，通过可学习参数泛化多步采样器。

**关键词**：扩散模型, ODE求解器, 采样加速, 可学习参数, 图像生成, 低NFE优化

## 3 点简述
- 扩散模型采样需大量函数评估，传统ODE方法选择预测类型和积分域导致不同采样行为。
- Dual-Solver引入可学习参数，连续插值预测类型、选择积分域和调整残差项，保持二阶局部精度。
- 在低函数评估次数下，Dual-Solver提升ImageNet和文本到图像生成的FID与CLIP分数。

## 摘要（原文）

> Diffusion models achieve state-of-the-art image quality. However, sampling is costly at inference time because it requires a large number of function evaluations (NFEs). To reduce NFEs, classical ODE numerical methods have been adopted. Yet, the choice of prediction type and integration domain leads to different sampling behaviors. To address these issues, we introduce Dual-Solver, which generalizes multistep samplers through learnable parameters that continuously (i) interpolate among prediction types, (ii) select the integration domain, and (iii) adjust the residual terms. It retains the standard predictor-corrector structure while preserving second-order local accuracy. These parameters are learned via a classification-based objective using a frozen pretrained classifier (e.g., MobileNet or CLIP). For ImageNet class-conditional generation (DiT, GM-DiT) and text-to-image generation (SANA, PixArt-$α$), Dual-Solver improves FID and CLIP scores in the low-NFE regime ($3 \le$ NFE $\le 9$) across backbones.

