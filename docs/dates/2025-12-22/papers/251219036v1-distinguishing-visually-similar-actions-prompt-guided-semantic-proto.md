---
layout: default
title: Distinguishing Visually Similar Actions: Prompt-Guided Semantic Prototype Modulation for Few-Shot Action Recognition
---

# Distinguishing Visually Similar Actions: Prompt-Guided Semantic Prototype Modulation for Few-Shot Action Recognition
**arXiv**：[2512.19036v1](https://arxiv.org/abs/2512.19036) · [PDF](https://arxiv.org/pdf/2512.19036.pdf)  
**作者**：Xiaoyang Li, Mingming Lu, Ruiqi Wang, Hao Li, Zewei Le  

**一句话要点**：提出CLIP-SPM框架，通过语义原型调制解决少样本动作识别中的视觉相似性和模态差距问题。

**关键词**：少样本动作识别, 语义原型调制, 时间建模, 视觉-文本对齐, 原型优化

## 3 点简述
- 核心问题：少样本动作识别面临时间建模干扰、视觉相似性区分难和视觉-文本模态差距挑战。
- 方法要点：结合HSMR模块、SPM策略和PADM方法，优化运动特征、桥接模态并增强原型一致性。
- 实验或效果：在Kinetics等基准测试中，1-shot、3-shot和5-shot设置下表现优异，验证了各组件有效性。

## 摘要（原文）

> Few-shot action recognition aims to enable models to quickly learn new action categories from limited labeled samples, addressing the challenge of data scarcity in real-world applications. Current research primarily addresses three core challenges: (1) temporal modeling, where models are prone to interference from irrelevant static background information and struggle to capture the essence of dynamic action features; (2) visual similarity, where categories with subtle visual differences are difficult to distinguish; and (3) the modality gap between visual-textual support prototypes and visual-only queries, which complicates alignment within a shared embedding space. To address these challenges, this paper proposes a CLIP-SPM framework, which includes three components: (1) the Hierarchical Synergistic Motion Refinement (HSMR) module, which aligns deep and shallow motion features to improve temporal modeling by reducing static background interference; (2) the Semantic Prototype Modulation (SPM) strategy, which generates query-relevant text prompts to bridge the modality gap and integrates them with visual features, enhancing the discriminability between similar actions; and (3) the Prototype-Anchor Dual Modulation (PADM) method, which refines support prototypes and aligns query features with a global semantic anchor, improving consistency across support and query samples. Comprehensive experiments across standard benchmarks, including Kinetics, SSv2-Full, SSv2-Small, UCF101, and HMDB51, demonstrate that our CLIP-SPM achieves competitive performance under 1-shot, 3-shot, and 5-shot settings. Extensive ablation studies and visual analyses further validate the effectiveness of each component and its contributions to addressing the core challenges. The source code and models are publicly available at GitHub.

