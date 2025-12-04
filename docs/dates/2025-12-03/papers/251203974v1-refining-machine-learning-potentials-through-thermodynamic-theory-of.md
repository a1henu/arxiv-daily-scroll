---
layout: default
title: Refining Machine Learning Potentials through Thermodynamic Theory of Phase Transitions
---

# Refining Machine Learning Potentials through Thermodynamic Theory of Phase Transitions
**arXiv**：[2512.03974v1](https://arxiv.org/abs/2512.03974) · [PDF](https://arxiv.org/pdf/2512.03974.pdf)  
**作者**：Paul Fuchs, Julija Zavadlav  

**一句话要点**：提出基于热力学相变理论的机器学习势函数微调策略，以校正相变温度预测偏差。

**关键词**：机器学习势函数, 相变温度校正, 可微分轨迹重加权, 热力学理论, 分子动力学模拟, 材料设计

## 3 点简述
- 机器学习势函数因参考数据偏差导致相变温度预测误差达数百开尔文。
- 采用可微分轨迹重加权算法，最小化相间自由能差以匹配实验数据。
- 在纯钛相图中校正温度至十分之一开尔文精度，并改进液态扩散常数。

## 摘要（原文）

> Foundational Machine Learning Potentials can resolve the accuracy and transferability limitations of classical force fields. They enable microscopic insights into material behavior through Molecular Dynamics simulations, which can crucially expedite material design and discovery. However, insufficiently broad and systematically biased reference data affect the predictive quality of the learned models. Often, these models exhibit significant deviations from experimentally observed phase transition temperatures, in the order of several hundred kelvins. Thus, fine-tuning is necessary to achieve adequate accuracy in many practical problems. This work proposes a fine-tuning strategy via top-down learning, directly correcting the wrongly predicted transition temperatures to match the experimental reference data. Our approach leverages the Differentiable Trajectory Reweighting algorithm to minimize the free energy differences between phases at the experimental target pressures and temperatures. We demonstrate that our approach can accurately correct the phase diagram of pure Titanium in a pressure range of up to 5 GPa, matching the experimental reference within tenths of kelvins and improving the liquid-state diffusion constant. Our approach is model-agnostic, applicable to multi-component systems with solid-solid and solid-liquid transitions, and compliant with top-down training on other experimental properties. Therefore, our approach can serve as an essential step towards highly accurate application-specific and foundational machine learning potentials.

