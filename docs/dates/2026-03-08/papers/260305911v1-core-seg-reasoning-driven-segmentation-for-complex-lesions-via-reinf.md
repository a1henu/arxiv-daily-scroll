---
layout: default
title: CORE-Seg: Reasoning-Driven Segmentation for Complex Lesions via Reinforcement Learning
---

# CORE-Seg: Reasoning-Driven Segmentation for Complex Lesions via Reinforcement Learning
**arXiv**：[2603.05911v1](https://arxiv.org/abs/2603.05911) · [PDF](https://arxiv.org/pdf/2603.05911.pdf)  
**作者**：Yuxin Xie, Yuming Chen, Yishan Yang, Yi Zhou, Tao Zhou, Zhen Zhao, Jiacheng Liu, Huazhu Fu  

**一句话要点**：提出CORE-Seg框架，通过强化学习实现复杂病灶的推理驱动分割。

**关键词**：医学图像分割, 推理驱动分割, 强化学习, 多模态大模型, 复杂病灶, 自适应奖励机制

## 3 点简述
- 核心问题：现有多模态大模型缺乏复杂病灶的视觉推理能力，传统分割模型缺乏逻辑可解释性。
- 方法要点：集成语义引导提示适配器，采用从SFT到GRPO的渐进训练策略和自适应双粒度奖励机制。
- 实验或效果：在ComLesion-14K基准上达到37.06%的平均Dice，比次优基线高14.89%，失败率降至18.42%。

## 摘要（原文）

> Medical image segmentation is undergoing a paradigm shift from conventional visual pattern matching to cognitive reasoning analysis. Although Multimodal Large Language Models (MLLMs) have shown promise in integrating linguistic and visual knowledge, significant gaps remain: existing general MLLMs possess broad common sense but lack the specialized visual reasoning required for complex lesions, whereas traditional segmentation models excel at pixel-level segmentation but lack logical interpretability. In this paper, we introduce ComLesion-14K, the first diverse Chain-of-Thought (CoT) benchmark for reasoning-driven complex lesion segmentation. To accomplish this task, we propose CORE-Seg, an end-to-end framework integrating reasoning with segmentation through a Semantic-Guided Prompt Adapter. We design a progressive training strategy from SFT to GRPO, equipped with an adaptive dual-granularity reward mechanism to mitigate reward sparsity. Our Method achieves state-of-the-art results with a mean Dice of 37.06\% (14.89\% higher than the second-best baseline), while reducing the failure rate to 18.42\%. Project Page: https://xyxl024.github.io/CORE-Seg.github.io/

