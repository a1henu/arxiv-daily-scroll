---
layout: default
title: MMRHP: A Miniature Mixed-Reality HIL Platform for Auditable Closed-Loop Evaluation
---

# MMRHP: A Miniature Mixed-Reality HIL Platform for Auditable Closed-Loop Evaluation
**arXiv**：[2510.18371v1](https://arxiv.org/abs/2510.18371) · [PDF](https://arxiv.org/pdf/2510.18371.pdf)  
**作者**：Mingxin Li, Haibo Hu, Jinghuai Deng, Yuchen Xi, Xinhong Chen, Jianping Wang  

**一句话要点**：提出MMRHP平台以支持自动驾驶系统的可审计闭环评估

**关键词**：自动驾驶验证, 硬件在环平台, 混合现实, 时空测量, SOTIF标准, 闭环评估

## 3 点简述
- 自动驾驶系统验证需平衡测试保真度、成本与可扩展性，现有微型HIL平台缺乏系统定量分析框架
- 设计基于统一时空测量核心的HIL平台，确保物理运动和系统时序的一致可追溯量化
- 实验验证平台空间精度10.27毫米RMSE，闭环延迟约45毫秒，识别Autoware在40毫秒延迟下的性能悬崖

## 摘要（原文）

> Validation of autonomous driving systems requires a trade-off between test
> fidelity, cost, and scalability. While miniaturized hardware-in-the-loop (HIL)
> platforms have emerged as a promising solution, a systematic framework
> supporting rigorous quantitative analysis is generally lacking, limiting their
> value as scientific evaluation tools. To address this challenge, we propose
> MMRHP, a miniature mixed-reality HIL platform that elevates miniaturized
> testing from functional demonstration to rigorous, reproducible quantitative
> analysis. The core contributions are threefold. First, we propose a systematic
> three-phase testing process oriented toward the Safety of the Intended
> Functionality(SOTIF)standard, providing actionable guidance for identifying the
> performance limits and triggering conditions of otherwise correctly functioning
> systems. Second, we design and implement a HIL platform centered around a
> unified spatiotemporal measurement core to support this process, ensuring
> consistent and traceable quantification of physical motion and system timing.
> Finally, we demonstrate the effectiveness of this solution through
> comprehensive experiments. The platform itself was first validated, achieving a
> spatial accuracy of 10.27 mm RMSE and a stable closed-loop latency baseline of
> approximately 45 ms. Subsequently, an in-depth Autoware case study leveraged
> this validated platform to quantify its performance baseline and identify a
> critical performance cliff at an injected latency of 40 ms. This work shows
> that a structured process, combined with a platform offering a unified
> spatio-temporal benchmark, enables reproducible, interpretable, and
> quantitative closed-loop evaluation of autonomous driving systems.

