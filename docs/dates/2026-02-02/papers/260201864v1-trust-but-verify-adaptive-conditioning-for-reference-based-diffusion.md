---
layout: default
title: Trust but Verify: Adaptive Conditioning for Reference-Based Diffusion Super-Resolution via Implicit Reference Correlation Modeling
---

# Trust but Verify: Adaptive Conditioning for Reference-Based Diffusion Super-Resolution via Implicit Reference Correlation Modeling
**arXiv**：[2602.01864v1](https://arxiv.org/abs/2602.01864) · [PDF](https://arxiv.org/pdf/2602.01864.pdf)  
**作者**：Yuan Wang, Yuhao Wan, Siming Zheng, Bo Li, Qibin Hou, Peng-Tao Jiang  

**一句话要点**：提出Ada-RefSR框架，通过自适应隐式关联门控解决参考图像与低质量输入对应不可靠问题

**关键词**：参考图像超分辨率, 扩散模型, 自适应引导, 隐式关联建模, 图像恢复

## 3 点简述
- 核心问题：真实退化导致参考图像与低质量输入对应不可靠，需自适应控制参考使用
- 方法要点：采用自适应隐式关联门控，通过可学习摘要令牌捕获隐式关联，轻量调节参考引导
- 实验或效果：在多个数据集上实现保真度、自然度和效率的平衡，对参考对齐变化保持鲁棒

## 摘要（原文）

> Recent works have explored reference-based super-resolution (RefSR) to mitigate hallucinations in diffusion-based image restoration. A key challenge is that real-world degradations make correspondences between low-quality (LQ) inputs and reference (Ref) images unreliable, requiring adaptive control of reference usage. Existing methods either ignore LQ-Ref correlations or rely on brittle explicit matching, leading to over-reliance on misleading references or under-utilization of valuable cues. To address this, we propose Ada-RefSR, a single-step diffusion framework guided by a "Trust but Verify" principle: reference information is leveraged when reliable and suppressed otherwise. Its core component, Adaptive Implicit Correlation Gating (AICG), employs learnable summary tokens to distill dominant reference patterns and capture implicit correlations with LQ features. Integrated into the attention backbone, AICG provides lightweight, adaptive regulation of reference guidance, serving as a built-in safeguard against erroneous fusion. Experiments on multiple datasets demonstrate that Ada-RefSR achieves a strong balance of fidelity, naturalness, and efficiency, while remaining robust under varying reference alignment.

