---
layout: default
title: Quantifying and Bridging the Fidelity Gap: A Decisive-Feature Approach to Comparing Synthetic and Real Imagery
---

# Quantifying and Bridging the Fidelity Gap: A Decisive-Feature Approach to Comparing Synthetic and Real Imagery
**arXiv**：[2512.16468v1](https://arxiv.org/abs/2512.16468) · [PDF](https://arxiv.org/pdf/2512.16468.pdf)  
**作者**：Danial Safaei, Siddartha Khastgir, Mohsen Alirezaei, Jeroen Ploeg, Son Tong, Xingyu Zhao  

**一句话要点**：提出决定性特征保真度以解决合成数据在自动驾驶安全测试中的行为一致性差距

**关键词**：合成数据保真度, 自动驾驶安全测试, 可解释AI, 机制对等性, 仿真校准

## 3 点简述
- 核心问题：像素级保真度不足确保自动驾驶系统在仿真与真实环境中的决策机制一致
- 方法要点：基于可解释AI识别并比较系统决策的决定性特征，引入机制对等性度量
- 实验或效果：在KITTI-VirtualKITTI2数据集上验证，DFF揭示传统方法忽略的差异并指导仿真校准

## 摘要（原文）

> Virtual testing using synthetic data has become a cornerstone of autonomous vehicle (AV) safety assurance. Despite progress in improving visual realism through advanced simulators and generative AI, recent studies reveal that pixel-level fidelity alone does not ensure reliable transfer from simulation to the real world. What truly matters is whether the system-under-test (SUT) bases its decisions on the same causal evidence in both real and simulated environments - not just whether images "look real" to humans. This paper addresses the lack of such a behavior-grounded fidelity measure by introducing Decisive Feature Fidelity (DFF), a new SUT-specific metric that extends the existing fidelity spectrum to capture mechanism parity - the agreement in causal evidence underlying the SUT's decisions across domains. DFF leverages explainable-AI (XAI) methods to identify and compare the decisive features driving the SUT's outputs for matched real-synthetic pairs. We further propose practical estimators based on counterfactual explanations, along with a DFF-guided calibration scheme to enhance simulator fidelity. Experiments on 2126 matched KITTI-VirtualKITTI2 pairs demonstrate that DFF reveals discrepancies overlooked by conventional output-value fidelity. Furthermore, results show that DFF-guided calibration improves decisive-feature and input-level fidelity without sacrificing output value fidelity across diverse SUTs.

