---
layout: default
title: Enhancing TableQA through Verifiable Reasoning Trace Reward
---

# Enhancing TableQA through Verifiable Reasoning Trace Reward
**arXiv**：[2601.22530v1](https://arxiv.org/abs/2601.22530) · [PDF](https://arxiv.org/pdf/2601.22530.pdf)  
**作者**：Tung Sum Thomas Kwok, Xinyu Wang, Hengzhi He, Xiaofeng Lin, Peng Lu, Liheng Ma, Chunhe Wang, Ying Nian Wu, Lei Ding, Guang Cheng  

**一句话要点**：提出RE-Tab框架，通过可验证推理轨迹奖励增强表格问答的推理能力

**关键词**：表格问答, 推理轨迹奖励, 部分可观测马尔可夫决策过程, 轻量级奖励模型, 状态转换优化, 模拟推理验证

## 3 点简述
- 核心问题：表格问答需多步推理和状态转换，静态输入无法直接推断答案
- 方法要点：基于部分可观测马尔可夫决策过程，设计轻量级免训练奖励模型，提供状态转换和模拟推理的显式反馈
- 实验或效果：在TableQA中实现最先进性能，推理成本降低约25%，问答准确率提升最高达41.77%

## 摘要（原文）

> A major challenge in training TableQA agents, compared to standard text- and image-based agents, is that answers cannot be inferred from a static input but must be reasoned through stepwise transformations of the table state, introducing multi-step reasoning complexity and environmental interaction. This leads to a research question: Can explicit feedback on table transformation action improve model reasoning capability? In this work, we introduce RE-Tab, a plug-and-play framework that architecturally enhances trajectory search via lightweight, training-free reward modeling by formulating the problem as a Partially Observable Markov Decision Process. We demonstrate that providing explicit verifiable rewards during State Transition (``What is the best action?'') and Simulative Reasoning (``Am I sure about the output?'') is crucial to steer the agent's navigation in table states. By enforcing stepwise reasoning with reward feedback in table transformations, RE-Tab achieves state-of-the-art performance in TableQA with almost 25\% drop in inference cost. Furthermore, a direct plug-and-play implementation of RE-Tab brings up to 41.77% improvement in QA accuracy and 33.33% drop in test-time inference samples for consistent answer. Consistent improvement pattern across various LLMs and state-of-the-art benchmarks further confirms RE-Tab's generalisability. The repository is available at https://github.com/ThomasK1018/RE_Tab .

