---
layout: default
title: Effect of Activation Function and Model Optimizer on the Performance of Human Activity Recognition System Using Various Deep Learning Models
---

# Effect of Activation Function and Model Optimizer on the Performance of Human Activity Recognition System Using Various Deep Learning Models
**arXiv**：[2512.20104v1](https://arxiv.org/abs/2512.20104) · [PDF](https://arxiv.org/pdf/2512.20104.pdf)  
**作者**：Subrata Kumer Paula, Dewan Nafiul Islam Noora, Rakhi Rani Paula, Md. Ekramul Hamidb, Fahmid Al Faridc, Hezerul Abdul Karimd, Md. Maruf Al Hossain Princee, Abu Saleh Musa Miahb  

**一句话要点**：分析激活函数与优化器组合对基于BiLSTM和ConvLSTM的人体活动识别系统性能的影响

**关键词**：人体活动识别, 激活函数, 优化器, ConvLSTM, BiLSTM, 医疗应用

## 3 点简述
- 核心问题：现有研究较少探讨激活函数与优化器组合对HAR系统性能的影响，尤其在医疗场景中。
- 方法要点：使用ReLU、Sigmoid、Tanh三种激活函数与SGD、Adam、RMSprop、Adagrad四种优化器，结合BiLSTM和ConvLSTM模型进行实验。
- 实验或效果：ConvLSTM在HMDB51和UCF101数据集上表现优于BiLSTM，最高准确率达99.00%，而BiLSTM在HMDB51上性能下降至约60.00%。

## 摘要（原文）

> Human Activity Recognition (HAR) plays a vital role in healthcare, surveillance, and innovative environments, where reliable action recognition supports timely decision-making and automation. Although deep learning-based HAR systems are widely adopted, the impact of Activation Functions (AFs) and Model Optimizers (MOs) on performance has not been sufficiently analyzed, particularly regarding how their combinations influence model behavior in practical scenarios. Most existing studies focus on architecture design, while the interaction between AF and MO choices remains relatively unexplored. In this work, we investigate the effect of three commonly used activation functions (ReLU, Sigmoid, and Tanh) combined with four optimization algorithms (SGD, Adam, RMSprop, and Adagrad) using two recurrent deep learning architectures, namely BiLSTM and ConvLSTM. Experiments are conducted on six medically relevant activity classes selected from the HMDB51 and UCF101 datasets, considering their suitability for healthcare-oriented HAR applications. Our experimental results show that ConvLSTM consistently outperforms BiLSTM across both datasets. ConvLSTM, combined with Adam or RMSprop, achieves an accuracy of up to 99.00%, demonstrating strong spatio-temporal learning capabilities and stable performance. While BiLSTM performs reasonably well on UCF101, with accuracy approaching 98.00%, its performance drops to approximately 60.00% on HMDB51, indicating limited robustness across datasets and weaker sensitivity to AF and MO variations. This study provides practical insights for optimizing HAR systems, particularly for real-world healthcare environments where fast and precise activity detection is critical.

