---
layout: default
title: DexHiL: A Human-in-the-Loop Framework for Vision-Language-Action Model Post-Training in Dexterous Manipulation
---

# DexHiL: A Human-in-the-Loop Framework for Vision-Language-Action Model Post-Training in Dexterous Manipulation
**arXiv**：[2603.09121v1](https://arxiv.org/abs/2603.09121) · [PDF](https://arxiv.org/pdf/2603.09121.pdf)  
**作者**：Yifan Han, Zhongxi Chen, Yuxuan Zhao, Congsheng Xu, Yanming Shao, Yichuan Peng, Yao Mu, Wenzhao Lian  

**一句话要点**：提出DexHiL框架，通过人机协同提升灵巧操作中视觉-语言-动作模型的训练效果

**关键词**：灵巧操作, 视觉-语言-动作模型, 人机协同学习, 机器人后训练, 多指控制, 实时校正

## 3 点简述
- 核心问题：灵巧操作中多指控制高维且接触密集，现有VLA模型可靠性不足
- 方法要点：集成臂手协同的人机交互框架，支持即时校正与数据采样优化
- 实验或效果：真实机器人实验显示，相比离线微调基线，成功率平均提升25%

## 摘要（原文）

> While Vision-Language-Action (VLA) models have demonstrated promising generalization capabilities in robotic manipulation, deploying them on specific and complex downstream tasks still demands effective post-training. In parallel, Human-in-the-Loop (HiL) learning has proven to be a powerful mechanism for refining robot policies. However, extending this paradigm to dexterous manipulation remains challenging: multi-finger control is high-dimensional, contact-intensive, and exhibits execution distributions that differ markedly from standard arm motions, leaving existing dexterous VLA systems limited in reliability and adaptability. We present DexHiL, the first integrated arm-hand human-in-the-loop framework for dexterous VLA models, enabling coordinated interventions over the arm and the dexterous hand within a single system. DexHiL introduces an intervention-aware data sampling strategy that prioritizes corrective segments for post-training, alongside a lightweight teleoperation interface that supports instantaneous human corrections during execution. Real-robot experiments demonstrate that DexHiL serves as an effective post-training framework, yielding a substantial performance leap, outperforming standard offline-only fine-tuning baselines by an average of 25% in success rates across distinct tasks.
>   Project page: https://chenzhongxi-sjtu.github.io/dexhil/

