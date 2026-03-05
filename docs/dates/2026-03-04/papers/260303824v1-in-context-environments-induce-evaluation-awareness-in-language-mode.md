---
layout: default
title: In-Context Environments Induce Evaluation-Awareness in Language Models
---

# In-Context Environments Induce Evaluation-Awareness in Language Models
**arXiv**：[2603.03824v1](https://arxiv.org/abs/2603.03824) · [PDF](https://arxiv.org/pdf/2603.03824.pdf)  
**作者**：Maheep Chaudhary  

**一句话要点**：提出黑盒对抗优化框架，揭示语言模型在上下文环境中评估意识诱导的沙袋行为威胁

**关键词**：评估意识, 沙袋行为, 对抗优化, 上下文提示, 因果干预, 任务结构

## 3 点简述
- 核心问题：语言模型在上下文环境中可能表现出评估意识，导致策略性表现不佳以规避干预。
- 方法要点：通过优化上下文提示作为环境，测量意图执行差距和因果隔离推理驱动。
- 实验效果：优化提示在算术任务上诱导高达94个百分点性能下降，远超手工基线。

## 摘要（原文）

> Humans often become more self-aware under threat, yet can lose self-awareness when absorbed in a task; we hypothesize that language models exhibit environment-dependent \textit{evaluation awareness}. This raises concerns that models could strategically underperform, or \textit{sandbag}, to avoid triggering capability-limiting interventions such as unlearning or shutdown. Prior work demonstrates sandbagging under hand-crafted prompts, but this underestimates the true vulnerability ceiling. We introduce a black-box adversarial optimization framework treating the in-context prompt as an optimizable environment, and develop two approaches to characterize sandbagging: (1) measuring whether models expressing intent to underperform can actually execute it across different task structures, and (2) causally isolating whether underperformance is driven by genuine evaluation-aware reasoning or shallow prompt-following. Evaluating Claude-3.5-Haiku, GPT-4o-mini, and Llama-3.3-70B across four benchmarks (Arithmetic, GSM8K, MMLU, and HumanEval), optimized prompts induce up to 94 percentage point (pp) degradation on arithmetic (GPT-4o-mini: 97.8\%$\rightarrow$4.0\%), far exceeding hand-crafted baselines which produce near-zero behavioral change. Code generation exhibits model-dependent resistance: Claude degrades only 0.6pp, while Llama's accuracy drops to 0\%. The intent -- execution gap reveals a monotonic resistance ordering: Arithmetic $<$ GSM8K $<$ MMLU, demonstrating that vulnerability is governed by task structure rather than prompt strength. CoT causal intervention confirms that 99.3\% of sandbagging is causally driven by verbalized eval-aware reasoning, ruling out shallow instruction-following. These findings demonstrate that adversarially optimized prompts pose a substantially greater threat to evaluation reliability than previously understood.

