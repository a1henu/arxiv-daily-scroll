---
layout: default
title: Enhancing Imbalanced Electrocardiogram Classification: A Novel Approach Integrating Data Augmentation through Wavelet Transform and Interclass Fusion
---

# Enhancing Imbalanced Electrocardiogram Classification: A Novel Approach Integrating Data Augmentation through Wavelet Transform and Interclass Fusion
**arXiv**：[2601.09103v1](https://arxiv.org/abs/2601.09103) · [PDF](https://arxiv.org/pdf/2601.09103.pdf)  
**作者**：Haijian Shao, Wei Liu, Xing Deng, Daze Lu  

**一句话要点**：提出基于小波变换的类间融合方法，以解决心电图分类中的类别不平衡和噪声问题。

**关键词**：心电图分类, 类别不平衡, 小波变换, 数据融合, 深度学习, 噪声处理

## 3 点简述
- 核心问题：心电图数据类别不平衡和噪声影响深度学习分类性能。
- 方法要点：利用小波变换进行特征融合，生成平衡的训练和测试特征库。
- 实验或效果：在CPSC 2018数据集上，分类准确率高达99%，平均92%-98%。

## 摘要（原文）

> Imbalanced electrocardiogram (ECG) data hampers the efficacy and resilience of algorithms in the automated processing and interpretation of cardiovascular diagnostic information, which in turn impedes deep learning-based ECG classification. Notably, certain cardiac conditions that are infrequently encountered are disproportionately underrepresented in these datasets. Although algorithmic generation and oversampling of specific ECG signal types can mitigate class skew, there is a lack of consensus regarding the effectiveness of such techniques in ECG classification. Furthermore, the methodologies and scenarios of ECG acquisition introduce noise, further complicating the processing of ECG data. This paper presents a significantly enhanced ECG classifier that simultaneously addresses both class imbalance and noise-related challenges in ECG analysis, as observed in the CPSC 2018 dataset. Specifically, we propose the application of feature fusion based on the wavelet transform, with a focus on wavelet transform-based interclass fusion, to generate the training feature library and the test set feature library. Subsequently, the original training and test data are amalgamated with their respective feature databases, resulting in more balanced training and test datasets. Employing this approach, our ECG model achieves recognition accuracies of up to 99%, 98%, 97%, 98%, 96%, 92%, and 93% for Normal, AF, I-AVB, LBBB, RBBB, PAC, PVC, STD, and STE, respectively. Furthermore, the average recognition accuracy for these categories ranges between 92\% and 98\%. Notably, our proposed data fusion methodology surpasses any known algorithms in terms of ECG classification accuracy in the CPSC 2018 dataset.

