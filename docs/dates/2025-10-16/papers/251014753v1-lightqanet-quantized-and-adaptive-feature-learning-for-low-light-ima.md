---
layout: default
title: LightQANet: Quantized and Adaptive Feature Learning for Low-Light Image Enhancement
---

# LightQANet: Quantized and Adaptive Feature Learning for Low-Light Image Enhancement
**arXiv**：[2510.14753v1](https://arxiv.org/abs/2510.14753) · [PDF](https://arxiv.org/pdf/2510.14753.pdf)  
**作者**：Xu Wu, Zhihui Lai, Xianxu Hou, Jie Zhou, Ya-nan Zhang, Linlin Shen  

**一句话要点**：提出LightQANet，通过量化与自适应特征学习增强低光图像

**关键词**：低光图像增强, 量化特征学习, 自适应特征学习, 光照建模, 图像质量提升

## 3 点简述
- 核心问题：低光图像像素信息退化，导致纹理恢复差、颜色不一致和伪影
- 方法要点：设计LQM量化光照因素，LAPM用可学习提示动态引导特征学习
- 实验或效果：多数据集实验显示，在多种光照场景下达到先进性能

## 摘要（原文）

> Low-light image enhancement (LLIE) aims to improve illumination while
> preserving high-quality color and texture. However, existing methods often fail
> to extract reliable feature representations due to severely degraded
> pixel-level information under low-light conditions, resulting in poor texture
> restoration, color inconsistency, and artifact. To address these challenges, we
> propose LightQANet, a novel framework that introduces quantized and adaptive
> feature learning for low-light enhancement, aiming to achieve consistent and
> robust image quality across diverse lighting conditions. From the static
> modeling perspective, we design a Light Quantization Module (LQM) to explicitly
> extract and quantify illumination-related factors from image features. By
> enforcing structured light factor learning, LQM enhances the extraction of
> light-invariant representations and mitigates feature inconsistency across
> varying illumination levels. From the dynamic adaptation perspective, we
> introduce a Light-Aware Prompt Module (LAPM), which encodes illumination priors
> into learnable prompts to dynamically guide the feature learning process. LAPM
> enables the model to flexibly adapt to complex and continuously changing
> lighting conditions, further improving image enhancement. Extensive experiments
> on multiple low-light datasets demonstrate that our method achieves
> state-of-the-art performance, delivering superior qualitative and quantitative
> results across various challenging lighting scenarios.

