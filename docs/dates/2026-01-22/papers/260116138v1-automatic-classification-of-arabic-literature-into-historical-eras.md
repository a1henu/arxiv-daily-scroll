---
layout: default
title: Automatic Classification of Arabic Literature into Historical Eras
---

# Automatic Classification of Arabic Literature into Historical Eras
**arXiv**：[2601.16138v1](https://arxiv.org/abs/2601.16138) · [PDF](https://arxiv.org/pdf/2601.16138.pdf)  
**作者**：Zainab Alhathloul, Irfan Ahmad  

**一句话要点**：提出基于神经网络的阿拉伯文本自动历史时期分类方法，填补非诗歌领域研究空白。

**关键词**：阿拉伯文本分类, 历史时期分类, 神经网络, 深度学习, 多类分类, 语言演变

## 3 点简述
- 核心问题：阿拉伯语言随时间演变，自动分类文本至历史时期的研究较少，尤其在非诗歌领域。
- 方法要点：采用神经网络和深度学习技术，处理从二元到15类的分类任务，考虑预设和自定义时期划分。
- 实验或效果：在两个公开语料库数据集上评估，二元分类F1分数达0.83和0.79，多类分类分数较低，如15类为0.20。

## 摘要（原文）

> The Arabic language has undergone notable transformations over time, including the emergence of new vocabulary, the obsolescence of others, and shifts in word usage. This evolution is evident in the distinction between the classical and modern Arabic eras. Although historians and linguists have partitioned Arabic literature into multiple eras, relatively little research has explored the automatic classification of Arabic texts by time period, particularly beyond the domain of poetry. This paper addresses this gap by employing neural networks and deep learning techniques to automatically classify Arabic texts into distinct eras and periods. The proposed models are evaluated using two datasets derived from two publicly available corpora, covering texts from the pre-Islamic to the modern era. The study examines class setups ranging from binary to 15-class classification and considers both predefined historical eras and custom periodizations. Results range from F1-scores of 0.83 and 0.79 on the binary-era classification task using the OpenITI and APCD datasets, respectively, to 0.20 on the 15-era classification task using OpenITI and 0.18 on the 12-era classification task using APCD.

