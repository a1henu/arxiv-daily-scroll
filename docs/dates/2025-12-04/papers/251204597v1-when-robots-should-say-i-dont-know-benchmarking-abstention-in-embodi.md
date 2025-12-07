---
layout: default
title: When Robots Should Say "I Don't Know": Benchmarking Abstention in Embodied Question Answering
---

# When Robots Should Say "I Don't Know": Benchmarking Abstention in Embodied Question Answering
**arXiv**：[2512.04597v1](https://arxiv.org/abs/2512.04597) · [PDF](https://arxiv.org/pdf/2512.04597.pdf)  
**作者**：Tao Wu, Chuhao Zhou, Guangyu Zhao, Haozhi Cao, Yewen Pu, Jianfei Yang  

**一句话要点**：提出AbstainEQA基准以评估具身问答中机器人何时应说“不知道”的拒绝能力

**关键词**：具身问答, 拒绝能力, 基准评估, 数据集构建, 人机交互, 认知理论

## 3 点简述
- 核心问题：现有具身问答基准假设所有问题必须回答，但机器人需知道何时信息不足而拒绝回答
- 方法要点：基于人类查询分析和认知理论，定义五类拒绝场景，并构建包含1636个案例的AbstainEQA数据集
- 实验或效果：评估显示前沿模型拒绝召回率仅42.79%，远低于人类的91.17%，且缩放、提示和推理改进有限

## 摘要（原文）

> Embodied Question Answering (EQA) requires an agent to interpret language, perceive its environment, and navigate within 3D scenes to produce responses. Existing EQA benchmarks assume that every question must be answered, but embodied agents should know when they do not have sufficient information to answer. In this work, we focus on a minimal requirement for EQA agents, abstention: knowing when to withhold an answer. From an initial study of 500 human queries, we find that 32.4% contain missing or underspecified context. Drawing on this initial study and cognitive theories of human communication errors, we derive five representative categories requiring abstention: actionability limitation, referential underspecification, preference dependence, information unavailability, and false presupposition. We augment OpenEQA by having annotators transform well-posed questions into ambiguous variants outlined by these categories. The resulting dataset, AbstainEQA, comprises 1,636 annotated abstention cases paired with 1,636 original OpenEQA instances for balanced evaluation. Evaluating on AbstainEQA, we find that even the best frontier model only attains 42.79% abstention recall, while humans achieve 91.17%. We also find that scaling, prompting, and reasoning only yield marginal gains, and that fine-tuned models overfit to textual cues. Together, these results position abstention as a fundamental prerequisite for reliable interaction in embodied settings and as a necessary basis for effective clarification.

