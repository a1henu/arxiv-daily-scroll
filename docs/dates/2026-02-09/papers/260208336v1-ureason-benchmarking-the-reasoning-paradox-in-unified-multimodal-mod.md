---
layout: default
title: UReason: Benchmarking the Reasoning Paradox in Unified Multimodal Models
---

# UReason: Benchmarking the Reasoning Paradox in Unified Multimodal Models
**arXiv**：[2602.08336v1](https://arxiv.org/abs/2602.08336) · [PDF](https://arxiv.org/pdf/2602.08336.pdf)  
**作者**：Cheng Yang, Chufan Shi, Bo Shui, Yaokang Wu, Muzi Tao, Huijuan Wang, Ivan Yee Lee, Yong Liu, Xuezhe Ma, Taylor Berg-Kirkpatrick  

**一句话要点**：提出UReason基准以评估统一多模态模型中推理对图像生成的忠实执行效果。

**关键词**：统一多模态模型, 推理悖论, 图像生成基准, 上下文干扰, 视觉合成评估

## 3 点简述
- 核心问题：推理在视觉合成中的实际作用不明确，存在推理悖论。
- 方法要点：引入诊断基准，包含五个任务族，比较直接生成、推理引导生成和去上下文生成。
- 实验或效果：在八个开源模型中观察到推理悖论，去上下文生成性能显著提升。

## 摘要（原文）

> To elicit capabilities for addressing complex and implicit visual requirements, recent unified multimodal models increasingly adopt chain-of-thought reasoning to guide image generation. However, the actual effect of reasoning on visual synthesis remains unclear. We present UReason, a diagnostic benchmark for reasoning-driven image generation that evaluates whether reasoning can be faithfully executed in pixels. UReason contains 2,000 instances across five task families: Code, Arithmetic, Spatial, Attribute, and Text reasoning. To isolate the role of reasoning traces, we introduce an evaluation framework comparing direct generation, reasoning-guided generation, and de-contextualized generation which conditions only on the refined prompt. Across eight open-source unified models, we observe a consistent Reasoning Paradox: Reasoning traces generally improve performance over direct generation, yet retaining intermediate thoughts as conditioning context often hinders visual synthesis, and conditioning only on the refined prompt yields substantial gains. Our analysis suggests that the bottleneck lies in contextual interference rather than insufficient reasoning capacity. UReason provides a principled testbed for studying reasoning in unified models and motivates future methods that effectively integrate reasoning for visual generation while mitigating interference.

