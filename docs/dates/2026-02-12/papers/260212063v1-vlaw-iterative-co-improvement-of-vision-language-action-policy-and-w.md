---
layout: default
title: VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model
---

# VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model
**arXiv**：[2602.12063v1](https://arxiv.org/abs/2602.12063) · [PDF](https://arxiv.org/pdf/2602.12063.pdf)  
**作者**：Yanjiang Guo, Tony Lee, Lucy Xiaoyang Shi, Jianyu Chen, Percy Liang, Chelsea Finn  

**一句话要点**：提出迭代协同改进算法，通过世界模型生成合成数据以提升视觉-语言-动作模型性能

**关键词**：视觉-语言-动作模型, 世界模型, 迭代改进, 合成数据生成, 机器人操作

## 3 点简述
- 核心问题：现有世界模型物理保真度不足，难以准确模拟接触丰富的物体操作细节
- 方法要点：利用真实世界数据迭代改进世界模型，生成合成数据辅助VLA模型训练
- 实验或效果：在真实机器人上实现39.2%绝对成功率提升，合成数据贡献11.6%改进

## 摘要（原文）

> The goal of this paper is to improve the performance and reliability of vision-language-action (VLA) models through iterative online interaction. Since collecting policy rollouts in the real world is expensive, we investigate whether a learned simulator-specifically, an action-conditioned video generation model-can be used to generate additional rollout data. Unfortunately, existing world models lack the physical fidelity necessary for policy improvement: they are predominantly trained on demonstration datasets that lack coverage of many different physical interactions (particularly failure cases) and struggle to accurately model small yet critical physical details in contact-rich object manipulation. We propose a simple iterative improvement algorithm that uses real-world roll-out data to improve the fidelity of the world model, which can then, in turn, be used to generate supplemental synthetic data for improving the VLA model. In our experiments on a real robot, we use this approach to improve the performance of a state-of-the-art VLA model on multiple downstream tasks. We achieve a 39.2% absolute success rate improvement over the base policy and 11.6% improvement from training with the generated synthetic rollouts. Videos can be found at this anonymous website: https://sites.google.com/view/vla-w

