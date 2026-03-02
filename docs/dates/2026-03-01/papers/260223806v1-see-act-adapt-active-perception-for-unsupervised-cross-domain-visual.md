---
layout: default
title: See, Act, Adapt: Active Perception for Unsupervised Cross-Domain Visual Adaptation via Personalized VLM-Guided Agent
---

# See, Act, Adapt: Active Perception for Unsupervised Cross-Domain Visual Adaptation via Personalized VLM-Guided Agent
**arXiv**：[2602.23806v1](https://arxiv.org/abs/2602.23806) · [PDF](https://arxiv.org/pdf/2602.23806.pdf)  
**作者**：Tianci Tang, Tielong Cai, Hongwei Wang, Gaoang Wang  

**一句话要点**：提出Sea²框架，通过智能姿态控制代理解决无监督跨域视觉适应问题。

**关键词**：无监督跨域适应, 主动感知, 视觉语言模型, 姿态控制代理, 强化学习, 室内场景理解

## 3 点简述
- 核心问题：预训练感知模型在新环境（如室内场景）中性能显著下降，传统微调方法导致灾难性遗忘且需昂贵标注。
- 方法要点：保持感知模块冻结，利用VLM构建姿态控制器，通过两阶段训练（规则探索轨迹微调和无监督强化学习）优化代理以获取信息视角。
- 实验或效果：在ReplicaCAD数据集上，视觉定位、分割和3D框估计任务性能分别提升13.54%、15.92%和27.68%。

## 摘要（原文）

> Pre-trained perception models excel in generic image domains but degrade significantly in novel environments like indoor scenes. The conventional remedy is fine-tuning on downstream data which incurs catastrophic forgetting of prior knowledge and demands costly, scene-specific annotations. We propose a paradigm shift through Sea$^2$ (See, Act, Adapt): rather than adapting the perception modules themselves, we adapt how they are deployed through an intelligent pose-control agent. Sea$^2$ keeps all perception modules frozen, requiring no downstream labels during training, and uses only scalar perceptual feedback to navigate the agent toward informative viewpoints. Specially, we transform a vision-language model (VLM) into a low-level pose controller through a two-stage training pipeline: first fine-tuning it on rule-based exploration trajectories that systematically probe indoor scenes, and then refining the policy via unsupervised reinforcement learning that constructs rewards from the perception module's outputs and confidence. Unlike prior active perception methods that couple exploration with specific models or collect data for retraining them, Sea$^2$ directly leverages off-the-shelf perception models for various tasks without the need for retraining. We conducted experiments on three visual perception tasks, including visual grounding, segmentation and 3D box estimation, with performance improvements of 13.54%, 15.92% and 27.68% respectively on dataset ReplicaCAD.

