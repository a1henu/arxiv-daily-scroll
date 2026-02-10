---
layout: default
title: CoTZero: Annotation-Free Human-Like Vision Reasoning via Hierarchical Synthetic CoT
---

# CoTZero: Annotation-Free Human-Like Vision Reasoning via Hierarchical Synthetic CoT
**arXiv**：[2602.08339v1](https://arxiv.org/abs/2602.08339) · [PDF](https://arxiv.org/pdf/2602.08339.pdf)  
**作者**：Chengyi Du, Yazhe Niu, Dazhong Shen, Luxin Xu  

**一句话要点**：提出CoTZero以解决视觉语言模型缺乏人类式视觉推理的问题

**关键词**：视觉语言模型, 视觉推理, 思维链合成, 分层推理, 强化微调, 无标注学习

## 3 点简述
- 核心问题：视觉语言模型依赖表面关联，缺乏逻辑连贯的结构化表示，阻碍组合和可验证推理。
- 方法要点：采用无标注范式，包括双阶段数据合成和认知对齐训练，通过合成思维链数据强化分层推理。
- 实验或效果：在包含词汇扰动负例的多级语义不一致基准上，F1得分达83.33%，验证了方法的有效性。

## 摘要（原文）

> Recent advances in vision-language models (VLMs) have markedly improved image-text alignment, yet they still fall short of human-like visual reasoning. A key limitation is that many VLMs rely on surface correlations rather than building logically coherent structured representations, which often leads to missed higher-level semantic structure and non-causal relational understanding, hindering compositional and verifiable reasoning. To address these limitations by introducing human models into the reasoning process, we propose CoTZero, an annotation-free paradigm with two components: (i) a dual-stage data synthesis approach and (ii) a cognition-aligned training method. In the first component, we draw inspiration from neurocognitive accounts of compositional productivity and global-to-local analysis. In the bottom-up stage, CoTZero extracts atomic visual primitives and incrementally composes them into diverse, structured question-reasoning forms. In the top-down stage, it enforces hierarchical reasoning by using coarse global structure to guide the interpretation of local details and causal relations. In the cognition-aligned training component, built on the synthesized CoT data, we introduce Cognitively Coherent Verifiable Rewards (CCVR) in Reinforcement Fine-Tuning (RFT) to further strengthen VLMs' hierarchical reasoning and generalization, providing stepwise feedback on reasoning coherence and factual correctness. Experiments show that CoTZero achieves an F1 score of 83.33 percent on our multi-level semantic inconsistency benchmark with lexical-perturbation negatives, across both in-domain and out-of-domain settings. Ablations confirm that each component contributes to more interpretable and human-aligned visual reasoning.

