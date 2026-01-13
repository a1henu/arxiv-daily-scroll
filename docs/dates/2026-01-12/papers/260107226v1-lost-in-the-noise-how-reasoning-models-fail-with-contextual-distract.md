---
layout: default
title: Lost in the Noise: How Reasoning Models Fail with Contextual Distractors
---

# Lost in the Noise: How Reasoning Models Fail with Contextual Distractors
**arXiv**：[2601.07226v1](https://arxiv.org/abs/2601.07226) · [PDF](https://arxiv.org/pdf/2601.07226.pdf)  
**作者**：Seongyun Lee, Yongrae Jo, Minju Seo, Moontae Lee, Minjoon Seo  

**一句话要点**：提出NoisyBench基准和Rationale-Aware Reward方法，以评估和增强推理模型在噪声上下文中的鲁棒性。

**关键词**：推理模型鲁棒性, 噪声上下文基准, Rationale-Aware Reward, 代理AI系统, 注意力可视化, 逆缩放趋势

## 3 点简述
- 核心问题：当前推理模型在噪声上下文（如随机文档、无关聊天历史）中性能显著下降，现有基准未能捕捉此现实。
- 方法要点：引入NoisyBench基准系统评估模型鲁棒性，并提出Rationale-Aware Reward方法激励模型识别噪声中有用信息。
- 实验或效果：评估显示先进模型性能下降高达80%，Rationale-Aware Reward显著提升鲁棒性，而提示、微调等方法无效。

## 摘要（原文）

> Recent advances in reasoning models and agentic AI systems have led to an increased reliance on diverse external information. However, this shift introduces input contexts that are inherently noisy, a reality that current sanitized benchmarks fail to capture. We introduce NoisyBench, a comprehensive benchmark that systematically evaluates model robustness across 11 datasets in RAG, reasoning, alignment, and tool-use tasks against diverse noise types, including random documents, irrelevant chat histories, and hard negative distractors. Our evaluation reveals a catastrophic performance drop of up to 80% in state-of-the-art models when faced with contextual distractors. Crucially, we find that agentic workflows often amplify these errors by over-trusting noisy tool outputs, and distractors can trigger emergent misalignment even without adversarial intent. We find that prompting, context engineering, SFT, and outcome-reward only RL fail to ensure robustness; in contrast, our proposed Rationale-Aware Reward (RARE) significantly strengthens resilience by incentivizing the identification of helpful information within noise. Finally, we uncover an inverse scaling trend where increased test-time computation leads to worse performance in noisy settings and demonstrate via attention visualization that models disproportionately focus on distractor tokens, providing vital insights for building the next generation of robust, reasoning-capable agents.

