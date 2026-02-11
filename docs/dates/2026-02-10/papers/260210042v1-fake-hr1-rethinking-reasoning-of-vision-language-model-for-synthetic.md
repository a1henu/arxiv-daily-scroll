---
layout: default
title: Fake-HR1: Rethinking reasoning of vision language model for synthetic image detection
---

# Fake-HR1: Rethinking reasoning of vision language model for synthetic image detection
**arXiv**：[2602.10042v1](https://arxiv.org/abs/2602.10042) · [PDF](https://arxiv.org/pdf/2602.10042.pdf)  
**作者**：Changjiang Jiang, Xinkuan Sha, Fengchang Yu, Jingjing Liu, Jian Liu, Mingqi Fang, Chenfeng Zhang, Wei Lu  

**一句话要点**：提出Fake-HR1以自适应推理提升合成图像检测效率

**关键词**：合成图像检测, 自适应推理, 混合微调, 强化学习, 视觉语言模型

## 3 点简述
- 问题：现有方法推理过长导致资源浪费，尤其在明显伪造图像上冗余。
- 方法：设计两阶段训练框架，结合混合微调和强化学习，自适应选择推理模式。
- 效果：实验显示模型在推理能力和检测性能上超越现有LLMs，同时显著提升响应效率。

## 摘要（原文）

> Recent studies have demonstrated that incorporating Chain-of-Thought (CoT) reasoning into the detection process can enhance a model's ability to detect synthetic images. However, excessively lengthy reasoning incurs substantial resource overhead, including token consumption and latency, which is particularly redundant when handling obviously generated forgeries. To address this issue, we propose Fake-HR1, a large-scale hybrid-reasoning model that, to the best of our knowledge, is the first to adaptively determine whether reasoning is necessary based on the characteristics of the generative detection task. To achieve this, we design a two-stage training framework: we first perform Hybrid Fine-Tuning (HFT) for cold-start initialization, followed by online reinforcement learning with Hybrid-Reasoning Grouped Policy Optimization (HGRPO) to implicitly learn when to select an appropriate reasoning mode. Experimental results show that Fake-HR1 adaptively performs reasoning across different types of queries, surpassing existing LLMs in both reasoning ability and generative detection performance, while significantly improving response efficiency.

