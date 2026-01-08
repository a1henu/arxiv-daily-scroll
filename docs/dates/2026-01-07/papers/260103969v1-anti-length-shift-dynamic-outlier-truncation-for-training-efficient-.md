---
layout: default
title: Anti-Length Shift: Dynamic Outlier Truncation for Training Efficient Reasoning Models
---

# Anti-Length Shift: Dynamic Outlier Truncation for Training Efficient Reasoning Models
**arXiv**：[2601.03969v1](https://arxiv.org/abs/2601.03969) · [PDF](https://arxiv.org/pdf/2601.03969.pdf)  
**作者**：Wei Wu, Liyi Chen, Congxi Xiao, Tianfu Wang, Qimeng Wang, Chengqiang Lu, Yan Gao, Yi Wu, Yao Hu, Hui Xiong  

**一句话要点**：提出动态异常截断以解决推理模型在训练中过度冗长的问题

**关键词**：推理模型, 动态截断, 强化学习, 效率优化, 训练干预

## 3 点简述
- 核心问题：强化学习增强的推理模型在简单查询上产生不必要冗长，导致部署成本高
- 方法要点：引入动态异常截断，选择性抑制训练中正确但过长的响应尾部冗余令牌
- 实验或效果：在AIME-24上减少78%推理令牌使用，同时提升准确率，超越现有高效推理方法

## 摘要（原文）

> Large reasoning models enhanced by reinforcement learning with verifiable rewards have achieved significant performance gains by extending their chain-of-thought. However, this paradigm incurs substantial deployment costs as models often exhibit excessive verbosity on simple queries. Existing efficient reasoning methods relying on explicit length penalties often introduce optimization conflicts and leave the generative mechanisms driving overthinking largely unexamined. In this paper, we identify a phenomenon termed length shift where models increasingly generate unnecessary reasoning on trivial inputs during training. To address this, we introduce Dynamic Outlier Truncation (DOT), a training-time intervention that selectively suppresses redundant tokens. This method targets only the extreme tail of response lengths within fully correct rollout groups while preserving long-horizon reasoning capabilities for complex problems. To complement this intervention and ensure stable convergence, we further incorporate auxiliary KL regularization and predictive dynamic sampling. Experimental results across multiple model scales demonstrate that our approach significantly pushes the efficiency-performance Pareto frontier outward. Notably, on the AIME-24, our method reduces inference token usage by 78% while simultaneously increasing accuracy compared to the initial policy and surpassing state-of-the-art efficient reasoning methods.

