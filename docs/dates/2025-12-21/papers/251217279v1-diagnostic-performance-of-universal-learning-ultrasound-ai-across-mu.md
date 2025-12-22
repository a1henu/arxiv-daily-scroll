---
layout: default
title: Diagnostic Performance of Universal-Learning Ultrasound AI Across Multiple Organs and Tasks: the UUSIC25 Challenge
---

# Diagnostic Performance of Universal-Learning Ultrasound AI Across Multiple Organs and Tasks: the UUSIC25 Challenge
**arXiv**：[2512.17279v1](https://arxiv.org/abs/2512.17279) · [PDF](https://arxiv.org/pdf/2512.17279.pdf)  
**作者**：Zehui Lin, Luyi Han, Xin Wang, Ying Zhou, Yanming Zhang, Tianyu Zhang, Lingyun Bao, Shandong Wu, Dong Xu, Tao Tan, the UUSIC25 Challenge Consortium  

**一句话要点**：评估通用深度学习模型在超声多器官分类与分割中的诊断性能与效率

**关键词**：超声图像分析, 多任务学习, 深度学习模型, 诊断性能评估, 域泛化

## 3 点简述
- 当前超声AI工具多为单任务，限制了临床实用性，需发展通用模型。
- 通过UUSIC25挑战赛，在11,644张图像上开发算法，使用独立多中心测试集评估。
- 最佳模型在分割任务中DSC达0.854，但未见数据上性能下降，凸显泛化挑战。

## 摘要（原文）

> IMPORTANCE: Current ultrasound AI remains fragmented into single-task tools, limiting clinical utility compared to versatile modern ultrasound systems.
>   OBJECTIVE: To evaluate the diagnostic accuracy and efficiency of single general-purpose deep learning models for multi-organ classification and segmentation.
>   DESIGN: The Universal UltraSound Image Challenge 2025 (UUSIC25) involved developing algorithms on 11,644 images (public/private). Evaluation used an independent, multi-center test set of 2,479 images, including data from a center completely unseen during training to assess generalization.
>   OUTCOMES: Diagnostic performance (Dice Similarity Coefficient [DSC]; Area Under the Receiver Operating Characteristic Curve [AUC]) and computational efficiency (inference time, GPU memory).
>   RESULTS: Of 15 valid algorithms, the top model (SMART) achieved a macro-averaged DSC of 0.854 across 5 segmentation tasks and AUC of 0.766 for binary classification. Models showed high capability in segmentation (e.g., fetal head DSC: 0.942) but variability in complex tasks subject to domain shift. Notably, in breast cancer molecular subtyping, the top model's performance dropped from AUC 0.571 (internal) to 0.508 (unseen external center), highlighting generalization challenges.
>   CONCLUSIONS: General-purpose AI models achieve high accuracy and efficiency across multiple tasks using a single architecture. However, performance degradation on unseen data suggests domain generalization is critical for future clinical deployment.

