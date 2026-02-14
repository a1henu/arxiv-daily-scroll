---
layout: default
title: InjectRBP: Steering Large Language Model Reasoning Behavior via Pattern Injection
---

# InjectRBP: Steering Large Language Model Reasoning Behavior via Pattern Injection
**arXiv**：[2602.12013v1](https://arxiv.org/abs/2602.12013) · [PDF](https://arxiv.org/pdf/2602.12013.pdf)  
**作者**：Xiuping Wu, Zhao Yu, Yuxin Cheng, Ngai Wong, Liangjun Ke, Tapas Mishra, Konstantinos V. Katsikopoulos  

**一句话要点**：提出InjectRBP方法，通过模式注入引导大语言模型推理行为，无需参数更新提升性能。

**关键词**：大语言模型推理, 行为模式分析, 模式注入, 无参数优化, 推理引导

## 3 点简述
- 核心问题：现有提示调整方法缺乏对推理行为模式的系统分析，影响大语言模型推理效果。
- 方法要点：基于行为模式分析，提出InjectCorrect和InjectRLOpt两种优化方法，通过注入模式引导推理过程。
- 实验或效果：在多种推理任务中，两种方法分别提升性能达5.34%和8.67%，无需修改模型参数。

## 摘要（原文）

> Reasoning can significantly enhance the performance of Large Language Models. While recent studies have exploited behavior-related prompts adjustment to enhance reasoning, these designs remain largely intuitive and lack a systematic analysis of the underlying behavioral patterns. Motivated by this, we investigate how models' reasoning behaviors shape reasoning from the perspective of behavioral patterns. We observe that models exhibit adaptive distributions of reasoning behaviors when responding to specific types of questions, and that structurally injecting these patterns can substantially influence the quality of the models' reasoning processes and outcomes. Building on these findings, we propose two optimization methods that require no parameter updates: InjectCorrect and InjectRLOpt. InjectCorrect guides the model by imitating behavioral patterns derived from its own past correct answers. InjectRLOpt learns a value function from historical behavior-pattern data and, via our proposed Reliability-Aware Softmax Policy, generates behavioral injectant during inference to steer the reasoning process. Our experiments demonstrate that both methods can improve model performance across various reasoning tasks without requiring any modifications to model parameters, achieving gains of up to 5.34% and 8.67%, respectively.

