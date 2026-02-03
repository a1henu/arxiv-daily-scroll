---
layout: default
title: Show, Don't Tell: Morphing Latent Reasoning into Image Generation
---

# Show, Don't Tell: Morphing Latent Reasoning into Image Generation
**arXiv**：[2602.02227v1](https://arxiv.org/abs/2602.02227) · [PDF](https://arxiv.org/pdf/2602.02227.pdf)  
**作者**：Harold Haodong Chen, Xinxiang Yin, Wen-Jie Shu, Hongfei Zhang, Zixin Zhang, Chenfei Liao, Litao Guo, Qifeng Chen, Ying-Cong Chen  

**一句话要点**：提出LatentMorph框架，通过隐式潜在推理增强文本到图像生成能力。

**关键词**：文本到图像生成, 潜在推理, 隐式推理, 自适应生成, 轻量组件

## 3 点简述
- 现有文本到图像生成方法缺乏动态推理能力，导致效率低下和信息损失。
- LatentMorph引入四个轻量组件，在连续潜在空间中进行隐式推理，避免显式推理瓶颈。
- 实验显示LatentMorph在多项基准上提升性能，同时减少推理时间和资源消耗。

## 摘要（原文）

> Text-to-image (T2I) generation has achieved remarkable progress, yet existing methods often lack the ability to dynamically reason and refine during generation--a hallmark of human creativity. Current reasoning-augmented paradigms most rely on explicit thought processes, where intermediate reasoning is decoded into discrete text at fixed steps with frequent image decoding and re-encoding, leading to inefficiencies, information loss, and cognitive mismatches. To bridge this gap, we introduce LatentMorph, a novel framework that seamlessly integrates implicit latent reasoning into the T2I generation process. At its core, LatentMorph introduces four lightweight components: (i) a condenser for summarizing intermediate generation states into compact visual memory, (ii) a translator for converting latent thoughts into actionable guidance, (iii) a shaper for dynamically steering next image token predictions, and (iv) an RL-trained invoker for adaptively determining when to invoke reasoning. By performing reasoning entirely in continuous latent spaces, LatentMorph avoids the bottlenecks of explicit reasoning and enables more adaptive self-refinement. Extensive experiments demonstrate that LatentMorph (I) enhances the base model Janus-Pro by $16\%$ on GenEval and $25\%$ on T2I-CompBench; (II) outperforms explicit paradigms (e.g., TwiG) by $15\%$ and $11\%$ on abstract reasoning tasks like WISE and IPV-Txt, (III) while reducing inference time by $44\%$ and token consumption by $51\%$; and (IV) exhibits $71\%$ cognitive alignment with human intuition on reasoning invocation.

