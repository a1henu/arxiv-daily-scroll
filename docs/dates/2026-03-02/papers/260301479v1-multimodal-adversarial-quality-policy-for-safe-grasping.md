---
layout: default
title: Multimodal Adversarial Quality Policy for Safe Grasping
---

# Multimodal Adversarial Quality Policy for Safe Grasping
**arXiv**：[2603.01479v1](https://arxiv.org/abs/2603.01479) · [PDF](https://arxiv.org/pdf/2603.01479.pdf)  
**作者**：Kunlin Xie Chenghao Li Haolan Zhang, Nak Young Chong  

**一句话要点**：提出多模态对抗质量策略以实现机器人安全抓取

**关键词**：多模态对抗攻击, 机器人安全抓取, RGBD模态, 补丁优化, 梯度平衡, 人机交互

## 3 点简述
- 核心问题：基于深度神经网络的视觉引导抓取在RGBD模态下存在安全风险，现有RGB对抗攻击方法效果有限。
- 方法要点：引入异构双补丁优化方案和梯度级模态平衡策略，通过模态特定初始化和梯度重加权优化多模态补丁生成。
- 实验或效果：在基准数据集和协作机器人上验证了MAQP的有效性，提升了多模态安全抓取性能。

## 摘要（原文）

> Vision-guided robot grasping based on Deep Neural Networks (DNNs) generalizes well but poses safety risks in the Human-Robot Interaction (HRI). Recent works solved it by designing benign adversarial attacks and patches with RGB modality, yet depth-independent characteristics limit their effectiveness on RGBD modality. In this work, we propose the Multimodal Adversarial Quality Policy (MAQP) to realize multimodal safe grasping. Our framework introduces two key components. First, the Heterogeneous Dual-Patch Optimization Scheme (HDPOS) mitigates the distribution discrepancy between RGB and depth modalities in patch generation by adopting modality-specific initialization strategies, employing a Gaussian distribution for depth patches and a uniform distribution for RGB patches, while jointly optimizing both modalities under a unified objective function. Second, the Gradient-Level Modality Balancing Strategy (GLMBS) is designed to resolve the optimization imbalance from RGB and Depth patches in patch shape adaptation by reweighting gradient contributions based on per-channel sensitivity analysis and applying distance-adaptive perturbation bounds. We conduct extensive experiments on the benchmark datasets and a cobot, showing the effectiveness of MAQP.

