---
layout: default
title: Multimodal Covariance Steering in Belief Space with Active Probing and Influence for Autonomous Driving
---

# Multimodal Covariance Steering in Belief Space with Active Probing and Influence for Autonomous Driving
**arXiv**：[2602.14540v1](https://arxiv.org/abs/2602.14540) · [PDF](https://arxiv.org/pdf/2602.14540.pdf)  
**作者**：Devodita Chakravarty, John Dolan, Yiwei Lyu  

**一句话要点**：提出多模态协方差引导框架，通过主动探测和影响在不确定性下实现自动驾驶安全交互。

**关键词**：自动驾驶不确定性规划, 多模态信念推理, 主动探测策略, 风险感知控制, 分层行为建模, 交互式决策

## 3 点简述
- 核心问题：自动驾驶在复杂交通中需处理不确定性，现有方法孤立处理预测与规划，导致交互不安全或保守。
- 方法要点：构建分层信念模型，结合主动探测策略和基于CVaR的风险评估，以引导人类行为并确保安全。
- 实验或效果：在车道合并和无信号交叉口场景中，相比现有方法，实现更高成功率和更短完成时间。

## 摘要（原文）

> Autonomous driving in complex traffic requires reasoning under uncertainty. Common approaches rely on prediction-based planning or risk-aware control, but these are typically treated in isolation, limiting their ability to capture the coupled nature of action and inference in interactive settings. This gap becomes especially critical in uncertain scenarios, where simply reacting to predictions can lead to unsafe maneuvers or overly conservative behavior. Our central insight is that safe interaction requires not only estimating human behavior but also shaping it when ambiguity poses risks. To this end, we introduce a hierarchical belief model that structures human behavior across coarse discrete intents and fine motion modes, updated via Bayesian inference for interpretable multi-resolution reasoning. On top of this, we develop an active probing strategy that identifies when multimodal ambiguity in human predictions may compromise safety and plans disambiguating actions that both reveal intent and gently steer human decisions toward safer outcomes. Finally, a runtime risk-evaluation layer based on Conditional Value-at-Risk (CVaR) ensures that all probing actions remain within human risk tolerance during influence. Our simulations in lane-merging and unsignaled intersection scenarios demonstrate that our approach achieves higher success rates and shorter completion times compared to existing methods. These results highlight the benefit of coupling belief inference, probing, and risk monitoring, yielding a principled and interpretable framework for planning under uncertainty.

