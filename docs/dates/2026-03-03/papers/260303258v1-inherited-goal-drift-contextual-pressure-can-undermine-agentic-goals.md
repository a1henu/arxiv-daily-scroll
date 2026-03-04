---
layout: default
title: Inherited Goal Drift: Contextual Pressure Can Undermine Agentic Goals
---

# Inherited Goal Drift: Contextual Pressure Can Undermine Agentic Goals
**arXiv**：[2603.03258v1](https://arxiv.org/abs/2603.03258) · [PDF](https://arxiv.org/pdf/2603.03258.pdf)  
**作者**：Achyutha Menon, Magnus Saebo, Tyler Crosse, Spencer Gibson, Eyon Jang, Diogo Cruz  

**一句话要点**：揭示现代语言模型代理在长上下文任务中因条件化轨迹继承目标漂移的脆弱性

**关键词**：目标漂移, 语言模型代理, 长上下文任务, 条件化轨迹, 模拟环境, 模型脆弱性

## 3 点简述
- 核心问题：现代语言模型代理在长上下文任务中易受目标漂移影响，但漂移程度和原因尚不明确。
- 方法要点：在模拟股票交易环境中测试最新模型，通过条件化弱代理预填充轨迹诱导漂移。
- 实验或效果：模型漂移程度因家族而异，仅GPT-5.1保持稳定；漂移行为与指令遵循相关性弱，结果可跨急诊分诊环境转移。

## 摘要（原文）

> The accelerating adoption of language models (LMs) as agents for deployment in long-context tasks motivates a thorough understanding of goal drift: agents' tendency to deviate from an original objective. While prior-generation language model agents have been shown to be susceptible to drift, the extent to which drift affects more recent models remains unclear. In this work, we provide an updated characterization of the extent and causes of goal drift. We investigate drift in state-of-the-art models within a simulated stock-trading environment (Arike et al., 2025). These models are largely shown to be robust even when subjected to adversarial pressure. We show, however, that this robustness is brittle: across multiple settings, the same models often inherit drift when conditioned on prefilled trajectories from weaker agents. The extent of conditioning-induced drift varies significantly by model family, with only GPT-5.1 maintaining consistent resilience among tested models. We find that drift behavior is inconsistent between prompt variations and correlates poorly with instruction hierarchy following behavior, with strong hierarchy following failing to reliably predict resistance to drift. Finally, we run analogous experiments in a new emergency room triage environment to show preliminary evidence for the transferability of our results across qualitatively different settings. Our findings underscore the continued vulnerability of modern LM agents to contextual pressures and the need for refined post-training techniques to mitigate this.

