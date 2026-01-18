---
layout: default
title: Think-Then-Generate: Reasoning-Aware Text-to-Image Diffusion with LLM Encoders
---

# Think-Then-Generate: Reasoning-Aware Text-to-Image Diffusion with LLM Encoders
**arXiv**：[2601.10332v1](https://arxiv.org/abs/2601.10332) · [PDF](https://arxiv.org/pdf/2601.10332.pdf)  
**作者**：Siqi Kou, Jiachun Jin, Zetong Zhou, Ye Ma, Yugang Wang, Quan Chen, Peng Jiang, Xiao Yang, Jun Zhu, Kai Yu, Zhijie Deng  

**一句话要点**：提出Think-Then-Generate范式，通过LLM推理重写提示以提升文本到图像生成的语义一致性与视觉真实感。

**关键词**：文本到图像生成, 扩散模型, 大语言模型编码器, 推理增强, 语义对齐, 联合优化

## 3 点简述
- 现有T2I扩散模型多作为文本-像素映射器，未充分利用LLM编码器的推理能力来推断视觉内容。
- 采用轻量级监督微调激活LLM的思考-重写模式，并通过Dual-GRPO联合优化编码器与扩散主干。
- 实验在基于推理的图像生成与编辑基准上显著提升事实一致性、语义对齐和视觉真实感，WISE得分达0.79。

## 摘要（原文）

> Recent progress in text-to-image (T2I) diffusion models (DMs) has enabled high-quality visual synthesis from diverse textual prompts. Yet, most existing T2I DMs, even those equipped with large language model (LLM)-based text encoders, remain text-pixel mappers -- they employ LLMs merely as text encoders, without leveraging their inherent reasoning capabilities to infer what should be visually depicted given the textual prompt. To move beyond such literal generation, we propose the think-then-generate (T2G) paradigm, where the LLM-based text encoder is encouraged to reason about and rewrite raw user prompts; the states of the rewritten prompts then serve as diffusion conditioning. To achieve this, we first activate the think-then-rewrite pattern of the LLM encoder with a lightweight supervised fine-tuning process. Subsequently, the LLM encoder and diffusion backbone are co-optimized to ensure faithful reasoning about the context and accurate rendering of the semantics via Dual-GRPO. In particular, the text encoder is reinforced using image-grounded rewards to infer and recall world knowledge, while the diffusion backbone is pushed to produce semantically consistent and visually coherent images. Experiments show substantial improvements in factual consistency, semantic alignment, and visual realism across reasoning-based image generation and editing benchmarks, achieving 0.79 on WISE score, nearly on par with GPT-4. Our results constitute a promising step toward next-generation unified models with reasoning, expression, and demonstration capacities.

