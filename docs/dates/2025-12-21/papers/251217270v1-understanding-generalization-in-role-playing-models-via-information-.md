---
layout: default
title: Understanding Generalization in Role-Playing Models via Information Theory
---

# Understanding Generalization in Role-Playing Models via Information Theory
**arXiv**：[2512.17270v1](https://arxiv.org/abs/2512.17270) · [PDF](https://arxiv.org/pdf/2512.17270.pdf)  
**作者**：Yongqi Li, Hao Lang, Fei Huang, Tieyun Qian, Yongbin Li  

**一句话要点**：提出信息论度量R-EMID以诊断角色扮演模型在分布偏移下的泛化性能下降

**关键词**：角色扮演模型, 泛化性能, 信息论度量, 分布偏移, 强化学习, 对话生成

## 3 点简述
- 角色扮演模型在真实部署中因用户、角色和对话组合偏移导致性能下降，现有方法缺乏细粒度诊断框架
- 引入基于推理的有效互信息差R-EMID作为可解释度量，并推导其上界以预测最坏情况泛化性能
- 提出协同进化强化学习框架增强对话响应概率估计，实验显示用户偏移风险最高且强化学习提升泛化最有效

## 摘要（原文）

> Role-playing models (RPMs) are widely used in real-world applications but underperform when deployed in the wild. This degradation can be attributed to distribution shifts, including user, character, and dialogue compositional shifts. Existing methods like LLM-as-a-judge fall short in providing a fine-grained diagnosis of how these shifts affect RPM generalization, and thus there lack formal frameworks to characterize RPM generalization behaviors. To bridge these gaps, we introduce an information-theoretic metric, named reasoning-based effective mutual information difference (R-EMID), to measure RPM performance degradation in an interpretable way. We also derive an upper bound on R-EMID to predict the worst-case generalization performance of RPMs and theoretically reveal how various shifts contribute to the RPM performance degradation. Moreover, we propose a co-evolving reinforcement learning framework to adaptively model the connection among user, character, and dialogue context and thus enhance the estimation of dialogue response generation probability, which is critical for calculating R-EMID. Finally, we evaluate the generalization performance of various RPMs using R-EMID, finding that user shift poses the highest risk among all shifts and reinforcement learning is the most effective approach for enhancing RPM generalization.

