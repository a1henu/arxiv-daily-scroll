---
layout: default
title: Fast-ARDiff: An Entropy-informed Acceleration Framework for Continuous Space Autoregressive Generation
---

# Fast-ARDiff: An Entropy-informed Acceleration Framework for Continuous Space Autoregressive Generation
**arXiv**：[2512.08537v1](https://arxiv.org/abs/2512.08537) · [PDF](https://arxiv.org/pdf/2512.08537.pdf)  
**作者**：Zhen Zou, Xiaoxiao Ma, Jie Huang, Zichao Yu, Feng Zhao  

**一句话要点**：提出Fast-ARDiff框架，通过熵引导策略和联合优化加速自回归-扩散混合生成

**关键词**：自回归-扩散混合生成, 熵引导加速, 推测解码, 联合蒸馏训练, 动态调度器, 图像生成加速

## 3 点简述
- 核心问题：自回归-扩散混合范式因顺序生成和迭代去噪导致高延迟
- 方法要点：采用熵引导推测解码和动态调度器联合优化自回归与扩散组件
- 实验或效果：在ImageNet 256×256上实现4.3倍无损加速，文本条件生成加速3倍

## 摘要（原文）

> Autoregressive(AR)-diffusion hybrid paradigms combine AR's structured modeling with diffusion's photorealistic synthesis, yet suffer from high latency due to sequential AR generation and iterative denoising. In this work, we tackle this bottleneck and propose a unified AR-diffusion framework Fast-ARDiff that jointly optimizes both components, accelerating AR speculative decoding while simultaneously facilitating faster diffusion decoding. Specifically: (1) The entropy-informed speculative strategy encourages draft model to produce higher-entropy representations aligned with target model's entropy characteristics, mitigating entropy mismatch and high rejection rates caused by draft overconfidence. (2) For diffusion decoding, rather than treating it as an independent module, we integrate it into the same end-to-end framework using a dynamic scheduler that prioritizes AR optimization to guide the diffusion part in further steps. The diffusion part is optimized through a joint distillation framework combining trajectory and distribution matching, ensuring stable training and high-quality synthesis with extremely few steps. During inference, shallow feature entropy from AR module is used to pre-filter low-entropy drafts, avoiding redundant computation and improving latency. Fast-ARDiff achieves state-of-the-art acceleration across diverse models: on ImageNet 256$\times$256, TransDiff attains 4.3$\times$ lossless speedup, and NextStep-1 achieves 3$\times$ acceleration on text-conditioned generation. Code will be available at https://github.com/aSleepyTree/Fast-ARDiff.

