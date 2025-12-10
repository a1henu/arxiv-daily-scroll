---
layout: default
title: Reflecting with Two Voices: A Co-Adaptive Dual-Strategy Framework for LLM-Based Agent Decision Making
---

# Reflecting with Two Voices: A Co-Adaptive Dual-Strategy Framework for LLM-Based Agent Decision Making
**arXiv**：[2512.08366v1](https://arxiv.org/abs/2512.08366) · [PDF](https://arxiv.org/pdf/2512.08366.pdf)  
**作者**：Wentao Zhang, Qunbo Wang, Tao Zhang, Junsheng Wu, Hongping Gan, Yang Liu, Ling Dai, Shizhuang Deng, Shuntong Sun  

**一句话要点**：提出DuSAR框架，通过双策略协同适应解决LLM代理决策中的脆弱性和高开销问题。

**关键词**：LLM代理决策, 双策略协同适应, 反思机制, 轻量级推理, 演示无关框架, 计算效率优化

## 3 点简述
- 核心问题：LLM代理依赖外部演示或检索增强规划，导致脆弱性、泛化差和计算开销高。
- 方法要点：采用双策略（全局规划和局部策略）与轻量级反思机制，实现协同适应推理，无需演示。
- 实验或效果：在ALFWorld和Mind2Web上实现SOTA性能，成功率和效率显著提升，消融研究验证双策略必要性。

## 摘要（原文）

> Large language model (LLM) agents often rely on external demonstrations or retrieval-augmented planning, leading to brittleness, poor generalization, and high computational overhead. Inspired by human problem-solving, we propose DuSAR (Dual-Strategy Agent with Reflecting) - a demonstration-free framework that enables a single frozen LLM to perform co-adaptive reasoning via two complementary strategies: a high-level holistic plan and a context-grounded local policy. These strategies interact through a lightweight reflection mechanism, where the agent continuously assesses progress via a Strategy Fitness Score and dynamically revises its global plan when stuck or refines it upon meaningful advancement, mimicking human metacognitive behavior. On ALFWorld and Mind2Web, DuSAR achieves state-of-the-art performance with open-source LLMs (7B-70B), reaching 37.1% success on ALFWorld (Llama3.1-70B) - more than doubling the best prior result (13.0%) - and 4.02% on Mind2Web, also more than doubling the strongest baseline. Remarkably, it reduces per-step token consumption by 3-9X while maintaining strong performance. Ablation studies confirm the necessity of dual-strategy coordination. Moreover, optional integration of expert demonstrations further boosts results, highlighting DuSAR's flexibility and compatibility with external knowledge.

