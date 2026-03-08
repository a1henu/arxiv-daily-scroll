---
layout: default
title: Logi-PAR: Logic-Infused Patient Activity Recognition via Differentiable Rule
---

# Logi-PAR: Logic-Infused Patient Activity Recognition via Differentiable Rule
**arXiv**：[2603.05184v1](https://arxiv.org/abs/2603.05184) · [PDF](https://arxiv.org/pdf/2603.05184.pdf)  
**作者**：Muhammad Zarar, MingZheng Zhang, Xiaowang Zhang, Zhiyong Feng, Sofonias Yitagesu, Kawsar Farooq  

**一句话要点**：提出Logi-PAR框架，通过可微分逻辑规则增强临床患者活动识别，实现可解释推理。

**关键词**：患者活动识别, 可微分逻辑规则, 可解释人工智能, 临床安全, 多视图融合, 端到端学习

## 3 点简述
- 核心问题：现有患者活动识别模型仅分类活动，缺乏逻辑显式推理以解释风险原因。
- 方法要点：集成上下文事实融合作为多视图基元提取器，并注入神经引导的可微分规则进行端到端学习。
- 实验或效果：在VAST和OmniFall基准上实现最先进性能，优于视觉语言模型和Transformer基线，提供可审计解释。

## 摘要（原文）

> Patient Activity Recognition (PAR) in clinical settings uses activity data to improve safety and quality of care. Although significant progress has been made, current models mainly identify which activity is occurring. They often spatially compose sub-sparse visual cues using global and local attention mechanisms, yet only learn logically implicit patterns due to their neural-pipeline. Advancing clinical safety requires methods that can infer why a set of visual cues implies a risk, and how these can be compositionally reasoned through explicit logic beyond mere classification. To address this, we proposed Logi-PAR, the first Logic-Infused Patient Activity Recognition Framework that integrates contextual fact fusion as a multi-view primitive extractor and injects neural-guided differentiable rules. Our method automatically learns rules from visual cues, optimizing them end-to-end while enabling the implicit emergence patterns to be explicitly labelled during training. To the best of our knowledge, Logi-PAR is the first framework to recognize patient activity by applying learnable logic rules to symbolic mappings. It produces auditable why explanations as rule traces and supports counterfactual interventions (e.g., risk would decrease by 65% if assistance were present). Extensive evaluation on clinical benchmarks (VAST and OmniFall) demonstrates state-of-the-art performance, significantly outperforming Vision-Language Models and transformer baselines. The code is available via: https://github.com/zararkhan985/Logi-PAR.git}

