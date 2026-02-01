---
layout: default
title: UEval: A Benchmark for Unified Multimodal Generation
---

# UEval: A Benchmark for Unified Multimodal Generation
**arXiv**：[2601.22155v1](https://arxiv.org/abs/2601.22155) · [PDF](https://arxiv.org/pdf/2601.22155.pdf)  
**作者**：Bo Li, Yida Yin, Wenhao Chai, Xingyu Fu, Zhuang Liu  

**一句话要点**：提出UEval基准以评估统一多模态生成模型，涵盖8个真实任务和1000个专家策划问题。

**关键词**：多模态生成评估, 统一模型基准, 量规评分系统, 专家策划问题, 推理能力分析

## 3 点简述
- 核心问题：现有评估方法难以捕捉开放多模态生成的细微差别，依赖MLLM评分可能不准确。
- 方法要点：设计基于量规的评分系统，结合MLLM生成和专家验证，包含10,417个已验证标准。
- 实验或效果：当前模型表现有限，GPT-5-Thinking得分66.4，推理模型优于非推理模型，推理能力可能关键。

## 摘要（原文）

> We introduce UEval, a benchmark to evaluate unified models, i.e., models capable of generating both images and text. UEval comprises 1,000 expert-curated questions that require both images and text in the model output, sourced from 8 real-world tasks. Our curated questions cover a wide range of reasoning types, from step-by-step guides to textbook explanations. Evaluating open-ended multimodal generation is non-trivial, as simple LLM-as-a-judge methods can miss the subtleties. Different from previous works that rely on multimodal Large Language Models (MLLMs) to rate image quality or text accuracy, we design a rubric-based scoring system in UEval. For each question, reference images and text answers are provided to a MLLM to generate an initial rubric, consisting of multiple evaluation criteria, and human experts then refine and validate these rubrics. In total, UEval contains 10,417 validated rubric criteria, enabling scalable and fine-grained automatic scoring. UEval is challenging for current unified models: GPT-5-Thinking scores only 66.4 out of 100, while the best open-source model reaches merely 49.1. We observe that reasoning models often outperform non-reasoning ones, and transferring reasoning traces from a reasoning model to a non-reasoning model significantly narrows the gap. This suggests that reasoning may be important for tasks requiring complex multimodal understanding and generation.

