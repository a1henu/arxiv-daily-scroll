---
layout: default
title: EMAG: Self-Rectifying Diffusion Sampling with Exponential Moving Average Guidance
---

# EMAG: Self-Rectifying Diffusion Sampling with Exponential Moving Average Guidance
**arXiv**：[2512.17303v1](https://arxiv.org/abs/2512.17303) · [PDF](https://arxiv.org/pdf/2512.17303.pdf)  
**作者**：Ankit Yadav, Ta Duc Huy, Lingqiao Liu  

**一句话要点**：提出指数移动平均引导以改进扩散变换器中的负样本生成质量

**关键词**：扩散模型, 引导采样, 注意力机制, 负样本生成, 自适应层选择

## 3 点简述
- 核心问题：现有引导方法缺乏对负样本粒度或难度的可靠控制，且目标层选择固定。
- 方法要点：基于统计的自适应层选择规则，在推理时修改注意力，生成更难的语义忠实负样本。
- 实验或效果：在人类偏好分数上比无分类器引导提升+0.46，并能与先进引导技术组合使用。

## 摘要（原文）

> In diffusion and flow-matching generative models, guidance techniques are widely used to improve sample quality and consistency. Classifier-free guidance (CFG) is the de facto choice in modern systems and achieves this by contrasting conditional and unconditional samples. Recent work explores contrasting negative samples at inference using a weaker model, via strong/weak model pairs, attention-based masking, stochastic block dropping, or perturbations to the self-attention energy landscape. While these strategies refine the generation quality, they still lack reliable control over the granularity or difficulty of the negative samples, and target-layer selection is often fixed. We propose Exponential Moving Average Guidance (EMAG), a training-free mechanism that modifies attention at inference time in diffusion transformers, with a statistics-based, adaptive layer-selection rule. Unlike prior methods, EMAG produces harder, semantically faithful negatives (fine-grained degradations), surfacing difficult failure modes, enabling the denoiser to refine subtle artifacts, boosting the quality and human preference score (HPS) by +0.46 over CFG. We further demonstrate that EMAG naturally composes with advanced guidance techniques, such as APG and CADS, further improving HPS.

