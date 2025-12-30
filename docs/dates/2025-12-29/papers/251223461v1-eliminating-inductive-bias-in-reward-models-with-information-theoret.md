---
layout: default
title: Eliminating Inductive Bias in Reward Models with Information-Theoretic Guidance
---

# Eliminating Inductive Bias in Reward Models with Information-Theoretic Guidance
**arXiv**：[2512.23461v1](https://arxiv.org/abs/2512.23461) · [PDF](https://arxiv.org/pdf/2512.23461.pdf)  
**作者**：Zhuo Li, Pengyu Cheng, Zhechao Yu, Feifei Tong, Anningzhe Gao, Tsung-Hui Chang, Xiang Wan, Erchao Zhao, Xiaoxi Jiang, Guanjun Jiang  

**一句话要点**：提出DIR方法，基于信息论优化消除奖励模型中的归纳偏差，提升RLHF性能。

**关键词**：奖励模型去偏, 信息论优化, 强化学习人类反馈, 归纳偏差缓解, 互信息最小化

## 3 点简述
- 奖励模型训练数据质量低，包含长度、奉承等复杂归纳偏差，易导致过拟合和奖励攻击。
- DIR基于信息瓶颈理论，最大化奖励分数与人类偏好的互信息，最小化与偏差属性的互信息。
- 实验验证DIR能有效缓解多种偏差，增强RLHF在基准测试中的泛化能力。

## 摘要（原文）

> Reward models (RMs) are essential in reinforcement learning from human feedback (RLHF) to align large language models (LLMs) with human values. However, RM training data is commonly recognized as low-quality, containing inductive biases that can easily lead to overfitting and reward hacking. For example, more detailed and comprehensive responses are usually human-preferred but with more words, leading response length to become one of the inevitable inductive biases. A limited number of prior RM debiasing approaches either target a single specific type of bias or model the problem with only simple linear correlations, \textit{e.g.}, Pearson coefficients. To mitigate more complex and diverse inductive biases in reward modeling, we introduce a novel information-theoretic debiasing method called \textbf{D}ebiasing via \textbf{I}nformation optimization for \textbf{R}M (DIR). Inspired by the information bottleneck (IB), we maximize the mutual information (MI) between RM scores and human preference pairs, while minimizing the MI between RM outputs and biased attributes of preference inputs. With theoretical justification from information theory, DIR can handle more sophisticated types of biases with non-linear correlations, broadly extending the real-world application scenarios for RM debiasing methods. In experiments, we verify the effectiveness of DIR with three types of inductive biases: \textit{response length}, \textit{sycophancy}, and \textit{format}. We discover that DIR not only effectively mitigates target inductive biases but also enhances RLHF performance across diverse benchmarks, yielding better generalization abilities. The code and training recipes are available at https://github.com/Qwen-Applications/DIR.

