---
layout: default
title: TriPlay-RL: Tri-Role Self-Play Reinforcement Learning for LLM Safety Alignment
---

# TriPlay-RL: Tri-Role Self-Play Reinforcement Learning for LLM Safety Alignment
**arXiv**：[2601.18292v1](https://arxiv.org/abs/2601.18292) · [PDF](https://arxiv.org/pdf/2601.18292.pdf)  
**作者**：Zhewen Tan, Wenhan Yu, Jianfeng Si, Tongxin Liu, Kaiqi Guan, Huiyan Jin, Jiawen Tao, Xiaokun Yuan, Duohe Ma, Xiangzheng Zhang, Tong Yang, Lin Sun  

**一句话要点**：提出TriPlay-RL框架，通过三角色自博弈强化学习实现大语言模型安全对齐

**关键词**：大语言模型安全对齐, 三角色自博弈, 强化学习框架, 协同进化, 对抗攻击防御

## 3 点简述
- 核心问题：大语言模型生成有害内容的风险突出，需高效安全对齐方法。
- 方法要点：采用攻击者、防御者、评估者三角色闭环强化学习，实现协同进化。
- 实验效果：攻击者对抗效果提升20%-50%，防御者安全性能增益10%-30%，评估者判断能力持续优化。

## 摘要（原文）

> In recent years, safety risks associated with large language models have become increasingly prominent, highlighting the urgent need to mitigate the generation of toxic and harmful content. The mainstream paradigm for LLM safety alignment typically adopts a collaborative framework involving three roles: an attacker for adversarial prompt generation, a defender for safety defense, and an evaluator for response assessment. In this paper, we propose a closed-loop reinforcement learning framework called TriPlay-RL that enables iterative and co-improving collaboration among three roles with near-zero manual annotation. Experimental results show that the attacker preserves high output diversity while achieving a 20%-50% improvement in adversarial effectiveness; the defender attains 10%-30% gains in safety performance without degrading general reasoning capability; and the evaluator continuously refines its fine-grained judgment ability through iterations, accurately distinguishing unsafe responses, simple refusals, and useful guidance. Overall, our framework establishes an efficient and scalable paradigm for LLM safety alignment, enabling continuous co-evolution within a unified learning loop.

