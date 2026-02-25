---
layout: default
title: PyVision-RL: Forging Open Agentic Vision Models via RL
---

# PyVision-RL: Forging Open Agentic Vision Models via RL
**arXiv**：[2602.20739v1](https://arxiv.org/abs/2602.20739) · [PDF](https://arxiv.org/pdf/2602.20739.pdf)  
**作者**：Shitian Zhao, Shaoheng Lin, Ming Li, Haoquan Zhang, Wenshuo Peng, Kaipeng Zhang, Chen Wei  

**一句话要点**：提出PyVision-RL框架以解决多模态智能体训练中的交互崩溃问题

**关键词**：多模态智能体, 强化学习框架, 交互崩溃, 视频理解, 工具使用, 上下文构建

## 3 点简述
- 核心问题：强化学习在多模态智能体训练中易导致交互崩溃，减少工具使用和多轮推理
- 方法要点：结合过采样-过滤-排序策略和累积工具奖励，稳定训练并促进多轮工具交互
- 实验或效果：开发PyVision-Image和PyVision-Video模型，在图像和视频理解中展示强性能和效率提升

## 摘要（原文）

> Reinforcement learning for agentic multimodal models often suffers from interaction collapse, where models learn to reduce tool usage and multi-turn reasoning, limiting the benefits of agentic behavior. We introduce PyVision-RL, a reinforcement learning framework for open-weight multimodal models that stabilizes training and sustains interaction. Our approach combines an oversampling-filtering-ranking rollout strategy with an accumulative tool reward to prevent collapse and encourage multi-turn tool use. Using a unified training pipeline, we develop PyVision-Image and PyVision-Video for image and video understanding. For video reasoning, PyVision-Video employs on-demand context construction, selectively sampling task-relevant frames during reasoning to significantly reduce visual token usage. Experiments show strong performance and improved efficiency, demonstrating that sustained interaction and on-demand visual processing are critical for scalable multimodal agents.

