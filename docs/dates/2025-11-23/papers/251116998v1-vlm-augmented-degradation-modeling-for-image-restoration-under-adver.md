---
layout: default
title: VLM-Augmented Degradation Modeling for Image Restoration Under Adverse Weather Conditions
---

# VLM-Augmented Degradation Modeling for Image Restoration Under Adverse Weather Conditions
**arXiv**：[2511.16998v1](https://arxiv.org/abs/2511.16998) · [PDF](https://arxiv.org/pdf/2511.16998.pdf)  
**作者**：Qianyi Shao, Yuanfan Zhang, Renxiang Xiao, Liang Hu  

**一句话要点**：提出MVLR模型以解决恶劣天气下图像恢复问题

**关键词**：图像恢复, 视觉语言模型, 隐式记忆库, 恶劣天气, 动态交叉注意力, 实时部署

## 3 点简述
- 核心问题：恶劣天气导致图像退化，影响自动驾驶和户外机器人视觉感知。
- 方法要点：结合视觉语言模型和隐式记忆库，通过链式推理和动态交叉注意力增强恢复。
- 实验或效果：在多个基准测试中PSNR和SSIM指标优于基线，平衡紧凑性和表达力。

## 摘要（原文）

> Reliable visual perception under adverse weather conditions, such as rain, haze, snow, or a mixture of them, is desirable yet challenging for autonomous driving and outdoor robots. In this paper, we propose a unified Memory-Enhanced Visual-Language Recovery (MVLR) model that restores images from different degradation levels under various weather conditions. MVLR couples a lightweight encoder-decoder backbone with a Visual-Language Model (VLM) and an Implicit Memory Bank (IMB). The VLM performs chain-of-thought inference to encode weather degradation priors and the IMB stores continuous latent representations of degradation patterns. The VLM-generated priors query the IMB to retrieve fine-grained degradation prototypes. These prototypes are then adaptively fused with multi-scale visual features via dynamic cross-attention mechanisms, enhancing restoration accuracy while maintaining computational efficiency. Extensive experiments on four severe-weather benchmarks show that MVLR surpasses single-branch and Mixture-of-Experts baselines in terms of Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index Measure (SSIM). These results indicate that MVLR offers a practical balance between model compactness and expressiveness for real-time deployment in diverse outdoor conditions.

