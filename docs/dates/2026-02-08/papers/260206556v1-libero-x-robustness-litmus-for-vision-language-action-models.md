---
layout: default
title: LIBERO-X: Robustness Litmus for Vision-Language-Action Models
---

# LIBERO-X: Robustness Litmus for Vision-Language-Action Models
**arXiv**：[2602.06556v1](https://arxiv.org/abs/2602.06556) · [PDF](https://arxiv.org/pdf/2602.06556.pdf)  
**作者**：Guodong Wang, Chenkai Zhang, Qingjie Liu, Jinjin Zhang, Jiancheng Cai, Junjie Liu, Xinmin Liu  

**一句话要点**：提出LIBERO-X基准以解决VLA模型在分布偏移下评估不可靠的问题

**关键词**：视觉-语言-动作模型, 基准测试, 分层评估, 分布偏移, 机器人操作, 泛化能力

## 3 点简述
- 核心问题：现有VLA基准因评估协议不足，难以捕捉真实世界分布偏移，导致评估有限或误导
- 方法要点：引入分层评估协议，针对空间泛化、物体识别和任务指令理解，结合高多样性训练数据
- 实验或效果：实验显示代表性VLA模型在累积扰动下性能显著下降，暴露场景理解和指令落地的局限

## 摘要（原文）

> Reliable benchmarking is critical for advancing Vision-Language-Action (VLA) models, as it reveals their generalization, robustness, and alignment of perception with language-driven manipulation tasks. However, existing benchmarks often provide limited or misleading assessments due to insufficient evaluation protocols that inadequately capture real-world distribution shifts. This work systematically rethinks VLA benchmarking from both evaluation and data perspectives, introducing LIBERO-X, a benchmark featuring: 1) A hierarchical evaluation protocol with progressive difficulty levels targeting three core capabilities: spatial generalization, object recognition, and task instruction understanding. This design enables fine-grained analysis of performance degradation under increasing environmental and task complexity; 2) A high-diversity training dataset collected via human teleoperation, where each scene supports multiple fine-grained manipulation objectives to bridge the train-evaluation distribution gap. Experiments with representative VLA models reveal significant performance drops under cumulative perturbations, exposing persistent limitations in scene comprehension and instruction grounding. By integrating hierarchical evaluation with diverse training data, LIBERO-X offers a more reliable foundation for assessing and advancing VLA development.

