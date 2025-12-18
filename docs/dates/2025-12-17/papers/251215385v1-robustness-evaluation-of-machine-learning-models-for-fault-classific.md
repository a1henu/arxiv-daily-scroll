---
layout: default
title: Robustness Evaluation of Machine Learning Models for Fault Classification and Localization In Power System Protection
---

# Robustness Evaluation of Machine Learning Models for Fault Classification and Localization In Power System Protection
**arXiv**：[2512.15385v1](https://arxiv.org/abs/2512.15385) · [PDF](https://arxiv.org/pdf/2512.15385.pdf)  
**作者**：Julian Oelhaf, Mehran Pashaei, Georg Kordowich, Christian Bergler, Andreas Maier, Johann Jäger, Siming Bayer  

**一句话要点**：提出统一框架以评估电力系统保护中机器学习模型的鲁棒性

**关键词**：电力系统保护, 机器学习鲁棒性, 故障分类, 故障定位, EMT模拟, 传感器退化

## 3 点简述
- 核心问题：可再生能源渗透挑战传统保护，机器学习需在数据缺失或噪声下保持可靠
- 方法要点：基于高保真EMT模拟，系统评估传感器中断、采样率降低等退化场景
- 实验或效果：故障分类稳定，单相损失下准确率下降约13%；故障定位更敏感，电压损失使误差增加超150%

## 摘要（原文）

> The growing penetration of renewable and distributed generation is transforming power systems and challenging conventional protection schemes that rely on fixed settings and local measurements. Machine learning (ML) offers a data-driven alternative for centralized fault classification (FC) and fault localization (FL), enabling faster and more adaptive decision-making. However, practical deployment critically depends on robustness. Protection algorithms must remain reliable even when confronted with missing, noisy, or degraded sensor data. This work introduces a unified framework for systematically evaluating the robustness of ML models in power system protection.
>   High-fidelity EMT simulations are used to model realistic degradation scenarios, including sensor outages, reduced sampling rates, and transient communication losses. The framework provides a consistent methodology for benchmarking models, quantifying the impact of limited observability, and identifying critical measurement channels required for resilient operation. Results show that FC remains highly stable under most degradation types but drops by about 13% under single-phase loss, while FL is more sensitive overall, with voltage loss increasing localization error by over 150%. These findings offer actionable guidance for robustness-aware design of future ML-assisted protection systems.

