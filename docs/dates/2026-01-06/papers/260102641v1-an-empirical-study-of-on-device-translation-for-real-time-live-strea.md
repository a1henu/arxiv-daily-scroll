---
layout: default
title: An Empirical Study of On-Device Translation for Real-Time Live-Stream Chat on Mobile Devices
---

# An Empirical Study of On-Device Translation for Real-Time Live-Stream Chat on Mobile Devices
**arXiv**：[2601.02641v1](https://arxiv.org/abs/2601.02641) · [PDF](https://arxiv.org/pdf/2601.02641.pdf)  
**作者**：Jeiyoon Park, Daehwan Lee, Changmin Yeo, Yongshin Han, Minseop Kim  

**一句话要点**：提出端侧翻译模型部署方法，解决直播聊天实时翻译在移动设备上的资源消耗与领域适应问题。

**关键词**：端侧AI, 实时翻译, 移动设备部署, 资源消耗, 领域适应, 基准测试

## 3 点简述
- 核心问题：端侧AI模型在真实部署中面临CPU利用率和热条件等资源限制，缺乏实际研究。
- 方法要点：通过构建LiveChatBench基准，评估模型选择、资源消耗及领域适应能力。
- 实验或效果：在五款移动设备上测试，性能接近GPT-5.1，为端侧AI提供部署见解。

## 摘要（原文）

> Despite its efficiency, there has been little research on the practical aspects required for real-world deployment of on-device AI models, such as the device's CPU utilization and thermal conditions. In this paper, through extensive experiments, we investigate two key issues that must be addressed to deploy on-device models in real-world services: (i) the selection of on-device models and the resource consumption of each model, and (ii) the capability and potential of on-device models for domain adaptation. To this end, we focus on a task of translating live-stream chat messages and manually construct LiveChatBench, a benchmark consisting of 1,000 Korean-English parallel sentence pairs. Experiments on five mobile devices demonstrate that, although serving a large and heterogeneous user base requires careful consideration of highly constrained deployment settings and model selection, the proposed approach nevertheless achieves performance comparable to commercial models such as GPT-5.1 on the well-targeted task. We expect that our findings will provide meaningful insights to the on-device AI community.

