---
layout: default
title: ScaleNet: Scaling up Pretrained Neural Networks with Incremental Parameters
---

# ScaleNet: Scaling up Pretrained Neural Networks with Incremental Parameters
**arXiv**：[2510.18431v1](https://arxiv.org/abs/2510.18431) · [PDF](https://arxiv.org/pdf/2510.18431.pdf)  
**作者**：Zhiwei Hao, Jianyuan Guo, Li Shen, Kai Han, Yehui Tang, Han Hu, Yunhe Wang  

**一句话要点**：提出ScaleNet以高效扩展预训练视觉Transformer模型

**关键词**：视觉Transformer, 模型扩展, 参数共享, 高效训练, 图像分类

## 3 点简述
- 核心问题：训练大型视觉Transformer模型计算成本高且耗时
- 方法要点：通过插入共享权重层和调整参数实现模型扩展
- 实验或效果：在ImageNet-1K上，2倍深度扩展模型准确率提升7.42%

## 摘要（原文）

> Recent advancements in vision transformers (ViTs) have demonstrated that
> larger models often achieve superior performance. However, training these
> models remains computationally intensive and costly. To address this challenge,
> we introduce ScaleNet, an efficient approach for scaling ViT models. Unlike
> conventional training from scratch, ScaleNet facilitates rapid model expansion
> with negligible increases in parameters, building on existing pretrained
> models. This offers a cost-effective solution for scaling up ViTs.
> Specifically, ScaleNet achieves model expansion by inserting additional layers
> into pretrained ViTs, utilizing layer-wise weight sharing to maintain
> parameters efficiency. Each added layer shares its parameter tensor with a
> corresponding layer from the pretrained model. To mitigate potential
> performance degradation due to shared weights, ScaleNet introduces a small set
> of adjustment parameters for each layer. These adjustment parameters are
> implemented through parallel adapter modules, ensuring that each instance of
> the shared parameter tensor remains distinct and optimized for its specific
> function. Experiments on the ImageNet-1K dataset demonstrate that ScaleNet
> enables efficient expansion of ViT models. With a 2$\times$ depth-scaled
> DeiT-Base model, ScaleNet achieves a 7.42% accuracy improvement over training
> from scratch while requiring only one-third of the training epochs,
> highlighting its efficiency in scaling ViTs. Beyond image classification, our
> method shows significant potential for application in downstream vision areas,
> as evidenced by the validation in object detection task.

