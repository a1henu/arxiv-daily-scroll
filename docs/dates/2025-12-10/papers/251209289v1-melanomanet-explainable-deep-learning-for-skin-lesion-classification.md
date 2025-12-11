---
layout: default
title: MelanomaNet: Explainable Deep Learning for Skin Lesion Classification
---

# MelanomaNet: Explainable Deep Learning for Skin Lesion Classification
**arXiv**：[2512.09289v1](https://arxiv.org/abs/2512.09289) · [PDF](https://arxiv.org/pdf/2512.09289.pdf)  
**作者**：Sukhrobbek Ilyosbekov  

**一句话要点**：提出MelanomaNet可解释深度学习系统，通过多机制提升皮肤病变分类的临床可解释性。

**关键词**：皮肤病变分类, 可解释深度学习, GradCAM++, 不确定性量化, 临床评估, EfficientNet V2

## 3 点简述
- 核心问题：深度学习模型在皮肤病变分类中因'黑箱'特性限制临床采用。
- 方法要点：结合EfficientNet V2骨干网络与GradCAM++、ABCDE准则提取、FastCAV和不确定性量化。
- 实验或效果：在ISIC 2019数据集上达到85.61%准确率，提供临床对齐的解释和不确定性分解。

## 摘要（原文）

> Automated skin lesion classification using deep learning has shown remarkable accuracy, yet clinical adoption remains limited due to the "black box" nature of these models. We present MelanomaNet, an explainable deep learning system for multi-class skin lesion classification that addresses this gap through four complementary interpretability mechanisms. Our approach combines an EfficientNet V2 backbone with GradCAM++ attention visualization, automated ABCDE clinical criterion extraction, Fast Concept Activation Vectors (FastCAV) for concept-based explanations, and Monte Carlo Dropout uncertainty quantification. We evaluate our system on the ISIC 2019 dataset containing 25,331 dermoscopic images across 9 diagnostic categories. Our model achieves 85.61% accuracy with a weighted F1 score of 0.8564, while providing clinically meaningful explanations that align model attention with established dermatological assessment criteria. The uncertainty quantification module decomposes prediction confidence into epistemic and aleatoric components, enabling automatic flagging of unreliable predictions for clinical review. Our results demonstrate that high classification performance can be achieved alongside comprehensive interpretability, potentially facilitating greater trust and adoption in clinical dermatology workflows. The source code is available at https://github.com/suxrobgm/explainable-melanoma

