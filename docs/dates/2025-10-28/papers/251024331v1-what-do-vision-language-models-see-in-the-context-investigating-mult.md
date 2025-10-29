---
layout: default
title: What do vision-language models see in the context? Investigating multimodal in-context learning
---

# What do vision-language models see in the context? Investigating multimodal in-context learning
**arXiv**：[2510.24331v1](https://arxiv.org/abs/2510.24331) · [PDF](https://arxiv.org/pdf/2510.24331.pdf)  
**作者**：Gabriel O. dos Santos, Esther Colombini, Sandra Avila  

**一句话要点**：系统研究视觉语言模型的多模态上下文学习，揭示其局限与影响因素

**关键词**：视觉语言模型, 上下文学习, 多模态集成, 注意力机制, 指令调优, 图像描述

## 3 点简述
- 核心问题：视觉语言模型在多模态上下文学习中的有效性未充分探索，存在视觉与文本信息整合不足
- 方法要点：评估七种模型在图像描述任务上，分析提示设计、架构选择和训练策略的影响
- 实验或效果：训练于图像-文本交错数据提升性能，但注意力分析显示模型主要依赖文本线索

## 摘要（原文）

> In-context learning (ICL) enables Large Language Models (LLMs) to learn tasks
> from demonstration examples without parameter updates. Although it has been
> extensively studied in LLMs, its effectiveness in Vision-Language Models (VLMs)
> remains underexplored. In this work, we present a systematic study of ICL in
> VLMs, evaluating seven models spanning four architectures on three image
> captioning benchmarks. We analyze how prompt design, architectural choices, and
> training strategies influence multimodal ICL. To our knowledge, we are the
> first to analyze how attention patterns in VLMs vary with an increasing number
> of in-context demonstrations. Our results reveal that training on imag-text
> interleaved data enhances ICL performance but does not imply effective
> integration of visual and textual information from demonstration examples. In
> contrast, instruction tuning improves instruction-following but can reduce
> reliance on in-context demonstrations, suggesting a trade-off between
> instruction alignment and in-context adaptation. Attention analyses further
> show that current VLMs primarily focus on textual cues and fail to leverage
> visual information, suggesting a limited capacity for multimodal integration.
> These findings highlight key limitations in the ICL abilities of current VLMs
> and provide insights for enhancing their ability to learn from multimodal
> in-context examples.

