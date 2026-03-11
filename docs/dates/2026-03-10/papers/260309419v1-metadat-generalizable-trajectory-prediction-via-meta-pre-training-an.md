---
layout: default
title: MetaDAT: Generalizable Trajectory Prediction via Meta Pre-training and Data-Adaptive Test-Time Updating
---

# MetaDAT: Generalizable Trajectory Prediction via Meta Pre-training and Data-Adaptive Test-Time Updating
**arXiv**：[2603.09419v1](https://arxiv.org/abs/2603.09419) · [PDF](https://arxiv.org/pdf/2603.09419.pdf)  
**作者**：Yuning Wang, Pu Zhang, Yuan He, Ke Wang, Jianru Xue  

**一句话要点**：提出MetaDAT框架，通过元预训练与数据自适应测试时更新，提升轨迹预测在分布偏移下的泛化性。

**关键词**：轨迹预测, 元学习, 测试时适应, 分布偏移, 在线学习, 数据自适应

## 3 点简述
- 现有轨迹预测方法在测试时分布偏移下性能显著下降，缺乏在线学习灵活性。
- 采用元学习框架优化预测器，实现快速准确在线适应，并引入数据自适应更新机制动态调整学习率与频率。
- 在nuScenes、Lyft和Waymo等跨数据集场景中验证，超越现有测试时训练方法，展现高适应精度与鲁棒性。

## 摘要（原文）

> Existing trajectory prediction methods exhibit significant performance degradation under distribution shifts during test time. Although test-time training techniques have been explored to enable adaptation, current approaches rely on an offline pre-trained predictor that lacks online learning flexibility. Moreover, they depend on fixed online model updating rules that do not accommodate the specific characteristics of test data. To address these limitations, we first propose a meta-learning framework to directly optimize the predictor for fast and accurate online adaptation, which performs bi-level optimization on the performance of simulated test-time adaptation tasks during pre-training. Furthermore, at test time, we introduce a data-adaptive model updating mechanism that dynamically adjusts the predefined learning rates and updating frequencies based on online partial derivatives and hard sample selection. This mechanism enables the online learning rate to suit the test data, and focuses on informative hard samples to enhance efficiency. Experiments are conducted on various challenging cross-dataset distribution shift scenarios, including nuScenes, Lyft, and Waymo. Results demonstrate that our method achieves superior adaptation accuracy, surpassing state-of-the-art test-time training methods for trajectory prediction. Additionally, our method excels under suboptimal learning rates and high FPS demands, showcasing its robustness and practicality.

