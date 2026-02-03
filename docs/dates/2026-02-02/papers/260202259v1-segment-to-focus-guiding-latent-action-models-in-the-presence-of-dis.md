---
layout: default
title: Segment to Focus: Guiding Latent Action Models in the Presence of Distractors
---

# Segment to Focus: Guiding Latent Action Models in the Presence of Distractors
**arXiv**：[2602.02259v1](https://arxiv.org/abs/2602.02259) · [PDF](https://arxiv.org/pdf/2602.02259.pdf)  
**作者**：Hamza Adnan, Matthew T. Jackson, Alexey Zakharov  

**一句话要点**：提出MaskLAM以解决潜在动作模型在干扰物存在下的特征解耦问题

**关键词**：潜在动作模型, 特征解耦, 分割掩码, 强化学习, 干扰物过滤, 重建损失加权

## 3 点简述
- 潜在动作模型面临从原始观测中分离动作相关特征与动作相关噪声的挑战
- 方法利用预训练分割模型加权重建损失，无需架构修改
- 在MuJoCo任务中，奖励提升达4倍，潜在动作质量提高3倍

## 摘要（原文）

> Latent Action Models (LAMs) learn to extract action-relevant representations solely from raw observations, enabling reinforcement learning from unlabelled videos and significantly scaling available training data. However, LAMs face a critical challenge in disentangling action-relevant features from action-correlated noise (e.g., background motion). Failing to filter these distractors causes LAMs to capture spurious correlations and build sub-optimal latent action spaces. In this paper, we introduce MaskLAM -- a lightweight modification to LAM training to mitigate this issue by incorporating visual agent segmentation. MaskLAM utilises segmentation masks from pretrained foundation models to weight the LAM reconstruction loss, thereby prioritising salient information over background elements while requiring no architectural modifications. We demonstrate the effectiveness of our method on continuous-control MuJoCo tasks, modified with action-correlated background noise. Our approach yields up to a 4x increase in accrued rewards compared to standard baselines and a 3x improvement in the latent action quality, as evidenced by linear probe evaluation.

