---
layout: default
title: StruVis: Enhancing Reasoning-based Text-to-Image Generation via Thinking with Structured Vision
---

# StruVis: Enhancing Reasoning-based Text-to-Image Generation via Thinking with Structured Vision
**arXiv**：[2603.06032v1](https://arxiv.org/abs/2603.06032) · [PDF](https://arxiv.org/pdf/2603.06032.pdf)  
**作者**：Yuanhuiyi Lyu, Kaiyu Lei, Ziqiao Weng, Xu Zheng, Lutao Jiang, Teng Li, Yangfu Li, Ziyuan Huang, Linfeng Zhang, Xuming Hu  

**一句话要点**：提出StruVis框架，通过结构化视觉思维增强基于推理的文本到图像生成

**关键词**：文本到图像生成, 推理增强, 结构化视觉表示, 多模态大语言模型, 计算效率

## 3 点简述
- 核心问题：现有基于推理的文本到图像生成方法存在视觉上下文缺失或计算成本高的问题
- 方法要点：使用基于文本的结构化视觉表示作为中间推理状态，避免中间图像生成
- 实验或效果：在T2I-ReasonBench和WISE基准上分别实现4.61%和4%的性能提升

## 摘要（原文）

> Reasoning-based text-to-image (T2I) generation requires models to interpret complex prompts accurately. Existing reasoning frameworks can be broadly categorized into two types: (1) Text-Only Reasoning, which is computationally efficient but lacks access to visual context, often resulting in the omission of critical spatial and visual elements; and (2) Text-Image Interleaved Reasoning, which leverages a T2I generator to provide visual references during the reasoning process. While this approach enhances visual grounding, it incurs substantial computational costs and constrains the reasoning capacity of MLLMs to the representational limitations of the generator. To this end, we propose StruVis, a novel framework that enhances T2I generation through Thinking with Structured Vision. Instead of relying on intermediate image generation, StruVis employs text-based structured visual representations as intermediate reasoning states, thereby enabling the MLLM to effectively "perceive" visual structure within a purely text-based reasoning process. Powered by this, the reasoning potential for T2I generation of the MLLM is unlocked through structured-vision-guided reasoning. Additionally, as a generator-agnostic reasoning framework, our proposed StruVis can be seamlessly integrated with diverse T2I generators and efficiently enhance their performance in reasoning-based T2I generation. Extensive experiments demonstrate that StruVis achieves significant performance improvements on reasoning-based T2I benchmarks, e.g., a 4.61% gain on T2I-ReasonBench and a 4% gain on WISE.

