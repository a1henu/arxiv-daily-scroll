---
layout: default
title: A Comedy of Estimators: On KL Regularization in RL Training of LLMs
---

# A Comedy of Estimators: On KL Regularization in RL Training of LLMs
**arXiv**：[2512.21852v1](https://arxiv.org/abs/2512.21852) · [PDF](https://arxiv.org/pdf/2512.21852.pdf)  
**作者**：Vedant Shah, Johan Obando-Ceron, Vineet Jain, Brian Bartoldson, Bhavya Kailkhura, Sarthak Mittal, Glen Berseth, Pablo Samuel Castro, Yoshua Bengio, Nikolay Malkin, Moksh Jain, Siddarth Venkatraman, Aaron Courville  

**一句话要点**：分析KL正则化在LLM强化学习训练中的梯度偏差问题，提出无偏估计器配置以提升性能与稳定性

**关键词**：强化学习, 大语言模型, KL正则化, 梯度偏差, 估计器配置, 训练稳定性

## 3 点简述
- 核心问题：KL正则化在LLM强化学习训练中，现有估计器配置导致梯度偏差，影响目标实现与模型性能
- 方法要点：系统研究多种KL估计器配置的梯度特性，揭示设计选择如何引入偏差，并识别无偏配置
- 实验或效果：通过RL微调多个LLM模型，验证无偏估计器配置能提升域内和域外任务性能，并稳定离策略训练

## 摘要（原文）

> The reasoning performance of large language models (LLMs) can be substantially improved by training them with reinforcement learning (RL). The RL objective for LLM training involves a regularization term, which is the reverse Kullback-Leibler (KL) divergence between the trained policy and the reference policy. Since computing the KL divergence exactly is intractable, various estimators are used in practice to estimate it from on-policy samples. Despite its wide adoption, including in several open-source libraries, there is no systematic study analyzing the numerous ways of incorporating KL estimators in the objective and their effect on the downstream performance of RL-trained models. Recent works show that prevailing practices for incorporating KL regularization do not provide correct gradients for stated objectives, creating a discrepancy between the objective and its implementation. In this paper, we further analyze these practices and study the gradients of several estimators configurations, revealing how design choices shape gradient bias. We substantiate these findings with empirical observations by RL fine-tuning \texttt{Qwen2.5-7B}, \texttt{Llama-3.1-8B-Instruct} and \texttt{Qwen3-4B-Instruct-2507} with different configurations and evaluating their performance on both in- and out-of-distribution tasks. Through our analysis, we observe that, in on-policy settings: (1) estimator configurations with biased gradients can result in training instabilities; and (2) using estimator configurations resulting in unbiased gradients leads to better performance on in-domain as well as out-of-domain tasks. We also investigate the performance resulting from different KL configurations in off-policy settings and observe that KL regularization can help stabilize off-policy RL training resulting from asynchronous setups.

