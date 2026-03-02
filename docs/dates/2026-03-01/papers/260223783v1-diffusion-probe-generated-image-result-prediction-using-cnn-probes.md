---
layout: default
title: Diffusion Probe: Generated Image Result Prediction Using CNN Probes
---

# Diffusion Probe: Generated Image Result Prediction Using CNN Probes
**arXiv**：[2602.23783v1](https://arxiv.org/abs/2602.23783) · [PDF](https://arxiv.org/pdf/2602.23783.pdf)  
**作者**：Benlei Cui, Bukun Huang, Zhizeng Ye, Xuemei Dong, Tuo Chen, Hui Xue, Dingkang Yang, Longtao Huang, Jingqun Tang, Haiwen Hong  

**一句话要点**：提出Diffusion Probe框架，利用早期交叉注意力分布预测生成图像质量，以提升文本到图像生成效率。

**关键词**：文本到图像生成, 扩散模型, 质量预测, 交叉注意力, 计算效率, 早期评估

## 3 点简述
- 核心问题：文本到图像扩散模型缺乏早期质量评估机制，导致多生成场景下试错成本高。
- 方法要点：基于早期交叉注意力图统计特性，设计轻量级预测器，在去噪初期预测最终图像质量。
- 实验或效果：在多种模型、设置和指标下验证，实现高相关性（PCC>0.7）和分类性能（AUC-ROC>0.9）。

## 摘要（原文）

> Text-to-image (T2I) diffusion models lack an efficient mechanism for early quality assessment, leading to costly trial-and-error in multi-generation scenarios such as prompt iteration, agent-based generation, and flow-grpo. We reveal a strong correlation between early diffusion cross-attention distributions and final image quality. Based on this finding, we introduce Diffusion Probe, a framework that leverages internal cross-attention maps as predictive signals.
>   We design a lightweight predictor that maps statistical properties of early-stage cross-attention extracted from initial denoising steps to the final image's overall quality. This enables accurate forecasting of image quality across diverse evaluation metrics long before full synthesis is complete.
>   We validate Diffusion Probe across a wide range of settings. On multiple T2I models, across early denoising windows, resolutions, and quality metrics, it achieves strong correlation (PCC > 0.7) and high classification performance (AUC-ROC > 0.9).
>   Its reliability translates into practical gains. By enabling early quality-aware decisions in workflows such as prompt optimization, seed selection, and accelerated RL training, the probe supports more targeted sampling and avoids computation on low-potential generations. This reduces computational overhead while improving final output quality.
>   Diffusion Probe is model-agnostic, efficient, and broadly applicable, offering a practical solution for improving T2I generation efficiency through early quality prediction.

