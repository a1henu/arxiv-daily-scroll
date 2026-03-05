---
layout: default
title: Weakly Supervised Patch Annotation for Improved Screening of Diabetic Retinopathy
---

# Weakly Supervised Patch Annotation for Improved Screening of Diabetic Retinopathy
**arXiv**：[2603.03991v1](https://arxiv.org/abs/2603.03991) · [PDF](https://arxiv.org/pdf/2603.03991.pdf)  
**作者**：Shramana Dey, Abhirup Banerjee, B. Uma Shankar, Ramachandran Rajalakshmi, Sushmita Mitra  

**一句话要点**：提出SAFE框架，通过弱监督和对比学习扩展稀疏标注，以改进糖尿病视网膜病变筛查。

**关键词**：糖尿病视网膜病变, 弱监督学习, 对比学习, 补丁标注, 医学图像分析, 特征空间集成

## 3 点简述
- 核心问题：糖尿病视网膜病变早期检测中，病变区域标注稀疏且不完整，限制深度学习模型性能。
- 方法要点：SAFE框架分两阶段，先学习病变补丁嵌入，再通过集成空间外推标注未标记区域，包含弃权机制平衡可靠性。
- 实验或效果：实验显示高准确度分离健康与病变补丁，下游分类任务F1分数和AUPRC显著提升，经眼科医生验证。

## 摘要（原文）

> Diabetic Retinopathy (DR) requires timely screening to prevent irreversible vision loss. However, its early detection remains a significant challenge since often the subtle pathological manifestations (lesions) get overlooked due to insufficient annotation. Existing literature primarily focuses on image-level supervision, weakly-supervised localization, and clustering-based representation learning, which fail to systematically annotate unlabeled lesion region(s) for refining the dataset. Expert-driven lesion annotation is labor-intensive and often incomplete, limiting the performance of deep learning models. We introduce Similarity-based Annotation via Feature-space Ensemble (SAFE), a two-stage framework that unifies weak supervision, contrastive learning, and patch-wise embedding inference, to systematically expand sparse annotations in the pathology. SAFE preserves fine-grained details of the lesion(s) under partial clinical supervision. In the first stage, a dual-arm Patch Embedding Network learns semantically structured, class-discriminative embeddings from expert annotated patches. Next, an ensemble of independent embedding spaces extrapolates labels to the unannotated regions based on spatial and semantic proximity. An abstention mechanism ensures trade-off between highly reliable annotation and noisy coverage. Experimental results demonstrate reliable separation of healthy and diseased patches, achieving upto 0.9886 accuracy. The annotation generated from SAFE substantially improves downstream tasks such as DR classification, demonstrating a substantial increase in F1-score of the diseased class and a performance gain as high as 0.545 in Area Under the Precision-Recall Curve (AUPRC). Qualitative analysis, with explainability, confirms that SAFE focuses on clinically relevant lesion patterns; and is further validated by ophthalmologists.

