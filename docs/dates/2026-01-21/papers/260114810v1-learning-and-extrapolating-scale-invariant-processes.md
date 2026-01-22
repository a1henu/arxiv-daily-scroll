---
layout: default
title: Learning and extrapolating scale-invariant processes
---

# Learning and extrapolating scale-invariant processes
**arXiv**：[2601.14810v1](https://arxiv.org/abs/2601.14810) · [PDF](https://arxiv.org/pdf/2601.14810.pdf)  
**作者**：Anaclara Alvez-Canepa, Cyril Furtlehner, François Landes  

**一句话要点**：提出基于尺度不变性的模型以预测无标度过程中的罕见事件

**关键词**：尺度不变性, 无标度过程, 罕见事件预测, 几何深度学习, 谱偏差, 粗粒度表示

## 3 点简述
- 研究如何回归无标度过程，如地震或雪崩，以预测训练集中罕见的大规模事件
- 利用几何深度学习，在U-net、Riesz网络等架构中融入尺度不变性，并设计基于小波分解的图神经网络和傅里叶-梅林神经算子
- 通过实验和线性案例分析，识别谱偏差和粗粒度表示问题，并讨论如何通过归纳偏置缓解

## 摘要（原文）

> Machine Learning (ML) has deeply changed some fields recently, like Language and Vision and we may expect it to be relevant also to the analysis of of complex systems. Here we want to tackle the question of how and to which extent can one regress scale-free processes, i.e. processes displaying power law behavior, like earthquakes or avalanches? We are interested in predicting the large ones, i.e. rare events in the training set which therefore require extrapolation capabilities of the model. For this we consider two paradigmatic problems that are statistically self-similar. The first one is a 2-dimensional fractional Gaussian field obeying linear dynamics, self-similar by construction and amenable to exact analysis. The second one is the Abelian sandpile model, exhibiting self-organized criticality. The emerging paradigm of Geometric Deep Learning shows that including known symmetries into the model's architecture is key to success. Here one may hope to extrapolate only by leveraging scale invariance. This is however a peculiar symmetry, as it involves possibly non-trivial coarse-graining operations and anomalous scaling. We perform experiments on various existing architectures like U-net, Riesz network (scale invariant by construction), or our own proposals: a wavelet-decomposition based Graph Neural Network (with discrete scale symmetry), a Fourier embedding layer and a Fourier-Mellin Neural Operator. Based on these experiments and a complete characterization of the linear case, we identify the main issues relative to spectral biases and coarse-grained representations, and discuss how to alleviate them with the relevant inductive biases.

