---
layout: default
title: Physics-Guided Tiny-Mamba Transformer for Reliability-Aware Early Fault Warning
---

# Physics-Guided Tiny-Mamba Transformer for Reliability-Aware Early Fault Warning
**arXiv**：[2601.21293v1](https://arxiv.org/abs/2601.21293) · [PDF](https://arxiv.org/pdf/2601.21293.pdf)  
**作者**：Changyu Li, Dingcheng Huang, Kexuan Yao, Xiaoya Ni, Lijuan Shen, Fei Luo  

**一句话要点**：提出物理引导的微型Mamba Transformer，用于旋转机械的可靠性感知早期故障预警。

**关键词**：旋转机械故障预警, 物理引导深度学习, 状态空间模型, 极值理论校准, 跨域迁移学习, 可靠性预测

## 3 点简述
- 核心问题：旋转机械在非平稳工况、域偏移和类别不平衡下，需实现准确、低误报的早期预警。
- 方法要点：采用三分支编码器，结合深度可分离卷积、状态空间模型和轻量Transformer，并引入物理对齐评分和极值理论校准决策。
- 实验或效果：在多个数据集上实现高精度-召回AUC、竞争性ROC AUC、短平均检测时间及强跨域迁移能力。

## 摘要（原文）

> Reliability-centered prognostics for rotating machinery requires early warning signals that remain accurate under nonstationary operating conditions, domain shifts across speed/load/sensors, and severe class imbalance, while keeping the false-alarm rate small and predictable. We propose the Physics-Guided Tiny-Mamba Transformer (PG-TMT), a compact tri-branch encoder tailored for online condition monitoring. A depthwise-separable convolutional stem captures micro-transients, a Tiny-Mamba state-space branch models near-linear long-range dynamics, and a lightweight local Transformer encodes cross-channel resonances. We derive an analytic temporal-to-spectral mapping that ties the model's attention spectrum to classical bearing fault-order bands, yielding a band-alignment score that quantifies physical plausibility and provides physics-grounded explanations. To ensure decision reliability, healthy-score exceedances are modeled with extreme-value theory (EVT), which yields an on-threshold achieving a target false-alarm intensity (events/hour); a dual-threshold hysteresis with a minimum hold time further suppresses chatter. Under a leakage-free streaming protocol with right-censoring of missed detections on CWRU, Paderborn, XJTU-SY, and an industrial pilot, PG-TMT attains higher precision-recall AUC (primary under imbalance), competitive or better ROC AUC, and shorter mean time-to-detect at matched false-alarm intensity, together with strong cross-domain transfer. By coupling physics-aligned representations with EVT-calibrated decision rules, PG-TMT delivers calibrated, interpretable, and deployment-ready early warnings for reliability-centric prognostics and health management.

