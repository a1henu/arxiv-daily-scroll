---
layout: default
title: Do I Really Know? Learning Factual Self-Verification for Hallucination Reduction
---

# Do I Really Know? Learning Factual Self-Verification for Hallucination Reduction
**arXiv**：[2602.02018v1](https://arxiv.org/abs/2602.02018) · [PDF](https://arxiv.org/pdf/2602.02018.pdf)  
**作者**：Enes Altinisik, Masoomali Fatehkia, Fatih Deniz, Nadir Durrani, Majd Hawasly, Mohammad Raza, Husrev Taha Sencar  

**一句话要点**：提出VeriFY框架，通过一致性自验证减少大语言模型的事实性幻觉。

**关键词**：事实性幻觉, 自验证训练, 一致性判断, 损失掩码, 大语言模型优化

## 3 点简述
- 核心问题：大语言模型存在事实性幻觉，现有方法依赖外部验证或直接弃权，导致保守行为。
- 方法要点：训练时引入结构化验证轨迹，指导模型生成答案、验证查询、一致性判断和弃权决策，采用阶段级损失掩码避免强化幻觉。
- 实验或效果：在多个模型和规模上，幻觉率降低9.7%至53.3%，召回率仅轻微下降0.4%至5.7%，单源训练可跨数据集泛化。

## 摘要（原文）

> Factual hallucination remains a central challenge for large language models (LLMs). Existing mitigation approaches primarily rely on either external post-hoc verification or mapping uncertainty directly to abstention during fine-tuning, often resulting in overly conservative behavior. We propose VeriFY, a training-time framework that teaches LLMs to reason about factual uncertainty through consistency-based self-verification. VeriFY augments training with structured verification traces that guide the model to produce an initial answer, generate and answer a probing verification query, issue a consistency judgment, and then decide whether to answer or abstain. To address the risk of reinforcing hallucinated content when training on augmented traces, we introduce a stage-level loss masking approach that excludes hallucinated answer stages from the training objective while preserving supervision over verification behavior. Across multiple model families and scales, VeriFY reduces factual hallucination rates by 9.7 to 53.3 percent, with only modest reductions in recall (0.4 to 5.7 percent), and generalizes across datasets when trained on a single source. The source code, training data, and trained model checkpoints will be released upon acceptance.

