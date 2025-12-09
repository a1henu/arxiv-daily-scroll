---
layout: default
title: Microseismic event classification with a lightweight Fourier Neural Operator model
---

# Microseismic event classification with a lightweight Fourier Neural Operator model
**arXiv**：[2512.07425v1](https://arxiv.org/abs/2512.07425) · [PDF](https://arxiv.org/pdf/2512.07425.pdf)  
**作者**：Ayrat Abdullin, Umair bin Waheed, Leo Eisner, Abdullatif Al-Shuhail  

**一句话要点**：提出轻量级傅里叶神经算子模型以解决微震事件实时分类中的计算效率问题

**关键词**：微震事件分类, 傅里叶神经算子, 轻量模型, 实时监测, 诱发地震, 波形处理

## 3 点简述
- 核心问题：实时监测诱发地震需快速准确分类微震事件，但现有深度学习模型计算需求高，限制实际应用。
- 方法要点：基于傅里叶神经算子构建轻量模型，利用其分辨率不变性和计算高效性处理波形数据。
- 实验或效果：在STEAD数据集上F1分数达95%，真实数据集上达98%，计算资源需求显著降低，适合实时监测。

## 摘要（原文）

> Real-time monitoring of induced seismicity is crucial for mitigating operational hazards, relying on the rapid and accurate classification of microseismic events from continuous data streams. However, while many deep learning models excel at this task, their high computational requirements often limit their practical application in real-time monitoring systems. To address this limitation, a lightweight model based on the Fourier Neural Operator (FNO) is proposed for microseismic event classification, leveraging its inherent resolution-invariance and computational efficiency for waveform processing. In the STanford EArthquake Dataset (STEAD), a global and large-scale database of seismic waveforms, the FNO-based model demonstrates high effectiveness for trigger classification, with an F1 score of 95% even in the scenario of data sparsity in training. The new FNO model greatly decreases the computer power needed relative to current deep learning models without sacrificing the classification success rate measured by the F1 score. A test on a real microseismic dataset shows a classification success rate with an F1 score of 98%, outperforming many traditional deep-learning techniques. A combination of high success rate and low computational power indicates that the FNO model can serve as a methodology of choice for real-time monitoring of microseismicity for induced seismicity. The method saves computational resources and facilitates both post-processing and real-time seismic processing suitable for the implementation of traffic light systems to prevent undesired induced seismicity.

