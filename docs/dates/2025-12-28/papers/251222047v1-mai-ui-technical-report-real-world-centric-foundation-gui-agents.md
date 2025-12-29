---
layout: default
title: MAI-UI Technical Report: Real-World Centric Foundation GUI Agents
---

# MAI-UI Technical Report: Real-World Centric Foundation GUI Agents
**arXiv**：[2512.22047v1](https://arxiv.org/abs/2512.22047) · [PDF](https://arxiv.org/pdf/2512.22047.pdf)  
**作者**：Hanzhang Zhou, Xu Zhang, Panrong Tong, Jianan Zhang, Liangyu Chen, Quyu Kong, Chenglin Cai, Chen Liu, Yue Wang, Jingren Zhou, Steven Hoi  

**一句话要点**：提出MAI-UI基础GUI智能体系列，通过自进化数据与设备-云协作解决现实部署挑战

**关键词**：GUI智能体, 设备-云协作, 自进化数据管道, 在线强化学习, 移动导航, GUI定位

## 3 点简述
- 核心问题：GUI智能体部署面临交互缺失、UI操作局限、架构不实用和环境动态性四大挑战
- 方法要点：采用自进化数据管道扩展交互数据，设备-云协作系统按任务状态路由，在线强化学习框架优化并行环境
- 实验效果：在GUI定位和移动导航基准上创多项SOTA，设备-云协作提升性能33%、减少云调用40%并保护隐私

## 摘要（原文）

> The development of GUI agents could revolutionize the next generation of human-computer interaction. Motivated by this vision, we present MAI-UI, a family of foundation GUI agents spanning the full spectrum of sizes, including 2B, 8B, 32B, and 235B-A22B variants. We identify four key challenges to realistic deployment: the lack of native agent-user interaction, the limits of UI-only operation, the absence of a practical deployment architecture, and brittleness in dynamic environments. MAI-UI addresses these issues with a unified methodology: a self-evolving data pipeline that expands the navigation data to include user interaction and MCP tool calls, a native device-cloud collaboration system routes execution by task state, and an online RL framework with advanced optimizations to scale parallel environments and context length. MAI-UI establishes new state-of-the-art across GUI grounding and mobile navigation. On grounding benchmarks, it reaches 73.5% on ScreenSpot-Pro, 91.3% on MMBench GUI L2, 70.9% on OSWorld-G, and 49.2% on UI-Vision, surpassing Gemini-3-Pro and Seed1.8 on ScreenSpot-Pro. On mobile GUI navigation, it sets a new SOTA of 76.7% on AndroidWorld, surpassing UI-Tars-2, Gemini-2.5-Pro and Seed1.8. On MobileWorld, MAI-UI obtains 41.7% success rate, significantly outperforming end-to-end GUI models and competitive with Gemini-3-Pro based agentic frameworks. Our online RL experiments show significant gains from scaling parallel environments from 32 to 512 (+5.2 points) and increasing environment step budget from 15 to 50 (+4.3 points). Finally, the native device-cloud collaboration system improves on-device performance by 33%, reduces cloud model calls by over 40%, and preserves user privacy.

