---
layout: default
title: EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience
---

# EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience
**arXiv**：[2601.15876v1](https://arxiv.org/abs/2601.15876) · [PDF](https://arxiv.org/pdf/2601.15876.pdf)  
**作者**：Taofeng Xue, Chong Peng, Mianqiu Huang, Linsen Guo, Tiancheng Han, Haozhe Wang, Jianing Wang, Xiaocheng Zhang, Xin Yang, Dengchang Zhao, Jinrui Ding, Xiandi Ma, Yuchen Xie, Peng Pei, Xunliang Cai, Xipeng Qiu  

**一句话要点**：提出EvoCUA，通过从可扩展合成经验中学习，以进化循环解决计算机使用代理在长时任务中的动态瓶颈。

**关键词**：计算机使用代理, 进化学习, 合成数据生成, 大规模经验获取, 策略优化, 多模态AI

## 3 点简述
- 核心问题：静态数据缩放限制计算机使用代理捕捉长时任务中的复杂因果动态。
- 方法要点：集成数据生成与策略优化，通过可验证合成引擎和异步沙盒大规模获取经验。
- 实验或效果：在OSWorld基准上达到56.7%成功率，超越开源和闭源模型，展示方法的可扩展性。

## 摘要（原文）

> The development of native computer-use agents (CUA) represents a significant leap in multimodal AI. However, their potential is currently bottlenecked by the constraints of static data scaling. Existing paradigms relying primarily on passive imitation of static datasets struggle to capture the intricate causal dynamics inherent in long-horizon computer tasks. In this work, we introduce EvoCUA, a native computer use agentic model. Unlike static imitation, EvoCUA integrates data generation and policy optimization into a self-sustaining evolutionary cycle. To mitigate data scarcity, we develop a verifiable synthesis engine that autonomously generates diverse tasks coupled with executable validators. To enable large-scale experience acquisition, we design a scalable infrastructure orchestrating tens of thousands of asynchronous sandbox rollouts. Building on these massive trajectories, we propose an iterative evolving learning strategy to efficiently internalize this experience. This mechanism dynamically regulates policy updates by identifying capability boundaries -- reinforcing successful routines while transforming failure trajectories into rich supervision through error analysis and self-correction. Empirical evaluations on the OSWorld benchmark demonstrate that EvoCUA achieves a success rate of 56.7%, establishing a new open-source state-of-the-art. Notably, EvoCUA significantly outperforms the previous best open-source model, OpenCUA-72B (45.0%), and surpasses leading closed-weights models such as UI-TARS-2 (53.1%). Crucially, our results underscore the generalizability of this approach: the evolving paradigm driven by learning from experience yields consistent performance gains across foundation models of varying scales, establishing a robust and scalable path for advancing native agent capabilities.

