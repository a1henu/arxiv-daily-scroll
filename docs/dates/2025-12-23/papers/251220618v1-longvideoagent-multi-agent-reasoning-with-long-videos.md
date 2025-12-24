---
layout: default
title: LongVideoAgent: Multi-Agent Reasoning with Long Videos
---

# LongVideoAgent: Multi-Agent Reasoning with Long Videos
**arXiv**：[2512.20618v1](https://arxiv.org/abs/2512.20618) · [PDF](https://arxiv.org/pdf/2512.20618.pdf)  
**作者**：Runtao Liu, Ziyi Liu, Jiaqi Tang, Yue Ma, Renjie Pi, Jipeng Zhang, Qifeng Chen  

**一句话要点**：提出多智能体框架LongVideoAgent，通过协调定位与视觉代理解决长视频问答中的时序定位与细粒度线索缺失问题。

**关键词**：长视频问答, 多智能体系统, 时序定位, 强化学习, 视觉语言模型

## 3 点简述
- 核心问题：现有方法压缩内容为有损摘要或依赖有限工具集，削弱时序定位并遗漏细粒度视觉线索。
- 方法要点：主LLM协调定位代理定位相关片段，视觉代理提取文本观察，结合强化学习训练以优化多智能体合作效率。
- 实验或效果：在LongTVQA和LongTVQA+数据集上显著优于非智能体基线，强化学习进一步增强了推理与规划能力。

## 摘要（原文）

> Recent advances in multimodal LLMs and systems that use tools for long-video QA point to the promise of reasoning over hour-long episodes. However, many methods still compress content into lossy summaries or rely on limited toolsets, weakening temporal grounding and missing fine-grained cues. We propose a multi-agent framework in which a master LLM coordinates a grounding agent to localize question-relevant segments and a vision agent to extract targeted textual observations. The master agent plans with a step limit, and is trained with reinforcement learning to encourage concise, correct, and efficient multi-agent cooperation. This design helps the master agent focus on relevant clips via grounding, complements subtitles with visual detail, and yields interpretable trajectories. On our proposed LongTVQA and LongTVQA+ which are episode-level datasets aggregated from TVQA/TVQA+, our multi-agent system significantly outperforms strong non-agent baselines. Experiments also show reinforcement learning further strengthens reasoning and planning for the trained agent. Code and data will be shared at https://longvideoagent.github.io/.

