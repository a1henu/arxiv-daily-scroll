---
layout: default
title: BioLLMAgent: A Hybrid Framework with Enhanced Structural Interpretability for Simulating Human Decision-Making in Computational Psychiatry
---

# BioLLMAgent: A Hybrid Framework with Enhanced Structural Interpretability for Simulating Human Decision-Making in Computational Psychiatry
**arXiv**：[2603.05016v1](https://arxiv.org/abs/2603.05016) · [PDF](https://arxiv.org/pdf/2603.05016.pdf)  
**作者**：Zuo Fei, Kezhi Wang, Xiaomin Chen, Yizhou Huang  

**一句话要点**：提出BioLLMAgent混合框架，结合认知模型与LLM，以增强计算精神病学中人类决策模拟的结构可解释性。

**关键词**：计算精神病学, 混合框架, 结构可解释性, 人类决策模拟, 认知模型, 大语言模型代理

## 3 点简述
- 核心问题：计算精神病学中传统RL模型可解释性强但行为真实性不足，LLM代理行为真实但结构可解释性差。
- 方法要点：框架包含内部RL引擎、外部LLM外壳和决策融合机制，通过加权效用整合组件。
- 实验或效果：在Iowa Gambling Task上验证，准确模拟人类行为，参数可识别性高，并成功模拟认知行为疗法原则。

## 摘要（原文）

> Computational psychiatry faces a fundamental trade-off: traditional reinforcement learning (RL) models offer interpretability but lack behavioral realism, while large language model (LLM) agents generate realistic behaviors but lack structural interpretability. We introduce BioLLMAgent, a novel hybrid framework that combines validated cognitive models with the generative capabilities of LLMs. The framework comprises three core components: (i) an Internal RL Engine for experience-driven value learning; (ii) an External LLM Shell for high-level cognitive strategies and therapeutic interventions; and (iii) a Decision Fusion Mechanism for integrating components via weighted utility. Comprehensive experiments on the Iowa Gambling Task (IGT) across six clinical and healthy datasets demonstrate that BioLLMAgent accurately reproduces human behavioral patterns while maintaining excellent parameter identifiability (correlations $>0.67$). Furthermore, the framework successfully simulates cognitive behavioral therapy (CBT) principles and reveals, through multi-agent dynamics, that community-wide educational interventions may outperform individual treatments. Validated across reward-punishment learning and temporal discounting tasks, BioLLMAgent provides a structurally interpretable "computational sandbox" for testing mechanistic hypotheses and intervention strategies in psychiatric research.

