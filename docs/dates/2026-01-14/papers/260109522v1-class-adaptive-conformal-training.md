---
layout: default
title: Class Adaptive Conformal Training
---

# Class Adaptive Conformal Training
**arXiv**：[2601.09522v1](https://arxiv.org/abs/2601.09522) · [PDF](https://arxiv.org/pdf/2601.09522.pdf)  
**作者**：Badr-Eddine Marani, Julio Silva-Rodriguez, Ismail Ben Ayed, Maria Vakalopoulou, Stergios Christodoulidis, Jose Dolz  

**一句话要点**：提出类自适应保形训练以解决深度神经网络概率估计不可靠问题

**关键词**：保形预测, 不确定性量化, 类自适应训练, 图像识别, 文本分类, 长尾分布

## 3 点简述
- 核心问题：深度神经网络概率估计不可靠，导致预测过度自信。
- 方法要点：通过增广拉格朗日优化自适应学习类条件预测集，无需分布假设。
- 实验效果：在多个基准数据集上优于现有方法，产生更小且信息丰富的预测集。

## 摘要（原文）

> Deep neural networks have achieved remarkable success across a variety of tasks, yet they often suffer from unreliable probability estimates. As a result, they can be overconfident in their predictions. Conformal Prediction (CP) offers a principled framework for uncertainty quantification, yielding prediction sets with rigorous coverage guarantees. Existing conformal training methods optimize for overall set size, but shaping the prediction sets in a class-conditional manner is not straightforward and typically requires prior knowledge of the data distribution. In this work, we introduce Class Adaptive Conformal Training (CaCT), which formulates conformal training as an augmented Lagrangian optimization problem that adaptively learns to shape prediction sets class-conditionally without making any distributional assumptions. Experiments on multiple benchmark datasets, including standard and long-tailed image recognition as well as text classification, demonstrate that CaCT consistently outperforms prior conformal training methods, producing significantly smaller and more informative prediction sets while maintaining the desired coverage guarantees.

