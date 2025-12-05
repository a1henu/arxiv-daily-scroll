---
layout: default
title: AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention in Agentic Systems
---

# AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention in Agentic Systems
**arXiv**：[2512.04367v1](https://arxiv.org/abs/2512.04367) · [PDF](https://arxiv.org/pdf/2512.04367.pdf)  
**作者**：Yun Piao, Hongbo Min, Hang Su, Leilei Zhang, Lei Wang, Yue Yin, Xiao Wu, Zhejing Xu, Liwei Qu, Hang Li, Xinxin Zeng, Wei Tian, Fei Yu, Xiaowei Li, Jiayi Jiang, Tongxu Liu, Hao Tian, Yufei Que, Xiaobing Tu, Bing Suo, Yuebing Li, Xiangting Chen, Zeen Zhao, Jiaming Tang, Wei Huang, Xuguang Li, Jing Zhao, Jin Li, Jie Shen, Jinkui Ren, Xiantao Zhang  

**一句话要点**：提出AgentBay沙盒服务，通过混合交互界面支持无缝人机干预，以增强自主AI代理的可靠性。

**关键词**：人机协同系统, 自适应流协议, 沙盒服务, AI代理, 低延迟交互, 任务成功率提升

## 3 点简述
- 核心问题：自主AI代理在现实世界异常中脆弱，需要人机协同监督以确保关键任务应用。
- 方法要点：提供安全隔离执行环境，采用自适应流协议实现AI与人类操作员间的低延迟无缝切换控制。
- 实验或效果：在复杂任务基准中，AgentBay模型提升成功率超48%，带宽消耗降低达50%，延迟减少约5%。

## 摘要（原文）

> The rapid advancement of Large Language Models (LLMs) is catalyzing a shift towards autonomous AI Agents capable of executing complex, multi-step tasks. However, these agents remain brittle when faced with real-world exceptions, making Human-in-the-Loop (HITL) supervision essential for mission-critical applications. In this paper, we present AgentBay, a novel sandbox service designed from the ground up for hybrid interaction. AgentBay provides secure, isolated execution environments spanning Windows, Linux, Android, Web Browsers, and Code interpreters. Its core contribution is a unified session accessible via a hybrid control interface: An AI agent can interact programmatically via mainstream interfaces (MCP, Open Source SDK), while a human operator can, at any moment, seamlessly take over full manual control. This seamless intervention is enabled by Adaptive Streaming Protocol (ASP). Unlike traditional VNC/RDP, ASP is specifically engineered for this hybrid use case, delivering an ultra-low-latency, smoother user experience that remains resilient even in weak network environments. It achieves this by dynamically blending command-based and video-based streaming, adapting its encoding strategy based on network conditions and the current controller (AI or human). Our evaluation demonstrates strong results in security, performance, and task completion rates. In a benchmark of complex tasks, the AgentBay (Agent + Human) model achieved more than 48% success rate improvement. Furthermore, our ASP protocol reduces bandwidth consumption by up to 50% compared to standard RDP, and in end-to-end latency with around 5% reduction, especially under poor network conditions. We posit that AgentBay provides a foundational primitive for building the next generation of reliable, human-supervised autonomous systems.

