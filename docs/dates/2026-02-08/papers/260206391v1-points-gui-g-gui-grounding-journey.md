---
layout: default
title: POINTS-GUI-G: GUI-Grounding Journey
---

# POINTS-GUI-G: GUI-Grounding Journey
**arXiv**：[2602.06391v1](https://arxiv.org/abs/2602.06391) · [PDF](https://arxiv.org/pdf/2602.06391.pdf)  
**作者**：Zhongyin Zhao, Yuan Liu, Yikun Liu, Haicheng Wang, Le Tian, Xiao Zhou, Yangxiu You, Zilin Yu, Yang Yu, Jie Zhou  

**一句话要点**：提出POINTS-GUI-G-8B模型，通过数据工程、训练策略和强化学习提升GUI grounding性能，实现自动化数字任务。

**关键词**：GUI grounding, 视觉语言模型, 数据工程, 强化学习, 自动化任务, 界面元素定位

## 3 点简述
- 核心问题：从基础模型POINTS-1.5出发，解决GUI grounding中界面元素精确定位的挑战，作为自动化任务的前提。
- 方法要点：采用数据工程统一格式与增强、训练策略优化视觉编码器与分辨率一致性，以及强化学习提升感知精度。
- 实验或效果：在ScreenSpot-Pro等基准测试中取得领先分数，如59.9和66.0，验证了方法的有效性。

## 摘要（原文）

> The rapid advancement of vision-language models has catalyzed the emergence of GUI agents, which hold immense potential for automating complex tasks, from online shopping to flight booking, thereby alleviating the burden of repetitive digital workflows. As a foundational capability, GUI grounding is typically established as a prerequisite for end-to-end task execution. It enables models to precisely locate interface elements, such as text and icons, to perform accurate operations like clicking and typing. Unlike prior works that fine-tune models already possessing strong spatial awareness (e.g., Qwen3-VL), we aim to master the full technical pipeline by starting from a base model with minimal grounding ability, such as POINTS-1.5. We introduce POINTS-GUI-G-8B, which achieves state-of-the-art performance with scores of 59.9 on ScreenSpot-Pro, 66.0 on OSWorld-G, 95.7 on ScreenSpot-v2, and 49.9 on UI-Vision. Our model's success is driven by three key factors: (1) Refined Data Engineering, involving the unification of diverse open-source datasets format alongside sophisticated strategies for augmentation, filtering, and difficulty grading; (2) Improved Training Strategies, including continuous fine-tuning of the vision encoder to enhance perceptual accuracy and maintaining resolution consistency between training and inference; and (3) Reinforcement Learning (RL) with Verifiable Rewards. While RL is traditionally used to bolster reasoning, we demonstrate that it significantly improves precision in the perception-intensive GUI grounding task. Furthermore, GUI grounding provides a natural advantage for RL, as rewards are easily verifiable and highly accurate.

