---
layout: default
title: VISTA: A Test-Time Self-Improving Video Generation Agent
---

# VISTA: A Test-Time Self-Improving Video Generation Agent
**arXiv**：[2510.15831v1](https://arxiv.org/abs/2510.15831) · [PDF](https://arxiv.org/pdf/2510.15831.pdf)  
**作者**：Do Xuan Long, Xingchen Wan, Hootan Nakhost, Chen-Yu Lee, Tomas Pfister, Sercan Ö. Arık  

**一句话要点**：提出VISTA多代理系统，通过迭代优化提示提升文本到视频生成质量。

**关键词**：文本到视频生成, 测试时优化, 多代理系统, 提示工程, 视频质量评估

## 3 点简述
- 现有方法依赖精确用户提示，视频生成质量不稳定。
- VISTA使用多代理分解、评估和反馈循环，自主改进提示。
- 实验显示VISTA在视频质量和用户意图对齐上优于基线，人类评估偏好率达66.4%。

## 摘要（原文）

> Despite rapid advances in text-to-video synthesis, generated video quality
> remains critically dependent on precise user prompts. Existing test-time
> optimization methods, successful in other domains, struggle with the
> multi-faceted nature of video. In this work, we introduce VISTA (Video
> Iterative Self-improvemenT Agent), a novel multi-agent system that autonomously
> improves video generation through refining prompts in an iterative loop. VISTA
> first decomposes a user idea into a structured temporal plan. After generation,
> the best video is identified through a robust pairwise tournament. This winning
> video is then critiqued by a trio of specialized agents focusing on visual,
> audio, and contextual fidelity. Finally, a reasoning agent synthesizes this
> feedback to introspectively rewrite and enhance the prompt for the next
> generation cycle. Experiments on single- and multi-scene video generation
> scenarios show that while prior methods yield inconsistent gains, VISTA
> consistently improves video quality and alignment with user intent, achieving
> up to 60% pairwise win rate against state-of-the-art baselines. Human
> evaluators concur, preferring VISTA outputs in 66.4% of comparisons.

