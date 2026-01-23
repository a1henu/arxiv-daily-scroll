---
layout: default
title: A Lightweight Brain-Inspired Machine Learning Framework for Coronary Angiography: Hybrid Neural Representation and Robust Learning Strategies
---

# A Lightweight Brain-Inspired Machine Learning Framework for Coronary Angiography: Hybrid Neural Representation and Robust Learning Strategies
**arXiv**：[2601.15865v1](https://arxiv.org/abs/2601.15865) · [PDF](https://arxiv.org/pdf/2601.15865.pdf)  
**作者**：Jingsong Xia, Siqi Wang  

**一句话要点**：提出轻量级脑启发机器学习框架，用于冠状动脉造影图像分类，以解决计算资源有限下的鲁棒性和泛化性挑战。

**关键词**：冠状动脉造影, 轻量级模型, 脑启发学习, 混合神经表示, 鲁棒训练, 医学图像分类

## 3 点简述
- 核心问题：冠状动脉造影图像存在复杂病变形态、类别不平衡、标签不确定性和计算资源限制，影响传统深度学习的鲁棒性和泛化性。
- 方法要点：基于预训练卷积神经网络构建轻量级混合神经表示，引入选择性神经可塑性训练策略和脑启发注意力调制损失函数，结合类别不平衡感知采样和余弦退火。
- 实验或效果：在二元冠状动脉造影分类中，模型实现高准确率、召回率、F1分数和AUC，同时保持计算效率，验证了脑启发机制在轻量级医学图像分析中的有效性。

## 摘要（原文）

> Background: Coronary angiography (CAG) is a cornerstone imaging modality for assessing coronary artery disease and guiding interventional treatment decisions. However, in real-world clinical settings, angiographic images are often characterized by complex lesion morphology, severe class imbalance, label uncertainty, and limited computational resources, posing substantial challenges to conventional deep learning approaches in terms of robustness and generalization.Methods: The proposed framework is built upon a pretrained convolutional neural network to construct a lightweight hybrid neural representation. A selective neural plasticity training strategy is introduced to enable efficient parameter adaptation. Furthermore, a brain-inspired attention-modulated loss function, combining Focal Loss with label smoothing, is employed to enhance sensitivity to hard samples and uncertain annotations. Class-imbalance-aware sampling and cosine annealing with warm restarts are adopted to mimic rhythmic regulation and attention allocation mechanisms observed in biological neural systems.Results: Experimental results demonstrate that the proposed lightweight brain-inspired model achieves strong and stable performance in binary coronary angiography classification, yielding competitive accuracy, recall, F1-score, and AUC metrics while maintaining high computational efficiency.Conclusion: This study validates the effectiveness of brain-inspired learning mechanisms in lightweight medical image analysis and provides a biologically plausible and deployable solution for intelligent clinical decision support under limited computational resources.

