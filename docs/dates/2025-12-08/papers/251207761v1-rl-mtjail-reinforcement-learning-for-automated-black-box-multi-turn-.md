---
layout: default
title: RL-MTJail: Reinforcement Learning for Automated Black-Box Multi-Turn Jailbreaking of Large Language Models
---

# RL-MTJail: Reinforcement Learning for Automated Black-Box Multi-Turn Jailbreaking of Large Language Models
**arXiv**：[2512.07761v1](https://arxiv.org/abs/2512.07761) · [PDF](https://arxiv.org/pdf/2512.07761.pdf)  
**作者**：Xiqiao Xiong, Ouxiang Li, Zhuo Liu, Moxin Li, Wentao Shi, Fuli Feng, Xiangnan He  

**一句话要点**：提出基于强化学习的多轮黑盒越狱方法，以优化长期攻击策略提升攻击成功率。

**关键词**：黑盒越狱攻击, 多轮强化学习, 启发式奖励, 攻击成功率, 大语言模型安全

## 3 点简述
- 研究黑盒多轮越狱攻击，通过序列交互训练攻击者LLMs以诱导有害内容。
- 将问题建模为多轮强化学习任务，引入启发式过程奖励以缓解稀疏监督并促进长期策略。
- 在多个基准测试中实验，显示攻击成功率一致提升，验证方法有效性。

## 摘要（原文）

> Large language models are vulnerable to jailbreak attacks, threatening their safe deployment in real-world applications. This paper studies black-box multi-turn jailbreaks, aiming to train attacker LLMs to elicit harmful content from black-box models through a sequence of prompt-output interactions. Existing approaches typically rely on single turn optimization, which is insufficient for learning long-term attack strategies. To bridge this gap, we formulate the problem as a multi-turn reinforcement learning task, directly optimizing the harmfulness of the final-turn output as the outcome reward. To mitigate sparse supervision and promote long-term attack strategies, we propose two heuristic process rewards: (1) controlling the harmfulness of intermediate outputs to prevent triggering the black-box model's rejection mechanisms, and (2) maintaining the semantic relevance of intermediate outputs to avoid drifting into irrelevant content. Experimental results on multiple benchmarks show consistently improved attack success rates across multiple models, highlighting the effectiveness of our approach. The code is available at https://github.com/xxiqiao/RL-MTJail. Warning: This paper contains examples of harmful content.

