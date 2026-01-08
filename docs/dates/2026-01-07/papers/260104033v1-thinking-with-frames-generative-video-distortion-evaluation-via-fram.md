---
layout: default
title: Thinking with Frames: Generative Video Distortion Evaluation via Frame Reward Model
---

# Thinking with Frames: Generative Video Distortion Evaluation via Frame Reward Model
**arXiv**：[2601.04033v1](https://arxiv.org/abs/2601.04033) · [PDF](https://arxiv.org/pdf/2601.04033.pdf)  
**作者**：Yuan Wang, Borui Liao, Huijuan Huang, Jinda Lu, Ouxiang Li, Kuien Liu, Meng Wang, Xiang Wang  

**一句话要点**：提出REACT帧级奖励模型以评估生成视频中的结构失真问题

**关键词**：生成视频评估, 结构失真检测, 帧级奖励模型, 强化学习优化, 人类偏好数据集

## 3 点简述
- 现有视频奖励模型常忽略结构失真，如异常物体外观和交互
- REACT通过两阶段训练和动态采样机制，专注于帧级失真识别与评分
- 实验表明REACT能补充现有模型，提供准确评估和可解释分析

## 摘要（原文）

> Recent advances in video reward models and post-training strategies have improved text-to-video (T2V) generation. While these models typically assess visual quality, motion quality, and text alignment, they often overlook key structural distortions, such as abnormal object appearances and interactions, which can degrade the overall quality of the generative video. To address this gap, we introduce REACT, a frame-level reward model designed specifically for structural distortions evaluation in generative videos. REACT assigns point-wise scores and attribution labels by reasoning over video frames, focusing on recognizing distortions. To support this, we construct a large-scale human preference dataset, annotated based on our proposed taxonomy of structural distortions, and generate additional data using a efficient Chain-of-Thought (CoT) synthesis pipeline. REACT is trained with a two-stage framework: ((1) supervised fine-tuning with masked loss for domain knowledge injection, followed by (2) reinforcement learning with Group Relative Policy Optimization (GRPO) and pairwise rewards to enhance reasoning capability and align output scores with human preferences. During inference, a dynamic sampling mechanism is introduced to focus on frames most likely to exhibit distortion. We also present REACT-Bench, a benchmark for generative video distortion evaluation. Experimental results demonstrate that REACT complements existing reward models in assessing structutal distortion, achieving both accurate quantitative evaluations and interpretable attribution analysis.

