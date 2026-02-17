---
layout: default
title: Broken Chains: The Cost of Incomplete Reasoning in LLMs
---

# Broken Chains: The Cost of Incomplete Reasoning in LLMs
**arXiv**：[2602.14444v1](https://arxiv.org/abs/2602.14444) · [PDF](https://arxiv.org/pdf/2602.14444.pdf)  
**作者**：Ian Su, Gaurav Purushothaman, Jey Narayan, Ruhika Goel, Kevin Zhu, Sunishchal Dev, Yash More, Maheep Chaudhary  

**一句话要点**：提出约束推理模态框架，评估大语言模型在令牌限制下的推理性能与成本

**关键词**：推理模态约束, 令牌预算削减, 数学基准评估, 模型鲁棒性分析, 推理成本优化

## 3 点简述
- 核心问题：推理专用模型在令牌约束下，不同推理模态（代码、自然语言等）的性能与成本影响
- 方法要点：通过框架强制模型仅用代码、注释、混合或无推理，并系统削减令牌预算至最优的10%-70%
- 实验或效果：在数学基准测试中，发现截断推理可能损害性能，代码模态更稳健，混合推理表现不佳，模型间鲁棒性差异显著

## 摘要（原文）

> Reasoning-specialized models like OpenAI's 5.1 and DeepSeek-V3.2 allocate substantial inference compute to extended chain-of-thought (CoT) traces, yet reasoning tokens incur significant costs. How do different reasoning modalities of code, natural language, hybrid, or none do perform under token constraints? We introduce a framework that constrains models to reason exclusively through code, comments, both, or neither, then systematically ablates token budgets to 10\%, 30\%, 50\%, and 70\% of optimal. We evaluate four frontier models (GPT-5.1, Gemini 3 Flash, DeepSeek-V3.2, Grok 4.1) across mathematical benchmarks (AIME, GSM8K, HMMT). Our findings reveal: (1) \textbf{truncated reasoning can hurt} as DeepSeek-V3.2 achieves 53\% with no reasoning but only 17\% with truncated CoT at 50\% budget; (2) \textbf{code degrades gracefully} as Gemini's comments collapse to 0\% while code maintains 43-47\%; (3) \textbf{hybrid reasoning underperforms} single modalities; (4) \textbf{robustness is model-dependent} as Grok maintains 80-90\% at 30\% budget where OpenAI and DeepSeek collapse to 7-27\%. These results suggest incomplete reasoning chains actively mislead models, with implications for deploying reasoning-specialized systems under resource constraints.

