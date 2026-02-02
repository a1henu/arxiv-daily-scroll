---
layout: default
title: WED-Net: A Weather-Effect Disentanglement Network with Causal Augmentation for Urban Flow Prediction
---

# WED-Net: A Weather-Effect Disentanglement Network with Causal Augmentation for Urban Flow Prediction
**arXiv**：[2601.22586v1](https://arxiv.org/abs/2601.22586) · [PDF](https://arxiv.org/pdf/2601.22586.pdf)  
**作者**：Qian Hong, Siyuan Chang, Xiao Zhou  

**一句话要点**：提出WED-Net，通过天气效应解耦与因果增强，提升极端天气下城市流量预测的鲁棒性。

**关键词**：城市流量预测, 天气效应解耦, 因果增强, Transformer架构, 时空预测

## 3 点简述
- 核心问题：极端天气下城市时空预测因事件稀有性和动态性而困难，现有方法缺乏细粒度天气效应捕捉机制。
- 方法要点：采用双分支Transformer架构，通过自注意力和交叉注意力分离内在与天气诱导流量模式，并引入判别器和因果数据增强。
- 实验或效果：在三个城市的出租车流量数据集上验证，WED-Net在极端天气条件下表现稳健，支持更安全的移动性和城市韧性。

## 摘要（原文）

> Urban spatio-temporal prediction under extreme conditions (e.g., heavy rain) is challenging due to event rarity and dynamics. Existing data-driven approaches that incorporate weather as auxiliary input often rely on coarse-grained descriptors and lack dedicated mechanisms to capture fine-grained spatio-temporal effects. Although recent methods adopt causal techniques to improve out-of-distribution generalization, they typically overlook temporal dynamics or depend on fixed confounder stratification. To address these limitations, we propose WED-Net (Weather-Effect Disentanglement Network), a dual-branch Transformer architecture that separates intrinsic and weather-induced traffic patterns via self- and cross-attention, enhanced with memory banks and fused through adaptive gating. To further promote disentanglement, we introduce a discriminator that explicitly distinguishes weather conditions. Additionally, we design a causal data augmentation strategy that perturbs non-causal parts while preserving causal structures, enabling improved generalization under rare scenarios. Experiments on taxi-flow datasets from three cities demonstrate that WED-Net delivers robust performance under extreme weather conditions, highlighting its potential to support safer mobility, highlighting its potential to support safer mobility, disaster preparedness, and urban resilience in real-world settings. The code is publicly available at https://github.com/HQ-LV/WED-Net.

