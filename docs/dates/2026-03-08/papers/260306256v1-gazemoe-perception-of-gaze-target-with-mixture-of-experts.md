---
layout: default
title: GazeMoE: Perception of Gaze Target with Mixture-of-Experts
---

# GazeMoE: Perception of Gaze Target with Mixture-of-Experts
**arXiv**：[2603.06256v1](https://arxiv.org/abs/2603.06256) · [PDF](https://arxiv.org/pdf/2603.06256.pdf)  
**作者**：Zhuangzhuang Dai, Zhongxi Lu, Vincent G. Zakka, Luis J. Manso, Jose M Alcaraz Calero, Chen Li  

**一句话要点**：提出GazeMoE框架，通过混合专家模块从冻结基础模型中自适应解码多模态线索，以提升机器人对人类注视目标的估计性能。

**关键词**：注视目标估计, 混合专家, 多模态融合, 类平衡损失, 数据增强, 机器人感知

## 3 点简述
- 核心问题：从可见图像估计人类注视目标，需处理多模态线索集成和类不平衡挑战。
- 方法要点：基于混合专家（MoE）设计端到端框架，结合类平衡辅助损失和数据增强策略。
- 实验或效果：在基准数据集上实现最先进性能，优于现有方法，代码和预训练模型已开源。

## 摘要（原文）

> Estimating human gaze target from visible images is a critical task for robots to understand human attention, yet the development of generalizable neural architectures and training paradigms remains challenging. While recent advances in pre-trained vision foundation models offer promising avenues for locating gaze targets, the integration of multi-modal cues -- including eyes, head poses, gestures, and contextual features -- demands adaptive and efficient decoding mechanisms. Inspired by Mixture-of-Experts (MoE) for adaptive domain expertise in large vision-language models, we propose GazeMoE, a novel end-to-end framework that selectively leverages gaze-target-related cues from a frozen foundation model through MoE modules. To address class imbalance in gaze target classification (in-frame vs. out-of-frame) and enhance robustness, GazeMoE incorporates a class-balancing auxiliary loss alongside strategic data augmentations, including region-specific cropping and photometric transformations. Extensive experiments on benchmark datasets demonstrate that our GazeMoE achieves state-of-the-art performance, outperforming existing methods on challenging gaze estimation tasks. The code and pre-trained models are released at https://huggingface.co/zdai257/GazeMoE

