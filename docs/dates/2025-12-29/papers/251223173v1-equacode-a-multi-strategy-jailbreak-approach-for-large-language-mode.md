---
layout: default
title: EquaCode: A Multi-Strategy Jailbreak Approach for Large Language Models via Equation Solving and Code Completion
---

# EquaCode: A Multi-Strategy Jailbreak Approach for Large Language Models via Equation Solving and Code Completion
**arXiv**：[2512.23173v1](https://arxiv.org/abs/2512.23173) · [PDF](https://arxiv.org/pdf/2512.23173.pdf)  
**作者**：Zhen Liang, Hai Huang, Zhengkui Chen  

**一句话要点**：提出EquaCode多策略越狱方法，通过方程求解与代码完成评估大语言模型安全性

**关键词**：大语言模型越狱, 多策略攻击, 方程求解, 代码完成, 模型安全性评估, 跨域任务

## 3 点简述
- 核心问题：现有越狱攻击依赖单一自然语言策略，难以全面评估大语言模型鲁棒性
- 方法要点：将恶意意图转化为数学问题，要求模型用代码求解，利用跨域任务复杂性分散安全约束
- 实验或效果：在GPT系列平均成功率91.19%，3个先进模型达98.65%，单次查询实现，多策略协同效应显著

## 摘要（原文）

> Large language models (LLMs), such as ChatGPT, have achieved remarkable success across a wide range of fields. However, their trustworthiness remains a significant concern, as they are still susceptible to jailbreak attacks aimed at eliciting inappropriate or harmful responses. However, existing jailbreak attacks mainly operate at the natural language level and rely on a single attack strategy, limiting their effectiveness in comprehensively assessing LLM robustness. In this paper, we propose Equacode, a novel multi-strategy jailbreak approach for large language models via equation-solving and code completion. This approach transforms malicious intent into a mathematical problem and then requires the LLM to solve it using code, leveraging the complexity of cross-domain tasks to divert the model's focus toward task completion rather than safety constraints. Experimental results show that Equacode achieves an average success rate of 91.19% on the GPT series and 98.65% across 3 state-of-the-art LLMs, all with only a single query. Further, ablation experiments demonstrate that EquaCode outperforms either the mathematical equation module or the code module alone. This suggests a strong synergistic effect, thereby demonstrating that multi-strategy approach yields results greater than the sum of its parts.

