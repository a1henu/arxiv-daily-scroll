---
layout: default
title: SKETCH: Semantic Key-Point Conditioning for Long-Horizon Vessel Trajectory Prediction
---

# SKETCH: Semantic Key-Point Conditioning for Long-Horizon Vessel Trajectory Prediction
**arXiv**：[2601.18537v1](https://arxiv.org/abs/2601.18537) · [PDF](https://arxiv.org/pdf/2601.18537.pdf)  
**作者**：Linyong Gan, Zimo Li, Wenxin Xu, Xingjian Li, Jianhua Z. Huang, Enmei Tu, Shuhang Chen  

**一句话要点**：提出语义关键点条件化框架以解决长时船舶轨迹预测中的全局一致性漂移问题

**关键词**：船舶轨迹预测, 语义关键点条件化, 长时预测, 全局一致性, AIS数据, 导航意图建模

## 3 点简述
- 核心问题：长时船舶轨迹预测因复杂导航行为和环境因素导致全局方向一致性差，易产生漂移或不合理轨迹。
- 方法要点：通过高层语义关键点（NKP）捕获导航意图，将预测分解为全局语义决策和局部运动建模，限制轨迹到语义可行子集。
- 实验或效果：在真实AIS数据上验证，方法在长时预测、方向准确性和细粒度轨迹预测方面优于现有技术。

## 摘要（原文）

> Accurate long-horizon vessel trajectory prediction remains challenging due to compounded uncertainty from complex navigation behaviors and environmental factors. Existing methods often struggle to maintain global directional consistency, leading to drifting or implausible trajectories when extrapolated over long time horizons. To address this issue, we propose a semantic-key-point-conditioned trajectory modeling framework, in which future trajectories are predicted by conditioning on a high-level Next Key Point (NKP) that captures navigational intent. This formulation decomposes long-horizon prediction into global semantic decision-making and local motion modeling, effectively restricting the support of future trajectories to semantically feasible subsets. To efficiently estimate the NKP prior from historical observations, we adopt a pretrain-finetune strategy. Extensive experiments on real-world AIS data demonstrate that the proposed method consistently outperforms state-of-the-art approaches, particularly for long travel durations, directional accuracy, and fine-grained trajectory prediction.

