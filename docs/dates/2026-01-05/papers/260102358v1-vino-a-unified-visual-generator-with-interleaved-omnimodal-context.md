---
layout: default
title: VINO: A Unified Visual Generator with Interleaved OmniModal Context
---

# VINO: A Unified Visual Generator with Interleaved OmniModal Context
**arXiv**：[2601.02358v1](https://arxiv.org/abs/2601.02358) · [PDF](https://arxiv.org/pdf/2601.02358.pdf)  
**作者**：Junyi Chen, Tong He, Zhoujie Fu, Pengfei Wan, Kun Gai, Weicai Ye  

**一句话要点**：提出VINO统一视觉生成器，通过交错多模态上下文实现图像与视频的生成与编辑。

**关键词**：统一视觉生成, 多模态扩散, 交错编码, 图像视频编辑, 身份保持

## 3 点简述
- 核心问题：传统方法依赖任务特定模型，难以统一处理多模态视觉生成与编辑。
- 方法要点：结合视觉语言模型与多模态扩散Transformer，以交错编码引导扩散过程。
- 实验或效果：在多样基准上展示高质量生成、指令遵循和身份保持能力。

## 摘要（原文）

> We present VINO, a unified visual generator that performs image and video generation and editing within a single framework. Instead of relying on task-specific models or independent modules for each modality, VINO uses a shared diffusion backbone that conditions on text, images and videos, enabling a broad range of visual creation and editing tasks under one model. Specifically, VINO couples a vision-language model (VLM) with a Multimodal Diffusion Transformer (MMDiT), where multimodal inputs are encoded as interleaved conditioning tokens, and then used to guide the diffusion process. This design supports multi-reference grounding, long-form instruction following, and coherent identity preservation across static and dynamic content, while avoiding modality-specific architectural components. To train such a unified system, we introduce a multi-stage training pipeline that progressively expands a video generation base model into a unified, multi-task generator capable of both image and video input and output. Across diverse generation and editing benchmarks, VINO demonstrates strong visual quality, faithful instruction following, improved reference and attribute preservation, and more controllable multi-identity edits. Our results highlight a practical path toward scalable unified visual generation, and the promise of interleaved, in-context computation as a foundation for general-purpose visual creation.

