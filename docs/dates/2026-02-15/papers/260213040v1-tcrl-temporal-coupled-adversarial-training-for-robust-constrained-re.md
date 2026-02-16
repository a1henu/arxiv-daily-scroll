---
layout: default
title: TCRL: Temporal-Coupled Adversarial Training for Robust Constrained Reinforcement Learning in Worst-Case Scenarios
---

# TCRL: Temporal-Coupled Adversarial Training for Robust Constrained Reinforcement Learning in Worst-Case Scenarios
**arXiv**：[2602.13040v1](https://arxiv.org/abs/2602.13040) · [PDF](https://arxiv.org/pdf/2602.13040.pdf)  
**作者**：Wentao Xu, Zhongming Yao, Weihao Li, Zhenghang Song, Yumeng Song, Tianyi Li, Yushuai Li  

**一句话要点**：提出TCRL框架以解决约束强化学习在时序耦合扰动下的鲁棒性问题

**关键词**：约束强化学习, 时序耦合扰动, 对抗训练, 鲁棒性, 最坏情况场景

## 3 点简述
- 现有鲁棒约束强化学习方法多关注单步扰动，缺乏对时序耦合扰动的显式建模
- TCRL引入最坏情况感知成本约束函数和双重约束防御机制，无需显式建模对抗攻击
- 实验表明TCRL在多种任务中优于现有方法，提升了对时序耦合攻击的鲁棒性

## 摘要（原文）

> Constrained Reinforcement Learning (CRL) aims to optimize decision-making policies under constraint conditions, making it highly applicable to safety-critical domains such as autonomous driving, robotics, and power grid management. However, existing robust CRL approaches predominantly focus on single-step perturbations and temporally independent adversarial models, lacking explicit modeling of robustness against temporally coupled perturbations. To tackle these challenges, we propose TCRL, a novel temporal-coupled adversarial training framework for robust constrained reinforcement learning (TCRL) in worst-case scenarios. First, TCRL introduces a worst-case-perceived cost constraint function that estimates safety costs under temporally coupled perturbations without the need to explicitly model adversarial attackers. Second, TCRL establishes a dual-constraint defense mechanism on the reward to counter temporally coupled adversaries while maintaining reward unpredictability. Experimental results demonstrate that TCRL consistently outperforms existing methods in terms of robustness against temporally coupled perturbation attacks across a variety of CRL tasks.

