---
layout: default
title: Bridging Efficiency and Transparency: Explainable CoT Compression in Multimodal Large Reasoning Models
---

# Bridging Efficiency and Transparency: Explainable CoT Compression in Multimodal Large Reasoning Models
**arXiv**：[2602.09485v1](https://arxiv.org/abs/2602.09485) · [PDF](https://arxiv.org/pdf/2602.09485.pdf)  
**作者**：Yizhi Wang, Linan Yue, Min-Ling Zhang  

**一句话要点**：提出可解释多模态思维链压缩器XMCC，以提升推理效率并保持解释性。

**关键词**：多模态推理, 思维链压缩, 可解释人工智能, 强化学习, 序列决策

## 3 点简述
- 核心问题：长思维链冗余影响多模态推理效率，且压缩过程缺乏解释性。
- 方法要点：基于强化学习的序列决策压缩，保留关键推理步骤并生成自然语言解释。
- 实验或效果：在代表性基准上验证了压缩效果和解释能力，提升推理效率。

## 摘要（原文）

> Long chains of thought (Long CoTs) are widely employed in multimodal reasoning models to tackle complex tasks by capturing detailed visual information. However, these Long CoTs are often excessively lengthy and contain redundant reasoning steps, which can hinder inference efficiency. Compressing these long CoTs is a natural solution, yet existing approaches face two major challenges: (1) they may compromise the integrity of visual-textual reasoning by removing essential alignment cues, and (2) the compression process lacks explainability, making it difficult to discern which information is critical. To address these problems, we propose XMCC, an eXplainable Multimodal CoT Compressor that formulates compression as a sequential decision-making process optimized via reinforcement learning. XMCC can effectively shorten reasoning trajectories while preserving key reasoning steps and answer correctness, and simultaneously generates natural-language explanations for its compression decisions. Extensive experiments on representative multimodal reasoning benchmarks demonstrate that XMCC not only reduces reasoning length but also provides explainable explanations, validating its effectiveness.

