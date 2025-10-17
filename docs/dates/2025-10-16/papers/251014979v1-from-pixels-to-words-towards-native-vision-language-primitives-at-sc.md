---
layout: default
title: From Pixels to Words -- Towards Native Vision-Language Primitives at Scale
---

# From Pixels to Words -- Towards Native Vision-Language Primitives at Scale
**arXiv**：[2510.14979v1](https://arxiv.org/abs/2510.14979) · [PDF](https://arxiv.org/pdf/2510.14979.pdf)  
**作者**：Haiwen Diao, Mingxuan Li, Silei Wu, Linjun Dai, Xiaohua Wang, Hanming Deng, Lewei Lu, Dahua Lin, Ziwei Liu  

**一句话要点**：提出NEO原生视觉语言模型，以解决视觉语言对齐与集成问题，适用于多样化场景。

**关键词**：原生视觉语言模型, 视觉语言对齐, 共享语义空间, 统一编码, 模型集成, 可扩展生态系统

## 3 点简述
- 核心问题：原生视觉语言模型与模块化模型的根本约束及可访问性挑战。
- 方法要点：设计共享语义空间，集成视觉语言模块，支持统一编码与推理。
- 实验或效果：NEO在390M图像文本数据上媲美顶级模块化模型，实现高效视觉感知。

## 摘要（原文）

> The edifice of native Vision-Language Models (VLMs) has emerged as a rising
> contender to typical modular VLMs, shaped by evolving model architectures and
> training paradigms. Yet, two lingering clouds cast shadows over its widespread
> exploration and promotion: (-) What fundamental constraints set native VLMs
> apart from modular ones, and to what extent can these barriers be overcome? (-)
> How to make research in native VLMs more accessible and democratized, thereby
> accelerating progress in the field. In this paper, we clarify these challenges
> and outline guiding principles for constructing native VLMs. Specifically, one
> native VLM primitive should: (i) effectively align pixel and word
> representations within a shared semantic space; (ii) seamlessly integrate the
> strengths of formerly separate vision and language modules; (iii) inherently
> embody various cross-modal properties that support unified vision-language
> encoding, aligning, and reasoning. Hence, we launch NEO, a novel family of
> native VLMs built from first principles, capable of rivaling top-tier modular
> counterparts across diverse real-world scenarios. With only 390M image-text
> examples, NEO efficiently develops visual perception from scratch while
> mitigating vision-language conflicts inside a dense and monolithic model
> crafted from our elaborate primitives. We position NEO as a cornerstone for
> scalable and powerful native VLMs, paired with a rich set of reusable
> components that foster a cost-effective and extensible ecosystem. Our code and
> models are publicly available at: https://github.com/EvolvingLMMs-Lab/NEO.

