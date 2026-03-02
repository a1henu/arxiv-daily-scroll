---
layout: default
title: RewardUQ: A Unified Framework for Uncertainty-Aware Reward Models
---

# RewardUQ: A Unified Framework for Uncertainty-Aware Reward Models
**arXiv**：[2602.24040v1](https://arxiv.org/abs/2602.24040) · [PDF](https://arxiv.org/pdf/2602.24040.pdf)  
**作者**：Daniel Yang, Samuel Stante, Florian Redhardt, Lena Libon, Parnian Kassraie, Ido Hakimi, Barna Pásztor, Andreas Krause  

**一句话要点**：提出RewardUQ框架以系统评估奖励模型的不确定性量化

**关键词**：奖励模型, 不确定性量化, 大语言模型对齐, 主动学习, 开源框架

## 3 点简述
- 核心问题：奖励模型依赖点估计，忽略有限人类反馈导致的认知不确定性。
- 方法要点：统一框架比较常见方法，提出结合准确性和校准度的新排名策略。
- 实验或效果：模型大小和初始化对性能影响最大，开源框架促进方法开发与部署。

## 摘要（原文）

> Reward models are central to aligning large language models (LLMs) with human preferences. Yet most approaches rely on pointwise reward estimates that overlook the epistemic uncertainty in reward models arising from limited human feedback. Recent work suggests that quantifying this uncertainty can reduce the costs of human annotation via uncertainty-guided active learning and mitigate reward overoptimization in LLM post-training. However, uncertainty-aware reward models have so far been adopted without thorough comparison, leaving them poorly understood. This work introduces a unified framework, RewardUQ, to systematically evaluate uncertainty quantification for reward models. We compare common methods along standard metrics measuring accuracy and calibration, and we propose a new ranking strategy incorporating both dimensions for a simplified comparison. Our experimental results suggest that model size and initialization have the most meaningful impact on performance, and most prior work could have benefited from alternative design choices. To foster the development and evaluation of new methods and aid the deployment in downstream applications, we release our open-source framework as a Python package. Our code is available at https://github.com/lasgroup/rewarduq.

