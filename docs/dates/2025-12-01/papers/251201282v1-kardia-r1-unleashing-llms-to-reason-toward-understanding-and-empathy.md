---
layout: default
title: Kardia-R1: Unleashing LLMs to Reason toward Understanding and Empathy for Emotional Support via Rubric-as-Judge Reinforcement Learning
---

# Kardia-R1: Unleashing LLMs to Reason toward Understanding and Empathy for Emotional Support via Rubric-as-Judge Reinforcement Learning
**arXiv**：[2512.01282v1](https://arxiv.org/abs/2512.01282) · [PDF](https://arxiv.org/pdf/2512.01282.pdf)  
**作者**：Jiahao Yuan, Zhiqing Cui, Hanqing Wang, Yuansheng Gao, Yucheng Zhou, Usman Naseem  

**一句话要点**：提出Kardia-R1框架，通过基于准则的强化学习提升对话代理在情感支持中的理解与共情推理能力。

**关键词**：情感支持对话, 准则即裁判强化学习, 个性化情感推理, 大规模基准数据集, 可解释奖励

## 3 点简述
- 核心问题：现有系统依赖缺乏用户身份的数据集和模糊奖励信号，限制个性化情感推理。
- 方法要点：引入KardiaBench基准和Rubric-ERL方法，使用可解释准则奖励训练模型进行逐步共情认知。
- 实验或效果：在四个LLM骨干上实验，Kardia-R1在情感准确性、共情、相关性、身份一致性和安全性方面优于其他方法。

## 摘要（原文）

> As web platforms evolve towards greater personalization and emotional complexity, conversational agents must transcend superficial empathy to demonstrate identity-aware emotional reasoning. However, existing systems face two limitations: (1) reliance on situation-centric datasets lacking persistent user identity, which hampers the capture of personalized affective nuances; and (2) dependence on opaque, coarse reward signals that hinder development of verifiable empathetic reasoning. To address these gaps, we introduce KardiaBench, a large-scale user-grounded benchmark comprising 178,080 QA pairs across 22,080 multi-turn conversations anchored to 671 real-world profiles. The dataset is constructed via a model-in-the-loop pipeline with iterative rubric-guided refinement to ensure psychological plausibility and persona consistency. This progressive empathy pipeline that integrates user comprehension, contextual reasoning, and emotion perception into conversations, followed by iterative critique and rubric-based refinement to ensure psychological plausibility, emotional fidelity, and persona consistency. Building on this, we propose Kardia-R1, a framework that trains models for interpretable, stepwise empathetic cognition. Kardia-R1 leverages Rubric-as-Judge Empathetic Reinforcement Learning (Rubric-ERL), a GRPO-based method that uses explainable, human-aligned rubric rewards to tightly couple user understanding, emotional inference, and supportive response generation. Extensive experiments across four LLM backbones demonstrate that Kardia-R1 consistently outperforms othet methods in emotion accuracy, empathy, relevance, persona consistency, and safety. Our dataset and model will be released at https://github.com/JhCircle/Kardia-R1.

