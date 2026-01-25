---
layout: default
title: VideoThinker: Building Agentic VideoLLMs with LLM-Guided Tool Reasoning
---

# VideoThinker: Building Agentic VideoLLMs with LLM-Guided Tool Reasoning
**arXiv**：[2601.15724v1](https://arxiv.org/abs/2601.15724) · [PDF](https://arxiv.org/pdf/2601.15724.pdf)  
**作者**：Chenglin Li, Qianglong Chen, Feng Han, Yikun Wang, Xingxi Yin, Yan Gong, Ruilin Li, Yin Zhang, Jiaqi Wang  

**一句话要点**：提出VideoThinker，通过LLM引导工具推理构建代理视频大模型以解决长视频理解难题

**关键词**：长视频理解, 代理视频大模型, 工具推理, 合成数据, 自适应检索, 时间缩放

## 3 点简述
- 核心问题：现有视频大模型依赖均匀采样帧，导致长视频中时间定位弱和信息丢失
- 方法要点：利用合成工具交互轨迹训练，将视频转为丰富字幕并用代理语言模型生成多步工具使用序列
- 实验或效果：在长视频基准测试中显著优于字幕语言模型代理和强视频模型基线

## 摘要（原文）

> Long-form video understanding remains a fundamental challenge for current Video Large Language Models. Most existing models rely on static reasoning over uniformly sampled frames, which weakens temporal localization and leads to substantial information loss in long videos. Agentic tools such as temporal retrieval, spatial zoom, and temporal zoom offer a natural way to overcome these limitations by enabling adaptive exploration of key moments. However, constructing agentic video understanding data requires models that already possess strong long-form video comprehension, creating a circular dependency. We address this challenge with VideoThinker, an agentic Video Large Language Model trained entirely on synthetic tool interaction trajectories. Our key idea is to convert videos into rich captions and employ a powerful agentic language model to generate multi-step tool use sequences in caption space. These trajectories are subsequently grounded back to video by replacing captions with the corresponding frames, yielding a large-scale interleaved video and tool reasoning dataset without requiring any long-form understanding from the underlying model. Training on this synthetic agentic dataset equips VideoThinker with dynamic reasoning capabilities, adaptive temporal exploration, and multi-step tool use. Remarkably, VideoThinker significantly outperforms both caption-only language model agents and strong video model baselines across long-video benchmarks, demonstrating the effectiveness of tool augmented synthetic data and adaptive retrieval and zoom reasoning for long-form video understanding.

