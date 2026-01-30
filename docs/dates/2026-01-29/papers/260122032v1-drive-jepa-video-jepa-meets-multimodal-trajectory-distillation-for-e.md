---
layout: default
title: Drive-JEPA: Video JEPA Meets Multimodal Trajectory Distillation for End-to-End Driving
---

# Drive-JEPA: Video JEPA Meets Multimodal Trajectory Distillation for End-to-End Driving
**arXiv**：[2601.22032v1](https://arxiv.org/abs/2601.22032) · [PDF](https://arxiv.org/pdf/2601.22032.pdf)  
**作者**：Linhan Wang, Zichong Yang, Chen Bai, Guoxiang Zhang, Xiaotong Liu, Xiaoyin Zheng, Xiao-Xiao Long, Chang-Tien Lu, Cheng Lu  

**一句话要点**：提出Drive-JEPA框架，结合视频JEPA与多模态轨迹蒸馏，以提升端到端自动驾驶性能。

**关键词**：端到端自动驾驶, 视频联合嵌入预测架构, 多模态轨迹蒸馏, ViT编码器, 动量选择机制, NAVSIM基准

## 3 点简述
- 核心问题：端到端自动驾驶中，视频预训练改进有限，且单一人轨迹难以学习多模态行为。
- 方法要点：适配V-JEPA预训练ViT编码器，并引入基于提议的规划器蒸馏多轨迹，结合动量选择机制。
- 实验或效果：在NAVSIM评估中，Drive-JEPA在感知无关设置下超越先前方法，达到新SOTA性能。

## 摘要（原文）

> End-to-end autonomous driving increasingly leverages self-supervised video pretraining to learn transferable planning representations. However, pretraining video world models for scene understanding has so far brought only limited improvements. This limitation is compounded by the inherent ambiguity of driving: each scene typically provides only a single human trajectory, making it difficult to learn multimodal behaviors. In this work, we propose Drive-JEPA, a framework that integrates Video Joint-Embedding Predictive Architecture (V-JEPA) with multimodal trajectory distillation for end-to-end driving. First, we adapt V-JEPA for end-to-end driving, pretraining a ViT encoder on large-scale driving videos to produce predictive representations aligned with trajectory planning. Second, we introduce a proposal-centric planner that distills diverse simulator-generated trajectories alongside human trajectories, with a momentum-aware selection mechanism to promote stable and safe behavior. When evaluated on NAVSIM, the V-JEPA representation combined with a simple transformer-based decoder outperforms prior methods by 3 PDMS in the perception-free setting. The complete Drive-JEPA framework achieves 93.3 PDMS on v1 and 87.8 EPDMS on v2, setting a new state-of-the-art.

