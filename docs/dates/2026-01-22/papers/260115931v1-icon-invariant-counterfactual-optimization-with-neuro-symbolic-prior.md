---
layout: default
title: ICON: Invariant Counterfactual Optimization with Neuro-Symbolic Priors for Text-Based Person Search
---

# ICON: Invariant Counterfactual Optimization with Neuro-Symbolic Priors for Text-Based Person Search
**arXiv**：[2601.15931v1](https://arxiv.org/abs/2601.15931) · [PDF](https://arxiv.org/pdf/2601.15931.pdf)  
**作者**：Xiangyu Wang, Zhixin Lv, Yongjiao Sun, Anrui Han, Ye Yuan, Hangxu Ji  

**一句话要点**：提出ICON框架，通过因果与拓扑先验解决基于文本的人物搜索中的鲁棒性问题。

**关键词**：基于文本的人物搜索, 因果不变性, 神经符号先验, 反事实优化, 鲁棒性学习, 空间语义对齐

## 3 点简述
- 核心问题：现有方法依赖被动观察，导致虚假相关和空间语义错位，缺乏分布偏移鲁棒性。
- 方法要点：整合规则引导空间干预、反事实上下文解耦、显著性驱动语义正则化和神经符号拓扑对齐。
- 实验或效果：在标准基准上保持领先性能，对遮挡、背景干扰和定位噪声展现卓越鲁棒性。

## 摘要（原文）

> Text-Based Person Search (TBPS) holds unique value in real-world surveillance bridging visual perception and language understanding, yet current paradigms utilizing pre-training models often fail to transfer effectively to complex open-world scenarios. The reliance on "Passive Observation" leads to multifaceted spurious correlations and spatial semantic misalignment, causing a lack of robustness against distribution shifts. To fundamentally resolve these defects, this paper proposes ICON (Invariant Counterfactual Optimization with Neuro-symbolic priors), a framework integrating causal and topological priors. First, we introduce Rule-Guided Spatial Intervention to strictly penalize sensitivity to bounding box noise, forcibly severing location shortcuts to achieve geometric invariance. Second, Counterfactual Context Disentanglement is implemented via semantic-driven background transplantation, compelling the model to ignore background interference for environmental independence. Then, we employ Saliency-Driven Semantic Regularization with adaptive masking to resolve local saliency bias and guarantee holistic completeness. Finally, Neuro-Symbolic Topological Alignment utilizes neuro-symbolic priors to constrain feature matching, ensuring activated regions are topologically consistent with human structural logic. Experimental results demonstrate that ICON not only maintains leading performance on standard benchmarks but also exhibits exceptional robustness against occlusion, background interference, and localization noise. This approach effectively advances the field by shifting from fitting statistical co-occurrences to learning causal invariance.

