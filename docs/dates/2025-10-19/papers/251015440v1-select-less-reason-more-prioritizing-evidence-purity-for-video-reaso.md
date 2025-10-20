---
layout: default
title: Select Less, Reason More: Prioritizing Evidence Purity for Video Reasoning
---

# Select Less, Reason More: Prioritizing Evidence Purity for Video Reasoning
**arXiv**：[2510.15440v1](https://arxiv.org/abs/2510.15440) · [PDF](https://arxiv.org/pdf/2510.15440.pdf)  
**作者**：Xuchen Li, Xuzhao Li, Shiyu Hu, Kaiqi Huang  

**一句话要点**：提出证据优先自适应框架以解决长视频推理中的信息稀释问题

**关键词**：长视频推理, 证据感知强化学习, 自适应帧选择, 视频大语言模型, 局部重采样

## 3 点简述
- 核心问题：长视频推理中均匀帧采样导致信息稀释，现有方法缺乏证据纯度和时间补充机制
- 方法要点：采用证据感知强化学习框架，动态选择关键帧并进行局部重采样以获取细节
- 实验或效果：在多个基准测试中达到开源视频大语言模型的新最优性能，提升推理准确率

## 摘要（原文）

> Long-form video reasoning remains a major challenge for Video Large Language
> Models (Video LLMs), as static uniform frame sampling leads to information
> dilution and obscures critical evidence. Furthermore, existing pixel-space
> video reasoning agents, which are designed to actively interact with the video
> to acquire new visual information, remain suboptimal due to their lack of
> rigorous reward mechanisms to enforce evidence purity and their inability to
> perform temporal information supplementation beyond pre-sampled frames. To
> address this critical gap, we propose a novel evidence-prioritized adaptive
> framework built upon our core philosophy: "Select Less, Reason More." Our core
> contribution is the evidence-aware reinforcement learning (EARL) framework,
> which transforms the model into an active interrogator of evidence. EARL is
> precisely engineered to dynamically select the most relevant frames and,
> crucially, to perform localized re-sampling around the selected key frames to
> access fine-grained temporal detail. Extensive experiments on five demanding
> video reasoning benchmarks demonstrate that our EARL-trained model achieves new
> state-of-the-art among open-source Video LLMs, simultaneously learning an
> effective and high-purity visual evidence selection policy. Impressively, our
> 7B model achieves 59.8% on LongVideoBench, 69.0% on MVBench and 64.9% on
> VideoMME. These results highlight the importance of prioritizing evidence
> purity and the effectiveness of our framework.

