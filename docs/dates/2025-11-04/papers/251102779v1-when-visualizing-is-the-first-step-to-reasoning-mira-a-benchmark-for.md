---
layout: default
title: When Visualizing is the First Step to Reasoning: MIRA, a Benchmark for Visual Chain-of-Thought
---

# When Visualizing is the First Step to Reasoning: MIRA, a Benchmark for Visual Chain-of-Thought
**arXiv**：[2511.02779v1](https://arxiv.org/abs/2511.02779) · [PDF](https://arxiv.org/pdf/2511.02779.pdf)  
**作者**：Yiyang Zhou, Haoqin Tu, Zijun Wang, Zeyu Wang, Niklas Muennighoff, Fan Nie, Yejin Choi, James Zou, Chaorui Deng, Shen Yan, Haoqi Fan, Cihang Xie, Huaxiu Yao, Qinghao Ye  

**一句话要点**：提出MIRA基准以评估模型在生成中间视觉图像辅助推理的场景

**关键词**：视觉推理基准, 多模态评估, 链式思维, 中间图像生成, 空间关系推理

## 3 点简述
- 核心问题：传统文本链式思维方法在复杂空间推理任务中表现不佳，需视觉辅助。
- 方法要点：设计546个多模态问题，包含中间视觉图像和统一评估协议。
- 实验或效果：提供视觉线索使模型性能平均提升33.7%，强调视觉想象的关键作用。

## 摘要（原文）

> We propose MIRA, a new benchmark designed to evaluate models in scenarios
> where generating intermediate visual images is essential for successful
> reasoning. Unlike traditional CoT methods that rely solely on text, tasks in
> MIRA require models to generate and utilize intermediate images - such as
> sketches, structural diagrams, or path drawings - to guide their reasoning
> process. This setup closely mirrors how humans solve complex problems through
> "drawing to think". To solve this, MIRA focuses on tasks that are intrinsically
> challenging and involve complex structures, spatial relationships, or reasoning
> steps that are difficult to express through language alone. To ensure that our
> evaluation data is of high-quality, we include 546 multimodal problems,
> annotated with intermediate visual images and final answers. We also propose a
> unified evaluation protocol for MIRA that spans three levels of evaluation
> input: direct input with image and question only, text-only CoT input with
> image and thinking prompts, and Visual-CoT input with both annotated image
> clues and textual thinking prompts. To probe the upper bound of model capacity
> on our benchmark, we also report pass@k and majority voting accuracies under
> different k settings. Experimental results show that existing multimodal large
> language models, including strongest private models as well as strong
> open-weight models, perform poorly when relying solely on textual prompts.
> However, when intermediate visual cues are provided, model performance improves
> consistently, yielding an average relative gain of 33.7% across all models and
> tasks. We also probe the upper bound by expanding the search space and
> designing textual prompts aligned with Visual-CoT, but both yield only limited
> improvements compared to our Visual-CoT setting. These results underscore the
> critical role of imagined visual information in enabling successful reasoning
> on MIRA.

