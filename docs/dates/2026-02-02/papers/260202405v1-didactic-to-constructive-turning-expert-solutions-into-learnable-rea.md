---
layout: default
title: Didactic to Constructive: Turning Expert Solutions into Learnable Reasoning
---

# Didactic to Constructive: Turning Expert Solutions into Learnable Reasoning
**arXiv**：[2602.02405v1](https://arxiv.org/abs/2602.02405) · [PDF](https://arxiv.org/pdf/2602.02405.pdf)  
**作者**：Ethan Mendes, Jungsoo Park, Alan Ritter  

**一句话要点**：提出分布对齐模仿学习以利用专家解决方案提升大语言模型推理能力

**关键词**：大语言模型推理, 模仿学习, 分布对齐, 专家解决方案, 对比学习, 样本效率

## 3 点简述
- 核心问题：专家解决方案与模型分布不匹配，且数据昂贵，阻碍有效训练。
- 方法要点：通过两步法将专家方案转化为详细推理轨迹，并应用对比目标聚焦学习。
- 实验或效果：使用少于1000个专家方案，在Qwen模型上实现10-25% pass@k提升和2-4倍效率改进。

## 摘要（原文）

> Improving the reasoning capabilities of large language models (LLMs) typically relies either on the model's ability to sample a correct solution to be reinforced or on the existence of a stronger model able to solve the problem. However, many difficult problems remain intractable for even current frontier models, preventing the extraction of valid training signals. A promising alternative is to leverage high-quality expert human solutions, yet naive imitation of this data fails because it is fundamentally out of distribution: expert solutions are typically didactic, containing implicit reasoning gaps intended for human readers rather than computational models. Furthermore, high-quality expert solutions are expensive, necessitating generalizable sample-efficient training methods. We propose Distribution Aligned Imitation Learning (DAIL), a two-step method that bridges the distributional gap by first transforming expert solutions into detailed, in-distribution reasoning traces and then applying a contrastive objective to focus learning on expert insights and methodologies. We find that DAIL can leverage fewer than 1000 high-quality expert solutions to achieve 10-25% pass@k gains on Qwen2.5-Instruct and Qwen3 models, improve reasoning efficiency by 2x to 4x, and enable out-of-domain generalization.

