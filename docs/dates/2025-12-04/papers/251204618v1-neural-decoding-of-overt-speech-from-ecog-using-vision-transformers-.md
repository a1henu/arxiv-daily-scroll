---
layout: default
title: Neural Decoding of Overt Speech from ECoG Using Vision Transformers and Contrastive Representation Learning
---

# Neural Decoding of Overt Speech from ECoG Using Vision Transformers and Contrastive Representation Learning
**arXiv**：[2512.04618v1](https://arxiv.org/abs/2512.04618) · [PDF](https://arxiv.org/pdf/2512.04618.pdf)  
**作者**：Mohamed Baha Ben Ticha, Xingchen Ran, Guillaume Saldanha, Gaël Le Godais, Philémon Roussel, Marc Aubert, Amina Fontanell, Thomas Costecalde, Lucas Struber, Serpil Karakas, Shaomin Zhang, Philippe Kahane, Guillaume Charvet, Stéphan Chabardès, Blaise Yvert  

**一句话要点**：提出基于视觉变换器和对比学习的编码器-解码器架构，用于从ECoG信号直接回归语音，以优化脑机接口中的语音解码。

**关键词**：脑机接口, 语音解码, 视觉变换器, 对比学习, ECoG信号处理, 无线植入系统

## 3 点简述
- 核心问题：从表面ECoG信号直接回归语音以支持流式解码，当前在无线植入系统上效果有限。
- 方法要点：集成视觉变换器和对比学习，增强ECoG信号到语音的回归性能。
- 实验或效果：在临床和无线植入ECoG数据集上评估，首次尝试从无线植入系统解码语音。

## 摘要（原文）

> Speech Brain Computer Interfaces (BCIs) offer promising solutions to people with severe paralysis unable to communicate. A number of recent studies have demonstrated convincing reconstruction of intelligible speech from surface electrocorticographic (ECoG) or intracortical recordings by predicting a series of phonemes or words and using downstream language models to obtain meaningful sentences. A current challenge is to reconstruct speech in a streaming mode by directly regressing cortical signals into acoustic speech. While this has been achieved recently using intracortical data, further work is needed to obtain comparable results with surface ECoG recordings. In particular, optimizing neural decoders becomes critical in this case. Here we present an offline speech decoding pipeline based on an encoder-decoder deep neural architecture, integrating Vision Transformers and contrastive learning to enhance the direct regression of speech from ECoG signals. The approach is evaluated on two datasets, one obtained with clinical subdural electrodes in an epileptic patient, and another obtained with the fully implantable WIMAGINE epidural system in a participant of a motor BCI trial. To our knowledge this presents a first attempt to decode speech from a fully implantable and wireless epidural recording system offering perspectives for long-term use.

