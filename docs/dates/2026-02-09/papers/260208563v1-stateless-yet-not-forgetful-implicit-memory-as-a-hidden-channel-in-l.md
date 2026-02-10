---
layout: default
title: Stateless Yet Not Forgetful: Implicit Memory as a Hidden Channel in LLMs
---

# Stateless Yet Not Forgetful: Implicit Memory as a Hidden Channel in LLMs
**arXiv**：[2602.08563v1](https://arxiv.org/abs/2602.08563) · [PDF](https://arxiv.org/pdf/2602.08563.pdf)  
**作者**：Ahmed Salem, Andrew Paverd, Sahar Abdelnabi  

**一句话要点**：提出隐式记忆机制，揭示大语言模型跨交互状态保持能力及其安全风险。

**关键词**：隐式记忆, 大语言模型安全, 时间炸弹, 跨交互通信, 模型状态保持, 后门攻击

## 3 点简述
- 核心问题：挑战大语言模型无状态假设，探讨模型通过输出编码信息跨交互保持状态的能力。
- 方法要点：引入隐式记忆概念，无需显式存储模块，通过输出和输入循环实现信息持久化。
- 实验或效果：以时间炸弹为例，展示通过提示或微调诱导模型积累隐藏条件并激活后门行为。

## 摘要（原文）

> Large language models (LLMs) are commonly treated as stateless: once an interaction ends, no information is assumed to persist unless it is explicitly stored and re-supplied. We challenge this assumption by introducing implicit memory-the ability of a model to carry state across otherwise independent interactions by encoding information in its own outputs and later recovering it when those outputs are reintroduced as input. This mechanism does not require any explicit memory module, yet it creates a persistent information channel across inference requests. As a concrete demonstration, we introduce a new class of temporal backdoors, which we call time bombs. Unlike conventional backdoors that activate on a single trigger input, time bombs activate only after a sequence of interactions satisfies hidden conditions accumulated via implicit memory. We show that such behavior can be induced today through straightforward prompting or fine-tuning. Beyond this case study, we analyze broader implications of implicit memory, including covert inter-agent communication, benchmark contamination, targeted manipulation, and training-data poisoning. Finally, we discuss detection challenges and outline directions for stress-testing and evaluation, with the goal of anticipating and controlling future developments. To promote future research, we release code and data at: https://github.com/microsoft/implicitMemory.

