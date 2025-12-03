---
layout: default
title: Masking Matters: Unlocking the Spatial Reasoning Capabilities of LLMs for 3D Scene-Language Understanding
---

# Masking Matters: Unlocking the Spatial Reasoning Capabilities of LLMs for 3D Scene-Language Understanding
**arXiv**：[2512.02487v1](https://arxiv.org/abs/2512.02487) · [PDF](https://arxiv.org/pdf/2512.02487.pdf)  
**作者**：Yerim Jeon, Miso Lee, WonJun Moon, Jae-Pil Heo  

**一句话要点**：提出3D-SLIM掩码策略以解决LLMs在3D场景理解中的空间推理限制

**关键词**：3D场景语言理解, 空间推理, 注意力掩码, 大型语言模型, 多模态学习

## 3 点简述
- 核心问题：标准因果掩码在3D场景中引入顺序偏见和受限注意力，阻碍空间推理
- 方法要点：使用几何自适应掩码和指令感知掩码，替代因果掩码，无需修改架构或增加参数
- 实验或效果：在多个基准测试中显著提升性能，验证了掩码策略的有效性

## 摘要（原文）

> Recent advances in 3D scene-language understanding have leveraged Large Language Models (LLMs) for 3D reasoning by transferring their general reasoning ability to 3D multi-modal contexts. However, existing methods typically adopt standard decoders from language modeling, which rely on a causal attention mask. This design introduces two fundamental conflicts in 3D scene understanding: sequential bias among order-agnostic 3D objects and restricted object-instruction attention, hindering task-specific reasoning. To overcome these limitations, we propose 3D Spatial Language Instruction Mask (3D-SLIM), an effective masking strategy that replaces the causal mask with an adaptive attention mask tailored to the spatial structure of 3D scenes. Our 3D-SLIM introduces two key components: a Geometry-adaptive Mask that constrains attention based on spatial density rather than token order, and an Instruction-aware Mask that enables object tokens to directly access instruction context. This design allows the model to process objects based on their spatial relationships while being guided by the user's task. 3D-SLIM is simple, requires no architectural modifications, and adds no extra parameters, yet it yields substantial performance improvements across diverse 3D scene-language tasks. Extensive experiments across multiple benchmarks and LLM baselines validate its effectiveness and underscore the critical role of decoder design in 3D multi-modal reasoning.

