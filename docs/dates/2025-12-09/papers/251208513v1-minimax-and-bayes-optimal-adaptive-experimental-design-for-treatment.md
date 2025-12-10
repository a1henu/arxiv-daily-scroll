---
layout: default
title: Minimax and Bayes Optimal Adaptive Experimental Design for Treatment Choice
---

# Minimax and Bayes Optimal Adaptive Experimental Design for Treatment Choice
**arXiv**：[2512.08513v1](https://arxiv.org/abs/2512.08513) · [PDF](https://arxiv.org/pdf/2512.08513.pdf)  
**作者**：Masahiro Kato  

**一句话要点**：提出两阶段自适应实验设计，实现治疗选择的最小最大和贝叶斯最优后悔

**关键词**：自适应实验设计, 治疗选择, 最小最大后悔, 贝叶斯最优, Neyman分配, 后悔分析

## 3 点简述
- 核心问题：在二元治疗自适应实验中，如何设计实验以最小化后悔并最大化福利。
- 方法要点：将治疗分配阶段分为两阶段，先估计标准差，再按标准差比例分配治疗。
- 实验或效果：证明该设计（Neyman分配）的后悔上界与推导的下界匹配，达到最优性。

## 摘要（原文）

> We consider an adaptive experiment for treatment choice and design a minimax and Bayes optimal adaptive experiment with respect to regret. Given binary treatments, the experimenter's goal is to choose the treatment with the highest expected outcome through an adaptive experiment, in order to maximize welfare. We consider adaptive experiments that consist of two phases, the treatment allocation phase and the treatment choice phase. The experiment starts with the treatment allocation phase, where the experimenter allocates treatments to experimental subjects to gather observations. During this phase, the experimenter can adaptively update the allocation probabilities using the observations obtained in the experiment. After the allocation phase, the experimenter proceeds to the treatment choice phase, where one of the treatments is selected as the best. For this adaptive experimental procedure, we propose an adaptive experiment that splits the treatment allocation phase into two stages, where we first estimate the standard deviations and then allocate each treatment proportionally to its standard deviation. We show that this experiment, often referred to as Neyman allocation, is minimax and Bayes optimal in the sense that its regret upper bounds exactly match the lower bounds that we derive. To show this optimality, we derive minimax and Bayes lower bounds for the regret using change-of-measure arguments. Then, we evaluate the corresponding upper bounds using the central limit theorem and large deviation bounds.

