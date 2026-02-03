---
layout: default
title: No Global Plan in Chain-of-Thought: Uncover the Latent Planning Horizon of LLMs
---

# No Global Plan in Chain-of-Thought: Uncover the Latent Planning Horizon of LLMs
**arXiv**：[2602.02103v1](https://arxiv.org/abs/2602.02103) · [PDF](https://arxiv.org/pdf/2602.02103.pdf)  
**作者**：Liyan Xu, Mo Yu, Fandong Meng, Jie Zhou  

**一句话要点**：提出Tele-Lens方法揭示LLMs在思维链中的短视规划特性，以增强不确定性估计

**关键词**：思维链, 潜在规划, 不确定性估计, 隐藏状态探测, 大语言模型, 推理轨迹

## 3 点简述
- 核心问题：探究LLMs内部状态与思维链推理轨迹的关系，特别是其潜在规划能力
- 方法要点：使用Tele-Lens探测隐藏状态，发现LLMs呈现短视规划，主要进行增量过渡
- 实验或效果：验证小部分思维链位置可有效代表整体不确定性，实现自动识别思维链旁路

## 摘要（原文）

> This work stems from prior complementary observations on the dynamics of Chain-of-Thought (CoT): Large Language Models (LLMs) is shown latent planning of subsequent reasoning prior to CoT emergence, thereby diminishing the significance of explicit CoT; whereas CoT remains critical for tasks requiring multi-step reasoning. To deepen the understanding between LLM's internal states and its verbalized reasoning trajectories, we investigate the latent planning strength of LLMs, through our probing method, Tele-Lens, applying to hidden states across diverse task domains. Our empirical results indicate that LLMs exhibit a myopic horizon, primarily conducting incremental transitions without precise global planning. Leveraging this characteristic, we propose a hypothesis on enhancing uncertainty estimation of CoT, which we validate that a small subset of CoT positions can effectively represent the uncertainty of the entire path. We further underscore the significance of exploiting CoT dynamics, and demonstrate that automatic recognition of CoT bypass can be achieved without performance degradation. Our code, data and models are released at https://github.com/lxucs/tele-lens.

