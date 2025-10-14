---
layout: default
title: XGrasp: Gripper-Aware Grasp Detection with Multi-Gripper Data Generation
---

# XGrasp: Gripper-Aware Grasp Detection with Multi-Gripper Data Generation
**arXiv**：[2510.11036v1](https://arxiv.org/abs/2510.11036) · [PDF](https://arxiv.org/pdf/2510.11036.pdf)  
**作者**：Yeonseo Lee, Jungwook Mun, Hyosup Shin, Guebin Hwang, Junhee Nam, Taeyeop Lee, Sungho Jo  

**一句话要点**：提出XGrasp框架以解决多夹具场景下的抓取检测问题

**关键词**：机器人抓取检测, 多夹具处理, 对比学习, 实时推理, 数据增强

## 3 点简述
- 核心问题：现有抓取方法多针对单一夹具，限制实际应用多样性。
- 方法要点：采用两阶段架构，结合全局场景和局部特征预测抓取点、角度与宽度。
- 实验或效果：在多种夹具上实现高抓取成功率，并显著提升推理速度。

## 摘要（原文）

> Most robotic grasping methods are typically designed for single gripper
> types, which limits their applicability in real-world scenarios requiring
> diverse end-effectors. We propose XGrasp, a real-time gripper-aware grasp
> detection framework that efficiently handles multiple gripper configurations.
> The proposed method addresses data scarcity by systematically augmenting
> existing datasets with multi-gripper annotations. XGrasp employs a hierarchical
> two-stage architecture. In the first stage, a Grasp Point Predictor (GPP)
> identifies optimal locations using global scene information and gripper
> specifications. In the second stage, an Angle-Width Predictor (AWP) refines the
> grasp angle and width using local features. Contrastive learning in the AWP
> module enables zero-shot generalization to unseen grippers by learning
> fundamental grasping characteristics. The modular framework integrates
> seamlessly with vision foundation models, providing pathways for future
> vision-language capabilities. The experimental results demonstrate competitive
> grasp success rates across various gripper types, while achieving substantial
> improvements in inference speed compared to existing gripper-aware methods.
> Project page: https://sites.google.com/view/xgrasp

