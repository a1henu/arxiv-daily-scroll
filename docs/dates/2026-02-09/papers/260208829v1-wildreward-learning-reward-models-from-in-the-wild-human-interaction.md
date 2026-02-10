---
layout: default
title: WildReward: Learning Reward Models from In-the-Wild Human Interactions
---

# WildReward: Learning Reward Models from In-the-Wild Human Interactions
**arXiv**：[2602.08829v1](https://arxiv.org/abs/2602.08829) · [PDF](https://arxiv.org/pdf/2602.08829.pdf)  
**作者**：Hao Peng, Yunjia Qi, Xiaozhi Wang, Zijun Yao, Lei Hou, Juanzi Li  

**一句话要点**：提出WildReward从真实交互中学习奖励模型，无需人工标注偏好对

**关键词**：奖励模型, 真实交互学习, 序数回归, 偏好学习, 大语言模型训练, 在线优化

## 3 点简述
- 核心问题：奖励模型通常依赖大规模人工标注偏好对，成本高且难以扩展
- 方法要点：利用WildChat交互数据提取可靠反馈，通过序数回归直接训练奖励模型
- 实验或效果：WildReward性能媲美或优于传统模型，校准和一致性更好，应用于DPO训练有显著提升

## 摘要（原文）

> Reward models (RMs) are crucial for the training of large language models (LLMs), yet they typically rely on large-scale human-annotated preference pairs. With the widespread deployment of LLMs, in-the-wild interactions have emerged as a rich source of implicit reward signals. This raises the question: Can we develop reward models directly from in-the-wild interactions? In this work, we explore this possibility by adopting WildChat as an interaction source and proposing a pipeline to extract reliable human feedback, yielding 186k high-quality instances for training WildReward via ordinal regression directly on user feedback without preference pairs. Extensive experiments demonstrate that WildReward achieves comparable or even superior performance compared to conventional reward models, with improved calibration and cross-sample consistency. We also observe that WildReward benefits directly from user diversity, where more users yield stronger reward models. Finally, we apply WildReward to online DPO training and observe significant improvements across various tasks. Code and data are released at https://github.com/THU-KEG/WildReward.

