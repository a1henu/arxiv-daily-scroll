---
layout: default
title: Rate-Distortion Signatures of Generalization and Information Trade-offs
---

# Rate-Distortion Signatures of Generalization and Information Trade-offs
**arXiv**：[2603.01568v1](https://arxiv.org/abs/2603.01568) · [PDF](https://arxiv.org/pdf/2603.01568.pdf)  
**作者**：Leyla Roksan Caglar, Pedro A. M. Mediano, Baihan Lin  

**一句话要点**：提出基于率失真理论的框架，以几何签名比较视觉系统在扰动下的泛化行为。

**关键词**：率失真理论, 泛化几何, 视觉鲁棒性, 深度网络, 心理物理学, 模型比较

## 3 点简述
- 核心问题：视觉系统在图像扰动下如何权衡准确性与鲁棒性，标准指标难以深入分析。
- 方法要点：将刺激-响应行为建模为通信信道，从混淆矩阵推导率失真前沿，提取斜率β和曲率κ作为几何签名。
- 实验或效果：应用于人类心理物理学和18个深度视觉模型，发现人类与AI系统遵循共同原则但占据不同率失真空间区域。

## 摘要（原文）

> Generalization to novel visual conditions remains a central challenge for both human and machine vision, yet standard robustness metrics offer limited insight into how systems trade accuracy for robustness. We introduce a rate-distortion-theoretic framework that treats stimulus-response behavior as an effective communication channel, derives rate-distortion (RD) frontiers from confusion matrices, and summarizes each system with two interpretable geometric signatures - slope ($β$) and curvature ($κ$) - which capture the marginal cost and abruptness of accuracy-robustness trade-offs. Applying this framework to human psychophysics and 18 deep vision models under controlled image perturbations, we compare generalization geometry across model architectures and training regimes. We find that both biological and artificial systems follow a common lossy-compression principle but occupy systematically different regions of RD space. In particular, humans exhibit smoother, more flexible trade-offs, whereas modern deep networks operate in steeper and more brittle regimes even at matched accuracy. Across training regimes, robustness training induces systematic but dissociable shifts in beta/kappa, revealing cases where improved robustness or accuracy does not translate into more human-like generalization geometry. These results demonstrate that RD geometry provides a compact, model-agnostic lens for comparing generalization behavior across systems beyond standard accuracy-based metrics.

