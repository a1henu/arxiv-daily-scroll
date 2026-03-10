---
layout: default
title: M$^3$-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering
---

# M$^3$-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering
**arXiv**：[2603.08369v1](https://arxiv.org/abs/2603.08369) · [PDF](https://arxiv.org/pdf/2603.08369.pdf)  
**作者**：Peijin Xie, Zhen Xu, Bingquan Liu, Baoxun Wang  

**一句话要点**：提出M3-ACE多智能体上下文工程框架以解决多模态数学推理中的视觉感知不准确问题

**关键词**：多模态数学推理, 视觉感知校正, 多智能体协作, 上下文工程, 数学视觉基准

## 3 点简述
- 核心问题：多模态大语言模型在视觉数学推理中性能受限，主要源于视觉感知提取错误或不完整，而非推理能力不足
- 方法要点：通过多智能体协作维护共享视觉证据列表，解耦感知与推理，引入摘要和精炼工具支持稳定迭代修正
- 实验或效果：在MathVision等基准测试中显著提升性能，MathVision达到89.1分，实现新SOTA结果

## 摘要（原文）

> Multimodal large language models have recently shown promising progress in visual mathematical reasoning. However, their performance is often limited by a critical yet underexplored bottleneck: inaccurate visual perception. Through systematic analysis, we find that the most failures originate from incorrect or incomplete visual evidence extraction rather than deficiencies in reasoning capability. Moreover, models tend to remain overly confident in their initial perceptions, making standard strategies such as prompt engineering, multi-round self-reflection, or posterior guidance insufficient to reliably correct errors.
>   To address this limitation, we propose M3-ACE, a multi-agentic context engineering framework designed to rectify visual perception in multimodal math reasoning. Instead of directly aggregating final answers, our approach decouples perception and reasoning by dynamically maintaining a shared context centered on visual evidence lists. Multiple agents collaboratively contribute complementary observations, enabling the system to expose inconsistencies and recover missing perceptual information. To support stable multi-turn collaboration, we further introduce two lightweight tools: a Summary Tool that organizes evidence from different agents into consistent, complementary, and conflicting components, and a Refine Tool that filters unreliable samples and guides iterative correction.
>   Extensive experiments demonstrate that M3-ACE substantially improves visual mathematical reasoning performance across multiple benchmarks. Our method establishes new state-of-the-art results 89.1 on the MathVision benchmark and achieves consistent improvements on other related datasets, including MathVista and MathVerse. These results highlight the importance of perception-centric multi-agent collaboration for advancing multimodal reasoning systems.

