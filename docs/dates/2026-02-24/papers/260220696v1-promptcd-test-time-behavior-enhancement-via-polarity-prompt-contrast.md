---
layout: default
title: PromptCD: Test-Time Behavior Enhancement via Polarity-Prompt Contrastive Decoding
---

# PromptCD: Test-Time Behavior Enhancement via Polarity-Prompt Contrastive Decoding
**arXiv**：[2602.20696v1](https://arxiv.org/abs/2602.20696) · [PDF](https://arxiv.org/pdf/2602.20696.pdf)  
**作者**：Baolong Bi, Yuyao Ge, Shenghua Liu, Yuchen He, Siqian Tong, Lizhe Chen, Lingrui Mei, Zehao Li, Yiwei Wang, Yujun Cai, Ming-Hsuan Yang, Xueqi Cheng  

**一句话要点**：提出PromptCD方法，通过极性提示对比解码在测试时增强大模型行为对齐

**关键词**：测试时行为控制, 对比解码, 大语言模型对齐, 视觉语言模型, 极性提示, 行为增强

## 3 点简述
- 核心问题：现有对齐方法依赖训练时数据和计算，成本高且适用范围窄
- 方法要点：构建正负提示对，对比模型内部分布以强化目标行为，无需额外训练
- 实验或效果：在LLMs上提升3H对齐目标，在VLMs上改善视觉注意力和VQA性能

## 摘要（原文）

> Reliable AI systems require large language models (LLMs) to exhibit behaviors aligned with human preferences and values. However, most existing alignment approaches operate at training time and rely on additional high-quality data, incurring significant computational and annotation costs. While recent work has shown that contrastive decoding can leverage a model's internal distributions to improve specific capabilities, its applicability remains limited to narrow behavioral scopes and scenarios. In this work, we introduce Polarity-Prompt Contrastive Decoding (PromptCD), a test-time behavior control method that generalizes contrastive decoding to broader enhancement settings. PromptCD constructs paired positive and negative guiding prompts for a target behavior and contrasts model responses-specifically token-level probability distributions in LLMs and visual attention patterns in VLMs-to reinforce desirable outcomes. This formulation extends contrastive decoding to a wide range of enhancement objectives and is applicable to both LLMs and Vision-Language Models (VLMs) without additional training. For LLMs, experiments on the "3H" alignment objectives (helpfulness, honesty, and harmlessness) demonstrate consistent and substantial improvements, indicating that post-trained models can achieve meaningful self-enhancement purely at test time. For VLMs, we further analyze contrastive effects on visual attention, showing that PromptCD significantly improves VQA performance by reinforcing behavior-consistent visual grounding. Collectively, these results highlight PromptCD as a simple, general, and cost-efficient strategy for reliable behavior control across modalities.

