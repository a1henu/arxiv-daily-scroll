---
layout: default
title: Layer-wise LoRA fine-tuning: a similarity metric approach
---

# Layer-wise LoRA fine-tuning: a similarity metric approach
**arXiv**：[2602.05988v1](https://arxiv.org/abs/2602.05988) · [PDF](https://arxiv.org/pdf/2602.05988.pdf)  
**作者**：Keith Ando Ogawa, Bruno Lopes Yamamoto, Lucas Lauton de Alcantara, Lucas Pellicer, Rosimeire Pereira Costa, Edson Bollis, Anna Helena Reali Costa, Artur Jordao  

**一句话要点**：提出基于相似性度量的层间LoRA微调方法，以进一步减少大语言模型微调参数

**关键词**：层间微调, LoRA, 相似性度量, 参数高效微调, 大语言模型, 内部表示分析

## 3 点简述
- 核心问题：LoRA等参数高效微调技术在大模型规模增长下仍可能参数过多，需进一步优化
- 方法要点：通过测量内部表示变化贡献，系统选择少数关键层进行LoRA微调，兼容现有低秩适应技术
- 实验或效果：在编码器和解码器架构上，减少高达50%可训练参数，预测性能保持或略有提升

## 摘要（原文）

> Pre-training Large Language Models (LLMs) on web-scale datasets becomes fundamental for advancing general-purpose AI. In contrast, enhancing their predictive performance on downstream tasks typically involves adapting their knowledge through fine-tuning. Parameter-efficient fine-tuning techniques, such as Low-Rank Adaptation (LoRA), aim to reduce the computational cost of this process by freezing the pre-trained model and updating a smaller number of parameters. In comparison to full fine-tuning, these methods achieve over 99\% reduction in trainable parameter count, depending on the configuration. Unfortunately, such a reduction may prove insufficient as LLMs continue to grow in scale. In this work, we address the previous problem by systematically selecting only a few layers to fine-tune using LoRA or its variants. We argue that not all layers contribute equally to the model adaptation. Leveraging this, we identify the most relevant layers to fine-tune by measuring their contribution to changes in internal representations. Our method is orthogonal to and readily compatible with existing low-rank adaptation techniques. We reduce the trainable parameters in LoRA-based techniques by up to 50\%, while maintaining the predictive performance across different models and tasks. Specifically, on encoder-only architectures, this reduction in trainable parameters leads to a negligible predictive performance drop on the GLUE benchmark. On decoder-only architectures, we achieve a small drop or even improvements in the predictive performance on mathematical problem-solving capabilities and coding tasks. Finally, this effectiveness extends to multimodal models, for which we also observe competitive results relative to fine-tuning with LoRA modules in all layers. Code is available at: https://github.com/c2d-usp/Layer-wise-LoRA-with-CKA

