---
layout: default
title: Physics-Informed Uncertainty Enables Reliable AI-driven Design
---

# Physics-Informed Uncertainty Enables Reliable AI-driven Design
**arXiv**：[2601.18638v1](https://arxiv.org/abs/2601.18638) · [PDF](https://arxiv.org/pdf/2601.18638.pdf)  
**作者**：Tingkai Xue, Chin Chun Ooi, Yang Jiang, Luu Trung Pham Duong, Pao-Hsiung Chiu, Weijiang Zhao, Nagarajan Raghavan, My Ha Dao  

**一句话要点**：提出物理信息不确定性方法，提升频率选择表面逆设计成功率与效率

**关键词**：逆设计, 不确定性量化, 物理信息机器学习, 频率选择表面, 多保真度优化

## 3 点简述
- 传统深度学习方法在数据稀疏区域预测不准，缺乏不确定性量化
- 利用模型预测违反物理定律的程度作为不确定性代理，成本低且有效
- 集成该方法于优化流程，成功率达50%以上，计算成本降低一个数量级

## 摘要（原文）

> Inverse design is a central goal in much of science and engineering, including frequency-selective surfaces (FSS) that are critical to microelectronics for telecommunications and optical metamaterials. Traditional surrogate-assisted optimization methods using deep learning can accelerate the design process but do not usually incorporate uncertainty quantification, leading to poorer optimization performance due to erroneous predictions in data-sparse regions. Here, we introduce and validate a fundamentally different paradigm of Physics-Informed Uncertainty, where the degree to which a model's prediction violates fundamental physical laws serves as a computationally-cheap and effective proxy for predictive uncertainty. By integrating physics-informed uncertainty into a multi-fidelity uncertainty-aware optimization workflow to design complex frequency-selective surfaces within the 20 - 30 GHz range, we increase the success rate of finding performant solutions from less than 10% to over 50%, while simultaneously reducing computational cost by an order of magnitude compared to the sole use of a high-fidelity solver. These results highlight the necessity of incorporating uncertainty quantification in machine-learning-driven inverse design for high-dimensional problems, and establish physics-informed uncertainty as a viable alternative to quantifying uncertainty in surrogate models for physical systems, thereby setting the stage for autonomous scientific discovery systems that can efficiently and robustly explore and evaluate candidate designs.

