---
layout: default
title: When RL Meets Adaptive Speculative Training: A Unified Training-Serving System
---

# When RL Meets Adaptive Speculative Training: A Unified Training-Serving System
**arXiv**：[2602.06932v1](https://arxiv.org/abs/2602.06932) · [PDF](https://arxiv.org/pdf/2602.06932.pdf)  
**作者**：Junxiong Wang, Fengxiang Bie, Jisen Li, Zhongzhu Zhou, Zelei Shao, Yubo Wang, Yinghui Liu, Qingyang Wu, Avner May, Sri Yanamandra, Yineng Zhang, Ce Zhang, Tri Dao, Percy Liang, Ben Athiwaratkun, Shuaiwen Leon Song, Chenfeng Xu, Xiaoxia Wu  

**一句话要点**：提出Aurora统一训练-服务系统，通过在线强化学习解决推测解码器部署滞后问题

**关键词**：推测解码, 强化学习, 在线训练, 大模型推理, 系统优化

## 3 点简述
- 核心问题：传统推测解码器训练与部署分离导致高延迟、反馈滞后和领域漂移
- 方法要点：将在线推测器学习重构为异步强化学习问题，利用推理轨迹持续训练
- 实验效果：在最新前沿模型上实现1.5倍初始加速，对分布漂移额外提升1.25倍速度

## 摘要（原文）

> Speculative decoding can significantly accelerate LLM serving, yet most deployments today disentangle speculator training from serving, treating speculator training as a standalone offline modeling problem. We show that this decoupled formulation introduces substantial deployment and adaptation lag: (1) high time-to-serve, since a speculator must be trained offline for a considerable period before deployment; (2) delayed utility feedback, since the true end-to-end decoding speedup is only known after training and cannot be inferred reliably from acceptance rate alone due to model-architecture and system-level overheads; and (3) domain-drift degradation, as the target model is repurposed to new domains and the speculator becomes stale and less effective.
>   To address these issues, we present Aurora, a unified training-serving system that closes the loop by continuously learning a speculator directly from live inference traces. Aurora reframes online speculator learning as an asynchronous reinforcement-learning problem: accepted tokens provide positive feedback, while rejected speculator proposals provide implicit negative feedback that we exploit to improve sample efficiency. Our design integrates an SGLang-based inference server with an asynchronous training server, enabling hot-swapped speculator updates without service interruption. Crucially, Aurora supports day-0 deployment: a speculator can be served immediately and rapidly adapted to live traffic, improving system performance while providing immediate utility feedback. Across experiments, Aurora achieves a 1.5x day-0 speedup on recently released frontier models (e.g., MiniMax M2.1 229B and Qwen3-Coder-Next 80B). Aurora also adapts effectively to distribution shifts in user traffic, delivering an additional 1.25x speedup over a well-trained but static speculator on widely used models (e.g., Qwen3 and Llama3).

