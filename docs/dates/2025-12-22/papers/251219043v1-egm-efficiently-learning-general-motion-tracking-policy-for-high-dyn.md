---
layout: default
title: EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control
---

# EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control
**arXiv**：[2512.19043v1](https://arxiv.org/abs/2512.19043) · [PDF](https://arxiv.org/pdf/2512.19043.pdf)  
**作者**：Chao Yang, Yingkai Sun, Peng Ye, Xin Chen, Chong Yu, Tao Chen  

**一句话要点**：提出EGM框架以高效学习通用运动跟踪策略，用于高动态人形机器人全身控制

**关键词**：人形机器人控制, 运动跟踪策略, 课程学习, 专家混合模型, 高动态运动

## 3 点简述
- 核心问题：传统方法数据利用和训练效率低，高动态运动跟踪性能有限
- 方法要点：集成基于箱的跨运动课程自适应采样、复合解耦专家混合架构和三阶段课程训练
- 实验或效果：仅用4.08小时数据训练，在49.25小时测试运动中泛化稳健，优于基线

## 摘要（原文）

> Learning a general motion tracking policy from human motions shows great potential for versatile humanoid whole-body control. Conventional approaches are not only inefficient in data utilization and training processes but also exhibit limited performance when tracking highly dynamic motions. To address these challenges, we propose EGM, a framework that enables efficient learning of a general motion tracking policy. EGM integrates four core designs. Firstly, we introduce a Bin-based Cross-motion Curriculum Adaptive Sampling strategy to dynamically orchestrate the sampling probabilities based on tracking error of each motion bin, eficiently balancing the training process across motions with varying dificulty and durations. The sampled data is then processed by our proposed Composite Decoupled Mixture-of-Experts (CDMoE) architecture, which efficiently enhances the ability to track motions from different distributions by grouping experts separately for upper and lower body and decoupling orthogonal experts from shared experts to separately handle dedicated features and general features. Central to our approach is a key insight we identified: for training a general motion tracking policy, data quality and diversity are paramount. Building on these designs, we develop a three-stage curriculum training flow to progressively enhance the policy's robustness against disturbances. Despite training on only 4.08 hours of data, EGM generalized robustly across 49.25 hours of test motions, outperforming baselines on both routine and highly dynamic tasks.

