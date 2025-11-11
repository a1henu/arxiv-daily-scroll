---
layout: default
title: From Attribution to Action: Jointly ALIGNing Predictions and Explanations
---

# From Attribution to Action: Jointly ALIGNing Predictions and Explanations
**arXiv**：[2511.06944v1](https://arxiv.org/abs/2511.06944) · [PDF](https://arxiv.org/pdf/2511.06944.pdf)  
**作者**：Dongsheng Hong, Chao Chen, Yanhui Chen, Shanshan Lin, Zhihao Chen, Xiangwen Liao  

**一句话要点**：提出ALIGN框架以联合优化分类器和掩码器，提升模型可解释性和泛化能力

**关键词**：解释引导学习, 掩码生成, 领域泛化, 可解释性, 联合训练

## 3 点简述
- 核心问题：现有解释引导学习依赖外部注释或启发式分割，监督信号质量低且难以扩展
- 方法要点：通过迭代训练，掩码器生成任务相关软掩码，分类器优化预测准确性和对齐性
- 实验或效果：在VLCS和Terra Incognita基准上，ALIGN在分布内外均优于基线，解释质量更高

## 摘要（原文）

> Explanation-guided learning (EGL) has shown promise in aligning model
> predictions with interpretable reasoning, particularly in computer vision
> tasks. However, most approaches rely on external annotations or heuristic-based
> segmentation to supervise model explanations, which can be noisy, imprecise and
> difficult to scale. In this work, we provide both empirical and theoretical
> evidence that low-quality supervision signals can degrade model performance
> rather than improve it. In response, we propose ALIGN, a novel framework that
> jointly trains a classifier and a masker in an iterative manner. The masker
> learns to produce soft, task-relevant masks that highlight informative regions,
> while the classifier is optimized for both prediction accuracy and alignment
> between its saliency maps and the learned masks. By leveraging high-quality
> masks as guidance, ALIGN improves both interpretability and generalizability,
> showing its superiority across various settings. Experiments on the two domain
> generalization benchmarks, VLCS and Terra Incognita, show that ALIGN
> consistently outperforms six strong baselines in both in-distribution and
> out-of-distribution settings. Besides, ALIGN also yields superior explanation
> quality concerning sufficiency and comprehensiveness, highlighting its
> effectiveness in producing accurate and interpretable models.

