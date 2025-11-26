---
layout: default
title: Feature-Modulated UFNO for Improved Prediction of Multiphase Flow in Porous Media
---

# Feature-Modulated UFNO for Improved Prediction of Multiphase Flow in Porous Media
**arXiv**：[2511.20543v1](https://arxiv.org/abs/2511.20543) · [PDF](https://arxiv.org/pdf/2511.20543.pdf)  
**作者**：Alhasan Abdellatif, Hannah P. Menke, Ahmed H. Elsheikh, Florian Doster, Kamaljit Singh  

**一句话要点**：提出UFNO-FiLM以改进多孔介质多相流预测

**关键词**：傅里叶神经算子, 多孔介质流动, 特征调制, 空间加权损失, 深度学习, 多相流预测

## 3 点简述
- UFNO处理标量输入效率低，在频域引入冗余常数信号
- 使用FiLM层解耦标量输入，并采用空间加权损失函数
- 实验显示气体饱和度MAE降低21%，优于UFNO

## 摘要（原文）

> The UNet-enhanced Fourier Neural Operator (UFNO) extends the Fourier Neural Operator (FNO) by incorporating a parallel UNet pathway, enabling the retention of both high- and low-frequency components. While UFNO improves predictive accuracy over FNO, it inefficiently treats scalar inputs (e.g., temperature, injection rate) as spatially distributed fields by duplicating their values across the domain. This forces the model to process redundant constant signals within the frequency domain. Additionally, its standard loss function does not account for spatial variations in error sensitivity, limiting performance in regions of high physical importance. We introduce UFNO-FiLM, an enhanced architecture that incorporates two key innovations. First, we decouple scalar inputs from spatial features using a Feature-wise Linear Modulation (FiLM) layer, allowing the model to modulate spatial feature maps without introducing constant signals into the Fourier transform. Second, we employ a spatially weighted loss function that prioritizes learning in critical regions. Our experiments on subsurface multiphase flow demonstrate a 21\% reduction in gas saturation Mean Absolute Error (MAE) compared to UFNO, highlighting the effectiveness of our approach in improving predictive accuracy.

