---
layout: default
title: Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents
---

# Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents
**arXiv**：[2602.12662v1](https://arxiv.org/abs/2602.12662) · [PDF](https://arxiv.org/pdf/2602.12662.pdf)  
**作者**：Ruihan Yang, Fanghua Ye, Xiang We, Ruoqing Zhao, Kang Luo, Xinbo Xu, Bo Zhao, Ruotian Ma, Shanyi Wang, Zhaopeng Tu, Xiaolong Li, Deqing Yang, Linus  

**一句话要点**：提出CogRouter框架，通过动态调整认知深度以优化LLM代理在长视野任务中的效率与性能。

**关键词**：LLM代理, 认知深度适配, 多步决策, ACT-R理论, 两阶段训练, 置信度优化

## 3 点简述
- 核心问题：现有LLM代理采用固定认知模式，在长视野任务中无法适应步骤间变化的认知需求，导致效率低下。
- 方法要点：基于ACT-R理论设计四层认知等级，通过两阶段训练（CoSFT和CoPO）实现步骤级认知深度动态适配，以最大化行动置信度。
- 实验或效果：在ALFWorld和ScienceWorld上达到SOTA性能，使用Qwen2.5-7B时成功率82.3%，优于GPT-4o等模型，且令牌使用减少62%。

## 摘要（原文）

> Large language models (LLMs) are increasingly deployed as autonomous agents for multi-turn decision-making tasks. However, current agents typically rely on fixed cognitive patterns: non-thinking models generate immediate responses, while thinking models engage in deep reasoning uniformly. This rigidity is inefficient for long-horizon tasks, where cognitive demands vary significantly from step to step, with some requiring strategic planning and others only routine execution. In this paper, we introduce CogRouter, a framework that trains agents to dynamically adapt cognitive depth at each step. Grounded in ACT-R theory, we design four hierarchical cognitive levels ranging from instinctive responses to strategic planning. Our two-stage training approach includes Cognition-aware Supervised Fine-tuning (CoSFT) to instill stable level-specific patterns, and Cognition-aware Policy Optimization (CoPO) for step-level credit assignment via confidence-aware advantage reweighting. The key insight is that appropriate cognitive depth should maximize the confidence of the resulting action. Experiments on ALFWorld and ScienceWorld demonstrate that CogRouter achieves state-of-the-art performance with superior efficiency. With Qwen2.5-7B, it reaches an 82.3% success rate, outperforming GPT-4o (+40.3%), OpenAI-o3 (+18.3%), and GRPO (+14.0%), while using 62% fewer tokens.

