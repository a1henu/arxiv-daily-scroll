---
layout: default
title: daVinci-Dev: Agent-native Mid-training for Software Engineering
---

# daVinci-Dev: Agent-native Mid-training for Software Engineering
**arXiv**：[2601.18418v1](https://arxiv.org/abs/2601.18418) · [PDF](https://arxiv.org/pdf/2601.18418.pdf)  
**作者**：Ji Zeng, Dayuan Fu, Tiantian Mi, Yumin Zhuang, Yaxing Huang, Xuefeng Li, Lyumanshan Ye, Muhang Xie, Qishuo Hua, Zhen Huang, Mohan Jiang, Hanning Wang, Jifan Lin, Yang Xiao, Jie Sun, Yunze Wu, Pengfei Liu  

**一句话要点**：提出agent-native中训练方法，通过合成上下文与环境原生轨迹数据，提升LLM在软件工程中的自主代理能力。

**关键词**：软件工程代理, 中训练, 数据合成, 轨迹数据, LLM能力提升

## 3 点简述
- 核心问题：静态训练数据与动态开发环境不匹配，阻碍代理中训练的有效性。
- 方法要点：合成上下文原生轨迹和环境原生轨迹，模拟真实代理工作流以增强数据真实性。
- 实验或效果：在SWE-Bench Verified上验证，32B和72B模型分别达到56.1%和58.5%解决率，优于Kimi-Dev。

## 摘要（原文）

> Recently, the frontier of Large Language Model (LLM) capabilities has shifted from single-turn code generation to agentic software engineering-a paradigm where models autonomously navigate, edit, and test complex repositories. While post-training methods have become the de facto approach for code agents, **agentic mid-training**-mid-training (MT) on large-scale data that mirrors authentic agentic workflows-remains critically underexplored due to substantial resource requirements, despite offering a more scalable path to instilling foundational agentic behaviors than relying solely on expensive reinforcement learning. A central challenge in realizing effective agentic mid-training is the distribution mismatch between static training data and the dynamic, feedback-rich environment of real development. To address this, we present a systematic study of agentic mid-training, establishing both the data synthesis principles and training methodology for effective agent development at scale. Central to our approach is **agent-native data**-supervision comprising two complementary types of trajectories: **contextually-native trajectories** that preserve the complete information flow an agent experiences, offering broad coverage and diversity; and **environmentally-native trajectories** collected from executable repositories where observations stem from actual tool invocations and test executions, providing depth and interaction authenticity. We verify the model's agentic capabilities on `SWE-Bench Verified`. We demonstrate our superiority over the previous open software engineering mid-training recipe `Kimi-Dev` under two post-training settings with an aligned base model and agentic scaffold, while using less than half mid-training tokens (73.1B). Besides relative advantage, our best performing 32B and 72B models achieve **56.1%** and **58.5%** resolution rates, respectively, which are ...

