---
layout: default
title: AgenticRed: Optimizing Agentic Systems for Automated Red-teaming
---

# AgenticRed: Optimizing Agentic Systems for Automated Red-teaming
**arXiv**：[2601.13518v1](https://arxiv.org/abs/2601.13518) · [PDF](https://arxiv.org/pdf/2601.13518.pdf)  
**作者**：Jiayi Yuan, Jonathan Nöther, Natasha Jaques, Goran Radanović  

**一句话要点**：提出AgenticRed以自动化设计红队系统，提升AI安全评估效率

**关键词**：自动化红队, 系统设计优化, 进化选择, AI安全评估, 上下文学习

## 3 点简述
- 核心问题：现有自动化红队方法依赖人工设计工作流，存在偏见且探索成本高。
- 方法要点：利用LLM上下文学习迭代设计红队系统，采用进化选择优化系统结构。
- 实验或效果：在HarmBench上攻击成功率显著提升，对专有模型具有强迁移性。

## 摘要（原文）

> While recent automated red-teaming methods show promise for systematically exposing model vulnerabilities, most existing approaches rely on human-specified workflows. This dependence on manually designed workflows suffers from human biases and makes exploring the broader design space expensive. We introduce AgenticRed, an automated pipeline that leverages LLMs' in-context learning to iteratively design and refine red-teaming systems without human intervention. Rather than optimizing attacker policies within predefined structures, AgenticRed treats red-teaming as a system design problem. Inspired by methods like Meta Agent Search, we develop a novel procedure for evolving agentic systems using evolutionary selection, and apply it to the problem of automatic red-teaming. Red-teaming systems designed by AgenticRed consistently outperform state-of-the-art approaches, achieving 96% attack success rate (ASR) on Llama-2-7B (36% improvement) and 98% on Llama-3-8B on HarmBench. Our approach exhibits strong transferability to proprietary models, achieving 100% ASR on GPT-3.5-Turbo and GPT-4o-mini, and 60% on Claude-Sonnet-3.5 (24% improvement). This work highlights automated system design as a powerful paradigm for AI safety evaluation that can keep pace with rapidly evolving models.

