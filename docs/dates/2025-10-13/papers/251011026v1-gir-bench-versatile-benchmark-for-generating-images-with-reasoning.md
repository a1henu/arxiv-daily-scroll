---
layout: default
title: GIR-Bench: Versatile Benchmark for Generating Images with Reasoning
---

# GIR-Bench: Versatile Benchmark for Generating Images with Reasoning
**arXiv**：[2510.11026v1](https://arxiv.org/abs/2510.11026) · [PDF](https://arxiv.org/pdf/2510.11026.pdf)  
**作者**：Hongxiang Li, Yaowei Li, Bin Lin, Yuwei Niu, Yuhang Yang, Xiaoshuang Huang, Jiayin Cai, Xiaolong Jiang, Yao Hu, Long Chen  

**一句话要点**：提出GIR-Bench基准以评估统一多模态模型在推理驱动图像生成中的能力

**关键词**：多模态基准, 图像生成, 推理评估, 理解-生成一致性, 文本到图像生成, 多步编辑

## 3 点简述
- 核心问题：缺乏系统基准评估多模态模型理解与生成的一致性和泛化能力
- 方法要点：设计三个子集评估理解-生成一致性、推理文本到图像生成和多步编辑
- 实验或效果：统一模型在推理任务中表现更好，但理解与生成间仍存在差距

## 摘要（原文）

> Unified multimodal models integrate the reasoning capacity of large language
> models with both image understanding and generation, showing great promise for
> advanced multimodal intelligence. However, the community still lacks a rigorous
> reasoning-centric benchmark to systematically evaluate the alignment between
> understanding and generation, and their generalization potential in complex
> visual tasks. To this end, we introduce \textbf{GIR-Bench}, a comprehensive
> benchmark that evaluates unified models across three complementary
> perspectives. Firstly, we investigate understanding-generation consistency
> (GIR-Bench-UGC), asking whether models can consistently leverage the same
> knowledge in both understanding and generation tasks. Secondly, we investigate
> whether models can perform reasoning-centric text-to-image generation that
> requires applying logical constraints and implicit knowledge to generate
> faithful visual content (GIR-Bench-T2I). Thirdly, we evaluate whether models
> can handle multi-step reasoning in editing (GIR-Bench-Edit). For each subset,
> we carefully design different task-specific evaluation pipelines tailored for
> each task. This enables fine-grained and interpretable evaluation while
> mitigating biases from the prevalent MLLM-as-a-Judge paradigm. Extensive
> ablations over various unified models and generation-only systems have shown
> that: Although unified models are more capable of reasoning-driven visual
> tasks, they still exhibit a persistent gap between understanding and
> generation. The data and code for GIR-Bench are available at
> \href{https://hkust-longgroup.github.io/GIR-Bench}{https://hkust-longgroup.github.io/GIR-Bench}.

