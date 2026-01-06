---
layout: default
title: RSwinV2-MD: An Enhanced Residual SwinV2 Transformer for Monkeypox Detection from Skin Images
---

# RSwinV2-MD: An Enhanced Residual SwinV2 Transformer for Monkeypox Detection from Skin Images
**arXiv**：[2601.01835v1](https://arxiv.org/abs/2601.01835) · [PDF](https://arxiv.org/pdf/2601.01835.pdf)  
**作者**：Rashid Iqbal, Saddam Hussain Khan  

**一句话要点**：提出增强型残差SwinV2变换器RSwinV2-MD，用于皮肤图像中的猴痘检测。

**关键词**：猴痘检测, 皮肤图像分类, SwinTransformer, 逆残差块, 计算机辅助诊断

## 3 点简述
- 核心问题：猴痘病变分类中，需处理局部与全局模式，并克服梯度消失问题。
- 方法要点：基于SwinTransformer定制层次结构，引入逆残差块和移位窗口注意力，增强特征链接。
- 实验或效果：在Kaggle数据集上达到96.21%准确率和95.62% F1分数，优于CNN和SwinTransformer。

## 摘要（原文）

> In this paper, a deep learning approach for Mpox diagnosis named Customized Residual SwinTransformerV2 (RSwinV2) has been proposed, trying to enhance the capability of lesion classification by employing the RSwinV2 tool-assisted vision approach. In the RSwinV2 method, a hierarchical structure of the transformer has been customized based on the input dimensionality, embedding structure, and output targeted by the method. In this RSwinV2 approach, the input image has been split into non-overlapping patches and processed using shifted windows and attention in these patches. This process has helped the method link all the windows efficiently by avoiding the locality issues of non-overlapping regions in attention, while being computationally efficient. RSwinV2 has further developed based on SwinTransformer and has included patch and position embeddings to take advantage of the transformer global-linking capability by employing multi-head attention in these embeddings. Furthermore, RSwinV2 has developed and incorporated the Inverse Residual Block (IRB) into this method, which utilizes convolutional skip connections with these inclusive designs to address the vanishing gradient issues during processing. RSwinV2 inclusion of IRB has therefore facilitated this method to link global patterns as well as local patterns; hence, its integrity has helped improve lesion classification capability by minimizing variability of Mpox and increasing differences of Mpox, chickenpox, measles, and cowpox. In testing SwinV2, its accuracy of 96.21 and an F1score of 95.62 have been achieved on the Kaggle public dataset, which has outperformed standard CNN models and SwinTransformers; RSwinV2 vector has thus proved its valiance as a computer-assisted tool for Mpox lesion observation interpretation.

