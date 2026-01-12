---
layout: default
title: CLewR: Curriculum Learning with Restarts for Machine Translation Preference Learning
---

# CLewR: Curriculum Learning with Restarts for Machine Translation Preference Learning
**arXiv**：[2601.05858v1](https://arxiv.org/abs/2601.05858) · [PDF](https://arxiv.org/pdf/2601.05858.pdf)  
**作者**：Alexandra Dragomir, Florin Brad, Radu Tudor Ionescu  

**一句话要点**：提出CLewR课程学习策略，通过重启机制优化机器翻译偏好学习的数据顺序问题。

**关键词**：课程学习, 偏好优化, 机器翻译, 灾难性遗忘, 重启策略, 大语言模型

## 3 点简述
- 核心问题：现有偏好优化方法在训练数据顺序方面研究不足，影响机器翻译性能。
- 方法要点：集成课程学习，引入重启策略，多次重复易到难数据顺序以减轻灾难性遗忘。
- 实验或效果：在多个模型和偏好优化技术上验证，实现一致性能提升，代码已开源。

## 摘要（原文）

> Large language models (LLMs) have demonstrated competitive performance in zero-shot multilingual machine translation (MT). Some follow-up works further improved MT performance via preference optimization, but they leave a key aspect largely underexplored: the order in which data samples are given during training. We address this topic by integrating curriculum learning into various state-of-the-art preference optimization algorithms to boost MT performance. We introduce a novel curriculum learning strategy with restarts (CLewR), which reiterates easy-to-hard curriculum multiple times during training to effectively mitigate the catastrophic forgetting of easy examples. We demonstrate consistent gains across several model families (Gemma2, Qwen2.5, Llama3.1) and preference optimization techniques. We publicly release our code at https://github.com/alexandra-dragomir/CLewR.

