---
layout: default
title: UCPO: Uncertainty-Aware Policy Optimization
---

# UCPO: Uncertainty-Aware Policy Optimization
**arXiv**：[2601.22648v1](https://arxiv.org/abs/2601.22648) · [PDF](https://arxiv.org/pdf/2601.22648.pdf)  
**作者**：Xianzhou Zeng, Jing Huang, Chunmei Xie, Gongrui Nan, Siye Chen, Mengyu Lu, Weiqi Xiong, Qixuan Zhou, Junhao Zhang, Qiang Zhu, Yadong Li, Xingzhong Xu  

**一句话要点**：提出UCPO框架以解决大语言模型强化学习中优势偏差和不确定性奖励失衡问题

**关键词**：不确定性感知, 强化学习, 大语言模型, 优势偏差, 奖励校准, 模型可靠性

## 3 点简述
- 核心问题：现有RL范式如GRPO因二元决策空间和静态不确定性奖励导致优势偏差，引发过度保守或自信
- 方法要点：采用三元优势解耦分离并独立归一化确定性和不确定性rollout，消除偏差；引入动态不确定性奖励调整机制实时校准权重
- 实验或效果：在数学推理和通用任务中验证UCPO有效解决奖励失衡，显著提升模型可靠性和校准能力

## 摘要（原文）

> The key to building trustworthy Large Language Models (LLMs) lies in endowing them with inherent uncertainty expression capabilities to mitigate the hallucinations that restrict their high-stakes applications. However, existing RL paradigms such as GRPO often suffer from Advantage Bias due to binary decision spaces and static uncertainty rewards, inducing either excessive conservatism or overconfidence. To tackle this challenge, this paper unveils the root causes of reward hacking and overconfidence in current RL paradigms incorporating uncertainty-based rewards, based on which we propose the UnCertainty-Aware Policy Optimization (UCPO) framework. UCPO employs Ternary Advantage Decoupling to separate and independently normalize deterministic and uncertain rollouts, thereby eliminating advantage bias. Furthermore, a Dynamic Uncertainty Reward Adjustment mechanism is introduced to calibrate uncertainty weights in real-time according to model evolution and instance difficulty. Experimental results in mathematical reasoning and general tasks demonstrate that UCPO effectively resolves the reward imbalance, significantly improving the reliability and calibration of the model beyond their knowledge boundaries.

