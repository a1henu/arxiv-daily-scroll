---
layout: default
title: FlyPrompt: Brain-Inspired Random-Expanded Routing with Temporal-Ensemble Experts for General Continual Learning
---

# FlyPrompt: Brain-Inspired Random-Expanded Routing with Temporal-Ensemble Experts for General Continual Learning
**arXiv**：[2602.01976v1](https://arxiv.org/abs/2602.01976) · [PDF](https://arxiv.org/pdf/2602.01976.pdf)  
**作者**：Hongwei Yan, Guanglong Sun, Kanglei Zhou, Qian Li, Liyuan Wang, Yi Zhong  

**一句话要点**：提出FlyPrompt框架，通过随机扩展路由与时间集成专家解决通用持续学习中的参数高效调优问题。

**关键词**：通用持续学习, 参数高效调优, 专家路由, 时间集成, 脑启发计算, 非平稳数据流

## 3 点简述
- 核心问题：通用持续学习需处理单次通过、非平稳数据流，现有方法依赖多轮训练和明确任务边界，限制实际应用。
- 方法要点：受果蝇记忆系统启发，设计随机扩展分析路由进行实例级专家激活，并采用时间集成输出头动态调整决策边界。
- 实验或效果：在CIFAR-100、ImageNet-R和CUB-200数据集上，性能提升分别达11.23%、12.43%和7.62%，优于现有基线。

## 摘要（原文）

> General continual learning (GCL) challenges intelligent systems to learn from single-pass, non-stationary data streams without clear task boundaries. While recent advances in continual parameter-efficient tuning (PET) of pretrained models show promise, they typically rely on multiple training epochs and explicit task cues, limiting their effectiveness in GCL scenarios. Moreover, existing methods often lack targeted design and fail to address two fundamental challenges in continual PET: how to allocate expert parameters to evolving data distributions, and how to improve their representational capacity under limited supervision. Inspired by the fruit fly's hierarchical memory system characterized by sparse expansion and modular ensembles, we propose FlyPrompt, a brain-inspired framework that decomposes GCL into two subproblems: expert routing and expert competence improvement. FlyPrompt introduces a randomly expanded analytic router for instance-level expert activation and a temporal ensemble of output heads to dynamically adapt decision boundaries over time. Extensive theoretical and empirical evaluations demonstrate FlyPrompt's superior performance, achieving up to 11.23%, 12.43%, and 7.62% gains over state-of-the-art baselines on CIFAR-100, ImageNet-R, and CUB-200, respectively. Our source code is available at https://github.com/AnAppleCore/FlyGCL.

