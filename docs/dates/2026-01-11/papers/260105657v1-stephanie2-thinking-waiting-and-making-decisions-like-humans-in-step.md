---
layout: default
title: Stephanie2: Thinking, Waiting, and Making Decisions Like Humans in Step-by-Step AI Social Chat
---

# Stephanie2: Thinking, Waiting, and Making Decisions Like Humans in Step-by-Step AI Social Chat
**arXiv**：[2601.05657v1](https://arxiv.org/abs/2601.05657) · [PDF](https://arxiv.org/pdf/2601.05657.pdf)  
**作者**：Hao Yang, Hongyuan Lu, Dingkang Yang, Wenliang Yang, Peng Sun, Xiaochuan Zhang, Jun Xiao, Kefan He, Wai Lam, Yang Liu, Xinhua Zeng  

**一句话要点**：提出Stephanie2以解决AI社交聊天中步进决策的自然性问题，通过主动等待和消息节奏适应实现更人性化交互。

**关键词**：步进决策对话, 主动等待机制, 消息节奏适应, 社交聊天AI, 图灵测试评估

## 3 点简述
- 核心问题：现有步进聊天系统缺乏主动等待机制，消息节奏不自然，影响交互体验。
- 方法要点：引入主动等待和消息节奏适应，决策发送或等待，建模思考与打字时间以优化节奏。
- 实验或效果：Stephanie2在自然性和参与度上优于Stephanie1，人类评估中通过角色识别图灵测试率更高。

## 摘要（原文）

> Instant-messaging human social chat typically progresses through a sequence of short messages. Existing step-by-step AI chatting systems typically split a one-shot generation into multiple messages and send them sequentially, but they lack an active waiting mechanism and exhibit unnatural message pacing. In order to address these issues, we propose Stephanie2, a novel next-generation step-wise decision-making dialogue agent. With active waiting and message-pace adaptation, Stephanie2 explicitly decides at each step whether to send or wait, and models latency as the sum of thinking time and typing time to achieve more natural pacing. We further introduce a time-window-based dual-agent dialogue system to generate pseudo dialogue histories for human and automatic evaluations. Experiments show that Stephanie2 clearly outperforms Stephanie1 on metrics such as naturalness and engagement, and achieves a higher pass rate on human evaluation with the role identification Turing test.

