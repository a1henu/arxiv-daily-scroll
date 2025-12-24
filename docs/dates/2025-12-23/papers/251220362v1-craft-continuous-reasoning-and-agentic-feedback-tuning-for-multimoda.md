---
layout: default
title: CRAFT: Continuous Reasoning and Agentic Feedback Tuning for Multimodal Text-to-Image Generation
---

# CRAFT: Continuous Reasoning and Agentic Feedback Tuning for Multimodal Text-to-Image Generation
**arXiv**：[2512.20362v1](https://arxiv.org/abs/2512.20362) · [PDF](https://arxiv.org/pdf/2512.20362.pdf)  
**作者**：V. Kovalev, A. Kuvshinov, A. Buzovkin, D. Pokidov, D. Timonin  

**一句话要点**：提出CRAFT框架，通过结构化推理提升多模态文本到图像生成的可靠性和可控性。

**关键词**：多模态生成, 推理时间优化, 结构化反馈, 文本到图像, 视觉语言模型, LLM代理

## 3 点简述
- 现有方法依赖隐式批判或无约束提示重写，导致行为难以解释、控制或可靠停止。
- CRAFT将提示分解为依赖结构视觉问题，使用视觉语言模型验证图像，并通过LLM代理进行针对性编辑。
- 在多个模型和基准测试中，CRAFT显著提升组合准确性、文本渲染和偏好评估，尤其对轻量级生成器效果明显。

## 摘要（原文）

> Recent work has shown that inference-time reasoning and reflection can improve text-to-image generation without retraining. However, existing approaches often rely on implicit, holistic critiques or unconstrained prompt rewrites, making their behavior difficult to interpret, control, or stop reliably. In contrast, large language models have benefited from explicit, structured forms of **thinking** based on verification, targeted correction, and early stopping.
>   We introduce CRAFT (Continuous Reasoning and Agentic Feedback Tuning), a training-free, model-agnostic framework that brings this structured reasoning paradigm to multimodal image generation. CRAFT decomposes a prompt into dependency-structured visual questions, veries generated images using a vision-language model, and applies targeted prompt edits through an LLM agent only where constraints fail. The process iterates with an explicit stopping criterion once all constraints are satised, yielding an interpretable and controllable inference-time renement loop.
>   Across multiple model families and challenging benchmarks, CRAFT consistently improves compositional accuracy, text rendering, and preference-based evaluations, with particularly strong gains for lightweight generators. Importantly, these improvements incur only a negligible inference-time overhead, allowing smaller or cheaper models to approach the quality of substantially more expensive systems. Our results suggest that explicitly structured, constraint-driven inference-time reasoning is a key ingredient for improving the reliability of multimodal generative models.

