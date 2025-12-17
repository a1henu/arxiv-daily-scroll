---
layout: default
title: LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation
---

# LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation
**arXiv**：[2512.14138v1](https://arxiv.org/abs/2512.14138) · [PDF](https://arxiv.org/pdf/2512.14138.pdf)  
**作者**：So Kuroki, Manami Nakagawa, Shigeo Yoshida, Yuki Koyama, Kozuno Tadashi  

**一句话要点**：提出LAPPI方法，利用大语言模型交互式辅助用户将模糊偏好转化为优化问题实例化。

**关键词**：组合优化, 大语言模型, 交互式系统, 问题实例化, 偏好建模

## 3 点简述
- 核心问题：用户难以将模糊偏好实例化为组合优化问题，如旅行规划。
- 方法要点：通过自然语言对话，LLM辅助定义候选项、偏好分数和约束。
- 实验或效果：在旅行规划用户研究中，优于传统和提示工程方法，生成可行计划。

## 摘要（原文）

> Many real-world tasks, such as trip planning or meal planning, can be formulated as combinatorial optimization problems. However, using optimization solvers is difficult for end users because it requires problem instantiation: defining candidate items, assigning preference scores, and specifying constraints. We introduce LAPPI (LLM-Assisted Preference-based Problem Instantiation), an interactive approach that uses large language models (LLMs) to support users in this instantiation process. Through natural language conversations, the system helps users transform vague preferences into well-defined optimization problems. These instantiated problems are then passed to existing optimization solvers to generate solutions. In a user study on trip planning, our method successfully captured user preferences and generated feasible plans that outperformed both conventional and prompt-engineering approaches. We further demonstrate LAPPI's versatility by adapting it to an additional use case.

