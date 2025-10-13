---
layout: default
title: Towards Safer and Understandable Driver Intention Prediction
---

# Towards Safer and Understandable Driver Intention Prediction
**arXiv**：[2510.09200v1](https://arxiv.org/abs/2510.09200) · [PDF](https://arxiv.org/pdf/2510.09200.pdf)  
**作者**：Mukilan Karuppasamy, Shankar Gangisetty, Shyam Nandan Rai, Carlo Masone, C V Jawahar  

**一句话要点**：提出视频概念瓶颈模型以提升自动驾驶中驾驶员意图预测的可解释性

**关键词**：驾驶员意图预测, 可解释人工智能, 多模态数据集, 视频理解, Transformer模型

## 3 点简述
- 核心问题：自动驾驶系统决策过程缺乏可解释性，影响人机交互安全。
- 方法要点：构建DAAD-X数据集，并开发VCBM框架生成时空一致的解释。
- 实验或效果：评估显示基于Transformer的模型比CNN更具可解释性。

## 摘要（原文）

> Autonomous driving (AD) systems are becoming increasingly capable of handling
> complex tasks, mainly due to recent advances in deep learning and AI. As
> interactions between autonomous systems and humans increase, the
> interpretability of decision-making processes in driving systems becomes
> increasingly crucial for ensuring safe driving operations. Successful
> human-machine interaction requires understanding the underlying representations
> of the environment and the driving task, which remains a significant challenge
> in deep learning-based systems. To address this, we introduce the task of
> interpretability in maneuver prediction before they occur for driver safety,
> i.e., driver intent prediction (DIP), which plays a critical role in AD
> systems. To foster research in interpretable DIP, we curate the eXplainable
> Driving Action Anticipation Dataset (DAAD-X), a new multimodal, ego-centric
> video dataset to provide hierarchical, high-level textual explanations as
> causal reasoning for the driver's decisions. These explanations are derived
> from both the driver's eye-gaze and the ego-vehicle's perspective. Next, we
> propose Video Concept Bottleneck Model (VCBM), a framework that generates
> spatio-temporally coherent explanations inherently, without relying on post-hoc
> techniques. Finally, through extensive evaluations of the proposed VCBM on the
> DAAD-X dataset, we demonstrate that transformer-based models exhibit greater
> interpretability than conventional CNN-based models. Additionally, we introduce
> a multilabel t-SNE visualization technique to illustrate the disentanglement
> and causal correlation among multiple explanations. Our data, code and models
> are available at: https://mukil07.github.io/VCBM.github.io/

