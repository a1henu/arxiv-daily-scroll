---
layout: default
title: Weaver: End-to-End Agentic System Training for Video Interleaved Reasoning
---

# Weaver: End-to-End Agentic System Training for Video Interleaved Reasoning
**arXiv**：[2602.05829v1](https://arxiv.org/abs/2602.05829) · [PDF](https://arxiv.org/pdf/2602.05829.pdf)  
**作者**：Yudi Shi, Shangzhe Di, Qirui Chen, Qinian Wang, Jiayin Cai, Xiaolong Jiang, Yao Hu, Weidi Xie  

**一句话要点**：提出Weaver端到端可训练多模态推理代理系统，以解决视频推理中的表示不匹配和感知限制问题。

**关键词**：视频推理, 多模态代理系统, 端到端训练, 强化学习, 长视频理解

## 3 点简述
- 核心问题：视频推理需强感知与解释能力，现有文本链式推理方法存在表示不匹配和感知限制。
- 方法要点：Weaver通过动态调用工具，逐步获取视觉线索并构建多模态推理轨迹，结合强化学习探索工具使用策略。
- 实验或效果：在多个复杂视频推理基准测试中提升性能，尤其针对长视频任务。

## 摘要（原文）

> Video reasoning constitutes a comprehensive assessment of a model's capabilities, as it demands robust perceptual and interpretive skills, thereby serving as a means to explore the boundaries of model performance. While recent research has leveraged text-centric Chain-of-Thought reasoning to augment these capabilities, such approaches frequently suffer from representational mismatch and restricted by limited perceptual acuity. To address these limitations, we propose Weaver, a novel, end-to-end trainable multimodal reasoning agentic system. Weaver empowers its policy model to dynamically invoke diverse tools throughout the reasoning process, enabling progressive acquisition of crucial visual cues and construction of authentic multimodal reasoning trajectories. Furthermore, we integrate a reinforcement learning algorithm to allow the system to freely explore strategies for employing and combining these tools with trajectory-free data. Extensive experiments demonstrate that our system, Weaver, enhances performance on several complex video reasoning benchmarks, particularly those involving long videos.

