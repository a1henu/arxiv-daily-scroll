---
layout: default
title: dVLM-AD: Enhance Diffusion Vision-Language-Model for Driving via Controllable Reasoning
---

# dVLM-AD: Enhance Diffusion Vision-Language-Model for Driving via Controllable Reasoning
**arXiv**：[2512.04459v1](https://arxiv.org/abs/2512.04459) · [PDF](https://arxiv.org/pdf/2512.04459.pdf)  
**作者**：Yingzi Ma, Yulong Cao, Wenhao Ding, Shuibai Zhang, Yan Wang, Boris Ivanovic, Ming Jiang, Marco Pavone, Chaowei Xiao  

**一句话要点**：提出dVLM-AD扩散视觉语言模型，通过可控推理增强端到端驾驶系统在分布外场景的泛化能力。

**关键词**：端到端驾驶, 扩散视觉语言模型, 可控推理, 分布外泛化, 行为-轨迹一致性, 长尾场景

## 3 点简述
- 现有自回归视觉语言模型在驾驶中因因果注意力和顺序生成导致高层推理与低层规划不一致。
- dVLM-AD基于离散扩散模型，利用双向注意力和迭代去噪实现感知、结构化推理和规划的统一。
- 在nuScenes和WOD-E2E上评估，行为-轨迹一致性提升9%，长尾场景RFS提高6%，性能优于自回归基线。

## 摘要（原文）

> The autonomous driving community is increasingly focused on addressing the challenges posed by out-of-distribution (OOD) driving scenarios. A dominant research trend seeks to enhance end-to-end (E2E) driving systems by integrating vision-language models (VLMs), leveraging their rich world knowledge and reasoning abilities to improve generalization across diverse environments. However, most existing VLMs or vision-language agents (VLAs) are built upon autoregressive (AR) models. In this paper, we observe that existing AR-based VLMs -- limited by causal attention and sequential token generation -- often fail to maintain consistency and controllability between high-level reasoning and low-level planning. In contrast, recent discrete diffusion VLMs equipped with bidirectional attention exhibit superior controllability and reliability through iterative denoising. Building on these observations, we introduce dVLM-AD, a diffusion-based vision-language model that unifies perception, structured reasoning, and low-level planning for end-to-end driving. Evaluated on nuScenes and WOD-E2E, dVLM-AD yields more consistent reasoning-action pairs and achieves planning performance comparable to existing driving VLM/VLA systems despite a modest backbone, outperforming AR-based baselines with a 9 percent improvement in behavior-trajectory consistency and a 6 percent increase in RFS on long-tail WOD-E2E scenarios. These results suggest a controllable and reliable pathway for scalable end-to-end driving.

