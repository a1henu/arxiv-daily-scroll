---
layout: default
title: Autoregressive Visual Decoding from EEG Signals
---

# Autoregressive Visual Decoding from EEG Signals
**arXiv**：[2602.22555v1](https://arxiv.org/abs/2602.22555) · [PDF](https://arxiv.org/pdf/2602.22555.pdf)  
**作者**：Sicheng Dai, Hongwang Xiao, Shan Yu, Qiwei Ye  

**一句话要点**：提出AVDE框架，通过自回归生成从EEG信号解码视觉信息，以提升脑机接口效率与一致性。

**关键词**：脑电图解码, 自回归生成, 多尺度预测, 对比学习, 脑机接口, 视觉重建

## 3 点简述
- 核心问题：EEG与图像模态差异大，现有方法多阶段适应复杂，易产生累积误差，且扩散模型计算开销大。
- 方法要点：基于预训练EEG模型LaBraM，通过对比学习对齐EEG与图像表示；采用自回归生成框架，从EEG嵌入预测多尺度图像令牌。
- 实验或效果：在两个数据集上，AVDE在图像检索和重建任务中优于先前方法，参数仅用10%，生成过程反映视觉感知层次。

## 摘要（原文）

> Electroencephalogram (EEG) signals have become a popular medium for decoding visual information due to their cost-effectiveness and high temporal resolution. However, current approaches face significant challenges in bridging the modality gap between EEG and image data. These methods typically rely on complex adaptation processes involving multiple stages, making it hard to maintain consistency and manage compounding errors. Furthermore, the computational overhead imposed by large-scale diffusion models limit their practicality in real-world brain-computer interface (BCI) applications. In this work, we present AVDE, a lightweight and efficient framework for visual decoding from EEG signals. First, we leverage LaBraM, a pre-trained EEG model, and fine-tune it via contrastive learning to align EEG and image representations. Second, we adopt an autoregressive generative framework based on a "next-scale prediction" strategy: images are encoded into multi-scale token maps using a pre-trained VQ-VAE, and a transformer is trained to autoregressively predict finer-scale tokens starting from EEG embeddings as the coarsest representation. This design enables coherent generation while preserving a direct connection between the input EEG signals and the reconstructed images. Experiments on two datasets show that AVDE outperforms previous state-of-the-art methods in both image retrieval and reconstruction tasks, while using only 10% of the parameters. In addition, visualization of intermediate outputs shows that the generative process of AVDE reflects the hierarchical nature of human visual perception. These results highlight the potential of autoregressive models as efficient and interpretable tools for practical BCI applications.

