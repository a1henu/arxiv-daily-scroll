---
layout: default
title: PathFinder: Advancing Path Loss Prediction for Single-to-Multi-Transmitter Scenario
---

# PathFinder: Advancing Path Loss Prediction for Single-to-Multi-Transmitter Scenario
**arXiv**：[2512.14150v1](https://arxiv.org/abs/2512.14150) · [PDF](https://arxiv.org/pdf/2512.14150.pdf)  
**作者**：Zhijie Zhong, Zhiwen Yu, Pengyu Li, Jianming Lv, C. L. Philip Chen, Min Chen  

**一句话要点**：提出PathFinder架构，通过解耦特征编码和掩码引导低秩注意力，解决单到多发射器场景下的无线路径损耗预测问题。

**关键词**：无线路径损耗预测, 多发射器场景, 解耦特征编码, 掩码引导注意力, 分布偏移泛化, 5G网络优化

## 3 点简述
- 核心问题：现有方法被动建模环境，忽视多发射器场景，泛化能力差于分布偏移。
- 方法要点：主动建模建筑与发射器，引入掩码引导低秩注意力和发射器导向混合策略。
- 实验或效果：在单到多发射器基准上显著优于先进方法，尤其在多发射器场景表现突出。

## 摘要（原文）

> Radio path loss prediction (RPP) is critical for optimizing 5G networks and enabling IoT, smart city, and similar applications. However, current deep learning-based RPP methods lack proactive environmental modeling, struggle with realistic multi-transmitter scenarios, and generalize poorly under distribution shifts, particularly when training/testing environments differ in building density or transmitter configurations. This paper identifies three key issues: (1) passive environmental modeling that overlooks transmitters and key environmental features; (2) overemphasis on single-transmitter scenarios despite real-world multi-transmitter prevalence; (3) excessive focus on in-distribution performance while neglecting distribution shift challenges. To address these, we propose PathFinder, a novel architecture that actively models buildings and transmitters via disentangled feature encoding and integrates Mask-Guided Low-rank Attention to independently focus on receiver and building regions. We also introduce a Transmitter-Oriented Mixup strategy for robust training and a new benchmark, single-to-multi-transmitter RPP (S2MT-RPP), tailored to evaluate extrapolation performance (multi-transmitter testing after single-transmitter training). Experimental results show PathFinder outperforms state-of-the-art methods significantly, especially in challenging multi-transmitter scenarios. Our code and project site are available at: https://emorzz1g.github.io/PathFinder/.

