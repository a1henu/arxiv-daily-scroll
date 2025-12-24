---
layout: default
title: Sample-Efficient Policy Constraint Offline Deep Reinforcement Learning based on Sample Filtering
---

# Sample-Efficient Policy Constraint Offline Deep Reinforcement Learning based on Sample Filtering
**arXiv**：[2512.20115v1](https://arxiv.org/abs/2512.20115) · [PDF](https://arxiv.org/pdf/2512.20115.pdf)  
**作者**：Yuanhao Chen, Qi Liu, Pengbin Chen, Zhongjian Qiao, Yanjie Li  

**一句话要点**：提出基于样本过滤的策略约束离线强化学习方法以提高样本效率与性能

**关键词**：离线强化学习, 策略约束, 样本过滤, 样本效率, 分布偏移

## 3 点简述
- 核心问题：离线强化学习中策略约束方法依赖数据集质量，低奖励样本导致学习缓慢与性能下降
- 方法要点：通过平均奖励和折扣奖励评估样本得分，筛选高得分样本用于训练
- 实验或效果：在多个离线强化学习算法和基准任务中验证，方法优于基线

## 摘要（原文）

> Offline reinforcement learning (RL) aims to learn a policy that maximizes the expected return using a given static dataset of transitions. However, offline RL faces the distribution shift problem. The policy constraint offline RL method is proposed to solve the distribution shift problem. During the policy constraint offline RL training, it is important to ensure the difference between the learned policy and behavior policy within a given threshold. Thus, the learned policy heavily relies on the quality of the behavior policy. However, a problem exists in existing policy constraint methods: if the dataset contains many low-reward transitions, the learned will be contained with a suboptimal reference policy, leading to slow learning speed, low sample efficiency, and inferior performances. This paper shows that the sampling method in policy constraint offline RL that uses all the transitions in the dataset can be improved. A simple but efficient sample filtering method is proposed to improve the sample efficiency and the final performance. First, we evaluate the score of the transitions by average reward and average discounted reward of episodes in the dataset and extract the transition samples of high scores. Second, the high-score transition samples are used to train the offline RL algorithms. We verify the proposed method in a series of offline RL algorithms and benchmark tasks. Experimental results show that the proposed method outperforms baselines.

