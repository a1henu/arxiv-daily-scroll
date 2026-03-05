---
layout: default
title: Bridging Human Evaluation to Infrared and Visible Image Fusion
---

# Bridging Human Evaluation to Infrared and Visible Image Fusion
**arXiv**：[2603.03871v1](https://arxiv.org/abs/2603.03871) · [PDF](https://arxiv.org/pdf/2603.03871.pdf)  
**作者**：Jinyuan Liu, Xingyuan Li, Qingyun Mei, Haoyuan Xu, Zhiying Jiang, Long Ma, Risheng Liu, Xin Fan  

**一句话要点**：提出反馈强化框架以解决红外与可见光图像融合中人类感知对齐问题

**关键词**：红外可见光图像融合, 人类反馈数据集, 强化学习, 感知质量评估, 组相对策略优化

## 3 点简述
- 核心问题：现有方法依赖手工损失和客观指标，导致融合结果与人类视觉偏好不一致，影响安全监控等应用。
- 方法要点：引入首个大规模人类反馈数据集，设计领域特定奖励函数，通过组相对策略优化微调融合网络。
- 实验或效果：实现最先进性能，融合图像更符合人类美学，代码已开源。

## 摘要（原文）

> Infrared and visible image fusion (IVIF) integrates complementary modalities to enhance scene perception. Current methods predominantly focus on optimizing handcrafted losses and objective metrics, often resulting in fusion outcomes that do not align with human visual preferences. This challenge is further exacerbated by the ill-posed nature of IVIF, which severely limits its effectiveness in human perceptual environments such as security surveillance and driver assistance systems. To address these limitations, we propose a feedback reinforcement framework that bridges human evaluation to infrared and visible image fusion. To address the lack of human-centric evaluation metrics and data, we introduce the first large-scale human feedback dataset for IVIF, containing multidimensional subjective scores and artifact annotations, and enriched by a fine-tuned large language model with expert review. Based on this dataset, we design a domain-specific reward function and train a reward model to quantify perceptual quality. Guided by this reward, we fine-tune the fusion network through Group Relative Policy Optimization, achieving state-of-the-art performance that better aligns fused images with human aesthetics. Code is available at https://github.com/ALKA-Wind/EVAFusion.

