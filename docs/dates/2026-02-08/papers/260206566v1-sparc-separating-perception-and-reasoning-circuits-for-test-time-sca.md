---
layout: default
title: SPARC: Separating Perception And Reasoning Circuits for Test-time Scaling of VLMs
---

# SPARC: Separating Perception And Reasoning Circuits for Test-time Scaling of VLMs
**arXiv**：[2602.06566v1](https://arxiv.org/abs/2602.06566) · [PDF](https://arxiv.org/pdf/2602.06566.pdf)  
**作者**：Niccolo Avogaro, Nayanika Debnath, Li Mi, Thomas Frick, Junling Wang, Zexue He, Hang Hua, Konrad Schindler, Mattia Rigotti  

**一句话要点**：提出SPARC框架以解决视觉语言模型测试时扩展中感知与推理纠缠的问题

**关键词**：视觉语言模型, 测试时扩展, 感知与推理分离, 视觉搜索, 模块化框架, 计算效率

## 3 点简述
- 核心问题：视觉语言模型测试时扩展中感知与推理纠缠，导致长上下文和错误级联。
- 方法要点：采用两阶段流水线，先视觉搜索定位相关区域，再基于区域进行推理。
- 实验或效果：在视觉推理基准上超越基线，如Qwen3VL-4B在V* VQA上准确率提升6.7个百分点。

## 摘要（原文）

> Despite recent successes, test-time scaling - i.e., dynamically expanding the token budget during inference as needed - remains brittle for vision-language models (VLMs): unstructured chains-of-thought about images entangle perception and reasoning, leading to long, disorganized contexts where small perceptual mistakes may cascade into completely wrong answers. Moreover, expensive reinforcement learning with hand-crafted rewards is required to achieve good performance. Here, we introduce SPARC (Separating Perception And Reasoning Circuits), a modular framework that explicitly decouples visual perception from reasoning. Inspired by sequential sensory-to-cognitive processing in the brain, SPARC implements a two-stage pipeline where the model first performs explicit visual search to localize question-relevant regions, then conditions its reasoning on those regions to produce the final answer. This separation enables independent test-time scaling with asymmetric compute allocation (e.g., prioritizing perceptual processing under distribution shift), supports selective optimization (e.g., improving the perceptual stage alone when it is the bottleneck for end-to-end performance), and accommodates compressed contexts by running global search at lower image resolutions and allocating high-resolution processing only to selected regions, thereby reducing total visual tokens count and compute. Across challenging visual reasoning benchmarks, SPARC outperforms monolithic baselines and strong visual-grounding approaches. For instance, SPARC improves the accuracy of Qwen3VL-4B on the $V^*$ VQA benchmark by 6.7 percentage points, and it surpasses "thinking with images" by 4.6 points on a challenging OOD task despite requiring a 200$\times$ lower token budget.

