---
layout: default
title: AdvJudge-Zero: Binary Decision Flips in LLM-as-a-Judge via Adversarial Control Tokens
---

# AdvJudge-Zero: Binary Decision Flips in LLM-as-a-Judge via Adversarial Control Tokens
**arXiv**：[2512.17375v1](https://arxiv.org/abs/2512.17375) · [PDF](https://arxiv.org/pdf/2512.17375.pdf)  
**作者**：Tung-Ling Li, Yuhao Wu, Hongliang Liu  

**一句话要点**：提出AdvJudge-Zero方法，通过对抗控制令牌揭示LLM-as-a-Judge系统的二进制决策翻转漏洞

**关键词**：LLM-as-a-Judge, 对抗攻击, 控制令牌, 奖励模型, 二进制决策, 后训练安全

## 3 点简述
- 核心问题：LLM-as-a-Judge系统在RLHF等后训练中易受低困惑度控制令牌攻击，导致二进制评估从正确'否'翻转为错误'是'
- 方法要点：利用模型的下一个令牌分布和束搜索探索，从头发现多样控制令牌序列，分析隐藏状态扰动集中在低秩'软模式'
- 实验或效果：在数学和推理基准上，控制令牌导致高误报率，基于LoRA的对抗训练可显著减少误报并保持评估质量

## 摘要（原文）

> Reward models and LLM-as-a-Judge systems are central to modern post-training pipelines such as RLHF, DPO, and RLAIF, where they provide scalar feedback and binary decisions that guide model selection and RL-based fine-tuning. We show that these judge systems exhibit a recurring vulnerability: short sequences of low-perplexity control tokens can flip many binary evaluations from correct ``No'' judgments to incorrect ``Yes'' judgments by steering the last-layer logit gap. These control tokens are patterns that a policy model could plausibly generate during post-training, and thus represent realistic reward-hacking risks rather than worst-case adversarial strings. Our method, AdvJudge-Zero, uses the model's next-token distribution and beam-search exploration to discover diverse control-token sequences from scratch, and our analysis shows that the induced hidden-state perturbations concentrate in a low-rank ``soft mode'' that is anti-aligned with the judge's refusal direction. Empirically, these tokens cause very high false positive rates when large open-weight and specialized judge models score incorrect answers on math and reasoning benchmarks. Finally, we show that LoRA-based adversarial training on small sets of control-token-augmented examples can markedly reduce these false positives while preserving evaluation quality.

