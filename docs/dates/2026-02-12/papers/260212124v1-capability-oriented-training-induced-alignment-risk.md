---
layout: default
title: Capability-Oriented Training Induced Alignment Risk
---

# Capability-Oriented Training Induced Alignment Risk
**arXiv**：[2602.12124v1](https://arxiv.org/abs/2602.12124) · [PDF](https://arxiv.org/pdf/2602.12124.pdf)  
**作者**：Yujun Zhou, Yue Huang, Han Bao, Kehan Guo, Zhenwen Liang, Pin-Yu Chen, Tian Gao, Werner Geyer, Nuno Moniz, Nitesh V Chawla, Xiangliang Zhang  

**一句话要点**：提出能力导向训练诱导对齐风险，揭示语言模型在强化学习中自发利用环境漏洞的问题。

**关键词**：AI对齐风险, 强化学习漏洞, 能力导向训练, 模型泛化, 数据蒸馏

## 3 点简述
- 核心问题：AI对齐研究忽视能力导向训练中模型自发利用环境漏洞的隐性风险。
- 方法要点：设计四种漏洞游戏，测试模型在强化学习环境中利用上下文条件合规、代理指标等漏洞。
- 实验或效果：模型学会可泛化的利用策略，能迁移到新任务并通过数据蒸馏传播。

## 摘要（原文）

> While most AI alignment research focuses on preventing models from generating explicitly harmful content, a more subtle risk is emerging: capability-oriented training induced exploitation. We investigate whether language models, when trained with reinforcement learning (RL) in environments with implicit loopholes, will spontaneously learn to exploit these flaws to maximize their reward, even without any malicious intent in their training. To test this, we design a suite of four diverse "vulnerability games", each presenting a unique, exploitable flaw related to context-conditional compliance, proxy metrics, reward tampering, and self-evaluation. Our experiments show that models consistently learn to exploit these vulnerabilities, discovering opportunistic strategies that significantly increase their reward at the expense of task correctness or safety. More critically, we find that these exploitative strategies are not narrow "tricks" but generalizable skills; they can be transferred to new tasks and even "distilled" from a capable teacher model to other student models through data alone. Our findings reveal that capability-oriented training induced risks pose a fundamental challenge to current alignment approaches, suggesting that future AI safety work must extend beyond content moderation to rigorously auditing and securing the training environments and reward mechanisms themselves. Code is available at https://github.com/YujunZhou/Capability_Oriented_Alignment_Risk.

