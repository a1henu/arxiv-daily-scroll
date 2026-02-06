---
layout: default
title: Towards Worst-Case Guarantees with Scale-Aware Interpretability
---

# Towards Worst-Case Guarantees with Scale-Aware Interpretability
**arXiv**：[2602.05184v1](https://arxiv.org/abs/2602.05184) · [PDF](https://arxiv.org/pdf/2602.05184.pdf)  
**作者**：Lauren Greenspan, David Berman, Aryeh Brill, Ro Jefferson, Artemy Kolchinsky, Jennifer Lin, Andrew Mack, Anindita Maiti, Fernando E. Rosas, Alexander Stapleton, Lucas Teixeira, Dmitry Vaintrob  

**一句话要点**：提出尺度感知可解释性框架，结合重整化理论以增强神经网络解释的鲁棒性和忠实性。

**关键词**：尺度感知可解释性, 神经网络解释, 重整化理论, AI安全, 多尺度特征, 鲁棒性保证

## 3 点简述
- 核心问题：现有神经网络解释方法缺乏对多尺度特征组合的显式追踪和细粒度噪声影响的保证。
- 方法要点：引入物理重整化框架，开发理论工具以克服当前方法的局限性，实现尺度感知解释。
- 实验或效果：未知，但提出统一研究议程，旨在合成跨领域成果为AI安全提供实用工具。

## 摘要（原文）

> Neural networks organize information according to the hierarchical, multi-scale structure of natural data. Methods to interpret model internals should be similarly scale-aware, explicitly tracking how features compose across resolutions and guaranteeing bounds on the influence of fine-grained structure that is discarded as irrelevant noise. We posit that the renormalisation framework from physics can meet this need by offering technical tools that can overcome limitations of current methods. Moreover, relevant work from adjacent fields has now matured to a point where scattered research threads can be synthesized into practical, theory-informed tools. To combine these threads in an AI safety context, we propose a unifying research agenda -- \emph{scale-aware interpretability} -- to develop formal machinery and interpretability tools that have robustness and faithfulness properties supported by statistical physics.

