---
layout: default
title: MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety
---

# MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety
**arXiv**：[2602.01539v1](https://arxiv.org/abs/2602.01539) · [PDF](https://arxiv.org/pdf/2602.01539.pdf)  
**作者**：Xiaoyu Wen, Zhida He, Han Qi, Ziyu Wan, Zhongtian Ma, Ying Wen, Tianhang Zheng, Xingcheng Xu, Chaochao Lu, Qiaosheng Zhang  

**一句话要点**：提出MAGIC框架，通过多智能体强化学习实现攻击者与防御者协同进化，以增强大语言模型的安全对齐鲁棒性。

**关键词**：大语言模型安全对齐, 对抗性游戏, 多智能体强化学习, 协同进化, 鲁棒性防御

## 3 点简述
- 核心问题：现有防御依赖静态数据分布，难以应对不断演化的对抗攻击，导致安全对齐鲁棒性不足。
- 方法要点：采用多轮多智能体强化学习，将安全对齐建模为非对称对抗游戏，攻击者迭代生成欺骗性提示，防御者优化策略识别并拒绝输入。
- 实验或效果：实验验证框架有效性，在保持模型帮助性的同时，实现更高的防御成功率，攻击者能演化出未见组合策略。

## 摘要（原文）

> Ensuring robust safety alignment is crucial for Large Language Models (LLMs), yet existing defenses often lag behind evolving adversarial attacks due to their \textbf{reliance on static, pre-collected data distributions}. In this paper, we introduce \textbf{MAGIC}, a novel multi-turn multi-agent reinforcement learning framework that formulates LLM safety alignment as an adversarial asymmetric game. Specifically, an attacker agent learns to iteratively rewrite original queries into deceptive prompts, while a defender agent simultaneously optimizes its policy to recognize and refuse such inputs. This dynamic process triggers a \textbf{co-evolution}, where the attacker's ever-changing strategies continuously uncover long-tail vulnerabilities, driving the defender to generalize to unseen attack patterns. Remarkably, we observe that the attacker, endowed with initial reasoning ability, evolves \textbf{novel, previously unseen combinatorial strategies} through iterative RL training, underscoring our method's substantial potential. Theoretically, we provide insights into a more robust game equilibrium and derive safety guarantees. Extensive experiments validate our framework's effectiveness, demonstrating superior defense success rates without compromising the helpfulness of the model. Our code is available at https://github.com/BattleWen/MAGIC.

