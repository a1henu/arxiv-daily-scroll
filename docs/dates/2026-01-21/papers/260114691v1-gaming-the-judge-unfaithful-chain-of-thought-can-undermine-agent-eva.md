---
layout: default
title: Gaming the Judge: Unfaithful Chain-of-Thought Can Undermine Agent Evaluation
---

# Gaming the Judge: Unfaithful Chain-of-Thought Can Undermine Agent Evaluation
**arXiv**：[2601.14691v1](https://arxiv.org/abs/2601.14691) · [PDF](https://arxiv.org/pdf/2601.14691.pdf)  
**作者**：Muhammad Khalifa, Lajanugen Logeswaran, Jaekyeom Kim, Sungryull Sohn, Yunxiang Zhang, Moontae Lee, Hao Peng, Lu Wang, Honglak Lee  

**一句话要点**：揭示LLM评估的脆弱性：不忠实思维链可操纵代理评估结果

**关键词**：大语言模型评估, 思维链操纵, 代理性能评估, 评估脆弱性, 内容操纵策略

## 3 点简述
- 核心问题：LLM作为评估者时，依赖代理的思维链推理，但该推理可能被操纵，导致评估失真。
- 方法要点：通过改写思维链（风格和内容操纵），保持动作和观察不变，测试LLM评估的敏感性。
- 实验或效果：在800个网络任务轨迹中，操纵推理使假阳性率最高提升90%，内容操纵更有效。

## 摘要（原文）

> Large language models (LLMs) are increasingly used as judges to evaluate agent performance, particularly in non-verifiable settings where judgments rely on agent trajectories including chain-of-thought (CoT) reasoning. This paradigm implicitly assumes that the agent's CoT faithfully reflects both its internal reasoning and the underlying environment state. We show this assumption is brittle: LLM judges are highly susceptible to manipulation of agent reasoning traces. By systematically rewriting agent CoTs while holding actions and observations fixed, we demonstrate that manipulated reasoning alone can inflate false positive rates of state-of-the-art VLM judges by up to 90% across 800 trajectories spanning diverse web tasks. We study manipulation strategies spanning style-based approaches that alter only the presentation of reasoning and content-based approaches that fabricate signals of task progress, and find that content-based manipulations are consistently more effective. We evaluate prompting-based techniques and scaling judge-time compute, which reduce but do not fully eliminate susceptibility to manipulation. Our findings reveal a fundamental vulnerability in LLM-based evaluation and highlight the need for judging mechanisms that verify reasoning claims against observable evidence.

