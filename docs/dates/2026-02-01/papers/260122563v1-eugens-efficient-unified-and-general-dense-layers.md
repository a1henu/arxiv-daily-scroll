---
layout: default
title: EUGens: Efficient, Unified, and General Dense Layers
---

# EUGens: Efficient, Unified, and General Dense Layers
**arXiv**：[2601.22563v1](https://arxiv.org/abs/2601.22563) · [PDF](https://arxiv.org/pdf/2601.22563.pdf)  
**作者**：Sang Min Kim, Byeongchan Kim, Arijit Sehanobish, Somnath Basu Roy Chowdhury, Rahul Kidambi, Dongseok Shim, Avinava Dubey, Snigdha Chaturvedi, Min-hwan Oh, Krzysztof Choromanski  

**一句话要点**：提出EUGens高效统一通用稠密层，以解决全连接前馈层的计算与参数瓶颈问题。

**关键词**：高效神经网络, 稠密层设计, 随机特征近似, 推理加速, 参数减少, 知识迁移

## 3 点简述
- 全连接前馈层在神经网络中引入计算和参数瓶颈，限制实时应用和资源受限环境下的扩展。
- EUGens利用随机特征近似标准全连接层，通过输入范数依赖统一现有高效扩展，将推理复杂度从二次降至线性。
- 实验表明，集成EUGens到Transformer和MLP中，在图像分类等任务上提升推理速度达27%，内存效率达30%。

## 摘要（原文）

> Efficient neural networks are essential for scaling machine learning models to real-time applications and resource-constrained environments. Fully-connected feedforward layers (FFLs) introduce computation and parameter count bottlenecks within neural network architectures. To address this challenge, in this work, we propose a new class of dense layers that generalize standard fully-connected feedforward layers, \textbf{E}fficient, \textbf{U}nified and \textbf{Gen}eral dense layers (EUGens). EUGens leverage random features to approximate standard FFLs and go beyond them by incorporating a direct dependence on the input norms in their computations. The proposed layers unify existing efficient FFL extensions and improve efficiency by reducing inference complexity from quadratic to linear time. They also lead to \textbf{the first} unbiased algorithms approximating FFLs with arbitrary polynomial activation functions. Furthermore, EuGens reduce the parameter count and computational overhead while preserving the expressive power and adaptability of FFLs. We also present a layer-wise knowledge transfer technique that bypasses backpropagation, enabling efficient adaptation of EUGens to pre-trained models. Empirically, we observe that integrating EUGens into Transformers and MLPs yields substantial improvements in inference speed (up to \textbf{27}\%) and memory efficiency (up to \textbf{30}\%) across a range of tasks, including image classification, language model pre-training, and 3D scene reconstruction. Overall, our results highlight the potential of EUGens for the scalable deployment of large-scale neural networks in real-world scenarios.

