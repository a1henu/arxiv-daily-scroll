---
layout: default
title: Scattering Transform for Auditory Attention Decoding
---

# Scattering Transform for Auditory Attention Decoding
**arXiv**：[2602.23003v1](https://arxiv.org/abs/2602.23003) · [PDF](https://arxiv.org/pdf/2602.23003.pdf)  
**作者**：René Pallenberg, Fabrice Katzberg, Alfred Mertins, Marco Maass  

**一句话要点**：提出散射变换作为预处理方法，以提升听觉注意解码性能，解决鸡尾酒会问题。

**关键词**：听觉注意解码, 散射变换, 脑电图预处理, 鸡尾酒会问题, 神经网络分类

## 3 点简述
- 核心问题：基于脑电图的听觉注意解码中，传统预处理方法可能限制性能，需改进以应对鸡尾酒会问题。
- 方法要点：引入两层散射变换作为替代预处理，与常规滤波器组、同步挤压短时傅里叶变换和常见方法对比。
- 实验或效果：在KUL和DTU数据集上测试，散射变换在主题相关条件下显著提升性能，尤其在KUL数据集上效果明显。

## 摘要（原文）

> The use of hearing aids will increase in the coming years due to demographic change. One open problem that remains to be solved by a new generation of hearing aids is the cocktail party problem. A possible solution is electroencephalography-based auditory attention decoding. This has been the subject of several studies in recent years, which have in common that they use the same preprocessing methods in most cases. In this work, in order to achieve an advantage, the use of a scattering transform is proposed as an alternative to these preprocessing methods. The two-layer scattering transform is compared with a regular filterbank, the synchrosqueezing short-time Fourier transform and the common preprocessing. To demonstrate the performance, the known and the proposed preprocessing methods are compared for different classification tasks on two widely used datasets, provided by the KU Leuven (KUL) and the Technical University of Denmark (DTU). Both established and new neural-network-based models, CNNs, LSTMs, and recent Transformer/graph-based models are used for classification. Various evaluation strategies were compared, with a focus on the task of classifying speakers who are unknown from the training. We show that the two-layer scattering transform can significantly improve the performance for subject-related conditions, especially on the KUL dataset. However, on the DTU dataset, this only applies to some of the models, or when larger amounts of training data are provided, as in 10-fold cross-validation. This suggests that the scattering transform is capable of extracting additional relevant information.

