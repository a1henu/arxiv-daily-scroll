---
layout: default
title: VPWEM: Non-Markovian Visuomotor Policy with Working and Episodic Memory
---

# VPWEM: Non-Markovian Visuomotor Policy with Working and Episodic Memory
**arXiv**：[2603.04910v1](https://arxiv.org/abs/2603.04910) · [PDF](https://arxiv.org/pdf/2603.04910.pdf)  
**作者**：Yuheng Lei, Zhixuan Liang, Hongyuan Zhang, Ping Luo  

**一句话要点**：提出VPWEM非马尔可夫视觉运动策略，结合工作与情景记忆解决机器人长时记忆任务

**关键词**：非马尔可夫策略, 视觉运动控制, 记忆压缩, Transformer模型, 机器人模仿学习, 长时记忆任务

## 3 点简述
- 问题：模仿学习中单步观测或短上下文策略难以处理需长时记忆的非马尔可夫任务，扩大上下文窗口导致计算成本高和过拟合。
- 方法：VPWEM使用滑动窗口作为工作记忆，并引入基于Transformer的情景记忆压缩器，递归转换历史观测为固定数量记忆令牌，与策略联合训练。
- 效果：在MIKASA和MoMaRT基准上，VPWEM优于扩散策略和VLA模型，提升超过20%和平均5%，实现近恒定每步内存与计算。

## 摘要（原文）

> Imitation learning from human demonstrations has achieved significant success in robotic control, yet most visuomotor policies still condition on single-step observations or short-context histories, making them struggle with non-Markovian tasks that require long-term memory. Simply enlarging the context window incurs substantial computational and memory costs and encourages overfitting to spurious correlations, leading to catastrophic failures under distribution shift and violating real-time constraints in robotic systems. By contrast, humans can compress important past experiences into long-term memories and exploit them to solve tasks throughout their lifetime. In this paper, we propose VPWEM, a non-Markovian visuomotor policy equipped with working and episodic memories. VPWEM retains a sliding window of recent observation tokens as short-term working memory, and introduces a Transformer-based contextual memory compressor that recursively converts out-of-window observations into a fixed number of episodic memory tokens. The compressor uses self-attention over a cache of past summary tokens and cross-attention over a cache of historical observations, and is trained jointly with the policy. We instantiate VPWEM on diffusion policies to exploit both short-term and episode-wide information for action generation with nearly constant memory and computation per step. Experiments demonstrate that VPWEM outperforms state-of-the-art baselines including diffusion policies and vision-language-action (VLA) models by more than 20% on the memory-intensive manipulation tasks in MIKASA and achieves an average 5% improvement on the mobile manipulation benchmark MoMaRT. Code is available at https://github.com/HarryLui98/code_vpwem.

