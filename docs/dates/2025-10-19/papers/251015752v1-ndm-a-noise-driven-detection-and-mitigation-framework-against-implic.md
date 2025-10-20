---
layout: default
title: NDM: A Noise-driven Detection and Mitigation Framework against Implicit Sexual Intentions in Text-to-Image Generation
---

# NDM: A Noise-driven Detection and Mitigation Framework against Implicit Sexual Intentions in Text-to-Image Generation
**arXiv**：[2510.15752v1](https://arxiv.org/abs/2510.15752) · [PDF](https://arxiv.org/pdf/2510.15752.pdf)  
**作者**：Yitong Sun, Yao Huang, Ruochen Zhang, Huanran Chen, Shouwei Ruan, Ranjie Duan, Xingxing Wei  

**一句话要点**：提出NDM框架以检测和缓解文本到图像生成中的隐式性意图

**关键词**：文本到图像生成, 隐式性内容检测, 噪声驱动框架, 自适应负引导, 扩散模型安全

## 3 点简述
- 核心问题：T2I扩散模型易受隐式性提示影响，现有方法难以检测且微调会降低生成质量。
- 方法要点：利用早期噪声可分离性进行检测，并通过噪声增强自适应负引导机制优化初始噪声。
- 实验或效果：在自然和对抗数据集上验证，性能优于SLD、UCE和RECE等现有方法。

## 摘要（原文）

> Despite the impressive generative capabilities of text-to-image (T2I)
> diffusion models, they remain vulnerable to generating inappropriate content,
> especially when confronted with implicit sexual prompts. Unlike explicit
> harmful prompts, these subtle cues, often disguised as seemingly benign terms,
> can unexpectedly trigger sexual content due to underlying model biases, raising
> significant ethical concerns. However, existing detection methods are primarily
> designed to identify explicit sexual content and therefore struggle to detect
> these implicit cues. Fine-tuning approaches, while effective to some extent,
> risk degrading the model's generative quality, creating an undesirable
> trade-off. To address this, we propose NDM, the first noise-driven detection
> and mitigation framework, which could detect and mitigate implicit malicious
> intention in T2I generation while preserving the model's original generative
> capabilities. Specifically, we introduce two key innovations: first, we
> leverage the separability of early-stage predicted noise to develop a
> noise-based detection method that could identify malicious content with high
> accuracy and efficiency; second, we propose a noise-enhanced adaptive negative
> guidance mechanism that could optimize the initial noise by suppressing the
> prominent region's attention, thereby enhancing the effectiveness of adaptive
> negative guidance for sexual mitigation. Experimentally, we validate NDM on
> both natural and adversarial datasets, demonstrating its superior performance
> over existing SOTA methods, including SLD, UCE, and RECE, etc. Code and
> resources are available at https://github.com/lorraine021/NDM.

