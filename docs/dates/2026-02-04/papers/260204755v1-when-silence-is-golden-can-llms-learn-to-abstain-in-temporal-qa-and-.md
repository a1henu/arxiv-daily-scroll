---
layout: default
title: When Silence Is Golden: Can LLMs Learn to Abstain in Temporal QA and Beyond?
---

# When Silence Is Golden: Can LLMs Learn to Abstain in Temporal QA and Beyond?
**arXiv**：[2602.04755v1](https://arxiv.org/abs/2602.04755) · [PDF](https://arxiv.org/pdf/2602.04755.pdf)  
**作者**：Xinyu Zhou, Chang Jin, Carsten Eickhoff, Zhijiang Guo, Seyed Ali Bahrainian  

**一句话要点**：提出结合思维链与强化学习的训练方法，以提升大语言模型在时序问答中的弃答能力。

**关键词**：时序问答, 弃答能力, 思维链, 强化学习, 不确定性建模

## 3 点简述
- 核心问题：大语言模型在时序问答中常忽略时间证据，产生误导性答案，缺乏弃答能力。
- 方法要点：将弃答作为可训练技能，通过思维链监督与弃答感知奖励的强化学习联合优化。
- 实验或效果：在TimeQA数据集上，模型超越GPT-4o，并在不可答问题上提升真阳性率20%。

## 摘要（原文）

> Large language models (LLMs) rarely admit uncertainty, often producing fluent but misleading answers, rather than abstaining (i.e., refusing to answer). This weakness is even evident in temporal question answering, where models frequently ignore time-sensitive evidence and conflate facts across different time-periods. In this paper, we present the first empirical study of training LLMs with an abstention ability while reasoning about temporal QA. Existing approaches such as calibration might be unreliable in capturing uncertainty in complex reasoning. We instead frame abstention as a teachable skill and introduce a pipeline that couples Chain-of-Thought (CoT) supervision with Reinforcement Learning (RL) guided by abstention-aware rewards. Our goal is to systematically analyze how different information types and training techniques affect temporal reasoning with abstention behavior in LLMs. Through extensive experiments studying various methods, we find that RL yields strong empirical gains on reasoning: a model initialized by Qwen2.5-1.5B-Instruct surpasses GPT-4o by $3.46\%$ and $5.80\%$ in Exact Match on TimeQA-Easy and Hard, respectively. Moreover, it improves the True Positive rate on unanswerable questions by $20\%$ over a pure supervised fine-tuned (SFT) variant. Beyond performance, our analysis shows that SFT induces overconfidence and harms reliability, while RL improves prediction accuracy but exhibits similar risks. Finally, by comparing implicit reasoning cues (e.g., original context, temporal sub-context, knowledge graphs) with explicit CoT supervision, we find that implicit information provides limited benefit for reasoning with abstention. Our study provides new insights into how abstention and reasoning can be jointly optimized, providing a foundation for building more reliable LLMs.

