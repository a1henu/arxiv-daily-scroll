---
layout: default
title: SimRPD: Optimizing Recruitment Proactive Dialogue Agents through Simulator-Based Data Evaluation and Selection
---

# SimRPD: Optimizing Recruitment Proactive Dialogue Agents through Simulator-Based Data Evaluation and Selection
**arXiv**：[2601.02871v1](https://arxiv.org/abs/2601.02871) · [PDF](https://arxiv.org/pdf/2601.02871.pdf)  
**作者**：Zhiyong Cao, Dunqiang Liu, Qi Dai, Haojun Xu, Huaiyan Xu, Huan He, Yafei Liu, Siyuan Liu, XiaoLin Lin, Ke Ma, Ruqian Shi, Sijia Yao, Hao Wang, Sicheng Zhou  

**一句话要点**：提出SimRPD框架，通过模拟器数据评估与选择优化招聘主动对话代理

**关键词**：主动对话代理, 用户模拟器, 数据选择, 意图链评估, 招聘对话系统

## 3 点简述
- 核心问题：招聘主动对话代理训练受限于高质量领域特定数据稀缺
- 方法要点：开发高保真用户模拟器合成数据，引入基于意图链的多维评估框架选择高质量数据
- 实验或效果：在真实招聘场景中优于现有模拟器数据选择策略，具有工业部署潜力

## 摘要（原文）

> Task-oriented proactive dialogue agents play a pivotal role in recruitment, particularly for steering conversations towards specific business outcomes, such as acquiring social-media contacts for private-channel conversion. Although supervised fine-tuning and reinforcement learning have proven effective for training such agents, their performance is heavily constrained by the scarcity of high-quality, goal-oriented domain-specific training data. To address this challenge, we propose SimRPD, a three-stage framework for training recruitment proactive dialogue agents. First, we develop a high-fidelity user simulator to synthesize large-scale conversational data through multi-turn online dialogue. Then we introduce a multi-dimensional evaluation framework based on Chain-of-Intention (CoI) to comprehensively assess the simulator and effectively select high-quality data, incorporating both global-level and instance-level metrics. Finally, we train the recruitment proactive dialogue agent on the selected dataset. Experiments in a real-world recruitment scenario demonstrate that SimRPD outperforms existing simulator-based data selection strategies, highlighting its practical value for industrial deployment and its potential applicability to other business-oriented dialogue scenarios.

