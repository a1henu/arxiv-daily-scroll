---
layout: default
title: BLINK: Behavioral Latent Modeling of NK Cell Cytotoxicity
---

# BLINK: Behavioral Latent Modeling of NK Cell Cytotoxicity
**arXiv**：[2603.05110v1](https://arxiv.org/abs/2603.05110) · [PDF](https://arxiv.org/pdf/2603.05110.pdf)  
**作者**：Iman Nematollahi, Jose Francisco Villena-Ossa, Alina Moter, Kiana Farhadyar, Gabriel Kalweit, Abhinav Valada, Toni Cathomen, Evelyn Ullrich, Maria Kalweit  

**一句话要点**：提出BLINK轨迹循环状态空间模型，以建模NK细胞与肿瘤细胞交互动力学并预测细胞毒性结果。

**关键词**：细胞交互建模, 状态空间模型, 轨迹分析, NK细胞毒性, 时间序列预测, 潜在表示学习

## 3 点简述
- 核心问题：NK细胞毒性基于时间交互，单帧分类无法可靠推断结果。
- 方法要点：基于轨迹学习潜在交互动态，预测凋亡增量累积为毒性结果。
- 实验或效果：在长时间NK-肿瘤记录中提升结果检测，支持预测与可解释行为模式。

## 摘要（原文）

> Machine learning models of cellular interaction dynamics hold promise for understanding cell behavior. Natural killer (NK) cell cytotoxicity is a prominent example of such interaction dynamics and is commonly studied using time-resolved multi-channel fluorescence microscopy. Although tumor cell death events can be annotated at single frames, NK cytotoxic outcome emerges over time from cellular interactions and cannot be reliably inferred from frame-wise classification alone. We introduce BLINK, a trajectory-based recurrent state-space model that serves as a cell world model for NK-tumor interactions. BLINK learns latent interaction dynamics from partially observed NK-tumor interaction sequences and predicts apoptosis increments that accumulate into cytotoxic outcomes. Experiments on long-term time-lapse NK-tumor recordings show improved cytotoxic outcome detection and enable forecasting of future outcomes, together with an interpretable latent representation that organizes NK trajectories into coherent behavioral modes and temporally structured interaction phases. BLINK provides a unified framework for quantitative evaluation and structured modeling of NK cytotoxic behavior at the single-cell level.

