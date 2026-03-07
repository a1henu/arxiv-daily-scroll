---
layout: default
title: Knowledge-informed Bidding with Dual-process Control for Online Advertising
---

# Knowledge-informed Bidding with Dual-process Control for Online Advertising
**arXiv**：[2603.04920v1](https://arxiv.org/abs/2603.04920) · [PDF](https://arxiv.org/pdf/2603.04920.pdf)  
**作者**：Huixiang Luo, Longyu Gao, Yaqi Liu, Qianqian Chen, Pingchun Huang, Tianning Li  

**一句话要点**：提出KBD方法，结合人类专家知识与双过程控制优化在线广告出价决策

**关键词**：在线广告出价优化, 知情机器学习, 决策变换器, 双过程控制, PID控制, 人类专家知识

## 3 点简述
- 核心问题：现有黑盒模型在数据稀疏、长期依赖和分布外场景下泛化能力差，无法模拟人类专家的自适应决策
- 方法要点：通过知情机器学习嵌入人类知识，使用决策变换器全局优化多步出价序列，结合基于规则的PID和DT实现双过程控制
- 实验或效果：广泛实验显示KBD优于现有方法，验证了人类专家知识和双过程控制对出价优化的益处

## 摘要（原文）

> Bid optimization in online advertising relies on black-box machine-learning models that learn bidding decisions from historical data. However, these approaches fail to replicate human experts' adaptive, experience-driven, and globally coherent decisions. Specifically, they generalize poorly in data-sparse cases because of missing structured knowledge, make short-sighted sequential decisions that ignore long-term interdependencies, and struggle to adapt in out-of-distribution scenarios where human experts succeed. To address this, we propose KBD (Knowledge-informed Bidding with Dual-process control), a novel method for bid optimization. KBD embeds human expertise as inductive biases through the informed machine-learning paradigm, uses Decision Transformer (DT) to globally optimize multi-step bidding sequences, and implements dual-process control by combining a fast rule-based PID (System 1) with DT (System 2). Extensive experiments highlight KBD's advantage over existing methods and underscore the benefit of grounding bid optimization in human expertise and dual-process control.

