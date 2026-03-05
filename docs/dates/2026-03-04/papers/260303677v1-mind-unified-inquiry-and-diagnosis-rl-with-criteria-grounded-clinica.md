---
layout: default
title: MIND: Unified Inquiry and Diagnosis RL with Criteria Grounded Clinical Supports for Psychiatric Consultation
---

# MIND: Unified Inquiry and Diagnosis RL with Criteria Grounded Clinical Supports for Psychiatric Consultation
**arXiv**：[2603.03677v1](https://arxiv.org/abs/2603.03677) · [PDF](https://arxiv.org/pdf/2603.03677.pdf)  
**作者**：Guoyi Li, Shihao Xu, Jiatong Ma, Yunyun Han, Jianhua Chen, Yafeng Deng  

**一句话要点**：提出MIND框架，通过标准基础临床支持解决精神科咨询中的诊断准确性和询问策略优化问题。

**关键词**：精神科咨询, 强化学习, 临床推理, 多轮对话, 诊断准确性

## 3 点简述
- 核心问题：现有方法在精神科咨询中易产生无依据临床断言，且多轮交互中询问易偏离主题或效率低。
- 方法要点：构建标准基础精神科推理库，提供临床支持；结合强化学习，通过过程奖励和轨迹修正机制优化询问与诊断决策。
- 实验或效果：在诊断准确性、交互质量、可解释性和泛化性上优于基线方法。

## 摘要（原文）

> Large language models (LLMs) have advanced medical dialogue systems, yet psychiatric consultation poses substantially higher demands due to subjective ambiguity and comorbidity complexity: an agent must continuously extract psychopathological cues from incomplete and inconsistent patient reports in multi-turn interactions and perform rigorous differential diagnostic reasoning. However, existing methods face two fundamental challenges. First, without criteria-grounded clinical supports, they are prone to unsupported clinical assertions when symptoms are atypical or underspecified. Second, in multi-turn interactions, they struggle to mitigate inquiry drift (off-topic or low-yield questioning) and optimize questioning strategies. To address these challenges, we propose MIND, a unified inquiry--diagnosis reinforcement learning framework for psychiatric consultation. Specifically, we build a Criteria-Grounded Psychiatric Reasoning Bank (PRB) that summarizes dialogue context into clinical retrieval states, retrieves semantically similar reference consultations, and distills reusable criteria-grounded clinical supports to guide criteria-aligned inquiry and reasoning. Building on this foundation, MIND enforces explicit clinical reasoning with rubric-based process rewards to provide fine-grained supervision over intermediate decision steps, and incorporates a value-aware trajectory rectification mechanism to jointly improve information acquisition and diagnostic decision-making across turns. Extensive experiments demonstrate that MIND consistently outperforms strong baselines in diagnostic accuracy, empathetic interaction quality, interpretability, and generalization.

