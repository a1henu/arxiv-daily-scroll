---
layout: default
title: Moving Beyond Functional Connectivity: Time-Series Modeling for fMRI-Based Brain Disorder Classification
---

# Moving Beyond Functional Connectivity: Time-Series Modeling for fMRI-Based Brain Disorder Classification
**arXiv**：[2602.08262v1](https://arxiv.org/abs/2602.08262) · [PDF](https://arxiv.org/pdf/2602.08262.pdf)  
**作者**：Guoqi Yu, Xiaowei Hu, Angelica I. Aviles-Rivero, Anqi Qiu, Shujun Wang  

**一句话要点**：提出DeCI框架，通过时间序列建模提升fMRI脑疾病分类性能

**关键词**：功能磁共振成像, 时间序列建模, 脑疾病分类, 周期漂移分解, 通道独立性

## 3 点简述
- 现有方法依赖功能连接，忽略BOLD信号的时间动态性
- DeCI分解周期与漂移成分，并采用通道独立性建模
- 在五个数据集上超越传统方法，验证了时间建模的有效性

## 摘要（原文）

> Functional magnetic resonance imaging (fMRI) enables non-invasive brain disorder classification by capturing blood-oxygen-level-dependent (BOLD) signals. However, most existing methods rely on functional connectivity (FC) via Pearson correlation, which reduces 4D BOLD signals to static 2D matrices, discarding temporal dynamics and capturing only linear inter-regional relationships. In this work, we benchmark state-of-the-art temporal models (e.g., time-series models such as PatchTST, TimesNet, and TimeMixer) on raw BOLD signals across five public datasets. Results show these models consistently outperform traditional FC-based approaches, highlighting the value of directly modeling temporal information such as cycle-like oscillatory fluctuations and drift-like slow baseline trends. Building on this insight, we propose DeCI, a simple yet effective framework that integrates two key principles: (i) Cycle and Drift Decomposition to disentangle cycle and drift within each ROI (Region of Interest); and (ii) Channel-Independence to model each ROI separately, improving robustness and reducing overfitting. Extensive experiments demonstrate that DeCI achieves superior classification accuracy and generalization compared to both FC-based and temporal baselines. Our findings advocate for a shift toward end-to-end temporal modeling in fMRI analysis to better capture complex brain dynamics. The code is available at https://github.com/Levi-Ackman/DeCI.

