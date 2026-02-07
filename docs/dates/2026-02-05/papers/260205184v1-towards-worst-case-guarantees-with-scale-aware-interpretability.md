---
layout: default
title: Towards Worst-Case Guarantees with Scale-Aware Interpretability
---

# Towards Worst-Case Guarantees with Scale-Aware Interpretability
**arXiv**：[2602.05184v1](https://arxiv.org/abs/2602.05184) · [PDF](https://arxiv.org/pdf/2602.05184.pdf)  
**作者**：Lauren Greenspan, David Berman, Aryeh Brill, Ro Jefferson, Artemy Kolchinsky, Jennifer Lin, Andrew Mack, Anindita Maiti, Fernando E. Rosas, Alexander Stapleton, Lucas Teixeira, Dmitry Vaintrob  

**一句话要点**：提出尺度感知可解释性研究议程，以增强神经网络可解释性的鲁棒性和忠实性

**关键词**：尺度感知可解释性, 神经网络可解释性, 重整化框架, AI安全, 统计物理, 鲁棒性保证

## 3 点简述
- 核心问题：当前可解释性方法缺乏对自然数据多尺度结构的显式追踪和保证，无法处理细粒度噪声的影响
- 方法要点：借鉴物理学的重整化框架，开发形式化工具，以跨分辨率跟踪特征组合并保证边界
- 实验或效果：未知，但旨在合成相邻领域成熟研究，构建理论指导的实用工具

## 摘要（原文）

> Neural networks organize information according to the hierarchical, multi-scale structure of natural data. Methods to interpret model internals should be similarly scale-aware, explicitly tracking how features compose across resolutions and guaranteeing bounds on the influence of fine-grained structure that is discarded as irrelevant noise. We posit that the renormalisation framework from physics can meet this need by offering technical tools that can overcome limitations of current methods. Moreover, relevant work from adjacent fields has now matured to a point where scattered research threads can be synthesized into practical, theory-informed tools. To combine these threads in an AI safety context, we propose a unifying research agenda -- \emph{scale-aware interpretability} -- to develop formal machinery and interpretability tools that have robustness and faithfulness properties supported by statistical physics.

