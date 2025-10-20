---
layout: default
title: BLIP3o-NEXT: Next Frontier of Native Image Generation
---

# BLIP3o-NEXT: Next Frontier of Native Image Generation
**arXiv**：[2510.15857v1](https://arxiv.org/abs/2510.15857) · [PDF](https://arxiv.org/pdf/2510.15857.pdf)  
**作者**：Jiuhai Chen, Le Xue, Zhiyang Xu, Xichen Pan, Shusheng Yang, Can Qin, An Yan, Honglu Zhou, Zeyuan Chen, Lifu Huang, Tianyi Zhou, Junnan Li, Silvio Savarese, Caiming Xiong, Ran Xu  

**一句话要点**：提出BLIP3o-NEXT统一文本到图像生成与编辑，实现高效推理和高保真图像。

**关键词**：文本到图像生成, 图像编辑, 自回归模型, 扩散模型, 强化学习, 数据质量

## 3 点简述
- 核心问题：图像编辑任务仍具挑战，需提升指令遵循和图像一致性。
- 方法要点：采用自回归+扩散架构，结合推理能力和细节渲染。
- 实验或效果：在多项基准测试中优于现有模型，展示优越性能。

## 摘要（原文）

> We present BLIP3o-NEXT, a fully open-source foundation model in the BLIP3
> series that advances the next frontier of native image generation. BLIP3o-NEXT
> unifies text-to-image generation and image editing within a single
> architecture, demonstrating strong image generation and image editing
> capabilities. In developing the state-of-the-art native image generation model,
> we identify four key insights: (1) Most architectural choices yield comparable
> performance; an architecture can be deemed effective provided it scales
> efficiently and supports fast inference; (2) The successful application of
> reinforcement learning can further push the frontier of native image
> generation; (3) Image editing still remains a challenging task, yet instruction
> following and the consistency between generated and reference images can be
> significantly enhanced through post-training and data engine; (4) Data quality
> and scale continue to be decisive factors that determine the upper bound of
> model performance. Building upon these insights, BLIP3o-NEXT leverages an
> Autoregressive + Diffusion architecture in which an autoregressive model first
> generates discrete image tokens conditioned on multimodal inputs, whose hidden
> states are then used as conditioning signals for a diffusion model to generate
> high-fidelity images. This architecture integrates the reasoning strength and
> instruction following of autoregressive models with the fine-detail rendering
> ability of diffusion models, achieving a new level of coherence and realism.
> Extensive evaluations of various text-to-image and image-editing benchmarks
> show that BLIP3o-NEXT achieves superior performance over existing models.

